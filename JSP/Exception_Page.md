# Exception Page

* 에러 페이지 대체 (미적, 보안 관점)



## Sol 1: page 지시자

* 대상 페이지

```jsp
<%@ page errorPage="errorPage.jsp"%>
```

* 예외 페이지

```jsp
<%@ page isErrorPage="true"%>
<% response.setStatus(200);%>

<%=exception.getMessage()%>
```



## web.xml에 설정

```xml
<error-page>
	<error-code>404</error-code>
    <location>/error404.jsp</location>
</error-page>

<error-page>
	<error-code>500</error-code>
    <location>/error500.jsp</location>
</error-page>
```

