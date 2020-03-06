# Java Bean

* 데이터(속성) + 기능(Method)로 구성된 클래스
* 액션 태그를 이용해 사용



## 작성

```java
package com.javalex.ex;

public class Student{
    private String name;
    private int age;
}

public Student(){
}

public String getName(){
    return name;
}

public void setName(String input){
    name = input;
}

public int getAge(){
    return age;
}

public void setAge(int input){
    age = input;
}
```



## 사용

```jsp
<jsp:useBean id="student" class="com.javalec.ex.Student" scope="page" />

<jsp:setProperty name="student" property="name" value="홍길동"/>
<jsp:getProperty name="student" property="name"/>
```



### scope

* page: 생성된 페이지 내에서만 사용
* request: 요청된 페이지 내에서만 사용
* session: 웹브라우저의 생명주기와 동일
* application: 웹 어플리케이션 생명주기와 동일