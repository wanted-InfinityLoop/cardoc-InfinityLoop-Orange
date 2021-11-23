import json
import requests
import re

from django.http  import JsonResponse, response
from django.views import View

from .models      import Car, FrontTire, RearTire
from users.models import User

class Tire():
    def __init__(self, tire_type):
        tire_info = re.split('/|R', tire_type)
        self.width        = tire_info[0]
        self.aspect_ratio = tire_info[1]
        self.wheel_size   = tire_info[2]

class TireCreateView(View):
    def post(self, request):
        try:
            datas = json.loads(request.body)

            if len(datas) > 5:
                return JsonResponse({"message" : "PAYLOAD_TOO_LONG"}, status=413)
            
            for data in datas:
                email   = data["email"]
                trim_id = data["trim_id"]

                url         = f"https://dev.mycar.cardoc.co.kr/v1/trim/{trim_id}"
                resp        = requests.get(url).text
                export_data = json.loads(resp)

                if not User.objects.filter(email = email).exists():
                    return JsonResponse({"message" : "USER_DOES_NOT_EXIST"}, status=400)

                user = User.objects.get(email = email)

                model_name = export_data["modelName"]
                front_tire_info = Tire(export_data["spec"]["driving"]["frontTire"]["value"])
                rear_tire_info  = Tire(export_data["spec"]["driving"]["rearTire"]["value"])

                front_tire, front_is_created =\
                    FrontTire.objects.get_or_create(
                        width        = front_tire_info.width,
                        aspect_ratio = front_tire_info.aspect_ratio,
                        wheel_size   = front_tire_info.wheel_size
                    )

                rear_tire, rear_is_created =\
                    RearTire.objects.get_or_create(
                        width        = rear_tire_info.width,
                        aspect_ratio = rear_tire_info.aspect_ratio,
                        wheel_size   = rear_tire_info.wheel_size
                    )

                if front_is_created:
                    Car.objects.create(
                        model_name = model_name,

                    )

            return JsonResponse({"message" : front_tire.width}, status=200)

        except Exception:
            pass


