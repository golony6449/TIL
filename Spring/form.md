# Form in Spring

## HttpServletRequest 클래스

* 메서드의 정의부에 지정

  ```java
  public String confirmId(HttpServletRequest httpServletReq, Model model){
      String value = httpServletReq.getParameter('key');
  }
  ```

* 클라이언트로 부터 전송된 데이터가 포함되어있는 객체



## @RequestParam 어노테이션

* 메서드의 매개변수로 전송된 데이터를 받음

  ```java
  public String confirmId(@RequestParam('key') String value){
      
  }
  ```

* 주의: 매개변수로 지정된 값이 없는경우 `404`에러 발생



## 데이터(커맨드) 객체

* 가장 많이 사용되는 방법: 기존의 방식이 코드가 복잡해지는 문제를 해결

  * 데이터 추출에 필요한 코드양이 많음
  * => 매개변수로 객체 자체를 받음

  ```java
  public String method(Data data){
      
  }
  ```

  

* 이때 해당 클래스는 필드, Getter, Setter로 구성됨

* 필드 이름과 동일한 키를 가지는 값으로 객체 생성

  * View에서 사용되는 객체 이름 변경: `@ModelAttribute`

    ```java
    public String method(Object obj){
        // View에서는 obj라는 이름으로 사용
    }
    // ==
    public String method(@ModelAttribute("obj") Object object){
        // View에서는 obj라는 이름으로 사용 가능
    }
    ```

    

* 메서드의 매개변수로 객체가 오는 경우, View에서 바로 사용 가능 

  * 이때 이름은 매개변수 이름 사용



## @PathVariable 어노테이션

* 경로에 변수를 넣어 파라메터로 사용가능

  * 주의) `{ }`안에 기재된 키 값과, 매개변수 명이 동일해야함
  * 별도로 반환할 필요없이 View에서 사용가능

  ```java
  // wget http://localhost/dev/student/10
  @RequestMapping("/student/{value}")
  public String method(@PathVariable String value){
      
  }
  ```

  

## 값 검증

* `Validator` 인터페이스를 사용해 커맨드 객체의 유효성 검사
  * 컨트롤러에서 Validator 객체를 사용해 커맨드 객체 검증

### Validator 정의

* `Validator` 인터페이스를 상속받아 정의

```java
public class ObjValidator implements Validator{
    @Override
    public boolean supports(Class<?> arg){
        // 검증할 객체의 클래스정보 명시 ==> 이 Validator로 검증 가능한 class 지정
        return 클래스명.class.isAssignableFrom(arg);
        
    }
    
    @Override
    public void validate(Object obj, Error error){
        // obj를 형변환 한 뒤, 필요한 검증 처리 구현
        // 에러 발생시 error 객체에 에러 추가
        error.rejectValue("값 이름(필드명)", "사유");
    }
}
```

### 컨트롤러에서 사용

```java
// 컨트롤러 내부
public String method(@ModelAttribute("student") Student s, BindingResult res){
    ObjValidator v = new ObjValidator();
    v.validate(obj, res);	// Binding Result는 검증 결과를 저장하는 객체
    if (res.hasError()){
        // 에러 발생시 수행사항
    }
    
}
```



### ValidationUtils 클래스

* `validate()` 메서드를 더 편리하게 사용 할 수 있도록 고안된 클래스

```java
ValidationUtils.rejectEmptyOrWhitespace(error, "값 이름(필드명)", "사유");
// 동일
Obj o = (Obj) obj;
String val = o.getValue();
if (val == null || val.trim().isEmpty()){
    error.rejectValue("값 이름(필드명)", "사유");
}
```



### @Valid and @InitBinder

* 직접 `validate()`를 호출하지 않고, Spring이 자동으로 호출

1. 의존성 추가

   ```xml
   <dependency>
   	<groupId>org.hibernate</groupId>
       <artifactId>hibernate-validator</artifactId>
       <version>4.2.0.Final</version>
   </dependency>
   ```

   

2. 검증 할 커맨드 객체 지정

```java
// Before
public String method(@ModelAttribute("object") Object o){
}

// After
public String method(@ModelAttribute("object") @Valid Object o){
}
```

3. 검증에 사용할 Validator 지정 (컨트롤러 내부에)

   ```java
   @InitBinder
   protected void initBinder(WebDataBinder binder){
       binder.setValidator(new ObjValidator());
   }
   ```

   