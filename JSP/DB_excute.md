# excute VS executeQuery VS executeUpdate

## execute

* `excuteQuery`, `executeUpdate` 모두를 포함
* ==> DDL, DML, DCL 모두 사용 가능
* 반환형: boolean



## executeQuery

* 반환형: ResultSet
* 주로 `SELECT`문을 사용



## executeUpdate

* 적용된 행의 수를 반환하는 메소드
* DDL(`INSERT`, `UPDATE`, `DELETE`), DML(`CREATE`, `DROP`, `ALTER`)에 사용