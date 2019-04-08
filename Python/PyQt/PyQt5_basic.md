# PyQt5 Basic

## 개요

* `PyQt5`를 사용하는 프로젝트의 기본 구성



## 설치

* `pip install pyqt5 pyqt5-tools`



## UI 작성

* `pyqt5-tools`의 `designer`를 이용해 `ui` 파일 작성
* `pyuic5 <파일명> -o <출력파일명>`
* 클래스 파일을 상속받아 필요한 요소 재정의
* 이때 생성된 UI파일내의 class, 생성한 UI 파일의 타입(`MainWindow`, `QDialog`)를 모두 상속 받아야 함
* (UI파일 내의 class는 아무것도 상속 받지 않음)



## 이벤트 연결

* `self.<위젯명>.connect(<호출되는 함수>)`