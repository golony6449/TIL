# class in Java

## Basic Class Definition

```java
class Car {
    int speed; // 기본값: public
    private String manufacturer;
    static int count; // 클래스 변수: 공유됨
    
    Car(){
        this.speed = 0;
        this.manufacturer = "KIA";
        this.count = this.count + 1;
    }
    
    protected void upSpeed(int speed){
        this.speed = speed;
    }
    
    static int getCount(){
        return count;
    }
}
```

* 클래스 변수는 인스턴스화 하지 않다고 사용할수 있다는 점을 제외하면, 일반적인 필드와 동일



## Inheritance

```java
class Sedan extends Car{
    ...
}
```

* 부모클래스의 생성자 호출 후, 자식 클래스의 생성자 호출됨
* 명시적인 부모 클래스 생성자 호출: `super()`. 이때 매개변수를 전달하면 오버로딩된 생성자 호출 가능
* `final` 키워드: Method - 오버라이딩을 차단. 필드 - 내용 변경 불가능



### 추상 클래스 (Abstract Class)

```java
abstract class Car{
    ...
}
```

* 인스턴스화가 불가능한 클래스 ==> 다른 클래스에 상속되어서 사용
* 나머지는 보통의 클래스와 동일
* 구성가능 요소: 일반 필드, `static final`, `static`, `final`, 추상 메서드, 일반 메서드

#### 추상 메서드 (Abstract Method)

```java
abstract void func();
```

* 함수의 정의만 존재
* 오버라이딩 되어 사용 ==> 오버라이딩 되지 않으면 에러 발생
* `반드시 해당 함수를 만들어야 한다`라는 의미가 내포되어있음



### 인터페이스 (interface)

* 인스턴스화 불가능
* `static final`(생략가능), 추상 메서드, 일반 메서드만 가능
* 인터페이스 간 상속은 `extends`
* 클래스로의 상속은 `implements`
* 클래스는 여러 인터페이스를 다중상속 가능
  * 인터페이스와 클래스를 동시에 상속받을 수도 있음: `class A extends B implements C`