# Dockerfile 구조

## 개요

* 도커 이미지 생성에 필요한 기술사항



## 변수

* LABEL: 이미지, 컨테이너에 라벨 삽입 (`docker inspect` 명령으로 확인 가능)
* USER: 컨테이너 내에서 프로세스를 실행할 유저 (기본값: root) (프로덕트 수준에서는 보안상 사용자 계정으로 사용해야 함)
* ENV: 환경변수 설정
* RUN: 명령어 수행 (주: apt, yum은 빌드 시간을 길게 만드는 원흉!)
* ADD: 로컬 파일시스템의 파일을 이미지로 카피하는데 사용
* WORKDIR: 컨테이너 내에서 작업 디렉토리 변경
* CMD: 컨테이너 내에서 실행하고 싶은 프로세스 실행



## .dockerignore

* 이미지를 빌드할때 도커 호스트에 업로드하지 않을 파일, 디렉토리 리스트
* ==> 이미지 빌드 시점에 포함되지 않음



## 참고자료와의 차이점

* MAINTAINER 속성 Deprecated ==> LABEL 속성에 `이메일` 형태로 기술



## 참고

* 도커: 설치에서 운영까지
* git: https://github.com/spkane/docker-node-hello.git