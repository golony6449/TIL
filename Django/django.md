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

### 3.1.1 Model(모델) - 데이터베이스 설계


