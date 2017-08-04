HTML
=====================
## HTML Tag
```html
<ui>    </ui>

<li>    </li>

<a> </a>: 하이퍼링크

href 속성

주의! href 속성의 링크는 반드시 "" 안에 기입해야 함

타 사이트 링크시에는 완전한 URL(ex http://www.google.com)을 기입해야 함 (//, www는 생략해도 되지만 프로토콜은 지정해야 함)

목적지 지정하기: URL + #id명 (ex: ./sample.html#s-1)

target 속성: 해당 링크가 열릴 목표 창 지정. 

해당 목표 창이 존재하지 않으면 해당 이름을 가진 창 생성, _blank 지정시, 새 창으로 열림

주의 1) 로컬 html파일이 아닌 외부 웹사이트로의 하이퍼링크인 경우 비정상적 동작(로컬파일이 동일한 이름을 가지는 경우, 현재 창에서 열림)

주의 2) TTS 등 접근성 관련 브라우저에서 문제 소지 있음

이미지에 링크 연결하기: <a> 태그에 <img>삽입


<h1> ~ <h6> </h1> ~ </h6>

<strong>    </strong>

<p>  </p>: 문단

<html>  </html>: 해당 파일이 HTML 문서임을 표시

<head>  </head>: 웹페이지에 관한 정보(title등)를 포함하는 Scope임을 표기

<body>  </body>: 웹페이지의 본문에 해당하는 Scope임을 표기. 브라우저에서 출력되는 영역

<title> </title>: 웹페이지 제목 지정

<q> </q>: 인용구 태그 (문단의 일부분으로 존재)

<blockquote>    </blockquote>: 긴 인용구 태그(문단과는 별도의 존재, 스스로 보여질 필요가 있는 긴 인용구)

<br> : 라인브레이크(줄바꿈)를 주는 역할만 하는 태그

<pre> : 브라우저에서 타이핑 한 형식 그대로 보여야 할때

<strong> : 강조해야 할 때

<code> : 코드를 보여줄때

<time> : 해당 컨텐츠가 날짜, 시간을 나타냄을 강조(브라우저에 알려줌)

<em> 강조 목적으로 사용
```

#### 공통 속성
* id 속성: 해당 위치로 이동할 수 있도록 지점 추가. 이때 id는 페이지 내에서 유일해야 함 (동일한 ID가 여러개인 경우 최상단 태그에 매칭됨)

* title 속성: 링크에 타이틀(GUI에서 tooltip과 유사) 추가

## CSS style
* 형태: 파라메터: 값;


* margin-(left,right): x% -> 좌우 여백


* pedding: 10px 10px 10px 10px -> 내용 - 경계선 간의 간격


* font-fammily: sans-serif -> 폰트 지정


* background-color: 색상코드 -> 배경색 지정


* border: px dotted black -> 테두리 지정