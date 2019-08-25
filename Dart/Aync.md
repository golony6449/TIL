# 비동기 in Dart

## 개요

* flutter 프로젝트에서 key-value store를 위해 사용하는 모듈이 비동기로 동작함
* 이를 처리할 필요가 있었음



## Async function in Dart

* 반환형이 `Future<T>`
* 이는 반환형에 대한 Template 역할을 수행함
* ==> 해당 코루틴 수행이 끝나면 결과값을 가지지만 그 전에는 `Future` 객체로서 존재



## 문제점

* 직접 추가한 Method는 수정이 가능하지만, Flutter 프레임워크는 손댈수 없음
* 그럼 async 함수를 만드는데 문제가 생김



## Solution

* `Future`객체의 `then()` 메서드를 사용해 작업이 완료되면 실행할 콜백 함수 지정 가능
* 주의: 반환형이 있는경우는 문제발생 
* (콜백함수에서 함수 밖으로 반환 할 수 없음)
* 함수 밖에 있는 변수에 직접 값을 할당하는 방법으로 처리



## Example

```dart
List<bool> status;

Widget build(BuildContext context) {
    // 주의: then 메서드는 콜백함수의 반환값을 처리할 수 없음
    getStatus().then(
            (List<bool> values) {
              status = values;
            });

    return new MaterialApp(
      home: ListRoute()
    );
  }
```





## 참고자료

* https://medium.com/flutter-community/futures-async-await-threading-in-flutter-baeeab1c1fe3
* [공식 문서](https://dart.dev/codelabs/async-await)
* https://javaexpert.tistory.com/964