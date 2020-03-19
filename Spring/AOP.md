# AOP

* Aspect(관점) Oriented Programming

## 등장 배경

* Java에서 OOP를 할때의 단점 보완
  * 다중상속 불가: 다양한 모듈에 공통기능을 부여하기 위해 적용하기에는 무리
  * 핵심 기능코드, 공통 기능코드의 혼재: 낮은 효율성



* AOP: 핵심기능과 공통기능을 분리, 핵심기능 구동에 필요한 공통기능을 호출

## 용어

* Aspect: 공통기능
* Advice: Aspect의 기능 자체
* Jointpoint: Advice를 적용해야하는 부분 (필드, 메소드)
* Pointcut: Joinpoint의 한 부분, 실제로 Advice가 적용된 부분
* Weaving: Advice를 핵심기능에 적용하는 행위



## AOP 구현 in Spring

* 호출부(client) -> 대행(Proxy) -> 핵심기능(Target)
* 핵심 기능 중 메소드에만 공통기능 적용 가능
* 프록시가 공통기능을 수행하고, 핵심기능과 제어권을 주고받음
* 구현: `XML` or `@Aspect`



### XML 기반의 AOP 구현

1. 의존 설정(`pom.xml`) - AOP 사용을 위한 라이브러리 지정

   ```xml
   <dependency>
   	<groupId>org.aspectj</groupId>
       <artifactId>aspectjweaver</artifactId>
       <version>1.7.4</version>
   </dependency>
   ```

   

2. 공통기능의 클래스 제작

3. XML 설정파일에 Aspect 설정

   * 이클립스의 `namespace`에도 추가해야함

   ```xml
   <bean .../>
   
   <aop:config>
       <aop:aspect id="ID" ref="프록시 역할의 클래스 경로">
           <!--advice가 적용될 대상(핵심기능)-->
           <aop:pointcut id="pointcut이름" expression="적용대상 ex:within(패키지명.*)" />
           <!--advice가 실행되는 시점 -->
           <apo:around pointcut-ref="지정할 pointcut ID" method="실행 할 method 이름"/>
       </aop:aspect>
   </aop:config>
   
   ```

#### 실행시점

* `<aop:before>`: 메서드 실행 전에 advice 수행
* `<aop:after-returning>`: 정상적으로 메서드 실행 후에 advice 수행
* `<aop:after-throwing>`: 메서드 실행 중 예외발생시 advice 수행
* `<aop:after>`: 메서드 실행 중 예외가 발생 해도 메서드 실행 이후 advice 수행
* `aop:around>`: 메서드 실행 전후 및 예회 발생 시 advice 수행

### Annotation을 사용한 AOP 구현

1. 의존 설정 (`pom.xml`)

   * namespace도 추가

2. `@Aspect` 어노테이션을 적용해 클래스 작성

   ```java
   @Aspect
   public class a {
       @Pointcut("within(com.javalec.ex.*)")
       private void pointcutMethod(){
       }
       
       @Around("pointcutMethod()")
       public Object loggerAop(ProceedingJoinPoint joinpnt) throws Throwable {
       }
       // 이렇게도 가능
       @Around("within(com.javalec.ex.*)")
       public Object loggerAop(ProceedingJoinPoint joinpnt) thorws Throwable{
       }
   }
   ```

   

3. `xml`에 `<aop:aspectj-autoproxy/>` 설정

   ```xml
   <aop:aspectj-autoproxy/>
   <bean ../>
   ```

   

## AspectJ 표현식

* `*`: 모든
* `.`: 현재
* `..`: 1개 이상



* execution: 한정자(public 등), 파라메터 등 특정 조건에 해당하는 메서드
* within: 특정 패키지, 클래스 내의 모든 메서드
* bean: 특정 빈에 적용