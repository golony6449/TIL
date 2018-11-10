# go and gRPC

## History
* Socket: 안정적인 사용을 위해서는 개발자의 부담이 큼(예외처리)
* RPC: Remote Procedure Call(낮은 효율, Socket의 문제점을 효율적으로 해결하지 못했음)
* SOAP: XML on HTTP (데이터가 커질경우 무거워짐)
* REST: JSON on HTTP

## gRPC - google RPC
* stubby를 공개 ==> gRPC

## gRPC의 동작
* stub: 교환되는 파라메터를 언어중립적으로 변경해주는 일련의 코드 (언어 독립성 제공)
* IDL: 서버 - 클라이언트 간 인터페이스 정의(입력 - 출력 결과, 형태), stub 코드 생성에 사용
* Protocol buffer: 직렬화 메커니즘


## golang - Context
* 맥락을 위해 필요한 값을 담아 전달

## golang - goRoutine

## Client
* `grpc`: 서버의 코드를 실행시키는데 사용


## 그외
* unary
* goroutine과 조합해서 사용 가능

## Tip
* `.proto`: 분리된 프로젝트에서 관리 ==> git의 submodule 활용시 편리
* `.proto`의 업데이트: 동일 이름 재사용 지양 (여러프로젝트에서 사용 ==> 예상치 못한 오류 유발 가능성 존재)

## 장점
* JSON(HTTP1.1) 보다 큰 쓰루풋, 낮은 CPU 사용량
* 양방향 비동기 통신
* 확실한 정의로 부터 오는 안전함

## 단점
* 번거로운 테스트 ==> 유닛 테스트 작성 필요
* 미성숙한 생태계

## REST 와의 비교?
* 상황, 방법에 따라 다름
* 둘다 사용하는 것도 가능 ==> gRPC gateway

## 마이크로서비스에 좋은 이유?
* 마이크로서비스: 느슨하게 연결된 서비스의 집합
* ==> 개발자, 팀이 독립적으로 개발
* 각자의 언어를 사용해서도, 하나의 서비스로 만든 것 처럼 동작 가능