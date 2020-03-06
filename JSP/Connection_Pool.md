# Connection Pool



## DAO

* Data Access Object
* DB에 접근 ==> 데이터 추가, 삭제 수정 작업(==로직) 수행 클래스
* JSP, Servlet 내부에 기술할 수도 있지만, 모듈화를 위해 별도의 DAO 생성해 사용



## DTO

* Data Transfer Object
* DAO 클래스를 이용해 DB관리시에 데이터를 클래스화(묶어서)해서 처리
* Servlet(JSP) - DAO 중간에 위치



## PreparedStatement 객체 살펴보기

* `Statement`의 중복코드가 많아지는 단점 해결

```java
Class.forName(driver);
conn = DriverManager.getConnection(url, uid, pw);
int n;
String query = "insert into memberforpre (id, pw, name, phone) values (?, ?, ?, ?)";
preparedStmt = conn.prepareStatement(query);

preparedStmt.setString(1, "abc");
preparedStmt.setString(2, "123");
preparedStmt.setString(3, "홍길동");
preparedStmt.setString(4, "010-1234-5678");
n = preparedStmt.executeUpdate();
```



## Connection Pool (DBCP)

* 클라이언트에서 다수의 요청 발생시 DB에 접속할때 발생하는 부하 발생
* 톰켓 서버 상에서 미리 커넥션을 생성 ==> 사용



### 적용

1. Tomcat 컨테이너가 DB 인증을 하도록 `context.xml` 파일 수정

```xml
<Resource
          auth="Container"
          driverClassName = "드라이버"
          url = "주소"
          username = "id"
          password = "pw"
          name = "이름"
          type = "javax.sql.DataSource"
          maxActive = "생성할 커넥션 갯수"
          maxWait = "커넥션 생성에 대한 Timeout 값"
```

2. DataSource 객체 생성
3. Context 객체 생성
4. lookup 수행
5. 데이터 소스에서 커넥션 획득

```java
DataSource dataSource;

try{
    Context context = new InitialContext();
    dataSource = (DataSource)context.lookup("이름");
}

catch (Exception e){
    e.printStackTrace();
}

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~``

conn = dataSource.getConnection();

```

