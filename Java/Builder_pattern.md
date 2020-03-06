# 빌더 패턴

* 객체 생성시 사용되는 패턴 중 하나
* 점층적 생성자 패턴, 자바빈 패턴의 단점 보완
* `Lombok`의 어노테이션을 사용해 간단히 적용 가능



## 예

```java
Member customer = Member.build()
    .name("홍길동")
    .age(25)
    .build();
```



## 참고자료

* https://johngrib.github.io/wiki/builder-pattern/