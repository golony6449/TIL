# JSP Standard Tag Library

* JSP = Java + HTML ==> 낮은 가독성
* Solution: JSTL



## 설치

1. JSTL 다운로드 (Apache 자카르타 톰캣 홈페이지)
2. Apache Tomcat 경로 ==> lib 안에 복사



## 라이브러리

* Core
* XML Processing
* I18N formatting
* SQL
* Function



## Core

* 출력, 제어문, 반복문 포함
* 값: `${변수명}` 형태 기술 (EL형식)



* `<%@ taglib uri=http://java.sun.com/jsp/jstl/core prefix="c" %>`
* 출력: `<c:out value="출력값" default="기본값" escapeXml="true or false">`
* 변수 설정: `<c:set var="변수명" value="설정값" target="객체" property="값" scope="범위">`
* 변수제거: `<c:remove var="변수명" scope="범위">`
* 예외 처리: `<c:catch var="변수명">`
* if: `<c:if test="조건" var="조건 처리 변수명" scope="범위">`
* switch

```jsp
<c:choose>
<c:when test="조건">처리내용</c:when>
<c:otherwise>처리 내용</c:otherwise>
</c:choose>
```

* 반복문

```jsp
<c:forEach items="객체명" begin="시작 인덱스" end="끝 인덱스" step="증감식" var="변수명" varStatus="상태변수">
```

* 페이지 이동: `c:redirect url="url">`
* 파라메터 전달: `<c:param name="파라메터명" value="값">`

