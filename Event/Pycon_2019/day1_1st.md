# 변수



## immutable VS mutable

* immuatable: 값변경 ==> 새로운 객체 생성



## class VS instance

* 주의: 클래스에 그냥 mutable 객체를 쓰면 모든 instance가 해당 리스트를 공유함
* Solution: `self.`를 붙혀서 **인스턴스 변수**로 써야
* 클래스 변수 접근은 클래스명으로 함
* 클래스변수: 인스턴스화 되는 시점에 같은 값을 조회
* 인스턴스 변수: 객체간 용유하지 않는 변수



## global, local, non-local

* non-local: 함수 밖이지만, 전역은 아님
* global: 전역



## PEP8

* 언더스코어
* 언더스코어 2개: 맹글링



## 구글 파이썬 코드 스타일 가이드

* __:를 사용하지 않을것을 권장