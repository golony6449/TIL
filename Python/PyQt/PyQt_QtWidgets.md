# PyQt5 : Python GUI Framework
* reference: https://opentutorials.org/course/2581 by 임덕규
===========================
### 기본폼
* PyQt5.QtWidgets 모듈에서 QWidget을 상속받아 폼 클래스 생성해 사용

* 대략적인 구현 순서
1. 폼 클래스 생성 (부모의 초기화 함수 호출 -(별도의 자체 초기화 메소드 생성을 권장)> 내부 위젯 객체 생성 -> 위젯 객체 설정)
2. QApplication 객체 생성
3. 폼 객체 생성
4. 폼 객체 출력
5. 무한루프(app.exec_()) 실행

* QLabel과 같은 위젯을 상속받아 클래스를 만듦으로서 특정 이벤트에 동일하게 반응하는 위젯을 만들 수 있음

### 이벤트 핸들러
* 특정 이벤트 발생시 실행되어 특정 명령을 수행하는 함수
* self.update() : paintEvent 발생!
| 메소드명 | 설명 | 예시 |
|---------|------|------|
| mouseMoveEvent(self, QMouseEvent) | 생성된 폼 위에서 마우스 커서가 움직일때 이벤트 발생 | 함수 마지막에 self.update() 수행 |
| moveEvent(self, QMoveEvent) | 생성된 폼이 움직일때 이벤트 발생 | " |
| paintEvent(self, QPaintEvenet) | 폼을 다시 그려야 할때 이벤트 발생(MFC에서 OninitDialog와 유사) | " |

### Widget
#### 지원 메소드
| 메소드명 | 설명 | 예시 |
|---------|------|------|
| .setStyleSheet(옵션:값) | 해당 객체의 스타일 관련 속성 지정(배경색 등) | |
| .setGraphicsEffect(이펙트객체) | 해당 객체에 이펙트(투명도 등) 적용| |

### Label
* 텍스트를 담고 있는 Widget

#### 지원 메소드
| 메소드명 | 설명 | 예시 |
|---------|------|------|
| .setText | 해당 위젯에 텍스트 입력(텍스트, 시퀀스 등 투입 가능) | lb.setText(msg) |
