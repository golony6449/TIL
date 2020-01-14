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



## Inheritance

* 