# PyQt + Web

## QWebChannel
* PyQt와 Web(JS)을 이어주는 역학
* 관련코드(qwebchannel.js)를 웹에 삽입해야 함

## 기존의 사이트에 QWebChannel 삽입
* 기존의 웹에 코드 삽입 + 웹브라우저 사용과 미사용을 상황을 분리
* 사용되는 데이터 타입: QJsonValue, QJsonDocument
