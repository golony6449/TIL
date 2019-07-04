# JSP

## ServletConfig

* 특정 Servlet 생성시 사용되는 초기값 지정
* Sol 1: web.xml
* Sol 2: Servlet에 `@WebServlet` 내부에 `initParams={}` 형태로 기술
* ==> ex: `@WebServlet(urlPatterns={"/path"}, initParams{@WebInitParam(name="id", value="abc")}, initParams{@WebInitParam(name="pw", value="123")})`
* 사용: `getInitParameter()`



## ServletContext

* 여러 Sevlet에서 특정 데이터 공유
* 작성: (`WEB-INF` 내부에 존재하는) `web.xml`에 기술 

```xml
<context-param>
	<param-name>id</param-name>
    <param-value>abcd</param-value>
</context-param>

<context-param>
    <param-name>pw</param-name>
    <param-value>1234</param-value>
</context-param>
```

* 사용: `getServletContext().getInitParameter()`



## ServletContextListener

* Servlet의 생명주기 감시
* 지정된 메서드의 시작(`contextInitialized()`), 종료(`contextDestroyed()`)시에 호출됨
* 작성 1: 클래스 제작 ==> `web.xml`에 리스너 기술
* 작성 2: 클래스 제작 ==> `@WebListner` 추가 (at 클래스)

```xml
<listener>
	<listner-class>클래스</listner-class>
</listener>
```

