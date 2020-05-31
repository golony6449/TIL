# OAuth

## 개요

* Open Authorization
* 서비스 제공자의 유저 정보를 비밀번호 제공 없이 Third Party에서 인증 할 수 있도록 하는 프로토콜



## 용어

* User: Service Provider에 계정이 있는, Consumer를 이용하려는 사용자
* Service Provider: OAuth API를 제공하는 서비스 제공자(FB, Google. Github......)
* Protected Resource: Service Provider로 부터 제공되는 API 자원
* Comsumer: OAuth 인증을 사용해 SP의 기능을 사용하려는 앱, 서비스
* Consumer Key: Consumer가 SP에게 자신을 식별하기위해 사용하는 키
* Consumer Secret : Consumer Key의 소유권 확립을 위해 사용
* Request Token: Consumer가 SP에게 접근권한 인증을 위해 사용하는 값. 인증 후 Access Token으로 교환
* Access Token: 인증 후 Consumer가 SP의 자원에 접근하기위한 키
* Token Secret: 주어진 토큰의 소유권 인증을 위한 Secret (Consumer가 사용)

## Ref

* https://minwan1.github.io/2018/02/24/2018-02-24-OAuth/
* https://d2.naver.com/helloworld/24942