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

###Qt Design으로 작업하기!
#### uic 모듈의 loadUi() 메소드 사용
| 장점 | 단점 |
|------|------|
| UI파일을 변환없이 바로 사용 가능 | 항상 UI 파일이 있어야 함 |
| 변환과정이 없음 -> 작업속도 빠름 | 에디터에서 메소드 자동완성(Intellisense) 사용 불가 |

#### pyuic5를 이용, ui파일을 py파일로 변환
장점: 에디터에서 자동완성 지원
단점: 디자인 변경시마다 ui파일 변환과정이 번거로움

#### without Designer
* 직접 코딩하기

### 시그널 - 슬롯
#### 1. Qt Designer 에서

#### 2. 직접 코딩
해당 위젯 문서(Qt와 문서 동일)를 참고해, 슬롯메소드를 만들고 이어줌

### 위젯(Widget) 사용
1. Qt 레퍼런스에서 해당 위젯 사용법 확인
2. 요구 형식에 맞춰 코드 작성

### Hello_World 작성
디자이너를 이용, ui 생성 후 아래의 코드 작성

'''python
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
'''

### Hello_World2 작성
디자이너를 이용 ui 작성 후 아래의 코드 작성

'''python
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
'''

