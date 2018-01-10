## 유니코드 스트림 처리
### http://raccoonyy.github.io/working-with-unicode-streams-in-python-korean/
================================

## Python2에서
* `open()`을 이용해 파일을 열고 `read()`로 읽음 => 용량이 작을때는 이것 만으로도 충분
* 파일이 커서 조각단위로 읽고자 할때 `read(바이트수)`를 이용하면 한 바이트의 유니코드가 여러개로 분리되는 상황 발생할 수 있음
* Decode시에 UnicodeDecodeError 발생

### codecs
* 한 바이트의 유니코드가 여러조각으로 나뉘는 예외발생 없이 파일을 조금씩 읽을 수 있음 => 데이터를 조금씩 로드(Load)

## Python3 에서는?
* 내장함수 `open()` 사용해 객체 생성
* `.read(바이트수)`를 이용해 조각 단위로 읽을 수 있음
* 유니코드 데이터 수정, 인코딩 변경에 필요한 기능이 포함되어 있음