# JSP

## 태그

* 지시자: `@` 페이지 속성, `page`, `include` (별도의 페이지를 현재에 삽입), `taglib`
* 주석
* 선언: <b>전역의 의미를 가지는 변수, 메서드 선언</b>
* 표현식: `=`
* 스크립트릿: Java 코드
* 액션 태그: `<jsp:action>`



* 스크립(`scripe`): 스크립트릿 + 선언 + 표현식



## 내부 객체

* 입출력: `request`, `response`, `out`
* 서블릿: `page`, `config`
* 세션: `session`
* 예외: `exception`



## request 객체

* `getContextPath()`
* `getMethod()`
* `getSession()`
* `getProtocol()`
* `getRequestURL()`
* `getRequestURI()`
* `getQueryString()`
* `getServerName()`
* `getServerPort()`
* `setCharacterEncoding()`: 파라메터 인코딩 방법 지정

### Parameter 관련

* `getParameter()`
* `getParameterNames()`
* `getParameterValues()`: Checkbox등 복수형 input에 사용



## response 객체

* `addCookie()`
* ``sendRedirect()`



## Action Tag

* JSP 내에서 어떤 동작을 하도록 지시하는 태그



### forward

* 현재의 페이지에 다른 `jsp`페이지를 로드
* 주의: URL만 그대로!, 내용은 호출한 jsp파일이 불러짐
* `<jsp:forward page="jsp파일"/>`



### include

* 현재의 페이지 내부에 다른 `jsp`페이지 로드
* `<jsp:include page="파일명"/>`



### param

* `forward`, `include`에 데이터 전달

```jsp
<jsp:forward page="jsp">
	<jsp:param name="id" value="abcd"/>
    <jsp:param name="pw" value="pw"/>
</jsp:forward>
```

* `request.getParameter()`로 불러와 사용