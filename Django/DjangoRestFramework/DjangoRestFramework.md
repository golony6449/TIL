# Django-Rest-Framework

## 개요

* `Django`기반의 REST API 서버를 만들때 사실상 표준인 라이브러리
* 구성요소: `serializer`, `viewset`



## Serializer

* Django ORM의 `QuerySet`을 JSON으로 매핑하는 과정 (참고자료 발췌)
* 응답에 사용할 필드 지정
* 응답에 적용될 옵션 지정



### ModelSerializer vs Serializer

* `Meta` 클래스에 지정된 필드 리스트를 사용해, 쿼리셋에서 값 추출
* 간단한 `create()`, `update()` 메서드를 자동으로 구현
* Serializer: https://www.django-rest-framework.org/tutorial/1-serialization/#creating-a-serializer-class
* ModelSerializer: https://www.django-rest-framework.org/tutorial/1-serialization/#using-modelserializers



## Viewset



## 참고자료

* https://medium.com/wasd/restful-api-in-django-16fc3fb1a238
* https://www.django-rest-framework.org/tutorial/quickstart/