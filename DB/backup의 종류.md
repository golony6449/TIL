## Backup
----------------------------
### 고려사항
* 백업할 대상 데이터 선별 - 보존가치, 전체 or 일부분, 같이 백업해야 할 다른 파일 유무
* 백업 방식 결정: 증분백업, 온라인 백업등 방식 결정
* 시기 결정: DB의 사용이 가장 적은 시간 파악, 보관 할 로그의 양 파악, 해당 DB를 사용하는 클라이언트 수 파악

### 종류
* 전체 백업 - Hot backup(online backup), Cold backup(offline backup)
* 증분 백업(Incremental backup)
* 소산 백업

### 전체 백업
* 데이터베이스 전체에 대해 특정 시점에 대한 백업(스냅샷) 생성

#### Hot backup(=Online backup)
* 운영 중인 DB에 대해 백업 작업 수행
* 운영 중인 상태이기 때문에, 커밋되지 않은 데이터 저장 우려 있음
* DB가 open 상태이어야 함

#### Cold backup(=offline backup)
* 정지 상태인 DB에 대해 백업 작업 수행
* 작업 중인 동안 서비스 불가능

### 증분 백업(Incremental backup)
* 전체 백업에 대해 종속적으로 수행되는 작업 -> 전체백업 수행 이후의 변경사항만을 선택적으로 백업
* 시간, 공간 절약 가능

### 소산백업(Off-site data protection)
* 화재, 천재지변으로 인한 물리적 자료소실을 대비해 원격지에 데이터를 백업하는 것
* 대역폭 등의 문제로 인해 자기테이프 등의 실물 매체에 저장한 뒤 운반하기도 함
* 큰 규모의 Off-site backup의 경우 DR Center(Data Recovery Center)라는 장소에 저장

* ex) rman, Dataguard(at ORACLE)

#### ORACLE에서의 소산 백업
* 원본-A, 원격지-B 일때, 한쪽은 primary key, 다른쪽을 standby key로 구성
* 한쪽에서 데이터 입력시 standby key에 메타데이터(transection 정보 or redo 파일)을 넘겨서 백업 하고 필요시 복구함
* 데이터의 용량 문제 때문에 데이터 파일 전체를 넘기지는 않음

* 메타데이터: 실제데이터 관련정보를 의미 (위치, 변경사항 등)