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

  