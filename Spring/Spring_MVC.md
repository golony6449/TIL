# Spring MVC

* 프로젝트 이름의 3번째(`dev.golony.xxx`)가 context 이름이 됨
  * `server.xml`의 `<Context>`에서 확인 가능

## src/webapp (루트 역할)

### WEB-INF

#### spring/appservlet/servlet-context.xml

* bean 등의 스프링 관련 설정 수행
* `InternalResourceViewResolver`에 지정된 sufix, prefix를 통해 view의 경로 지정

* `<context:component-scan base-package="패키지명">`: 해당 패키지를 스캔

#### views

* view에 해당하는 jsp 파일들이 존재

#### web.xml

* Dispatcher 서블릿 매핑

  * Dispatcher 서블릿: 요청을 최초로 받아 컨트롤러에 전달

* Spring 설정파일 위치 정의

  ```xml
  <init-param>
  	<param-name>contextConfigLocation</param-name>
      <param-value>/WEB-INF/spring/appServlet/servlet-context.xml</param-value>
  </init-param>
  ```

  

* 특정 URL로 요청시, 실행할 클래스를 지정



### resources

* 이미지, CSS 등 static 파일이 위치하는 곳

* Dispatcher에 의해 핸들링 되지 않는 요청 (`servlet-context.xml`)

  ```xml
  <resources mapping="/resources/*" location="webapp 하위 경로"/>
  ```

  

## Controller

* Dispatcher에서 전달된 요청을 처리

* `@Controller` 어노테이션으로 컨트롤러임을 명시

* 반환 값: View의 이름

* 함수 형은 `Model`의 필요 유무에 따라 적절하게 생성 가능

  ```java
  public String viewWithOutModel(){
  }
  // or
  public String viewWithModel(Model model){
  }
  ```

* `@RequestMapping`: 처리할 요청 주소 지정
  
  * 클래스에도 지정된 경우: 클래스에 지정된 주소 + 메서드에 지정된 주소 = 처리할 주소
  * 처리할 HTTP Method 지정가능: 핸들링할 메서드가 없는 경우 405 에러 발생
    * `@RequestMapping(method=RequestMethod.GET, value="URL")`
    * `@RequestMapping(method=RequestMethod.POST, value="URL")`
  
* `ModelAndView` 클래스를 이용하는 경우는 값, 뷰 이름을 객체에 설정하고 객체를 반환

* redirect를 하려면 `"redirect:URL"`을 반환하면 가능



## View

* View에서 Context 이름 얻기

  ```
  <%
     String context = request.getContextPath();
  %>
  ```

  