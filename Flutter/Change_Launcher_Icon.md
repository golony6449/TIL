# 설정된 런처 아이콘 변경

## 개요

* 아이콘으로 사용될 이미지를 동일한 이름으로 덮어 써서 아이콘을 바꾸려고 시도했음
* 코드상에서 사용된 이미지는 변경되었으나, 런처 아이콘은 변경되지 않는 문제 발생



## 해결

* 명령을 통해 Icon override 수행

```
> flutter pub pub run flutter_launcher_icons:main
Android minSdkVersion = 21
Creating default icons Android
Overwriting the default Android launcher icon with a new icon
Overwriting default iOS launcher icon with new icon

```

