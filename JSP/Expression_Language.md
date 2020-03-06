# Expression Language

* 표현식, 액션태그를 대신해 값을 표현하는 방식



## 표현식

* `<%=value%>` ==> `${value}`
* 산술, 비교, 조건(`a?b:c`), 논리식 표현 가능



## 액션태그

* `<jsp:getProperty name="member" property="name"/>`
* ==> `${member.name}`



## 내장객체

* pageScope: page객체
* requestScope: request 객체
* sessionScope
* applicationScope



* param: 요청 파라메터
* paramValues: 여러개의 값을 가지는 파라메터
* initParam: Servlet에서 초기화 값(`context-param`) 참조
* cookie
* `***.setAttribute("키", "값")`(JSP) ==> `${***Scope.키}`



### param

* `request.getParameter("id");` 
* ==> `${param.id}`
* ==> `${param["id"]}`



### initParam

* `<context-param>` (in `web.xml`)
* `getServletContext().getInitParameter("키")`
* ==> `${initParam.키}`