## Web Assembly
* http://webassembly.org/
-----------------------------
* LLVM을 내부적으로 사용
* LLVM 정보: https://ko.wikipedia.org/wiki/LLVM

### 미리보기 - LLVM
* 일반적인 컴파일러는 소스코드 -> 기계어 로 변환
* 이때 LLVM은 중간 단계를 추가해, human readable, 최적화 가능한 중간코드 생성 (ex: Java의 bytecode)
* 장점: 지원하는 언어(컴파일러의 프론트엔드), 기계어(백엔드) 다양 -> 프론트엔드, 백엔드 변경시 다양한 언어를 다양한 아키텍처에서 실행가능

### 개요
* Java의 bytecode를 확장시킨 느낌
* 언어(현재: C, C++)를 bytecode형태로 컴파일 후 이를 웹브라우저에서 실행 -> 웹브라우저가 일종의 중간코드가 실행되는 VM 역할 수행
* 백엔드가 브라우저로 변경되면 더 이상 Web Programming에 JS를 고집할 필요가 없어질 것으로 보임

* 파이어폭스, 구글 크롬, IE에 탑재되어 있음
* 현재 W3C에서 표준화 작업중에 있음

### 보안
* 샌드박스 안에서 구동되는 방식