SECRET_KEY = 'my_orange_123'

DATABASES = {
    'default' : {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cardoc',
        'USER': 'root',
        'PASSWORD': '1234',
        'HOST': '127.0.0.1',
        'PORT': '3306',
				'OPTIONS': {'charset': 'utf8mb4'}
    }
}
