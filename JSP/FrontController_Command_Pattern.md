# url-pattern

* 디렉터리 패턴: 디렉터리 형태로 해당 컴포넌트 실행 (서블릿 매핑)



* 확장자 패턴: 확장자 형태(`file.type`)로 컴포넌트를 실행 
* ==> 동일 확장자면 동일 서블릿 실행



# FrontController 패턴

* 클라이언트의 다양한 요청은 한 곳으로 집중 ==> 높은 개발 효율성
* 중복코드 최소화
* **서블릿이 요청을 직접 처리**

```java
@WebServlet("*.do")	
//.do로 들어온 요청은 해당 서블릿이 처리
```

## 적용

1. 요청 URI 획득
2. ContextPath 획득
3. URI에서 ContextPath의 길이만큼 삭제
4. 요청에 대한 정보획득
5. 분기



### Web.xml

```xml
<!-- 프런트 컨트롤러 서블릿 등록 -->
<servlet>
    <servlet-name>front</servlet-name>
    <servlet-class>com.dev.controller.FrontController</servlet-class>
</servlet>
 
<!-- URL패턴 맵핑-->
<servlet-mapping>
    <servlet-name>front</servlet-name>
    <url-pattern>*.do</url-pattern>
</servlet-mapping>
```





# Command 패턴

* 요청을 서블릿이 직접 처리하지 않고, 해당 클래스가 처리하도록 함
* 요청을 **다른 서블릿으로 전달**



## 적용

1. 초기작업은 FrontController와 동일
2. 이후 다른 서블릿에 존재하는 객체 생성 후 매개변수 전달
3. 처리 후, 반환값을 이용해 응답 내용 생성