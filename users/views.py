import json
import bcrypt
import jwt
from datetime import datetime, timedelta

from django.views import View
from django.http  import JsonResponse

from .models          import User
from core.validations import (
    email_validator,
    password_validator
)
from my_settings      import SECRET_KEY


class SignUpView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)

            name     = data["name"]
            email    = data["email"]
            password = data["password"]

            if not (email_validator(email) and password_validator(password)):
                return JsonResponse(
                    {"message" : "VALIDATION_ERROR"}, status = 400
                )

            if User.objects.filter(email = email).exists():
                return JsonResponse(
                    {"message" : "USER_ALREADY_EXIST"}, status = 409
                )

            hashed_password  = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
            decoded_password = hashed_password.decode("utf-8")

            User.objects.create(
                name     = name,
                email    = email,
                password = decoded_password
            )

            return JsonResponse({"message" : "CREATED"}, status = 201)

        except KeyError:
            return JsonResponse({"message" : "KEY_ERROR"}, status = 400)


class SignInView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)

            email         = data["email"]
            password      = data["password"]
            CHARACTER_SET = 'utf-8'

            if not User.objects.filter(email = email).exists():
                return JsonResponse({"message" : "INVALID_USER"}, status = 401)

            user = User.objects.get(email = email)

            check_password = bcrypt.checkpw(
                password.encode(CHARACTER_SET), user.password.encode(CHARACTER_SET)
            )

            if not check_password:
                return JsonResponse({"message" : "INVALID_USER"}, status = 401)

            access_token = jwt.encode(
                {"id"  : str(user.id), "exp" : datetime.now() + timedelta(days = 3)}, SECRET_KEY, "HS256")

            return JsonResponse(
                {"message" : "SUCCESS", "access_token" : access_token}, status = 200
            )

        except KeyError:
            return JsonResponse({"message" : "KEY_ERROR"}, status = 400)

            