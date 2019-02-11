# Docker 이미지 생성, 로드 명령어간 차이점

## 개요

* `docker container` 명령에는 컨테이너에서 출력하는 명령(export/save)과 출력물에서 컨테이너를 생성하는 명령(import/load) 존재
* 이 명령간 차이점 정리



## export VS save

* export는 단순히 컨테이너 내부에 존재하는 파일을 외부로 출력(`export`)하는 명령
* ==> 압축을 풀면, 루트폴더 구조를 확인할 수 있음
* save는 이미지의 레이어 구조까지 포함해 외부로 출력
* ==> 이미지의 해시값 확인 가능



## import VS load

* 각각 export, save에 매칭되는 명령어