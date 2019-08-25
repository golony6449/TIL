# Class

## 생성자

* 클래스 생성시 호출될 함수 지정
* 기본 접근제한자: `public`
* `{  }`를 사용한 생성자: 매개변수를 optional 하게 만듦



### Example 1

* 보통의 OOP의 생성자와 동일

```dart
class Class{
    int val;
    Class(int value){
        // 구현
        this.val = value;
    }
}
```



### Example 2

* `this` 키워드를 사용한 간략화 가능

```dart
class Class{
    int val;
    Class({this.val = 10});
}
```



## Method

### Operator

* `=>`: 값을 반환하는 간단한 메서드 구현시 사용

### 특수한 메서드

```dart
class Class{
    int val;
    
    @override
    String toString() => "Value is $val";
    // 객체의 출력 형식 지정
}
```



## 참고자료

* [생성자](https://duzi077.tistory.com/294)
* [optional한 생성자 변수](https://duzi077.tistory.com/295)

