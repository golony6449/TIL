# JDBC

* Java 프로그램에서 SQL 쿼리를 통한 데이터 관리를 위한 API
* DBMS와 매칭됨
* JDBC만 교체하면 다른 DBMS로 전환 가능



## 적용

* 이클립스에 설정된(`JRE_LIB`) classpath에 드라이버(`.jar`) 복사
* 또는 `프로젝트` -> `Java Resources` -> `Libraries` -> `Web App Libraries`에 복사



## 구현

1. JDBC 드라이버 로드: `Class.forName("JDBC")`
2. DB 연결: Connection 객체 `DriverManager.getConnection(Addr, ID, PW)`
3. Statement 생성: `connection.createStatement()`
4. SQL문 실행:`stmt.executeQuery()`, `stmt.executeUpdate()`
5. 결과 사용: ResultSet
6. 연결 해제



### Statement

* 쿼리를 실행시키는 객체
* `executeQuery()`: 여러개의 결과값 (`SELECT`)
* `executeUpdate()`: 테이블 내용이 변경되는 경우



### ResultSet

* `next()`: 다음 레코드
* `previous()`: 이전 레코드 이동
* `first()`: 처음으로 이동
* `last()`: 마지막으로 이동
* `getString()`
* `getInt()`