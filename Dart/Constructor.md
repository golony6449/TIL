# Constructor

## 개요

* 생성자



## Initializer List

* 생성자의 body가 실행되기전에 인스턴스 변수 초기화 가능
* 특히 `final` 변수는 `Initializer list`를 이용해 초기화 해야함
* 자세한 내용은 참고자료의 `Initializer list` 참조



### Example

```dart
// Initializer list sets instance variables before
// the constructor body runs.
Point.fromJson(Map<String, num> json)
    : x = json['x'],
      y = json['y'] {
  print('In Point.fromJson(): ($x, $y)');
}
```





## 참고자료

* https://dart.dev/guides/language/language-tour#constructors