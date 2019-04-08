# PyQt5 - Mouse Event

## 개요

* `PyQt5`에서 마우스 이벤트 처리



## 마우스 Press 이벤트

* `mousePressEvent(self, event)`를 재정의해 사용



## 마우스 Release 이벤트

* `mouseReleaseEvent(self, event)`를 재정의해 사용



## 마우스 커서 이동 이벤트

* `mouseMoveEvent(self, event)`를 재정의해 사용
* 주의: 기본값으로는 마우스 버튼이 <b>눌러진 경우에만 발동</b>
* <https://freeprog.tistory.com/329?category=716617>

### 마우스를 클릭하지 않고도 발생하게 하려면?

* `self.setMouseTracking(True)`
* `True`: 마우스 버튼을 누르지 않아도 추적
* `False`: 마우스 버튼을 누른 경우에만 추적 (기본값)
* 주의: `MainWindow` 유형에서는 `self.setMouseTracking(True)`와 `self.centralwidget.setMouseTracking(True)` 모두 필요
* `centralwidget`: `PyQt5`에서 생성한 Hidden 위젯
* 참고자료: <https://stackoverflow.com/questions/9638420/qmainwindow-not-tracking-mouse-with-setmousetracking>