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
```
python manage.py sqlmigrate polls 0001
```

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

namespace: 이름 형태로 구분

#### 뷰함수, 템플릿 작성
* 뷰함수 - URL에 따른 요청에 실행되는 함수

render(request,html파일,변수)

이때, 변수는 사전 타입 자료형

# 4. 주요기능
## 4.1. DB 다루기
### 4.1.1. Admin 사이트 변경
<b> admin.py </b>

models.py에서 정의한 테이블(필드)에 따라 해당 테이블을 조작할 수 있는 UI를 보여줌

-> admin 페이지에서 CRUD 가능

History, 현재시간 등에서 시간이 맞지 않을때는 settings.py의 TIME_ZONE 세팅 확인

* 테이블 변경 UI 양식 변경 - admin.py
예시 - Question 클래스(테이블)의 UI 변경
```python
class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question_text']

admin.site.register(Question,QuestionAdmin)
```

* 테이블 변경 UI에서 각 필드 별로 분리
예시 - Question 클래스(테이블)의 필드 입력 UI를 분리
```python
fieldsets=[('Question Statement', {'fields':['question_text']}),
            ('Date Infomation', {'fields':['pub_date']})]
```

* <b> 주의) fields, fieldsets는 둘 중 하나만 정의 가능 (2개 다 설정시 오류 발생) </b>

* 테이블 변경 UI에서 각 필드 접기(folding)
```python
('Date Infomation', {'fields':['pub_date'], 'classes': ['collapse']})
```

#### <b>[('필드명', {옵션 : [값], 옵션 : 값})] - 튜플안에 (필드명, {옵션}) 으로 묶어서 사용 </b>

* 외래키 관계 화면
Choice 테이블은 Question 테이블의 question_text를 외래키로 사용

두 테이블을 같이 보면서 수정하는 방법
<b> Question 테이블을 기준으로 여러개의 Choice가 연결 -> Question 클래스 수정 </b>

```python
class ChoiceInline(admin.StackedInline):
    model=Choice
    extra=2

class QuestionAdmin(admin.ModelAdmin):
    #fields = ['pub_date', 'question_text']
    fieldsets=[(None, {'fields':['pub_date']}),
               ('Question Statement', {'fields':['question_text'],'classes': ['collapse']})]
    inlines=[ChoiceInline]
```

테이블 형식으로 UI 변경
```python
class ChoiceInline(admin.StackedInline)
```
->
```python
class ChoiceInline(admin.TabularInline)
```

* 테이블 리스트에서 각 레코드의 제목(컬럼 이름) 지정
Default: models.py의 __unicode()__ 함수 리턴 값

```python
class QuestionAdmin(admin.ModelAdmin):
    list_display=('속성이름','속성이름')
```

* UI에 필터 사이드바 추가
지정한 필드에 따라 적절한 옵션항목 제공
```python
class QuestionAdmin(admin.ModelAdmin):
    list_filter = ['pub_date']
```

* UI에 검색박스 추가
지정한 필드에서 입력된 키워드를 Like 쿼리로 검색
```python
class QuestionAdmin(admin.ModelAdmin):
    search_fields=['question_text']
```

* Admin 사이트 템플릿 변경
Django의 기본 admin 템플릿을 프로젝트로 가져온 뒤, 수정해 적용

이유는 모르겠지만 적용 안됨 ㅠㅠ
##### 수정 예정

### 장고 파이썬 쉘로 데이터 조작하기
* Admin 사이트 접속 불가능 상황시 or 다양한 데이터 관리 명령 사용시 사용

간단한 처리는 Admin 사이트에서 처리 -> 복잡한 처리 or 웹서버 접속상태일때 쉘을 이용해 처리

쉘 실행
```
python manage.py shell
```

* 파이썬 쉘과의 차이점: manage.py에서 정의한 DJANGO_SETTING_MODULE 속성을 이용해 mysite/setting.py를 임포트

#### CRUD
#####Create - 데이터 생성/입력
1. 필드값 지정(객체 생성)
2. save()메소드 호출
```python
from polls.models import Question, Choice
from django.utils import timezone
q=Question(question_text="What's new?", pub_date=timezone.now())    #객체 생성
q.save()    #저장
```

#####Read - 데이터 조회
* QuerySet 객체 사용 - DB 테이블에서 가져온 객체 콜랙션

(다수의 객체를 모아 각각의 객체를 동일 한 방식으로 다룰 수 있게 해주는 데이터구조)

* QuerySet은 필터를 가질수 있음 -> 필터를 이용해 조건에 맞는 레코드만 추출

| QuerySet | QuerySet의 필터 |
|----------|----------------|
| SELECT문 | WHERE, LIMIT문 |

QuerySet 객체 생성 - objects객체 사용
```python
Question.objects.all()  #테이블.레코드.조건
```

* 조건 (QuerySet의 메소드)
1. filter() 메소드: 주어진 조건에 맞는 객체들을 담고있는 QuerySet 반환
2. exclude() 메소드: 주어진 조건에 맞지않는 객체들을 담고있는 QuerySet 반환
3. get() 메소드: 1개의 요소만을 검색하는 경우

* 배열 슬라이싱 문법 사용 가능 - 요소의 갯수 제한 ex)Question.objects.all()[5:10]

#####Update - 데이터수정
1. 필드의 속성값 수정
2. save() 메소드 호출
#작성중
```python
from polls.models import Question, Choice
from django.utils import timezone
q=Question    #객체 생성
q.question.question_text='What is your favorite hobby?'
q.save()    #저장
```