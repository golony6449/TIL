# Docker 명령어

## 종류

1. `docker run`: `docker create` + `docker start`
   * ``-t`: 종료시 컨테이너 삭제
   * `-i`: interactive 모드
   * `-v <경로>`: 호스트에서 컨테이너로 파일시스템 마운트 (주: 마운트할 디렉토리는 미리 생성해 두어야 함)
   * `--dns`: dns 설정
   * `--restart`: 컨테이너 종료시, Docker가 자동으로 재시작, 최대 3회까지 재시도 (`no | on-failure | always`), 

2. `docker create`: 이미지로 부터 컨테이너 생성
   * --name: 컨테이너 이름 지정

3. `docker pause` / `docker unpause`: 일시중지, 재개
4. `docker stop` / `docker kill`: 컨테이너 중지(SIGTERM 시그널) / 강제종료
5. `docker ps`: 실행중인 컨테이너 목록
   * `-a`: 모든 컨테이너 목록 (pause, stop 상태 포함)

6. `docker rm` / `docker rmi`: 컨테이너 / 이미지 삭제
   * `docker rm $(docker ps -a -q)`: 모든 컨테이너 삭제
   * `docker rmi $(docker images -q -)`: 모든 이미지 삭제
   * `-q`: ID만 출력하는 옵션
   * 필요하다면 별도의 명령인자 사용 가능
   * ex) `docker rm $(docker ps -a -q --filter 'exited!=0')`: 0이 아닌 종료코드로 종료한 모든 컨테이너 삭제
   * 

## 라벨(Label)

* Dockerfile or `create` 명령의 옵션으로 지정 가능
* `docker ps` 에서 라벨을 기준으로 검색, 필터링 가능

## 자원분배

### CPU

* Docker는 전체 CPU 파워를 1024로 간주
* `--cpu-shares <수치>`: 해당 컨테이너에 부여할 CPU 파워 비율, 스케줄링 될 시간을 결정 (상대적 ==> 합이 1024를 넘어도 무관)
* `--cpuset`: 특정한 코어를 지정 (복수 지정 가능 `--cpuset 0,1,2`)

### 메모리

* 컨테이너가 점유 가능한 최대 크기 고정
* `-m <수치> b|k|m|g`: 바이트, 킬로, 메가, 기가 단위 메모리 제한
* `-memory-swap`: 스왑 메모리 공간 제한
* `--kernel-memory`: 컨테이너가 사용가능한 커널 메모리 양 제한
* 허가된 이상의 메모리 점유 시도시, 리눅스의 Out Of Memory 킬러 호출 (비활성화 가능)