# Forwarding

* 서블릿, JSP에서 요청을 받을 후 다른 컴포넌트로 요청 위임

## RequestDispatcher 클래스

* 요청받은 요청객체(`request`)를 위임하는 컴포넌트에 동일하게 전달

```java
RequestDispatcher dispatcher = request.getRequestDispatcher("위임 받을 컴포넌트 경로");
dispatcher.forward(request, response);
```

or

```jsp
<% RequestDispatcher dispatcher = request.getRequestDispatcher("컴포넌트 경로");
dispatcher.forward(request, response);
%>
```



## HttpServletResponse

* **새로운 요청 객체를 생성해** 위임 받을 컴포넌트에 전달
* 요청받은 컴포넌트가 클라이언트에 응답
* ==> 위임받은 컴포넌트에 클라이언트가 새로운 요청 시도
* 설정한 값(속성) 전달 불가능 (새로운 요청 시도)
* 흔히 이야기하는 `Redirect`

```jsp
response.sendRedirect("컴포넌트")
```

