# Docker-compose

## 개요

* <b>동일한 호스트 상에서</b> 연관되어 동작하는 여러 컨테이너를 관리하는 기능

## stop VS down VS rm

* `docker-compose stop`: 연관된 컨테이너를 단순히 **정지**
* `docker-compose down`: 연관된 컨테이너를 정지하고 컨테이너와 **관련 네트워크 까지 삭제** == > `up` 명령으로 생성된 모든것을 삭제
* `docker-compose rm`: 연관된 컨테이너를 정지하고 삭제

