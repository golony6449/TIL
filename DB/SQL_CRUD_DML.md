# SQL - DML

## Create (INSERT)

```sql
INSERT INTO 테이블 명 VALUES (값, 값, 값 ...);

INSERT INTO 테이블 명 (컬럼명, 컬럼명, ...) VALUES (값, 값, ...);
```

* 문자열은 `'문자열'` 형태로 입력
* 입력 데이터(`VALUES`의 뒷부분) 대신 `SELECT`문을 사용하면 쿼리 결과를 입력데이터로 사용 (스키마가 일치하는 경우만 가능)



## Read (SELECT)

```sql
SELECT 컬럼 리스트 FROM 테이블 목록 WHERE 조건 
GROUP BY 기준 필드 HAVING 그룹화에 사용할 조건 ORDER BY 정렬기준 필드명;
```

* 기본값은 오름차순, 필요시 쿼리 마지막에 `DESC` 키워드를 추가해 내림차순 정리



### UNION 키워드

* 두 쿼리문의 결과를 합치는 연산자
* 행의 모든 값이 일치하는 경우는 1번만 출력 ==> 1개의 필드라도 다르면 별도로 출력
* 주의) 출력의 컬럼 갯수가 같아야 가능
* 응용: `FULL OUTER JOIN` 키워드가 없는 DB(mysql)에서 `LEFT JOIN`, `RIGHT JOIN`으로 구현
  * ==> `LEFT JOIN`, `RIGHT JOIN`의 중복부분은 생략되어 `FULL OUTER JOIN` 구현가능



### 조건 (WHERE)

* `<>`: 다름
* `=`: 같음
* `AND` 키워드를 사용해 여러가지 조건을 부여할 수 있음



### 그룹 함수

* `GROUP BY`키워드로 그룹화 한 뒤 출력형식을 위해 사용되는 형태
* `SELECT`의 출력형식 지정시, `HAVING`의 그룹조건 지정에 사용됨
* 참고자료: https://keep-cool.tistory.com/37

| 함수 이름 | 기능           |
| --------- | -------------- |
| COUNT     | 행의 갯수 계산 |
| MAX       |                |
| MIN       |                |
| AVG       |                |
| SUM       |                |
| VARIANCE  | 분산 계산      |
| STDDEV    | 표준편차 계산  |



## Update

```sql
UPDATE 테이블명 SET 컬럼명=값, 컬럼명=값, ... WHERE 조건;
```

* 주의: 해당 조건에 해당하는 모든 행의 값이 변경됨



### 함수

* `REPLACE(컬럼명, 타켓 값, 변경할 값)`: 특정컬럼에서 해당하는 값을 변경 (`SELECT`문으로 변경될 값을 미리 확인한 뒤 수행)
* `CONCAT(컬럼명, 문자열)`: 해당 컬럼에 문자열을 덧붙임



## Delete

```sql
DELETE FROM 테이블 명 WHERE 조건;
```

* 주의: 조건이 없으면 해당 테이블 내의 모든 행 삭제됨
* `TRUNCATE 테이블명`으로 더 빠르게 테이블 전체 데이터 삭제 가능



### 조건(WHERE)

* `컬럼명 in 쿼리결과`: 해당 쿼리 결과에 결과가 존재하면 삭제

```SQL
DELETE FROM 테이블 명 WHERE id in (SELECT 문)
```