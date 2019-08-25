# FutureBuilder

## 개요

* 비동기 작업을 `build` 함수 내에서 사용하기 위한 객체
* `future`에서 반환된 `Future<T>` 객체의 준비여부에 따라 반환할 Widget을 다르게 할 수 있음



## Example

```dart
Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("설정"),
      ),
      body: FutureBuilder(
        future: getStatus(),
        builder: (BuildContext context, AsyncSnapshot snapshot) {
          if (snapshot.hasData) {
            print("데이터 준비 끝");
            SettingListState.status = snapshot.data;
            return SettingList();
          }
          else if (snapshot.hasError){
            Text("ERROR: $snapshot.error");
          }
          print("데이터 준비중");
          return Center(
            child: CircularProgressIndicator(),
          );
        },
      )
    );
  }
```





## 참고자료

* [블로그 글](https://medium.com/@changjoopark/플러터-flutter-앱-만들기-블로그-글-상세-dc1ba68d4cef)