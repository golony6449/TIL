Django Web Framework: 장고 웹 프레임워크
===================

# 1. 특징
작성중

# 2. 설치법
## 2.1 설치
작성중

# 3. 개발방식

## 3.1. MTV 모델
#### <b> Model - Template - View </b>

Model: 데이터베이스에 저장되는 데이터
Template: 사용자에게 보여지는 부분
View: 실질적인 프로그램 로직

* 처리순서
1. 요청 받은 URL 분석해 처리 할 View 결정 (in URLconf)
2. View 실행, 필요시 Model에 DB처리 요청 및 결과 반환받음
3. 로직 처리 완료 후 Template를 이용, 전송 할 HTML 작성
4. 클라이언트로 송신

### 3.1.1. Model(모델) - 데이터베이스 설계
작성중
### 3.1.2. Temlplate(템플릿) - 화면 UI 설계
작성중
### 3.1.3. View(뷰) - 로직 설계
작성중

## 개발
* 모든 어플리케이션은 설정파일(settings.py)에 지정되어야 함
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    <b>'polls',</b>
]
```

### 애플리케이션 개발 - Model 코딩
* 사용할 DB 지정 - 프로젝트 폴더 내의 settings.py
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```

### 테이블 정의
* 필요한 DB 테이블, 컬럼 생성 in models.py (어플리케이션 내)
* 1개의 테이블 = 1개의 클래스, 1개 컬럼 = 1개의 클래스 변수
* 클래스 정의시 django.db.models.Model 을 상속받아 정의
* 클래스 변수 타입 또한 장고에서 미리 정의 된 필드 클래스 사용

* 유의사항
1. PK(primary key)는 테이블명의 소문자를 접두어로하는 Not Null, Autoincrement 속성을 자동으로 장고에서 만듦
2. FK(foreign key)는 항상 다른 테이블의 PK와 연결됨

#### Admin page에 반영
* 어플리케이션 내의 admin.py에 등록
```python
admin.site.register(Question)
admin.site.register(Choice)
```

#### DB에 변경사항 반영
* 테이블 생성, 정의 변경 시에 이를 DB에 반영해주는 작업 필요
* <b> Why? ORM기반  (앱 - ORM - DB) </b>
```
python manage.py makemigrations
python manage.py migrate
```

* 장고에서 DB에 반영할 때 사용하는 SQL 문장 확인 방법
'''
python manage.py sqlmigrate polls 0001
'''

### 애플리케이션 개발 - View, Templete 코딩
#### URLconf - URL/뷰 매핑
    urls.py에 저장됨
    주) URL과 뷰는 1:1 관계로 매핑

<b> url() </b>
필수 인자: regex, view
* regex - url을 정규표현식으로 표현. 뷰 함수에 넘겨줄 파라메터 추출 가능.
* view - URL 매칭시 호출 할 뷰 함수 지정. 인자로 HttpRequest, regex에서 추출한 항목 전달
* kwargs - 추출한 파라메터 외에 전달할 추가적인 인자. 데이터타입 - Dictionary
* name - 각 URL 별로 붙일 이름. 템플릿 파일에서 사용됨
* prefix - 뷰 함수에 대한 접두사

정의 방법
1. 프로젝트 폴더 안의 urls.py에 직접 정의
2. 앱의 urls.py 정의 후 프로젝트 폴더의 urls.py에서 해당 urls.py를 include (recommended)
이유: 재사용, 유지보수 용이
* include()의 namespace 파라메터: 패턴의 이름간 충돌 방지
namespace:이름 형태로 구분

#### 뷰함수, 템플릿 작성
* 뷰함수 - URL에 따른 요청에 실행되는 함수
render(request,html파일,변수)
이때, 변수는 사전 타입 자료형