# Thymeleaf

## 개요

* Spring에서 사용되는 템플릿 엔진 중 **하나**
  * ​	==> 다른 엔진도 존재



## 예시

```html
<html>
    <head>
        <title>Main</title>
    </head>

    <body>
        <h1>Main Page</h1>

        <h3 th:text="${temp}">Name: </h3>
    </body>
</html>
```



## 다른 태그 들

### 메시지식

* `#{ }`
* `src/main/resources/messages.properties`에 기재



### 리터럴 치환

```html
<body>
    <h1 th:text="#{content.id}">Hello</h1>			<!--메시지식-->
    <div th:object="${object}">						<!--변수식-->
        <p th:text="|id : * {id}, name : *{name}|"> <!--리터럴 치환-->
            message
        </p>
    </div>
</body>
```





## 참고자료

* 기초: https://araikuma.tistory.com/30

* 여러가지 태그: https://strongstar.tistory.com/17