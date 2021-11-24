import jwt

from django.http import JsonResponse

from users.models    import User
from my_settings     import SECRET_KEY

def authorization(func):
    def wrapper(self, request, *arg, **kwargs):
        try:
            bearer_token = request.headers.get("Authorization", None)

            if not bearer_token:
                return JsonResponse({"message": "TOKEN_DEOS_NOT_EXIST"}, status=401)

            if not bearer_token.startswith("Bearer "):
                return JsonResponse({"message": "AUTHENTICATION_ERROR"}, status=401)

            access_token = bearer_token.split()[1]
            payload      = jwt.decode(access_token, SECRET_KEY, "HS256")
            user         = User.objects.get(id=payload["id"])
            request.user = user

        except jwt.exceptions.DecodeError:
            return JsonResponse({"message" : 'INVALID_TOKEN' }, status = 401)

        except jwt.exceptions.ExpiredSignatureError:
            return JsonResponse({"message" : 'TOKEN_EXPIRED'}, status = 401)

        except User.DoesNotExist:
            return JsonResponse({"message": "INVALID_USER"}, status=404)

        return func(self, request, *arg, **kwargs)

    return wrapper
