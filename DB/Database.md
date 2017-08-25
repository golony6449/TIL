# Database
### based on 만화로 쉽게 배우는 데이터베이스, 컴퓨터시스템개론
=================================

## 기존의 방식 - 파일시스템
* 각각의 프로그램(부서)에서 데이터를 파일형태로 따로따로 저장
* 프로그램과 파일은 1:1로 매칭됨

### 파일시스템의 문제점
* 데이터중복 -> 리소스 낭비, 공통되는 데이터 변경시 오류 가능성 있음
* 데이터가 분산되어 있음 -> 기존의 데이터를 그대로 재사용 불가능 -> 별도의 파일 추가 생성 (프로그램-파일은 1:1) -> 문제점 심화

#### 문제점 해결을 위해 Database 도입!

## Database
* 가지고 있는 데이터를 여러 사람들이 사용하기 위함

### 요구사항
* 간단한 데이터 입출력 방법 제공
* 안정성 확보 (기밀성, 장애 대비)
* 동시에 일어나는 동일데이터의 수정 상황 대비
* 신속성 (속도)

### DBMS
* DataBase Management System
* 사용자(프로그램) - DB 사이에 존재, 요구사항 충족

### 기본용어
* Recode(레코드): 데이터의 기본 단위, 행렬에서의 행
* Field(필드): 레코드 안 각각의 항목, 행렬에서의 열, 자료의 속성 결정(자료형, 길이, NULL값 가능 여부 등)
* 유일성을 가진다: 값이 중복되지 않는 필드값, 해당 값을 통해 레코드를 구분 할 수 있음 
* NULL: 공란, 값이 비어있음

### 데이터베이스 모델
* 계층형 데이터 모델(Hierarchical Data Model): 데이터들이 계층관계(Tree)를 이루고 있는 모델 (하위데이터들이 <br>1개의</br>상위데이터에 연결됨)
* 그물형 데이터 모델(Network Data ModeL): 데이터들이 그물처럼 서로서로 연결되어 있는 모델 (하위데이터들이 <br>여러개의</br>상위데이터에 연결됨)
* 관계형 데이터 모델(Relational Data Model): 데이터들이 표(Table=Relation) 형태로 구성되어 있는 모델, <br>나머지 2개 모델은 현재 사용하지 않음</br>

### 관계형 데이터베이스
* 표 형태 기반 데이터베이스
* 행: 레코드, 열: 필드
* 키(key): 필드에 부여된 역할
* 기본키(primary key): 레코드에 있어서 중요한 역할을 하는 필드(ex: 유일성을 가짐 or etc)
* 외래키(foreign key): 다른 테이블의 기본키를 참조(reference)하는 필드(열)

#### 장점
* 표를 기반으로 함 -> 쉽게 익숙해질 수 있음
* 연산을 조합해 DB에 대한 다양한 조작 수행 가능

#### RDB의 연산
* 수학에서 사용되는 개념 도입 - 일반 집합 연산자
* 합집합(union): 2개의 표(테이블)에 포함된 행을 전부 출력(세로방향), 동일한 레코드의 경우 1번만 출력
* 차집합(difference): 둘 중 1개의 표에만 있는 레코드 출력(기준표에 따라 결과 달라짐)
* 교집합(intersection): 공통으로 존재하는 레코드만 출력
* 곱집합(cartesian product): 2개의 표에 있는 행들을 조합한 모든 경우의 수

* DB 고유의 연산 - 순수 관계 연산자
* 프로젝션(projection): 특정 열을 출력
* 셀렉션(selection): 특정 행을 출력
* 조인(join): 2개의 테이블을 이어주는 기능, 이때 각 테이블의 기본키(primary key)를 참조(reference)해 적절한 레코드와 연결. (ex: A.join(B)일 때, B의 기본키를 참조하는 A의 필드(열)를 외래키(foreign key)라고 함)
* 디비전(division): 나뉨을 당하는 표에서 나누는 역할의 표의 행을 포함하는 모든 행을 추출 -> 추출한 행에서 나누는 역할의 표에 있는 모든 행을 지우는 연산, 나뉨당하는 표 - 나누는 표의 공통점 중, 나누는 표에 없는 내용을 추출

## DB 설계
* 현재의 데이터를 일정한 모델로 만들어 분석

### E-R 모델 (Entity - Relationship 모델)
* 현실 세계를 `Entity(개체)`와 `Relationship(관계)` 개념을 사용해 DB로 표현
* 주의) 개체를 바라보는 관점에 따라 관계가 달라질 수 있음
* ex) 1개의 강의는 1명의 강사가 담당 but, 1명의 교사는 여러개의 강의를 담당할 수 있음

#### 용어
* 개체: 현실에서 인식가능한 모든 것 (ex: 과일, 수출처)
* 관계: 개체간의 연결을 의미 (ex: 판매(과일과 수출처는 파는 행위로서 연결됨))
* `1:1`: 1개의 개체가 1개의 다른 개체와 연결된 상태(ex: 사과를 미국으로만 수출(사과: 미국(단일국가))
* `다:다`: 다수의 개체가 다수의 개체와 연결된 상태(ex:많은 종류의 과일을 파는 국가(다수의 과일: 다수의 판매국))
* `1:다`: 1개의 개체가 다수의 개체와 연결된 상태(ex: 앵두만 파는 국가(앵두:다수의 판매국))
* <br>정규화: 한개의 표에 1개의 행 항에 일치하지 않는 정보가 없도록, 이를 2개(다수)의 표로 나누는 작업을 의미</br>

#### 정규화 과정 예시
* 매출보고서 표의 필드:  보고서번호, 일자, 수출처코드, 수출처명, 상품코드, 상품명, 단가, 수량
* 이때 1개의 보고서 번호에 여러개의 상품코드가 연결되어 있음 (한번 수출할때 여러개의 상품을 수출하기 때문)
* 이러한 표를 `비정규형`이라고 함

##### 1차 정규화
* 이를 수출표(보고서코드,일자, 수출처코드, 수출처명), 메출명세표(보고서코드, 상품코드, 상품명, 단가, 수량) 과 같이 2개로 나눔 -> `1차 정규형`
* 이때 보고서 코드는 2개의 표의 관계를 알기 위해서 중복시킴

##### 2차정규화
* <br> 2차정규형: 기본키의 값이 정해지면 다른 열의 값도 정해지도록(함수종속성) 나눠진 표를 의미</br> -> 수출표는 이미 2차정규형(기본키: 보고서 코드)
* 즉, 기본키를 정하는 과정
* 함수종속성: 특정열의 값에 의해 다른 열의 값이 정해지는 특성

* 테이블의 필드는 기본적으로 NULL값을 가질 수 없음 -> 매출이 없는 상품은 매출명세표에 추가 불가능 (보고서 코드, 수량 값이 없음)
* 이는 매출명세표에 2개의 개체(상품, 매출)에 대한 데이터가 섞여 있음을 의미
* 매출명세표를 상품표(상품코드, 상품명, 단가), 매출명세표(보고서코드, 상품코드, 수량)로 나눔 -> `2차 정규형`
* 이때 상품표의 기본키는 상품코드, 매출명세표의 기본키는 보고서코드 + 상품코드가 됨

##### 3차 정규화
* <br>3차 정규형: 기본키 이외의 것들로 인해 다른 열들이 정해지는 일(이행종속)이 없도록 나눠진 표</br>
* 즉, 각 항목이 기본키 이외의 항목에 의해 정해지는 경우가 없도록 함
* 이행종속: 특정열의 값에 의해 간접적으로 다른 열의 값이 정해지는 특성

* 수출표의 경우 수출처를 관리 할 수 없음(수출 이력이 없는 국가는 추가 불가능)
* 즉, 수출표의 기본키 정해짐(보고서코드) -> 수출처코드 정해짐 -> 수출처명 정해짐 => 간접적으로 수출처 명이 정해지는 상황

* 수출표 -> 매출표(보고서코드, 일자, 수출처코드), 수출처(수출처코드, 수출처명)으로 나눔 -> `3차 정규형`

#### 1개의 표를 4개의 표로 나눔 but, 각각의 표는 데이터들간의 <br>관계</br>를 나타냄 -> 관계형 데이터베이스
* 외래키: 다른표의 기본키를 참조하고 있는 열을 의미(매출표: 수출처코드 매출명세표: 보고서코드, 상품코드)

### 데이터베이스의 설계
* 개념스키마: 현실세계를 모델링 하는 단계. DB의 논리적인 구조 결정 (ex: E-R모델)
* 내부스키마: 컴퓨터 내부에서 바라본 DB. DB의 물리적인 구조 결정 (ex: DB의 빠른 검색방법 설계)
* 외부스키마: 유저 어플리케이션 입장에서 본 DB. (ex: 어플리케이션을 필요로 하는 데이터 설계)

## SQL
* RDB를 조작할때 사용되는 언어
* 1개의 요청(대화)을 문 이라고 함
* ISO에 의해 표준화 but, 제품마다 독자적인 사양(추가사항)이 존재할수 있으므로 레퍼런스를 참고할 필요 있음

### 기능
* 표 작성 - 데이터 정의어 (Data Definition Language)
* 데이터 입출력(검색, 변경 포함) - 데이터 조작어 (Data Manipulation Language)
* 유저 관리(접근제어 등) - 데이터 제어어 (Data Control Language)

### SELECT - 가장 기본적인 쿼리문
* SELECT 필드명 FROM 테이블 [WHERE 조건 LIKE %두 ORDER BY 행];
* ex: SELECT 상품명 FROM 상품 WHERE 단가>=200;
* 모든 열을 요청할때는 와일드카드(*) 사용
* LIKE: 패턴지정
* ORDER BY: 지정된 행 기준으로 오름차순 정렬
* BETWEEN: 범위 지정
* GROUP BY: 그룹화

#### WHERE - 조건
* A=B: A와 B가 같다
* A>B, (A>=B): A가 B보다 크다(크거나 같다).
* A<>B: A, B가 다르다.
* 조건A AND 조건B: A와 B 둘다 참일때
* 조건A OR 조건B: A, B 중 하나 이상이 참일때
* NOT (조건): 해당 조건의 부정
* IN (): ()안의 값이 일치하는 행과 매칭 

#### LIKE - 패턴을 사용하는 조건
* %: 임의의 수의 문자와 일치
* _: 문자 1개와 일치
* ex: WHERE 이름 LIKE '%수' -> 수로 끝나는 이름 검색

#### BETWEEN - 범위지정
* ex: WHERE 단가 BETWEEN 150 AND 200

#### IS NULL
* 널값 여부를 확인하는 조건
* ex: WHERE 단가 IS NULL

### 통계함수
* ex: SELECT AVG(단가) FROM 상품 -> 상품 테이블에서 모든 단가의 평균값 출력

#### 종류
1. COUNT(*): 행의 갯수
2. COUNT(열의 이름): NULL을 제외한 행의 수
3. COUNT(DISTINCT 열의 이름): NULL, 중복된 값을 제외한 행의 수
4. SUM(열의 이름): 모든 행에서 해당 열의 값 합계
5. AVG(열의 이름): 모든 행에서 해당 열의 평균
6. MAX(열의 이름): 모든 행에서 해당 열의 최대값
7. MIN(열의 이름): 모든 행에서 해당 열의 최솟값

#### GROUP BY - 그룹화
* ex: SELECT 지방 AVG(단가) FROM 상품 GROUP BY 지방; -> 상품 테이블에서 '지방'행을 그룹화해 단가 평균을 표시

##### HAVING: 그룹화를 시켜 집계한 값에 대해 한번더 조건을 지정할 때 사용
* ex: SELECT 지방, AVG(단가) FROM 상품 GROUP BY 지방 HAVING AVG(단가)>=200G; -> '지방'행을 그룹화해 얻은 지방별 평균단가값이 200보다 큰 지방명, 평균단가를 출력

### 서브쿼리(subquery)
* 쿼리 도중 별도의 질의 수행
* SELECT * FROM 상품 WHERE 상품코드 IN (SELECT 상품코드 FROM 매출명세 WHERE 수량>=1000); -> 메출 명세표에서 수량이 1000개 이상인 상품코드와 매칭되는 상품테이블의 상품코드 레코드를 출력
* 안쪽쿼리의 결과 -> 바깥 쿼리에 전달

#### 상관관계 서브쿼리 (correlated subquery)
* 서브쿼리의 바깥에서 지정한 표를 안쪽에서 사용하는 것
* ex: SELECT * FROM 메출명세 U WHERE 수량>(SELECT AVG(수량) FROM 매출명세 WHERE 상품코드=U.상품코드);
* 바깥 쿼리의 결과에 U라는 별칭을 붙혀 <br>한 행씩</br> 안쪽쿼리에 전달 -> 안쪽쿼리의 값(수량의 평균값)을 바깥의 조건(WHERE)에 전달 -> 반복
* 즉, 상품별로 매출수량이 평균보다 큰 경우 출력

### join
* 정규화를 통해 나눠진 표를 다시 연결
* SELECT문을 사용하지만, <br>기본키와 그것을 참조하고 있는 외래키는 같다.</br>라는 조건을 붙혀줘야 함
* ex: SELECT 매출.보고서코드, 일자, 매출.수출처코드, 수출처명, 매출명세.상품코드, 상품명,단가 수량 FROM 매출, 매출명세, 상품, 수출처 WHERE 매출.보고서코드 = 매출명세.보고서코드 AND 매출명세.상품코드=상품.상품코드 AND 수출처.수출처코드=매출.수출처코드;
* 같은 열의 이름이 존재 -> `표이름.열이름` 으로 표기
* 열의 이름은 , 로 구분

#### 종류
* equi join(이퀴조인): 같은 의미를 나타내고 있는 열들을 이용해 조인방식 -> 같은 값을 가지는 행을 조인 조건으로 지정해 연결
* natural join(자연조인): 중복하는 열들을 하나로 정리하는 조인방식
* inner join(이너조인): 공통적인 행만을 선택해 합치는 조인 방식
* outer join(외부조인): 한쪽의 표로 행 전체를 넘긴 뒤, 다른 표에 없는 행은 NULL값으로 지정하는 조인 방식 (왼쪽 테이블로 넘긴경우: 좌외부조인, 오른쪽 테이블로 넘긴경우: 우외부조인)

### CREATE TABLE
* 테이블 생성
* 열의 속성(이름, 자료형, 데이터 범위) 지정, 기본키, 외래키 설정
* ex: CREATE TABLE 상품 (상품코드 NUMBER(3,0), 상품명 CHAR(20), 단가 NUMBER(10,0), PRIMARY KEY(상품코드));

#### 테이블 설정
* PRIMARY KEY: 기본키 설정
* UNIQUE: 유일성 설정
* NOT NULL: NULL값 허용 X
* CHECK: 범위 혹안
* DEFAULT: 디폴트값 설정
* FOREIGN KEY/REFERENCES: 외래키 설정

### INSERT
* 테이블에 데이터(레코드) 추가
* ex: INSERT INTO 상품(상품코드, 상품명, 단가) VALUES(101,'멜론',800);

* 이미 동일한 기본키를 가진 레코드가 존재하는 경우 추가 불가능

### UPDATE
* 테이블의 데이터(레코드) 갱신
* ex: UPDATE 상품 SET 상품명='머스크멜론' WHERE 상품명='멜론';

### DELETE
* 테이블의 데이터(레코드) 삭제
* ex: DELETE FROM 상품 WHERE 상품명='앵두';

### 뷰 (View)
* 유저들에게 보여질 때만 존재하는 가상의 표
* 베이스 테이블의 데이터 일부만 공개하고 싶은 경우 사용하면 편리
* ex: CREATE VIEW 고액상품(상품코드, 상품명, 단가) AS SELECT * FROM 상품 WHERE 단가>=200;

* 뷰 테이블 생성 후에는 고액상품표를 베이스 테이블처럼 검색 가능 (ex: SELECT * FROM 고액상품 WHERE 단가>=500;)

* 삭제 -> DROP VIEW 고액상품

### 응용프로그램에서 SQL 이용하기
* 정적 SQL: 컴파일시에 SQL문을 발행
* 동적 SQL: 실행시 SQL문을 발행

#### 커서를 이용한 행 이동
* 통상적인 프로그래밍언어에서 하나의 명령(쿼리문)에 의한 표의 여러행을 한번에 처리하는 기능은 없음 -> 커서를 이용해 표의 1행씩 액세스 
* 반복문을 사용해 커서를 이동함으로서 한 행씩 순서대로 액세스 가능(fetch)
* fetch? -> 커서를 이용해 한 행씩 데이터를 출력하는 것 

## 트랜잭션(transaction)
* DB에서는 의미있는 데이터조작을 한번에 모아서 처리하도록 설계됨 -> 이러한 데이터의 조작 단위: 트랜잭션
* ex: 데이터 읽기 + 데이터저장 -> 하나의 트랜잭션

* DB는 다수의 유저들에 의해 공유됨 -> 여러개의 트랜잭션이 동시에 실행되어도 불일치가 발생하지 않아야함 -> ACID 속성 요구됨

#### ACID 속성
* A(Atomicity): 원자성 - 트랜잭션은 커밋, 롤백 둘 중 하나로 종료되어야 함
* C(Consistency): 일관성 - 트랜잭션을 실행할 때, DB의 일관성은 손실되지 않아야 함
* I(Isolation): 격리성 - 트랜잭션을 병렬적으로 처리할 경우라도, 순차 처리 했을때와 처리 결과는 동일 해야 함
* D(Durability): 영속성 - 완료된 트랜잭션의 내용은 장애에 의해서 손실되지 않아야 함

### A(tomicity) - 커밋 & 롤백
* ACID 속성에서 A(atomicity) 성질 충족을 위한 기능
* 자동으로 실행되는 경우, 유저의 명령에 의해 실행되는 경우가 있음

#### 커밋(commit)
* 트랜잭션 작업이 올바르게 종료된 경우 수행되는 작업
* 데이터 베이스의 처리를 확정하기 위한 명령
* COMMIT; -> 커밋을 강제로 실행

#### 롤백(rollback)
* 일정시간 이상 대기상태 지속시 트랜잭션을 조사해 취소하는 것 (트랜잭션으로 실행된 작업을 합쳐서 전부 취소 -> 아예 작업이 이뤄지지 않은 상태)
* 데드락(락이 걸린 2개의 데이터가 서로의 락이 풀릴 때까지 대기)상태를 해결하기 위한 방법
* ROLLBACK; -> 롤백을 명시적으로 실행

#### 트랙잭션은 커밋 or 롤백 둘 중 하나로 종료

### C(onsistency) - 일관성
* 트랜잭션 작업전 DB간 불일치가 없는 경우, 작업실행 후에도 불일치가 없어야 한다는 성질
* -> 트랜잭션이 같은 자원에 병렬적으로(동시에) 엑세스해도 불일치가 없도록 처리

* 자원(resource): 트랜잭션의 작업대상을 의미. ex: 표, 행

#### 갱신 무효 문제(lost update)
* A, B가 동시에 작업(갱신)한 경우, 둘 중 하나의 작업이 무시된 경우를 의미

### I(solation) - 격리성
* 요구사항: 직렬가능성 충족
* 직렬가능: 복수의 트랜잭션을 병렬처리했을때도 순차처리 했을때와 결과가 같을때를 의미
* 직렬가능성 충족을 위해 병행제어 수행

#### 병행제어
* 락을 사용해 복수의 트랙잭션을 제어하는 것 -> 가능한 많은 사람들이 이용하면서도, 데이터간의 불일치를 방지

##### 종류
1. 락(lock)
2. 시간기록기 제어(timestamp control): 트랜잭션이 엑세스하는 데이터에 타임스탬프 부여. 해당 트랜잭션 보다 새로운 타임스탬프의 트랜잭션이 데이터를 갱신하면 데이터의 입출력을 허가 하지 않음 (허가X방법: 롤백)
3. 낙관적제어(optimistic control): 일단은 모든 트랜잭션의 입출력 허가. 이후, 입력 지점을 시작으로 다른 트랜잭션에 의한 데이터 갱신 여부를 검사. (갱신된 경우, 롤백 수행)

#### 락(lock) - 가장 널리 사용
* DB는 다수의 유저들이 동시에 액세스해도 데이터가 이상을 일으키지 않도록 트랜잭션을 컨트롤함

* 트랜잭션 시작전 락을 검 -> 작업이 끝나기 전 까지는 다른 유저의 트랙잭션은 대기
* 각각의 트랜잭션 작업이 올바르게 끝난 경우 실행 완료처리(커밋, commit) 수행

* 단, DB는 많은 사람들이 데이터를 공유함 -> 지나친 락 남발은 좋지않음, 상황에 따라 분별사용 권장

#### 락의 종류
* 공유락: 락이 걸린 동안 출력은 가능, 입력은 불가 (유저들이 데이터 출력 작업만 하는 경우 사용) -> 다른 트랜잭션이 공유락은 동시에 걸수 있음
* 배타락: 락이 걸린 동안 입출력 모두 불가능 (유저들이 데이터 입력을 해야하는 경우 사용) -> 걸린동안, 공유락, 배타락 모두 불가능

#### 2단계 락킹(two-phase locking)
* 직렬가능성 보장을 위해 설정된 락을 설정/해제에 대한 규약
* 각각의 트랜잭션을 락을 거는 단계, 해제하는 단계로 구성하는 것 (모든 필요한 DB 락 -> 처리 -> 락한 DB 해제)

#### 차단범위 - 락을 거는 범위
* 단위: 표단위, 행단위
* 큰 차단 범위: 각각의 트랜잭션이 락을 거는 횟수 감소(CPU 부담 감소), 다른 트랜잭션이 락의 해제를 기다리는 시간이 길어짐(동시실행 가능한 트랜잭션 수 적음)
* 작은 차단 범위: 각각의 트랜잭션이 락을 거는 횟수 증가(CPU부담 증가), 락의 해제를 기다리는 시간 감소(동시실행 가능한 트랜잭션 수 많음)

### 격리수준
* 동시에 실행 가능한 트랜잭션의 증가를 위해, 트랜잭션들이 간섭가능한 레벨을 지정한 것
* ex: SET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED;

#### 종류
| 명칭 | 오손 판독 | 반복 불가능 읽기 | 유령 읽기 |
|-----|-------------|--------------|------------|
| READ UNCOMMITTED | 발생가능성 있음 | 발생가능성 있음 | 발생가능성 있음 |
| READ COMMITTED | 발생 X | 발생가능성 있음 | 발생가능성 있음 |
| REPEATABLE READ | 발생 X | 발생 X | 발생 가능성 있음 |
| SERIALIZABLE | 발생 X | 발생 X | 발생 X |

* 오손판독(dirty read): 트랜잭션 A의 커밋 이전에 트랜잭션 B가 해당 행을 출력 -> 존재하지 않는 행을 출력하는 상황
* 반복 불가능 읽기(non-repeatable read): A가 행을 출력했을때, B가 행을 갱신후 커밋한 상황 (A가 다시 출력했을 때 다른 값이 출력됨)
* 유령 읽기(phantom read): A가 조건검색을 수행해서 결과를 얻었음. 이때, B가 해당 조건을 만족하는 행을 추가한 상황 (A가 재검색 했을때 검색 결과가 달라짐)

### 보안
* 액세스 제어(ID/Password), 작업권한 설정

#### 작업권한 부여 - GRANT
* 작성한 표에 대한 권한을 다른유저에게 부여
* GRANT SELECT, UPDATE ON 상품 TO 외국부; -> 상품표의 SELECT, UPDATE권한을 외국부에게 부여
* GRANT SELECT, UPDATE ON 상품 TO 외국부 WITH GRANT OPTION; -> 부여받은 권한에 한해 다른 유저에게 권한 부여 가능

* 권한을 그룹으로 만들어 한번에 부여 할 수도 있음

##### 권한종류
1. SELECT: 표 안의 행을 검색할 수 있는 권한
2. INSERT: 표 안의 행을 삽입할 수 있는 권한
3. UPDATE: 표 안의 행을 갱신할 수 있는 권한
4. DELETE: 표 안의 행을 삭제할 수 있는 권한
5. ALL: 모든 것이 가능한 권한

#### 권한 철회 - REVOKE
* REVOKE SELECT, UPDATE ON 상품 FROM 외국부;

### 인덱스 그리고 고속화
* 데이터 검색을 1행부터 순차로 진행
* DB의 규모가 증가 -> 검색처리 지연등의 문제 발생 -> 인덱스를 지정해 해결
* 특정 행에 대해 인덱스를 미리 작성 ->  해당 행으로 검색시 저장된 장소를 바로 알수 있음
* ex: 상품코드 행에 대해 인덱스 지정 -> 상품코드=101 검색시 빠른 장소파악 가능

#### 인덱싱 방법
* B-트리: 트리형태로 관리. 검색은 2진 탐색트리와 유사하게 진행됨 (참고자료: https://ko.wikipedia.org/wiki/B_%ED%8A%B8%EB%A6%AC , http://runtoyourdream.tistory.com/137)
* 해시: 데이터의 키 값에 대해 해싱함수를 적용해 위치계산. 완전일치검색(ex: code=101)에 유리. 비교조건, LIKE와 같은 연산에는 대응 불가

#### 인덱스는 만능일까?
* 모든 데이터에 대한 연산(출력등)인 경우 처리가 오히려 늦어짐(순차적으로 연산하면 되는 데, 인덱스는 여기에 추가적인 연산을 필요로 함)
* 너무 많은 인덱스는 효율 저하 가능성 있음 (데이터의 잦은 갱신 -> 잦은 인덱스 재 작성)

### 쿼리 최적화
* optimizer: DB에서 쿼리 최적화를 담당하는 기능

* 룰 베이스(rule base): 사전에 룰을 지정하고, 지정된 룰(우선순위)에 따라 수단 선택 -> 적절치 않은 룰 설정시 현재 상태에 맞지않는 방법 적용
* 코스트 베이스(cost base): DB내부의 통계정보에 따라 수단 선택 -> 유연한 최적화 가능, 통계정보를 정기적으로 작성 할 필요 있음 -> 별도의 통계관련 관리 분석 필요

#### 쿼리의 수행순서
* 동일한 역할의 쿼리문이라고 해도 수행 순서에따라 처리시간이 달라짐
* ex: SELECT 일자,품명 FROM 상품, 매출 WHERE 단가>=200 AND 상품.상품코드=매출.상품코드;

1. 상품표, 매출표 JOIN 수행
2. 단가 200G 이상인 레코드 SELECT
3. 일자, 품명 열 출력(PROJECTION)

* 1->2->3 순서: JOIN을 수행하면 행수가 많은 중간표가 생성됨 -> 처리지연 발생

* 3->2->1: PROJECTION, SELECTION(단가비교)을 먼저 수행 -> 비교적 행수가 적은 중간표 생성

#### 일반적인 쿼리 순서 결정
* SELECTION: 행수 감소 -> 인덱스등의 방법으로 최적화
* PROJECTION: 결과와 무관한 행 무시
* JOIN: 마지막에 수행(수행 이후 표의 규모 증가하기 때문)

#### JOIN 방법
* 네스티드 루프 조인 - nested loop join: 한 표의 1행을 다른 표와 비교해 가면서, 같은 경우 조인한 행을 결과로서 작성
* 소트 머지 조인 - sort merge join: 각 표를 정렬(sort)한 뒤, 선두 행 부터 대조해 같은 겨우 조인한 행을 결과로서 작성. sort에 소요되는 cost에 유의
* 해시 조인 - hash join: 표를 해싱함수로 분할, 다른 표에서 같은 해시 값을 가지는 행을 조인

### D(urability) - 영속성
* 트랜잭션이 장애에 의해 잘못된 결과로 바뀌지 않도록 하는 성질 -> 사전에 백업, 로그를 만드는 작업 수행
* DB는 장애복구(회복)기능을 가지고 있음
* 데이터를 조작 할 때 마다 로그(log) 기록 (DB의 변경사항 기록) -> <br>DB를 갱신할 때, 갱신 전후를 기록!</br>

#### 장애 상황
* 트랜잭션 장애: 트랜잭션의 오류에 의해 트랜잭션 완료 불가 상황 -> 해당 트랜잭션 롤백
* 시스템 장애: 시스템이 다운된 상황 (정전 등) -> 발생시점에 커밋되지 않은 트랜잭션은 롤백, 커밋된 트랜잭션은 롤 포워드 수행
* 미디어 장애: 저장매체가 손상된 상황 -> 백업파일을 바탕으로 장애복구. 백업 이후 커밋된 트랜잭션에 대해 롤 포워드 수행

#### 장애가 발생했다!!
1. 시스템 재기동
2. 로그를 이용해 DB 복구

##### 트랜잭션이 커밋 된 경우
* 커밋된 트랜잭션은 처리가 확정된 상태 -> 처리결과를 반영한 복구(롤 포워드) 수행
* 롤 포워드(roll forward): 데이터를 갱신했을 당시, 갱신 후의 값을 참조해 복구

##### 커밋이 되지 않은 경우
* 처리 중간에 장애 발생 케이스 -> 롤백 수행(트랜잭션 시작 전으로 되돌림)
* 갱신 전의 값을 참조해 트랜잭션 처리 취소

#### 체크포인트 and 복구
* 버퍼에 입력된 내용이 DB에 갱신되는 지점
* 버퍼: 효율적인 입력을 위해 일시적으로 데이터를 저장해두는 공간 이름

* 반영시점에 커밋이 된 트랜잭션은 장애복구를 수행할 필요 없음(반영완료), but 커밋되지 않은 것은 장애복구 대상이 됨
* 체크포인트 - 장애발생 사이에 커밋이 된 경우 -> 롤 포워드, else 롤백

## DB의 활용
* DB는 동시접속에 대응가능하며, 장애대응도 가능하기 때문에 여러 기업, 관공서에서 활용중

### Web and DB
* 3층 클라이언트, 서버 시스템: 클라이언트 - (웹 서버 - 웹어플리케이션 서버) - DB 서버

* 프리젠테이션 계층: 유저의 입력(검색조건 등)을 받아들이고, 그에 따른 결과 표시 수행.
* 평션 계층: 데이터 가공(쿼리문 작성) 수행
* 데이터 계층: 각종 쿼리문을 받아, DB가 가동되고 있는 계층

* 클라 -> 웹서버: HTTP Request
* 웹서버 -> DB 서버: SQL query
* DB 서버 -> 웹서버: SQL Response
* 웹서버 <- 클라: HTTP Response

* 웹 서버: 웹페이지를 작성. 요청에 응답. 웹페이지 작성에 필요한 자료를 웹앱 서버에 요청
* 웹어플리케이션 서버: 웹 서버가 요청한 자료를 처리 (SQL 쿼리 요청 등의 작업 수행)

### 분산형 데이터베이스
* 데이터베이스를 여러 개의 서버로 관리 -> 3층 시스템에서 데이터베이스 자체를 다른 환경으로 분산 시킨 경우를 의미
* 단, 분산되어 있더라도 유저(웹앱 서버)가 사용할 때는 하나의 데이터베이스(한 장소)인 것 처럼 다룰 수 있어야 함 -> 무관성(transparency)

#### 구성방법
##### 수평분산
* 여러 개의 대등한 데이터베이스 서버 사용 -> 각각은 다른 DB 서버의 데이터를 이용 할 수도 있고, 자신의 데이터를 제공하기도 함
* 서버중 하나에 장애발생시에도 나머지 DB는 가동가능 -> 장애 대처에 강한 시스템

##### 수직분산
* 각각의 DB 서버가 다른기능을 가지도록 하는 방식
* 중심 역할의 주 서버(main server), 주 서버가 처리를 맡기는 각각의 서버로 구성
* 각 서버는 메인 서버의 DB를 이용 가능, but 주 서버는 나머지 서버의 DB 이용 <br>불가능</br>
* 메인 서버의 관리가 용이, but 메인 서버에 트래픽이 집중되는 약점 존재

#### 장점 and 주의점
* 서버 일부에 문제가 생겨도, DB전체가 다운되지 않음 -> 안정성 증가

* 커밋 수행시, 여러 개의 서버간에 불일치가 발생하지 않도록 유의 해야할 필요 있음 (네트워크 장애와 같은 상황 대비 필요)

#### 데이터 분할
* 분산형 DB에서는 데이터를 각 서버에 분할해 저장

##### 수평 분할
* 테이블을 행 방향으로 분할
* 같은 종류의 데이터를 분산시킬때 사용

##### 수직분할
* 테이블을 열 방향으로 분할
* 필드의 속성별로 분산시킬때 사용

#### 2단계 커밋
* 커밋을 2단계(조정자, 참가자)로 나눠 구성
* 보통의 커밋으로는 다른 서버가 갱신 되지 않을 가능성 존재 -> 원자성(atomicity), 일관성(consistency) 위반 우려 -> 2단계 커밋 수행

##### 1단계 - 조정자
* 시큐어 작업 수행
* 각각의 참가자에 대해 커밋 가능 여부 질의 -> 커밋가능하면 OK 를 reponse

##### 2단계 - 참가자
* 조정자가 커밋의 지시에 따라 참가자에 의한 커밋 수행

###### 1단계에서 어느 하나의 장소라도 시큐어 실패시 모든 참가자에게 롤백 지시

#### 분산형 DB를 이용한 join의 종류
* 분산형 DB에서 join은 일반적인 DB보다 더 주의해야할 필요 있음 -> 서버간의 네트워크에 걸리는 부하까지 고려해야 하기 때문

1. 네스티드 루프 조인(nested loop join): 서버 A의 표를 1행씩 서버 B로 송신 -> B의 모든 행과 비교해 join 수행
2. 소트 머지 조인(sort merge join): 각 서버의 표를 join 하기 전 sort 수행 -> 한 행씩 읽어가면서 join 수행
3. 세미 조인(semi join): 서버 A의 키 열을 B로 전송 -> B는 전송받은 열을 조건으로 해 SELECT 연산 수행, 수행 결과를 A로 전송 -> A는 응답받은 결과를 토대로 join 수행
4. 해시 세미 조인(hash semi join): 서버 A가 열들에 대한 해시값 계산, 이를 B로 전송 -> B에서도 B의 해시값 계산, 이후 전송받은 해시값을 대조해 join 수행

#### 레플리케이션(replication)
* 네트워크 부하 감소를 위해 DB(메인 서버)를 복제하는 것
* 원본 DB: 마스터 데이터베이스, 복제된 DB: 레플리카

##### 종류
* 출력전용: 마스터 DB(메인 서버)에서 출력전용의 레플리카를 작성, 이를 다운로드. 레플리카는 출력만 가능하도록 설정됨

* 메인 서버에 갱신 가능: 마스터 DB를 복제 -> 레플리카를 이용해 갱신작업 가능! (레플리카 갱신시 마스터 DB에 반영)

* 각각의 서버로 갱신 가능: 각각의 서버끼리 같은 마스터 DB를 가지는 방법. 각각의 서버에서 레플리카를 갱신하면, 마스터를 포함한 나머지 레플리카도 갱신됨

### 그외의 응용
* XML(eXtensible Markup Language): 데이터 저장방식 중 하나. 데이터를 태그로 구분해 나타내는 확장가능 마크를 붙인 언어. 엄격한 문법을 가지기 때문에 프로그래밍에 의한 처리가 매우 간편. 

* 객체 중심 데이터베이스(OODB): 그림 등의 데이터의 경우 RDB에서 표 형식의 텍스트로 저장시 유연성이 결여되는 문제점 존재 ->  객체 개념을 도입한 DB. 클래스를 이용해 각각의 객체(instance)를 작성. 캡슐화, 상속과 같은 OOP의 개념 적용 가능

### 스토어드(Stored) and 트리거(Trigger)
#### 스토어드 프로그램(Stored program)
* 네트워크에 부담을 줄이기 위해, 자주 사용하는 작업을 미리 DB에 저장 -> 매번 쿼리문을 발행 할 필요없이 저장된 프로그램을 수행하는 것으로 갈음

* 스토어드 프로시저 (Stored procedure): 처리 순서를 거꾸로 되돌릴 수 없는 프로그램
* 스토어드 평션 (Stored function): 처리순서를 거꾸로 되돌릴 수 있는 프로그램
* 트리거(Trigger): 데이터베이스에 작업을 실행하는 전후(=특정 조건 충족시)에 기동하는 스토어드 프로그램. (ex: 주문으로 인한 DB 갱신 발생 -> 재고감소, 발송처리 자동 수행)

#### DB는 웹서버의 뒷 단에서 작동 -> 유저가 사용할때 DB의 존재를 인식하기는 어려움 (오히려 인식하지 못할때 DB는 자기 역할을 충실히 수행한다고 볼수 있음)