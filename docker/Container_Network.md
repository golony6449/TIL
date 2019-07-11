# Docker Container Network

## 개요

* 컨테이너 간 통신, 컨테이너 - 외부간 통신에 사용되는 네트워크
* 별다른 옵션이 없는경우 기본으로 생성된 Bridge 네트워크가 사용됨

## 이름 문제

* 사실 이름.... 이라는게 뭔지 잘 모르겠으나, 공유기에서 NAT와 유사한 것으로 보임
* 기본 브릿지 네트워크 사용시, 실행된 컨테이너는 이름문제 해결 불가능 ==> `docker container run` 명령어 수행 시점에 `--link` 옵션을 통해 설정해야 함
* `--link` 설정 ==> 컨테이너 내의 `/etc/hosts`파일에 컨테이너명, 컨테이너에 할당된 IP가 기재됨
* 사용자 정의 네트워크 사용시, docker 데몬에 내장된 DNS 서버에 의해 해결 ==> `hosts`파일에 의존하지 않고 이름문제 해결 가능 및 alias 사용가능 
* ==> <b>특별한 이유가 없다면 사용자정의 네트워크 사용이 유리</b> 
