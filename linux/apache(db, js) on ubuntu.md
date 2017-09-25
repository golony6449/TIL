# apache and friends(DB, JS)
-------------------------

## 개요
### 웹서버?
* 클라이언트가 HTTP 요청을 보내는 타겟(target). 요청을 받은 웹서버는 이를 받아 응답함.
* 단, 내부적으로는 복잡한 통신과정을 거침(Hand-shaking 등)

### 동적 웹서비스
* 서버에서 클라이언트가 필요로하는 정보를  처리 후 그 결과를 HTML형식으로 만들어 클라이언트에게 응답하는 형태의 서비스

* 초창기는 미리 만들어 놓은 HTML 문서를 단순히 전송하기만 했음 (정적 웹서비스)
* 현재는 클라이언트 - 서버 간의 상호작용을 필요로 함 -> 동적 웹서비스

* 이때, 사용자의 요청을 처리하는 응용프로그램 -> 웹어플리케이션 (웹 응용프로그램)이라 함
* 또한, 웹어플리케이션에서 처리할 방대한 데이터 관리를 위해 RDBMS 등장

## 웹서버 구축
### 아파치 웹서버(apache web server) - httpd
* Apache는 오픈 소프트웨어 재단을 의미 -> 아파치 웹서버라는 명칭이 적합
* 가장 널리 사용 중인 웹서버
* 기존의 `NCSA 웹서버`의 패치파일을 제공하던 사람들이 모여 새로 개발한 웹서버 -> NCSA 웹서버에 향상된 기능들을 탑재해 발전함
* 다양한 환경, 플랫폼에서 안정적인 동작 가능

#### 설치
* `sudo apt install apache2`

#### 설정
* 설정파일 경로: `/etc/apache2`
* `apache2.conf`: 기본설정
* `ports.conf`: 포트설정
* `./conf-available/`: 고급기능 설정 (Charecter set, security 등)
* `./mods-available/`: 웹서버의 추가기능(모듈) 저장 위치
* `./mods-enabled/`: 사용하고자 하는 모듈의 링크파일을 저장 (링크파일이 있는 모듈을 활성화)
* `./sites-available/`: 가상호스팅 사용시, 사이트 각각의 설정파일을 보관하는 위치
* `./sites-enabled/`: 사용자가 제공할 웹사이트의 링크 저장 (링크가 저장된 웹사이트는 활성화됨)

### 다른 웹앱, DB와의 연동
* 사용하려고 하는 웹앱 base(ex: PHP, django), DB(ex: Mysql)의 아파치 확장 모듈 설치
* `libapache2-mod-(기능-)모듈명`
* ex: `libapache2-mod-auth-mysql` , `libapache2-mod-php`

* 이때 웹앱의 경우는 dir.conf 파일에 초기 index 웹페이지 코드 포함 (PHP의 경우 index.php)

### Virtual host - 가상호스트
* 싱글유저 기반 웹 서버 1대에서 여러 웹사이트를 운영하는 방법 - apache만 가상화 해놓은 느낌
* 이름기반, IP 기반, 포트 기반 가상화

#### 설정
##### 이름기반 가상화
1. `/etc/apache2/sites-available/000-default.conf`를 복사해 가상호스트 설정파일 생성
2. 설정파일에 `ServerName`, `DocumentRoot` 정보 설정

## 모듈 관리
### 모듈 결합
* `mods-available`의 모듈의 링크파일을 `mods-enable`에 저장
* `a2enmod 모듈명` 명령어 실행

### 모듈 분리
* `mods-enable`의 링크파일 삭제
* `a2dismod 모듈명` 명령어 실행