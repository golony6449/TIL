# 인증 (Authenticate)

## 예상 시나리오

* 로그인 -> 인증결과 -> 메인 -> 로그아웃
* 회원가입 -> 회원가입 결과 -> 로그인
* 인증 -> DAO 



## 로그인 여부 확인

* Session에 특정값(`id`)가 존재하는지 확인



## 로그인 & 회원가입 페이지

* submit으로 로그인  처리 페이지에 폼 전달
* 회원 가입은 Javascript를 이용해 버튼 클릭시 이동



## 회원가입 처리

* DAO 객체를 이용해 DB에 접근 ==> 매개변수, 반환형은 대개 DTO
* 매개변수로 전달된 값을 이용해 DB에 추가
* 기본적인 값 검증은 Javascript를 이용해 Client단에서 처리
* DAO에서 DTO를 이용해, 서버측 값 검증 수행
* `<jsp:setProperty name="tdo" property="*"/>`
* DAO의 생성자는 `private` ==> 자신클래스를 반환하는 객체 
* 싱글턴 패턴: 인스턴스를 하나만 만들어 사용하기 위한 패턴



## 로그인 처리

* Javascript `history` 객체: 사용 기록 관련 객체

