# Widget - Switch

## 개요

* 좌우로 조작할 수 있는 Widget
* 상태값으로 사용할 `value`와 이벤트 발생시 발동될 `onChange` 지정 필요



## 주의

* 그냥 단순히 콜백처럼 구현했더니, 화면을 다시 그리는 상황(방향전환)을 발생 시켜야 변경된 상태가 적용되는 문제 발생
* `bool` 값을 받는 Anonymous 함수 작성 => 내부에 `setState()` 함수 탑재 ==> 그 안에 함수 구현
* 이렇게 해야 값이 변경될때 `setState()`에 의해 화면을 다시 그리는 작업을 수행함
* 당연한건데 왜 신경을 못썼지...



## Example 1

```dart
  Widget _buildListElementSwitch(int i){
    return Switch(
      onChanged: (bool value) {
          // 이벤트 핸들러를 setState 내부에 콜백으로 구현
        setState(() {
          status[i] = value;
          print("Switch: Status Changed");
          print(value);
        });
      },
      value: status[i],
    );
  }
```



## Example 2

```dart
Widget _buildListElementSwitch(int i){
    return Switch(
      onChanged: (bool value) {
        status[i] = value;
        print("Switch: Status Changed");
        print(value);

        setState(() {});	// 그냥 다시 그리기 명령
      },
      value: status[i],
    );
  }
```



## 참고자료

* [스위치 onChange 설정](https://stackoverflow.com/questions/52222712/flutter-switch-onchanged-not-changing)
* [Document](https://api.flutter.dev/flutter/material/Switch/onChanged.html)