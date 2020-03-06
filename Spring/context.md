# Context

## XML

* 생성

```java
AbstractApplicationContext ctx = new GenericXmlApplication(경로 리스트);
```

## Java

* `Annotation`을 이용한 설정
* `@Configuration`: 스프링 설정에 사용되는 클래스임을 명시
* `@Bean`: `@Configuration` 클래스의 메서드에 명시
  * 함수 명: `id` 프로퍼티
  * 함수의 반환형: 클래스 지정
  * 객체 생성 후 반환



#### 사용

```java
AnnotationConfigApplicationContext ctx = new AnnotationConfigApplicationContext(설정 클래스 이름.class);
```

