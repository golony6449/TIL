## Bacula - 네트워크 기반 백업
-------------------------------

* 네트워크 기반 오픈소스 백업 도구
* 로컬 뿐만 아니라, 원격 시스템의 백업도 가능(원격지에 File daemon 설정)
* Pool/Volume으로 자료를 저장 -> 유연한 백업 가능(공간적)

### 구성
1. Director: 백업, 복구 작업을 중앙제어하는 역할
2. Storage: 백업 매체 관리, Director에서 백업요청을 받으면 파일을 백업
3. File daemon: 백업 클라이언트로 백업할 대상 목록을 Director에 전송
4. Database: 작업대상 파일 목록(Catalog)을 저장

### 용어
* Catalog: 파일 목록 정보(metadata)
* Volume: 백업한 파일. Catalog 정보(백업 날짜, 시간, 백업파일에 대한 정보, 볼륨크기)도 같이 저장
* Pool: Volume을 모아 놓은 그룹
* Lable: 백업 전, 저장할 Volume의 이름을 정하고, Pool에 새로운 Volume을 추가하는 과정

### 구성요소 설정
* 구성 요소별 설정 필요
* path: `/tec/bacula/`
* 각각의 설정 파일은 기능을 세분화, 섹션으로 정의 (각 섹션은 {}로 구분)
* 공백은 ""로 묶어야 함
* 구성 요소의 이름은 Bacula가 호스트 이름을 바탕으로 자동 생성 -> 필요시 수정
* conf 파일에서 사용되는 주소는 localhost, 127.0.0.1이 아닌 domain 주소, IP주소 사용해야 함

#### Director
* 나머지 요소에 비해 비교적 복잡한 설정파일
* 섹션: Director(전역설정), Job(할일 목록), FileSet(백업 할 파일 목록), Schedule(스케줄), Client(파일데몬 정보(=클라이언트), Pool(파일을 저장할 풀), Messages(성공, 오류 메세지 처리)

#### Storage
* `bacula-sd.conf`
* 섹션: Storage(전역설정), Director(통신할 Director에 대한 설정), Device(백업 장치 설정), Messages(성공, 오류 메세지 처리)

#### File daemon
* `bacula-fd.conf`
* 섹션: Director(통신할 Director에 대한 설정), FileDaemon(데몬 자신에 대한 설정), Messages(성공, 오류 메세지 처리)
* 이때, Director, FileDaemon 설정은 Director의 Client 섹션을 기준으로 함

### Console 설정
* `bconsole.conf`
* 섹션: Director