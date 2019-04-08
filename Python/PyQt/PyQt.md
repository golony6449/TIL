# PyQt5 : Python GUI Framework
* reference: https://opentutorials.org/course/2581 by 임덕규
===========================
## 새로운 시작!

### 주요 클래스
1. QtCore: Qt에서 사용되는 상수값들
2. QtWidgets: Widgets 모음
3. QtGui: Qicon, QPixmap, QFont 등

### PyQt4 -> PyQt5 변경점
* Gui -> Widgets, Gui로 분리
* connect() 방법(패러다임) 변경
| PyQt4 | PyQt5 |
|-------|-------|
| connect(객체, 이벤트, 함수) | self.객체.이벤트.connect(함수) |

### Qt Design으로 작업하기!
#### uic 모듈의 loadUi() 메소드 사용
| 장점 | 단점 |
|------|------|
| UI파일을 변환없이 바로 사용 가능 | 항상 UI 파일이 있어야 함 |
| 변환과정이 없음 -> 작업속도 빠름 | 에디터에서 메소드 자동완성(Intellisense) 사용 불가 |

#### pyuic5를 이용, ui파일을 py파일로 변환
장점: 에디터에서 자동완성 지원

단점: 디자인 변경시마다 ui파일 변환과정이 번거로움

* 적용방법
```
pyuic5 -o 출력파일명 ui파일명
```
1. 커맨드 입력
2. py파일 포함
3. 파이썬에서 해당폼 클래스에 py파일 안의 ui 클래스를 상속

or
1. 커맨드 입력
2. py파일 포함
3. 폼 클래스 안에 ui 객체 생성

#### without Designer
* 직접 코딩하기

### 시그널 - 슬롯 설정방법
| Signal | Slot |
|--------|------|
| Sender(시그널 송신), Receiver(시그널 수신) | 시그널에 반응하는 메소드

#### 1. Qt Designer 에서
Edit Signals/Slots 모드에서 설정
#### 2. 직접 코딩
해당 위젯 문서(Qt와 문서 동일)를 참고해, 슬롯메소드를 만들고 이어줌

### 위젯(Widget) 사용
1. Qt 레퍼런스에서 해당 위젯 사용법 확인
2. 요구 형식에 맞춰 코드 작성

## 구현
* Exec_ : Tk의 mainloop()와 동일한 역할 수행
### Hello_World 작성
디자이너를 이용, ui 생성 후 아래의 코드 작성

```python
import sys
from PyQt5 import QtWidgets
from PyQt5 import uic

class Form(QtWidgets.QDialog):
        def __init__(self,parent=None):
            QtWidgets.QDialog.__init__(self,parent)
            self.ui=uic.loadUi('hello.ui')  #ui파일 로드
            self.ui.show()  #윈도우 생성
if __name__=='__main__':
    app=QtWidgets.QApplication(sys.argv)
    w=Form()
    sys.exit(app.exec())
```

### Hello_World2 작성
디자이너를 이용 ui 작성 후 아래의 코드 작성

```python
import sys
from PyQt5 import QtGui,uic,QtCore,QtWidgets
from PyQt5.QtCore import pyqtSlot

class Form(QtWidgets.QDialog):
    def __init__(self,parent=None):
        QtWidgets.QDialog.__init__(self,parent)
        self.ui=uic.loadUi('hello.ui',self) #사용자 지정 슬롯 정의를 위해 Form클래스를 baseinstance로 전달
        self.ui.show()

    #슬롯 정의
    def slot_1st(self):
        self.ui.label.setText('첫번째 버튼')

    def slot_2nd(self):
        self.ui.label.setText('두번째 버튼')
        
    def slot_3rd(self):
        self.ui.label.setText('세번째 버튼')

if __name__=='__main__':
    app=QtWidgets.QApplication(sys.argv)
    w=Form()
    sys.exit(app.exec())
```

### Main Window - Dialog
* 공통점: 둘 다 최상위 위젯

* 차이점
| 특징 | Main Window | Dialog |
|------|-------------|--------|
| 상태바 | O | X |
| 메뉴바 | O | X |
| 툴바 | O | X |

Dialog는 특별한 용도의 윈도우라고 볼 수 있음!

### 한 윈도우에서 다른 윈도우 생성하기
* 첫 윈도우 생성 이후 추가 윈도우 생성

* 구현
1. 첫번째 폼 객체에 2번째 폼 객체(이하 폼2) 생성
2. 폼2 출력(.show())

(폼2 초기화는 폼2의 생성자에서 수행)

### 슬롯-시그널 connect 할때 파라메터 전달 방법
* 객체.시그널.connect(lambda:함수(파라메터))

```python
Button.clicked.connect(lambda:func(i))
```

* 주의사항
1. for문 등에서 lambda식에 변수 사용시 마지막 변수값으로 connect되는 현상 있음(관련 자료: https://www.facebook.com/groups/pythonkorea/permalink/1426254617457695/?comment_id=1426282120788278&reply_comment_id=1426295050786985&notif_t=group_comment_reply&notif_id=1500722281191515)
2. 형식매개변수명=실매개변수(i=k) 형태로 매개변수 전달 불가능!

### 이벤트 종류
| 이벤트 명 | 발생조건 | 기타 |
|----------|---------|-------|
| clicked() | 위젯 클릭시 발생 | |
| doubleclicked() | 위젯 더블클릭시 발생 | |
| KeyPressEvent() | 키보드가 눌려졌을 때 발생 | 'PyQt5.QtCore.Qt.Key_키값'에 있는 값 사용 |
