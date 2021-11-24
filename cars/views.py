import json
import requests
import re
import concurrent.futures
import time

from django.http  import JsonResponse
from django.views import View

from .models          import Car, FrontTire, RearTire
from users.models     import User
from core.validations import tire_info_validator
from core.utils       import authorization


class Tire():
    def __init__(self, tire_type):
        tire_info = re.split('/|R', tire_type)
        self.width        = tire_info[0]
        self.aspect_ratio = tire_info[1]
        self.wheel_size   = tire_info[2]


class TireCreateView(View):
    def get_tire_and_user_info(self, data):
        try:
            time.sleep(0.5)
            email   = data["email"]
            trim_id = data["trim_id"]
            user    = User.objects.get(email = email)
            url     = f"https://dev.mycar.cardoc.co.kr/v1/trim/{trim_id}"

            response = requests.get(url, timeout = 3)
            print(response.url)

            if response.status_code!=200:
                return (user.email, "BAD_REQUEST", 400)

            external_data = response.json()

            model_name = external_data["modelName"]

            if tire_info_validator(external_data["spec"]["driving"]["frontTire"]["value"]):
                front_tire_info = Tire(external_data["spec"]["driving"]["frontTire"]["value"])

                front_tire, _ =\
                    FrontTire.objects.get_or_create(
                        width        = front_tire_info.width,
                        aspect_ratio = front_tire_info.aspect_ratio,
                        wheel_size   = front_tire_info.wheel_size
                    )

            if tire_info_validator(external_data["spec"]["driving"]["rearTire"]["value"]):
                rear_tire_info  = Tire(external_data["spec"]["driving"]["rearTire"]["value"])
                
                rear_tire, _ =\
                    RearTire.objects.get_or_create(
                        width        = rear_tire_info.width,
                        aspect_ratio = rear_tire_info.aspect_ratio,
                        wheel_size   = rear_tire_info.wheel_size
                    )

            Car.objects.update_or_create(
                model_name = model_name,
                user       = user,
                front_tire = front_tire,
                rear_tire  = rear_tire
            )

            return (user.email, "CREATED", 200)
        
        except KeyError:
            return ("empty", "KEY_ERROR", 400)

        except TimeoutError:
            return ("empty", "TIME_OUT", 400)

        except User.DoesNotExist:
            return ("empty", "USER_DOES_NOT_EXIST", 404)

    def post(self, request):
        datas   = json.loads(request.body)

        if len(datas) > 5:
            return JsonResponse({"message" : "PAYLOAD_TOO_LONG"}, status=413)
        
        with concurrent.futures.ThreadPoolExecutor(max_workers = 5) as executor:
            results = [exe for exe in executor.map(self.get_tire_and_user_info, datas)]

        messages = [
            {
                "id" : result[0],
                "message" : result[1],
                "status" : result[2]
            } for result in results
        ]

        return JsonResponse({"messages" : messages}, status=201)
