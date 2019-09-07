# Multidex

## 개요

* `firebase` 모듈 적용시 발생하는 오류 해결



## 원인

* 64KB를 넘는 메서드 앱에 대한 처리



## 해결

* `minSdkVersion`을 21 이상으로 설정
* 또는 의존성 추가(참고자료 참조)



## 참고자료

* https://developer.android.com/studio/build/multidex