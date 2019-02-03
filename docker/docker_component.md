# Docker Component - 도커 컴포넌트

## 종류

* Docker Engine
* Docker Registry
* Docker Compose
* Docker Machine
* Docker Swarm

## Docker Engine

* 도커의 핵심기능
* 이미지 생성, 컨테이너 기동
* CLI 조작



## Docker Registry

* 이미지 공개/공유 기능



## Docker Compose

* 여러 개의 컨테이너 구성정보를 코드로서 정의
* 명령 실행을 통해 애플리케이션의 실행환경을 구성하는 컨터이너들을 <b>일원 관리</b>



## Docker Machine

*  로컬호스트 or AWS EC2, Azure 등의 클라우드 환경에 도커 실행환경 자동생성을 위한 툴



## Docker Swarm

* 여러 Docker 호스트를 클러스터화 하기 위한 툴
* Manager: 클러스터 관리, API 제공
* Node: 컨테이너 실행
* Kubernetes 이용도 가능