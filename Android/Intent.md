## Intent
=======================

### Intent?
* 의미: 내가하고자 하는 행위
* Android에서 앱 구성요소간 데이터 전달, 기능 실행등의 역할을 수행함
* 안드로이드 플랫폼에 필요한 기능을 전달하는 역할

### Example
```java
...
public void onButton2Clicked(View v) {
    Intent myIntent = new Intent(Intent.ACTION_VIEW, Uri.parse("tel:010-1234-5678"));
    startActivity(myIntent);
    // 기본 전화어플로 연결
}

public void onButton3Clicked(View v) {
    Intent myIntent = new Intent(Intent.ACTION_VIEW, Uri.parse("http://m.naver.com"));
    startActivity(myIntent);
}
```