# Cookie

* 연결이 끊어질때 정보를 유지하기 위해 정보를 저장
* 4KB, 300개 까지 저장
* 서버 요청시 같이 전송됨
* 로컬상에 저장되기 때문에 보안문제 존재함



## 적용

1. 쿠키 객체 생성
2. 속성 설정
3. 쿠키 탑재 `response.addCookie()`



### 속성

* `setMaxAge()`: 초 단위
* `setPath()`: 쿠키를 사용할 수 있는 디렉토리 지정 (자주 사용되지 않음)
* `setValue()`
* `setVersion()`
* `getMaxAge()`
* `getName()`
* `getPath()`
* `getValue()`
* `getVersion()`



## 로그인 구현

1. 로그인 시도
2. 성공시, 쿠키에(or 세션에) 유저 정보(ID 등) 저장
3. 리다이렉트
4. 쿠키에 유저정보가 있다면, 로그인 상태로 간주



## 로그아웃 구현

1. 사전에 지정된 유저정보가 포함된 Name 삭제

# Session

* 서버와의 관계를 유지하기 위한 수단
* 서버상에 존재 ==> 비교적 높은 보안성
* 접속 클라이언트 1개당 1개의 세션을 자동으로 생성



## Java 코드상에서 Session 객체 생성

`HttpSession httpSession = request.getSession()`



## Method

* `setAttribute()`
* `getAttribute()`
* `getAttributeNames()`: Enumerate 객체 반환
* `getId()`: 유니크한 세션 값 확인
* `isNew()`: 최초 생성 여부 확인
* `getMaxInactiveInterval()`: web.xml에서 기본값 수정 가능
* `removeAttribute()`
* `Invalidate()`: 모든 데이터 제거
* `request.isRequestedSessionIdValid()`: 세션이 유효한지 확인

