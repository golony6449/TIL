# REST API 문서

## 문서의 필요성

* 많은 수의 API
* 많은 사용자
* 서버와 프론트 개발이 분리됨



## 구성요소

* 소개, 라이센스, 호스트
* 인증방법, URI, method



## OpenAPI Specification

* API내용을 사람, 컴퓨터가 모두 읽을수있도록 구조화
* JSON, YAML
* Swagger ==> OpenAPI Specification
* Swagger: API 개발을 돕는 프로젝트 (Codegen, Editor, UI)
* 이때 UI가 JSON/YAML을 API문서로 렌더링



## Code ==> YAML

* 구성요소: 서버, 라우팅 정보, 요청 변수, 응답 형식
*  서버정보: 직접 적어주기
* 라우팅: urls.urlpatterns
* 요청: View, Model
* 응답: View, Model
* Django:  View Class에서 폼, 모델 정보 파악
* Flask, Django 모두 별도의 확장 필요 ㅠㅠ



## Django

* DRF 사용
* Serializer: 값 검증, DB 저장 등 가능
* OpenAPI schema를 기본제공 하나, 단점 있음
* DRF Yet another Swagger generator: 유일



### DRF YASG

* 설정된 serializer로 request, response 생성
* `generator.get_schema()`
* 한계: read_only, write_only 인식 못함, serializer 필수, 기본 UI가..., OpenAPI Spec이 `v2`



### 구현

* `get_schema_view()` ==> 이를 `urlpatterns`에 연결
* Meta class?
* 거~~~의 문서 자동화 가능. 
* serializer에서만 관련정보를 가져옴. 이때는 별도의 schema 작성 필요



## Flask

* `Flask-RESTful ` ,`Flask-RESTPlus`
* Flask RESTful Swagger (사실상 deprecated)
* SQLAlchemy Flask RESTful: Model과 직접관련되지 않은 method는 docstring에 의지
* Resource 단위로 뷰 생성



## 결론

* 어떻게든 YAML로 생성하면 나머지는 알아서 됨
* 