# View on DRF

## 개요

* Django 기반의 REST API 구성시 사용되는 View



## 지금까지 했던 짓들

* CSRF_TOKEN 관련 오류를 무시하기 위해 함수, 클래스에 `csrf_exempt` 데코레이터 사용
* 권장사항은 확실히 아님



## DRF 모듈 기반 설정

### 요청/응답

* 응답은 Django의 `HttpResponse`, `JsonResponse`가 아닌 `rest_framework.response.Response` 사용
* Django와 거의 유사하지만 요청에 따라 적절한 응답형태를 지정할 수 있음



### Function Based View

* `rest_framework.decorators.api_view` 데코레이터를 함수에 적용
* 데코레이터의 매개변수로 허용할 Method 지정 가능 (`@api_view(['GET', 'POST'])`)



## Class Based View

* Django의 `django.views.View` 대신 `rest_framework.views.APIView`를 상속받아서 CBV 구성가능



### 요청에 따른 응답 형태 지정

1. FBV의 매개변수로 `format=None` 추가 ==> `def snippet_list(request, format=None)`
2. `urls.py`하단에 `urlpatters = format_suffix_patterns(urlpatterns)` 추가



* 헤더(`Content-type`)나 주소(`localhost/snippet.json` or `localhost/snippet.api`)로 Browsable API or JSON 응답 형태 지정 가능