import json

from django.http import response
import bcrypt
import jwt
from datetime import datetime, timedelta

from django.test import TestCase, Client

from .models     import User
from my_settings import SECRET_KEY

class SignUpViewTest(TestCase):
    def setUp(self):
        user = User.objects.create(
            email    = "abcd1234@gmail.com",
            password = "abcd123!@",
            name     = "orange"
        )

    def tearDown(self):
        User.objects.all().delete()

    def test_post_sign_up_success(self):
        client = Client()
        data   = {
            "name"     : "test_name_1",
            "email"    : "test1@naver.com",
            "password" : "test1234!@"
        }
        
        response = client.post(
            '/users/signup', json.dumps(data), content_type = "application/json"
        )

        self.assertEqual(response.json(), {"message" : "CREATED"})
        self.assertEqual(response.status_code, 201)

    def test_post_sign_up_email_validation_error(self):
        client = Client()
        data   = {
            "name"   : "test_name_2",
            "email"  : "test.com",
            "password" : "test1234!@"
        }

        response = client.post(
            '/users/signup', json.dumps(data), content_type = "application/json"
        )

        self.assertEqual(response.json(), {"message" : "VALIDATION_ERROR"})
        self.assertEqual(response.status_code, 400)

    def test_post_sign_up_password_validation_error(self):
        client = Client()
        data   = {
            "name"   : "test_name_2",
            "email"  : "test@naver.com",
            "password" : "test123"
        }

        response = client.post(
            '/users/signup', json.dumps(data), content_type = "application/json"
        )

        self.assertEqual(response.json(), {"message" : "VALIDATION_ERROR"})
        self.assertEqual(response.status_code, 400)

    def test_post_sign_up_user_already_exist(self):
        client = Client()
        data   = {
            "name"   : "test_name_2",
            "email"  : "abcd1234@gmail.com",
            "password" : "test123!@"
        }

        response = client.post(
            '/users/signup', json.dumps(data), content_type = "application/json"
        )

        self.assertEqual(response.json(), {"message" : "USER_ALREADY_EXIST"})
        self.assertEqual(response.status_code, 409)

    def test_post_sign_up_key_error(self):
        client = Client()
        data   = {
            "nameaaa"   : "test_name_2",
            "email"  : "abcd124@gmail.com",
            "password" : "test123!@"
        }

        response = client.post(
            '/users/signup', json.dumps(data), content_type = "application/json"
        )

        self.assertEqual(response.json(), {"message" : "KEY_ERROR"})
        self.assertEqual(response.status_code, 400)

    
class SignInViewTest(TestCase):
    def setUp(self):
        password         = "test1234!@"
        hashed_password  = bcrypt.hashpw(
            password.encode("utf-8"), bcrypt.gensalt()
        )
        decoded_password = hashed_password.decode("utf-8")

        user = User.objects.create(
            name     = "sch",
            email    = "test123@gmail.com",
            password = decoded_password
        )

        self.access_token = jwt.encode(
            {
                "id"  : str(user.id),
                "exp" : datetime.utcnow() + timedelta(days = 3)
            }, SECRET_KEY, algorithm = "HS256"
        )

    def tearDown(self):
        User.objects.all().delete()

    def test_post_sign_in_success(self):
        client = Client()
        data   = {
            "email"    : "test123@gmail.com",
            "password" : "test1234!@"
        }

        response = client.post(
            '/users/signin', json.dumps(data), content_type = "application/json"
        )

        self.assertEqual(response.json(), {
            "message" : "SUCCESS",
            "access_token" : self.access_token
        })
        self.assertEqual(response.status_code, 200)
