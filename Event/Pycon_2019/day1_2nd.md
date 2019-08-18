# 하나의 Django 코드로 여러 사이트 운영하기

* sites 프레임워크
* 동일 로직이지만 DB 등 서비스 룬리가 필요할때
* DB에서 사이트 지정



## 활성화

* INSTALLED_APP 추가
* migration
* 기본 사이트 지정
* 로컬 개발시에는 hosts에 지정해 테스트 수행



## 미들웨어

* 요청 응답을 가로 채 특정 작업 수행
* 2가지 추가 필요
* 미들 웨어 클래스는 `__call__` 메서드에서 도메인에 따라 `site_id`를 수정



## 설정

* `__call__` 메서드에서 `settings` 파일을 불러와 적용
* 적용: `setattr(settings, field, new_value)`
* 기본 설정을 다른 값으로 override 하는 것
* `urls.py`도 마찬가지



## 템플릿 불러오기

* 사이트 별로 다른 템플릿 사용의 예
* `multisite.template_loaders.MultiSiteLoader`를 `Template`의 `loaders`에 추가
* 만약 커스텀하게 설정하는 상황에서는 장고 기본 로더 2개를 추가해야 함
* `yelid` 지시자는 뭘까?
* Loader를 상속받아 커스텀 로더 작성
* Static Finder?
* Static 또한 도메인 별 분리가 가능해 보임
* 사이트 별 리소스 불러오기





* 모든 세팅은 `overload` 아래에 도메인 별로 존재하도록 디렉토리 구성
* 