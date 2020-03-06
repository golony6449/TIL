# Spring Property

* 코드에는 `setter`, `getter`를 생성해야 함
* 장점: 언어에 의존되지 않는 서비스 구성 가능, 테스트 케이스 작성 가능

## Bean 생성

```xml
<bean id="명칭" class="클래스의 완전한 경로">
</bean>
```



## 값 초기화

* Spring이 적절한 자료형으로 변경해 필드 초기화 수행

```xml
<property name="필드 명">
	<value>값</value>
</property>
```

* `ArrayList`의 경우

```xml
<property name="필드명">
	<list>
    	<value>값 1</value>
        <value>값 2</value>
    </list>
</property>
```

* 다른 bean 참조

```xml
<ref bean="bean의 id 값"/>
```

* 생성자 매개변수 (생성자 매개변수 순서대로)

```xml
<constructor-arg>
	<value>값</value>
</constructor-arg>
```



### 네임 스페이스 사용

1. 사용할 네임스페이스 명시 (c: `constructor-arg`, p: `property`에 매칭 됨)

```xml
<beans .....
	xmls:c="http://www.springframework.org/schema/c"
     xmls:p="https://www.springframework.org/schema/p"
       ...>
	<bean id="고유 값" class="클래스 경로" c:필드 명="값" p:필드명="값"/>
</beans>
```

