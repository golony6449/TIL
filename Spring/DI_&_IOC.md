# DI and IOC Container

## Dependency Injection

* A객체가 B/C객체에 의존하는 상황
  * 방법 1: A객체 내부에서 직접 의존하는 B/C 객체를 생성
  * 방법 2: A객체 외부에서 `setter`, `constructor`를 사용해 외부에서 **주입** (main class 포함)
    * 코드 수정없이 모듈 수정을 가능하도록 하는것이 목적



## Inversion Of Control

* 객체생성에 필요한 모듈(의존성 등)을 담고있는 컨테이너 (`xml`이나 `Context`로 봐도 될듯)
* 인터페이스(`setter`, `constructor`)를 이용해 전송



### 스프링을 기능을 활용

1. `xml`파일을 이용해 모듈을 담고있는 `Context` 생성
2. `Context`에서 해당 객체를 선택해서 사용 
   * 각각의 모듈을 `bean` 이라고 부름 (생성: `Spring Bean Configuration File`)