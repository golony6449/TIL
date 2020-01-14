# Class library in Java

## Java API

* `java.util`: ArrayList, Scanner
* `java.io`: 입출력 관련



## Wrapper Class

* 기본 자료형을 클래스 형태로 '감싼' 것

| 자료형 | 래퍼 클래스 |
| ------ | ----------- |
| int    | Integer     |
| byte   | Byte        |
| char   | Charactor   |
| short  | Short       |
| long   | Long        |
| float  | Float       |
| double | Double      |



### Example

```java
Integer int1 = new Integer(100);
Double db1 = new Double(10.0);
Character ch = new Character('123');
```





### 형변환

* `변경할 자료형의 래퍼클래스.valueOf(값)` (클래스 Method)



### 문자열로 변환

* 클래스 Method 사용: `자료형.toString(값)`
* 인스턴스 Method 사용: `변수명.toString()` (래퍼 클래스로 생성된 객체에서만 가능)



## Math Class

* `Math.abs()`: 절댓값
* `Math.max()`, `Math.min()`
* `Math.random()`: 0.0 ~ 1.0미만의 난수 반환