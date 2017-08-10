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
##### Create - 데이터 생성/입력
1. 필드값 지정(객체 생성)
2. save()메소드 호출
```python
from polls.models import Question, Choice
from django.utils import timezone
q=Question(question_text="What's new?", pub_date=timezone.now())    #객체 생성
q.save()    #저장
```

##### Read - 데이터 조회
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

##### Update - 데이터수정
1. 모델 객체 생성
2. 필드의 속성값 수정
3. save() 메소드 호출
#작성중
```python
from polls.models import Question, Choice
from django.utils import timezone
q=Question.objects.get(조건)    #객체 생성
q.question.question_text='What is your favorite hobby?'
q.save()    #저장
```

##### Delete - 데이터 삭제
```python
Question.objects.filter(pub_date=2005).delete() #pub_date 필드 값(연도)이 2005년인 모든 객체 삭제
Question.objects.objects.all().delete() # Question 테이블의 모든 객체 삭제
Question.objects.delete() # Django에서 허용하지 않는 문장 (의도치 않은 모든 레코드 삭제를 막기 위한 안전장치)
```

##### 실습
* 2개의 테이블이 1:N 관계인 경우 choice_set() API를 사용
* __(언더바 2개)를 이용해 객체 간의 관계를 표현할 수 있음

##### 여러가지 쉘 명령어 예제
```python
Question.objects.all() # Question 테이블의 모든 레코드 반환
Question.objects.get(question_text="What's wrong") # Question 테이블에서 question_text 컬럼이 What's wrong인 튜플 반환
Question.objects.filter(question_text_startswith='What') # Questin테이블의 question_text 컬럼에서 What으로 시작하는 모든 튜플 반환
Choice.objects.filter(question__pub_date__year=current_year) # pub_date가 올해인 Question객체(테이블)에 연결된 Choice 객체 전부를 반환
```

### 템플릿 시스템
* UI를 담당
* 렌더링: 템플릿 코드 -해석> 템플릿파일(HTML,CSV,XML)

##### 템플릿 변수
```python
{{ variable }}
```

* Dot(.)의 역할 (ex: foo.bar)
1. foo가 사전타입인지 확인 -> 사전타입이면 foo['bar']로 해석
2. foo의 속성 검색 -> bar라는 속성이 있을때는 foo.bar로 해석
3. foo가 list인지 확인 -> list라면 foo[bar]로 해석

#### 템플릿 필터
* 객체, 처리결과에 추가적인 명령 적용 -> 해당 명령에 맞게 최종 결과 변경하는 것을 의미

ex)
```python
{{ name|lower }} # name변수값을 모든 문자를 소문자로 바꿔주는 필터
{{ text|escape|linebreaks }} # 필터를 체인으로 연결할 수도 있음
```

* 인자를 가지는 필터
```python
{{ bio|truncatewords:30 }} # bio변수 값 중 앞의 30개 단어만 보여주는 필터(특수문자 무시)
{{ list|join:" // " }} # 인자가 빈칸을 가지는 경우
{{ value|default:"nothing" }} # 변수값이 False이거나 없는경우
{{ value|length }} # 변수의 길이 반환
{{ value|striptags }} # 변수값에서 HTML태그를 제거 (100% 보장은 불가능)
{{ value|pluralize }} # 변수가 1이 아닌경우 복수 접미사 s를 붙혀줌 (if 1 -> number, if >1 -> numbers)
```

* 덧셈 필터
```python
{{ value|add:"2" }} # 덧셈 연산 수행
{{ first|add:second }} # 변수끼리의 연산또한 가능
```

* 처음에는 두 변수 모두 정수라고 간주하고 덧셈 시도-> 실패한 경우, 타입이 허용하는 덧셈 수행

1. 두 변수 모두 문자열인 경우 -> 이어 붙임
2. 두 변수 모두 list인 경우 -> 원소별 덧셈 연산 수행
3. 두 변수 모두 정수 -> 덧셈 연산 수행

* 연산에 실패한 경우 빈 문자열 반환

#### 템플릿 태그
* 형식: {% 태그명 %}
* 역할: 텍스트 결과물 생성, 템플릿 로직 제어, 외부파일을 템플릿 내로 로딩

##### 종류
###### {% for %} 태그
* 리스트에 담겨 있는 항목들을 순회
* 예제
```html
<ul>
{% for athlete in athlete_list %}
    <li>{{ athlete.name }}</li>
{% endfor %}
</ul>
```

* for태그에서 사용 되는 변수 이름
| 변수명 | 설명 |
|-------|------|
| forloop.counter | 현재까지의 루프 카운터 (1부터) |
| forloop.counter() | " (0부터) |
| forloop.revcounter | 루프 끝에서 현재까지의 카운터(1부터) |
| forloop.revcounter | " (0부터) |
| forloop.first | 루프에서 첫번째 실행일때 True |
| forloop.last | 루프에서 마지막 실행일때 True |
| forloop.parentloop | 중첩된 루프에서 현재 루프 바로 상위의 루프를 의미 |

###### {% if %} 태그
* 변수를 평가해 True면 <b>바로 아래의 문장</b> 실행
* 예제
```html
{% if athlete_list|length > 10 %}   <!-- 조건식 사용 가능. 단, 대부분의 필터가 스트링을 반환하기 때문에 산술조건 사용시 유의 -->
    Too many athletes (>10)
{% elif athlete_list %}
     Number of athletes: {{ athlete_list|length }}
{% else %}
    No athletes.
{% endif %}
```

###### {% scrf_token %} 태그
* POST 방식의 <form> 사용하는 템플릿 코드에서 CSRF 공격 방어를 위해 사용하는 태그 (악의적 스크립트 대비)
```html
<form action="."method="post">{% csrf_token %}
```

* CSRF 공격이란? -> 이미 인증을 받은 사용자가 공격코드가 삽입된 페이지를 열면, 타겟 사이트는 공격명령이 믿을수 있는 사용자에게서 발송된것으로 판단해, 공격을 받게 되는 방식

###### {% url %}
* 소스코드에 URL을 하드코딩(직접 입력) 하는 것을 막기 위한 태그

* 예제
```html
<form action="{% url 'polls:vote' question.id %}" method="post">
<form action="/polls/3/vote/" method="post">    <!--url 태그를 사용하지 않은 경우-->
```

* 사용하는 이유?
1. URL 변경시 URLconf뿐만 아니라 모든 소스코드에서 해당 부분을 찾아서 변경해야 하는 문제 발생
2. 중간의 '3' 이라는 숫자는 런타임에 따라 변하는 값 -> 별도의 변수처리를 해야하는 번거로움 존재

-> url 태그를 사용하면, URLconf를 변경하는 것만으로 대응 가능

* 사용형식
```html
{% url 'namespace:view-name' arg1 arg2 %}
```

1. namespace: urls.py파일의 include()에서 정의함 이름공간
2. view-name: urls.py파일의 URL 패턴에서 정의한 뷰함수 or 패턴이름
3. argN: 뷰 함수에서 사용하는 인자(Option), 여러 개인 경우 빈칸으로 구분

###### {% with %} 태그
* 특정 값을 변수에 저장해 DB조회와 같은 큰 부하의 동작을 줄이기 위한 태그
* with 태그에서 사용된 변수의 scope: {% with %} ~ {% endwith %}

* 예제
```html
{% with total=business.employees.count %}
{% with business.employees.count as total %}    <!--구버전 문법-->
    {{ total }} people works at business
{% endwith %}
```

###### {% load %} 태그
* 사용자가 정의한 사용자 정의 태그, 필터를 사용하기 전 로딩

##### 템플릿 주석
* 형식
```html
{# greeting #} hello <!--한 문장 or 문장의 일부분 주석처리-->
{% comment %}
    내용
{% endcomment %} <!--해당 범위에 속한 여러 문장 주석 처리-->
```

##### HTML 이스케이프
* 템플릿을 렌더링 할때, 사용 하는 변수에 HTML 테그가 포함 된 경우 원치않는 결과를 유발 할 수 있음
* ex) `name="<b>username"` -> `Hello {{ name }}` -> `Hello <b>username`
* 이러한 문제를 이용해 XSS 공격 수행

* 이러한 보안상 취약점 방지를 위해 Django에서는 자동 이스케이프 기능 제공 -> HTML에서 사용 되는 문자들을 의미를 제거한 문자로 변경

###### 자동 이스케이프 기능 비활성화
* 비활성화 시켜야 하는 경우도 있음 -> HTML 태그를 그대로 출력, 이메일 메세지를 탬플릿으로 출력

* 방법
1. safe 필터를 이용해 해당 변수만 비활성화 -> ex) {{ name|safe }}
2. autoscape 태그를 이용해 전체 or 특정 스코프에서 비활성화 -> ex) {% autoescape off %} ~ {% endautoscape %}

* 주의) 필터의 인자로 사용되는 스트링 리터럴(상수)은 자동 이스케이프 기능 적용 X

##### 템플릿 상속
* 부모 탬플릿은 템플릿을 뼈대 생성 + `{% block %}` 태그를 이용해 하위로 상속 할 부분 지정
* 자식 템플릿은 부모 템플릿에서 생성 한 뼈대 사용 + `{% block %}` 태그 부분 렌더링

* 템플릿 코드 재사용 가능 -> 사이트의 룩앤필의 일관성 유지
* 부모의 block 태그를 모두 채워야 할 필요는 없음 -> 채워지지 않은 블록은 부모의 내용 그대로 사용

* 사이트 전체의 조화로운 룩앤필을 위해 일반적으로 템플릿 상속을 3단계로 사용하는 것을 권장
1. 사이트 전체의 룩앤필 -> base.html
2. base.html을 상속받는 사이트 하위의 섹션별 스타일 -> base_news.html, base_sports.html 
3. 개별 섹션을 상속받는 개별페이지

###### 예시
* 부모
```html
<title>{% block title %}My amazing site{% endblock %}</title>
```

* 자식
```html
{% extends "base.html" %} <!--부모(base.html)로 부터 상속받음을 의미함-->
{% block site %}My amazing blog{% endblock %}
```

###### 주의사항
1. `{% extends %}`태그는 상속 받는 태그보다 위에 기재되어야 함
2. 템플릿의 공통점을 최대한 많이 부모 템플릿에 `{% block %}`이 많을 수록 좋음
3. 부모 템플릿의 내용을 그대로 사용하고 싶을때는, {{ block.super }}변수 사용 (부모T의 내용에 자식T 내용을 추가하는 경우 유용)
4. 가독성을 위해 `{% endblock content %}` 처럼 블록명을 작성해도 무관함

#### 폼 처리하기
##### HTML에서의 폼
* 사용자로 부터 입력을 받기 위해 사용
* `<form> ~~ </form>` 형태로 사용
* 간단한 폼(텍스트입력, 체크박스등)은 HTML의 기본 위젯을 사용 -> 복잡한 요소(달력, 슬라이드바 등)는 CSS, JS를 사용하기도 함
* 입력을 받는 `<input>`요소와 입력받을 데이터를 전달할 곳을 지정하는 action 속성, 어떤 HTML 메소드(GET,POST)로 보낼지 지정하는 method 속성 설정

##### HTML 메소드
* GET: 시스템의 상태를 바꾸지 않는 요청에 사용 -> 보안 위험(로그, 히스토리에 비밀번호 노출)때문에 패스워드 폼에서는 사용하지 않도록 권장
* POST: 서버 시스템의 상태를 바꾸는 요청 (ex: DB 내용 변경) -> 데이터가 URL에 저장되지 않아, 공유, 재전송, 북마크 저장 힘듦

##### Django의 폼 기능
1. 폼 생성에 필요한 데이터를 폼 클래스로 구조화
2. 폼 클래스의 데이터를 렌더링해 HTML 폼 만들기
3. 사용자로 부터 제출된 폼과 데이터를 수신하고 처리하기

##### 폼 클래스
* 폼의 형태, 작동방법, 외형 기술
* 폼 클래스의 필드 - HTML폼의 `<input>`에 맵핑, 필드 자체도 일종의 클래스, 브라우저에서 HTML 위젯으로 표현
* 폼이 제출 되었을때, 자신의 데이터에 대한 유효성 검사 수행

* 장고에서 제공하는 필드 타입: DateField(날짜와 관련된 데이터), FileField(파일과 관련된 데이터)
* 필드 마다 다른 종류의 데이터 처리 -> 유효성 검사 방식, 디폴트 위젯클래스 다름 -> 적절한 타입 사용해야 할 필요 있음

* 폼 또한 템플릿을 일부 -> 템플릿 코드에 포함되어 렌더링 절차 거침
* 폼은 렌더링 이후 사용자가 데이터를 채우는 것이 보통 -> 뷰 함수에서 객체를 생성할 때, 데이터를 없이 할지, 채워서 할지 적절히 구분해서 코딩해야 할 필요 있음
* 폼을 채울때는 모델객체 or 직전에 제출된 HTML 폼으로 부터 채울 수 있음

* 언바운드 폼: 데이터가 없는 폼 -> 폼이 비어있거나, 디폴트 값이 채워진 상태로 렌더링
* 바운드 폼: 사용자로 부터 제출된 데이터를 가지고 있는 폼 -> 유효성검사에 사용

##### 폼 클래스로 폼 생성하기
###### 대략적 플로우
1. 템플릿 작성
2. 