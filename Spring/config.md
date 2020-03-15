# Spring Config

## Environment 객체

* `Context`에서 `Env`를 추출하고 `Env`에서 `PropertySources` 추출
* 이후 `PropertySources`객체에 `obj.addLast(new ResourcePropertySources("property 경로"))`
* 사용: `env.getProperty("키")`

## Bean과 결합해서 사용

### Environment 객체 사용

1. `EnvironmentAware`를 상속(implements) 후 `setEnvironment()` 오버라이드
   * 빈 초기화(`afterPropertiesSet()`) 이전에 수행됨
2. 이후 `afterPropertySet()`을 오버라이드 해, ENV에 있는 값으로 객체 초기화
   * `xml`에 `<property>`로 값을 기입하지 않고도 값을 초기화 할 수 있음

### Environment 객체 없이 초기화 (XML에서 properties 참조)

1. 프로퍼티 파일 참조 키워드 추가

   * 이클립스의 `namespace`에서 `context` 추가
   * `<context:property-placeholder location="파일1, 파일2"/>`

2. 값 참조

   ```xml
   <bean ...>
   	<property>
       	<value>{$프로퍼티 안의 값}</value>
       </property>
   </bean>
   ```

   

### Environment 객체 없이 초기화 (Annotation 사용)

* 클래스 변수 상단에 `@Value` 어노테이션 추가

```java
public class AppConfig{
    @Value("$프로퍼티 안의 값")
    private String var;
}
```



* Placeholder 지정

```java
@Bean
public static PropertySourcesPlaceholderConfigurer Properties(){
    PropertySourcesPlaceholderConfigurer configurer = new ...();
    
    Resource[] loc = new Resource[2];
    loc[0] = new ClassPathResource("파일명");
    ...
    
    configurer.setLocation(loc);
    return configurer;
}
```

