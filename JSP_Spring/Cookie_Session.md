# Cookie

* 연결이 끊어질때 정보를 유지하기 위해 정보를 저장
* 4KB, 300개 까지 저장
* 서버 요청시 같이 전송됨



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