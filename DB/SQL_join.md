# JOIN

## 개요

* 테이블을 연결해 거대한 가상의 테이블을 만들어 데이터를 검색하는 방법
* 많은 연산량 요구
* 종류: `(INNER) JOIN`,  `LEFT (OUTER) JOIN`, `RIGHT (OUTER) JOIN`,  `FULL OUTER JOIN`



## INNER JOIN

* 두 테이블의 교집합 요소만 출력

### WHERE을 이용한 JOIN

```sql
SELECT * FROM student, location WHERE student.location = location.id;
```



### ANSI 표준 JOIN

```sql
SELECT * FROM student JOIN location ON student.location = location.id;
```



## LEFT JOIN

* FROM 키워드(왼쪽)의 테이블의 모든 정보 + 연관된 JOIN 키워드의 테이블 정보 출력
* 테이블의 위치를 바꾸면 RIGHT JOIN과 동일한 결과

```sql
SELECT * FROM student LEFT JOIN location ON student.location = location.id;
```



* `ORACLE`에서는 아래 형태로도 가능 (연관시킬 테이블에 `(+)` 키워드 추가)

```sql
SELECT * FROM student, location WHERE student.location_id=location.id(+);
```





## RIGHT JOIN

* JOIN 키워드(우측)의 테이블 정보 + 연관된 FROM 키워드(왼쪽) 테이블의 정보
* 테이블의 위치를 바꾸면 LEFT JOIN과 동일한 결과

```sql
SELECT * FROM student RIGHT JOIN location ON student.location_id = location.id;
```



* `ORACLE`에서는 아래 형태로도 가능 (연관시킬 테이블에 `(+)` 키워드 추가)

```sql
SELECT * FROM student, location WHERE student.location_id(+)=location.id;
```





## FULL OUTER JOIN

* 두 테이블의 합집합
* 오라클에서만 가능한 키워드

```sql
SELECT * FROM student FULL OUTER JOIN location ON student.location_id=location.id;
```



* MySQL의 경우는 `UNION`을 사용해 동일한 결과물을 얻을 수 있음

```sql
SELECT * FROM student LEFT OUTER JOIN location ON student.location_id=location.id
UNION
SELECT * FROM student RIGHT OUTER JOIN location ON student.location_id=location.id;
```





## 3개 이상의 테이블의 JOIN

### WHERE을 사용한 JOIN

```sql
SELECT * FROM student, location, subject 
WHERE student.location_id=location.id AND student.subject_id=subject.id;
```



### ANSI 표준 JOIN

* JOIN ~ ON을 연달아서 명시

```sql
SELECT * FROM student
JOIN location ON student.location_id=location.id
JOIN subject ON student.subject_id=subject.id;
```





## 참고자료

* JOIN의 종류: https://opentutorials.org/course/195/1409
* (Oracle) Join: https://goddaehee.tistory.com/62
* (Oracle) Join: https://devjhs.tistory.com/73