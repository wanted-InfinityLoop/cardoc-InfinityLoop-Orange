# Wanted X Wecode PreOnBoarding Backend Course

원티드 4주차 기업 과제 :  Cardoc Individual Assignment Project
✅ 카닥 기업 과제입니다.

<br>
<br>


# 🔖 목차
- 과제 내용
- 기술 환경 및 tools
- 모델링 ERD
- API 명세서
- 기능 구현 추가설명
- 설치 및 실행 방법


<br>
<br>

# 📖 과제 내용    

## 1. 배경 및 공통 요구사항

<aside>
    
> 
    😁 **카닥에서 실제로 사용하는 프레임워크를 토대로 타이어 API를 설계 및 구현합니다.**

</aside>

- 데이터베이스 환경은 별도로 제공하지 않습니다.
 **RDB중 원하는 방식을 선택**하면 되며, sqlite3 같은 별도의 설치없이 이용 가능한 in-memory DB도 좋으며, 가능하다면 Docker로 준비하셔도 됩니다.
- 단, 결과 제출 시 README.md 파일에 실행 방법을 완벽히 서술하여 DB를 포함하여 전체적인 서버를 구동하는데 문제없도록 해야합니다.
- 데이터베이스 관련처리는 raw query가 아닌 **ORM을 이용하여 구현**합니다.
- Response Codes API를 성공적으로 호출할 경우 200번 코드를 반환하고, 그 외의 경우에는 아래의 코드로 반환합니다.

### **[필수 포함 사항]**

- README 작성
    - 프로젝트 빌드, 자세한 실행 방법 명시
    - 구현 방법과 이유에 대한 간략한 설명
    - 완료된 시스템이 배포된 서버의 주소
    - Swagger나 Postman을 통한 API 테스트할때 필요한 상세 방법
    - 해당 과제를 진행하면서 회고 내용 블로그 포스팅
- Swagger나 Postman을 이용하여 API 테스트 가능하도록 구현



### **[기능 개발]**

✔️ **REST API 기능**

- User 회원가입 및 로그인 기능 구현
- 유저가 소유한 자동차의 타이어 정보 저장하는 기능 구현
- 유저가 소유한 자동차의 타이어 정보 조회하는 기능 구현

<br>
<br>

# ➡️ Deploy URL(AWS EC2)

<br>
<br>

# ⚒️ 기술 환경 및 tools
- Back-End: Python 3.9.7, Django 3.2.9
- Deploy: AWS EC2, RDS
- ETC: Git, Github, Postman

<br>
<br>

# 📋 모델링 ERD

`cardoc.drawio.png` 파일 참조

<br>
<br>

# 🌲 디렉토리 구조
```
.
├── PULL_REQUEST_TEMPLATE.md
├── README.md
├── __pycache__
│   └── my_settings.cpython-39.pyc
├── cardoc
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── cardoc.drawio.png
├── cars
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── concurrents.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── 0002_auto_20211123_1802.py
│   │   ├── 0003_auto_20211123_1806.py
│   │   ├── 0004_auto_20211123_1905.py
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       ├── 0001_initial.cpython-39.pyc
│   │       ├── 0002_auto_20211123_1802.cpython-39.pyc
│   │       ├── 0003_auto_20211123_1806.cpython-39.pyc
│   │       └── 0004_auto_20211123_1905.cpython-39.pyc
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── core
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   ├── utils.py
│   ├── validations.py
│   └── views.py
├── db.sqlite3
├── manage.py
├── my_settings.py
├── requirements.txt
└── users
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── migrations
    │   ├── 0001_initial.py
    │   ├── 0002_auto_20211123_1802.py
    │   ├── 0003_alter_user_id.py
    │   └── 0004_alter_user_id.py
    ├── models.py
    ├── tests.py
    ├── urls.py
    └── views.py
```

<br>
<br>

# 🔖 API 명세서

[Postman API Document](https://documenter.getpostman.com/view/17231503/UVJZndcH)

<br>

### 👉 회원가입/로그인

[회원가입]

- Method: POST
```
http://3.38.118.39:8000/users/signup
```

<br>

- parameter : request_body
```
{
    "name": "관리자2",
    "email": "hayejun10@server.co.kr",
    "phone_number": "010-2222-3333"
}
```

<br>

- response
```
{
    "message": "SUCCUESS"
}
```

<br>

[로그인]

- Method: POST
```
http://3.38.118.39:8000/users/signin
```

<br>

- parameter : request_body

```
{
    "email": "hayejun1013@naver.com",
    "phone_number": "010-2723-4713"
}
```

<br>

- response
```
{
    "message": "Success",
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiOWNlZjllMDItMTA2ZC00MjQ4LWIyMTItMzUyMjc1OTBlYzFjIn0.8ubSxYVGeyGAjgGkb1DxCsc9uw2i27ihhksFBhlJ3Mg"
}
```

<br>

### 👉 킥보드 대여 기능

1. 로그인 한 유저가 대여할 킥보드를 요청한다.
2. 로그인 한 유저의 유효성 검증 후 존재하지 않는 유저의 경우 에러 메시지를 반환한다.
3. 존재하지 않는 킥보드시 에러 메시지를 반환한다. 

<br>

- Method: POST
```
http://3.38.118.39:8000/vehicles/lend
```

<br>

- header : Bearer token
- parameter : request_body
```
{
    "deer_name": "씽씽이"
}
```

<br>

- response 

```
{
    "message": "SUCCESS"
}
```

<br>

### 👉 서비스 지역 추가 기능


- Method: POST

```
http://3.38.118.39:8000/areas/service/f48d910f42cd487c89921fa6f8fee579
```

<br>

- header : Bearer token
- parameter : request_body


```
{
    "name": "여의도_2",
    "boundary": [
        [
            126.9191962480545,
            37.52151216125405
        ],
        [
            126.9208323955536,
            37.52151216125405
        ],
        [
            126.9208323955536,
            37.52279280068019
        ],
        [
            126.9191962480545,
            37.52279280068019
        ],
        [
            126.9191962480545,
            37.52151216125405
        ]
    ],
    "center": [
        126.92001700401306,
        37.52213333794024
    ],
    "code": []
}
```

<br>

- response

```

```

<br>

### 👉 할인/벌금 요금 조건 추가기능

[할인요금 추가]

1. 관리자가 할인 요금 조건을 추가하기 위해 요청한다.
2. 관리자 외 유저가 요금을 추가할 시 에러를 반환한다.
3. 할인요금 코드형식이 다를 시 에러를 반환한다.
4. 이미 존재하는 할인요금시 에러를 반환한다.

<br>

- Method: POST
```
http://3.38.118.39:8000/charges/discount
```

<br>

- header : Bearer token
- parameter : request_body


```
{
    "code": "D-P-7",
    "number": 10,
    "description": "파킹 할인 유형7"
}
```

<br>

- response   

```
{
    "message": "SUCCESS"
}
```

<br>

[벌금요금 추가]

1. 관리자가 벌금요금 조건을 추가하기 위해 요청한다.
2. 관리자 외 유저가 요금을 추가할 시 에러를 반환한다.
3. 벌금요금 코드형식이 다를 시 에러를 반환한다.
4. 이미 존재하는 벌금요금시 에러를 반환한다.

<br>

- Method: POST
```
http://3.38.118.39:8000/charges/penalty
```

<br>

- header : Bearer token
- parameter : request_body


```
{
    "code": "P-P-19",
    "number": 1000,
    "description": "파킹 벌금 유형1"
}
```

<br>

- response   

```
{
    "message": "SUCCESS"
}
```

<br>

### 👉 할인/벌금 요금 조건 수정기능

[할인요금 수정]

1. 관리자가 할인 요금 조건을 수정하기 위해 요청한다.
2. 관리자 외 유저가 요금 수정 시 에러를 반환한다.
3. 할인조건에 대한 id가 없을 시 에러를 반환한다.

<br>

- Method: POST
```
http://3.38.118.39:8000/charges/discount/D-P-1
```

<br>

- header : Bearer token
- parameter : request_body
- path parameter : 요금code


```
{
    "number" : 30,
    "description" : "주차존 반납"
}
```

<br>

- response   

```
{
    "message": "SUCCESS"
}
```

<br>

[벌금요금 수정]

1. 관리자가 벌금 요금 조건을 수정하기 위해 요청한다.
2. 관리자 외 유저가 요금 수정 시 에러를 반환한다.
3. 벌금조건에 대한 id가 없을 시 에러를 반환한다.

<br>

- Method: POST
```
http://3.38.118.39:8000/charges/penalty/P-P-1
```

<br>

- header : Bearer token
- parameter : request_body
- path parameter : 요금code


```
{
    "number" : 6000,
    "description" : "반납금지지역 반납"
}
```

<br>

- response   

```
{
    "message": "SUCCESS"
}
```

<br>


### 👉 서비스 지역에 할인/벌금 요금 추가

1. 관리자가 지역에 할인/벌금요금을 추가하기 위해 요청한다.
2. 관리자 외 유저가 요금 추가 시 에러를 반환한다.
3. 할인/벌금조건에 대한 id가 없을 시 에러를 반환한다.
4. 존재하지 않은 요금 코드시 에러를 반환한다.
5. 존재하지 않은 지역시 에러를 반환한다.

<br>

- Method: POST

```
http://3.38.118.39:8000/areas/event?region=강남  
```

<br>

- header : Bearer token
- parameter : request_body
- query parameter : 지역 name


```
{
    "code": "P-P-5"
}
```

<br>

- response 

```
{
    "message": "SUCCESS"
}
```

<br>


### 👉 서비스 지역에 할인/벌금 요금 수정

1. 관리자가 지역에 할인/벌금요금을 수정하기 위해 요청한다.
2. 관리자 외 유저가 요금 수정 시 에러를 반환한다.
3. 할인/벌금조건에 대한 id가 없을 시 에러를 반환한다.
4. 존재하지 않은 요금 코드시 에러를 반환한다.
5. 존재하지 않은 지역시 에러를 반환한다.

<br>

- Method: POST

```
http://3.38.118.39:8000/areas/ 
```

<br>

- header : Bearer token
- parameter : request_body
- query parameter : 지역 name


```
{
    "code": "P-P-5"
}
```

<br>

- response 

```
{
    "message": "SUCCESS"
}
```

<br>

### 👉 킥보드 반납 기능


- Method: POST

```
http://3.38.118.39:8000/charges/<str:vehicle_id>  
```

<br>

- header : Bearer token
- parameter : request_body
- path parameter : 킥보드 id


```
{
    "code": "P-P-5"
}
```

<br>

- response 

```
{
    "message": "SUCCESS"
}
```

<br>
<br>

# ➕ 기능 구현 추가설명

### [111111]

<br>

### [222222]

<br>

# 🔖 설치 및 실행 방법

### 로컬 및 테스트용
1. 해당 프로젝트를 clone하고, 프로젝트로 들어간다.
```
https://github.com/wanted-InfinityLoop/deer-InfinityLoop.git .
cd deer
```

2. 가상환경으로 miniconda를 설치한다. [Go](https://docs.conda.io/en/latest/miniconda.html)

```
conda create -n deer python=3.9
conda actvate deer
```   

3. 가상환경 생성 후, requirements.txt를 설치한다.

```
pip install -r requirements.txt

Django==3.2.9
django-cors-headers==3.10.0
gunicorn==20.1.0
mysqlclient==2.1.0
PyMySQL==1.0.2
bcrypt==3.2.0
PyJWT==2.3.0

```


4. migrate 후 로컬 서버 가동
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```



