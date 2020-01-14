# SQL - DDL

## Create

* `CREATE` 키워드 사용
* DB 생성

```sql
CREATE DATABASE 이름;
```



### 테이블 생성

* 일반적인 쿼리

```sql
CREATE TABLE 이름 (
	컬럼명 데이터타입 조건,
    컬럼명 데이터타입,
    ...
    
    CONSTRAINT 조건이름 조건 (컬럼명)
);
```

* `SELECT`의 출력 형태로 테이블을 만들 수도 있음

```sql
CREATE TABLE 이름 AS
```





#### 제약조건

* PRIMARY KEY: UNIQUE + NOT NULL
* UNIQUE: 해당 행 안에서의 유일성을 보장 (NULL 제외)
* NOT NULL
* FOREIGN KEY: `CONSTRAINT 조건이름 (컬럼명) REFERENCES 테이블명(컬럼명)`



## Read

* 테이블 구조 확인: `DESC(RIBE) 테이블명`
* 테이블 목록 확인: `SHOW TABLES`



## Update (ALTER)

* 테이블 구조 수정

* 컬럼 추가

```sql
ALTER TABLE 테이블명 ADD COLUMN 컬럼명 자료형 조건;
```

* 컬럼 변경 (이름 유지)

```sql
ALTER TABLE 테이블명 MODIFY COLUMN 컬럼명 자료형 조건;
```

* 컬럼 변경 (이름 변경)

```SQL
ALTER TABLE 테이블명 CHANGE COLUMN 컬럼명 변경할 컬럼명 자료형 조건;
```

* 컬럼 삭제

```SQL
ALTER TABLE 테이블명 DROP COLUMN 컬럼명;
```

* 테이블 명 변경

```SQL
ALTER TABLE 테이블명 RENAME 새로운 테이블명;
```



## Delete(DROP)

* 지정된 요소 삭제
* `DROP 요소`
* 요소: DATABASE, TABLE, VIEW