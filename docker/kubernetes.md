# Kubenetes

## 개요

* 구글에서 개발한 Docker 오케스트레이션 도구



## 용어

* 마스터 서버(Kubernetes Master): 클러스터안의 컨테이너를 조작하기 위한 서버
* 백엔드 데이터베이스(etcd): 클러스터 구성 정보 관리.
* 노드(Node): 실제로 Docker 컨테이너를 작동시키는 서버
* 인그레스: 서비스를 쿠버네티스 클러스터 외부로 노출



## 구성 

* Pod: 앱의 전개 단위(컨테이너 생성/시작/정지/삭제 단위), 단일 역할로 구성해야 함, 여러개의 컨테이너로 구성됨
* ReplicaSet: 미리 지정된 Pod를 실행시키는 장치. 실행중인 Pod 감시, 필요시 재시작
* Deployment: Pod + ReplicaSet, ReplicaSet의 이력 관리(버전 업데이트/롤백 기능 제공)
* DaemonSet: 노드별로 특정 Pod를 배치할때 사용



## 네트워크 관리(Service)

* 외부에서 Pod에 접근할때 정의
* Load Balancer: 4계층의 부하 분산
* Cluster IP: 클러스터 안의 Pod간 통신을 위한 주소 (Private)
* External IP: 외부에서 접속하기 위한 주소 (Public)



## Label

* 리소스 관리를 위한 이름
* 특정 Pod로만 리퀘스트가 전송되도록 할 수 있음 ==> 논리적 그룹핑



## 구조

### Master

#### API Server

* 리소스 관리를 위한 프론트엔드 REST API

* etcd <-> 리소스 간 통신 중계

#### Scheduler

* Pod를 어떤 노드에서 작동시킬지 제어

#### Controller Manager

* Kubernetes 클러스터 상태를 감시



### 데이터 스토어(etcd)

* API Server가 참조
* 클러스터 구성에 관한 정보 저장



### Node

#### kubelet

* Pod 정의 파일에 따라 컨테이너 수행, 스토리지 마운트
* 노트 상태 감시

#### docker

* 도커 서비스