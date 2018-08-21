# Legacy_Django

## 대부분
* Java, JS로 이루어진 코드 베이스
* 많은 수의 테이블
* Python을 일부 사용하고 싶음

## Integrating
* inspectdb ==> 기존의 DB로 model.py를 생성 ==> legacy에 Django 도입 가능

## 기존 시스템에 Django 도입
### 2개의 DB 연결
* 기존 + Django 구동에 필요한 DB

### inspectdb
* 스크립트를 만들어 자동화 (기존의 DB와 동기화)
* 임시파일을 거쳐서 생성
* 기존 시스템의 로그인정보를 활용, 기존 어드민을 그대로 사용

* 어드민에 모델 등록 (inspect 모듈을 이용해 자동화)

### 기존의 inspectdb를 확장
* 기본적으로는 모든 필드를 require로 지정 => 해당 부분 추가
* bollean을 textarea type으로 변환 => 관련 설정