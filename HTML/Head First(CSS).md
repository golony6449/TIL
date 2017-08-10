Head First HTML and CSS
========================
## Chapter 7 CSS
* 구성: 요소(태그) + 해당 요소의 속성 + 속성에 적용할 스타일
* ex)
```html
p { <!--디자인 할 요소 선택-->
    background-color: red;  <!--속성과 스타일 선택-->
}
```

* 요소를 선택할때, 한번에 여러 요소를 선택할 수 있음
* 이미 스타일을 적용한 요소에 또 다른 스타일을 적용 할 수 있음
* ex)
```html
h1, h2 
{
    font-family: sans-serif;
    color: gray;
}
h1
{
    border-bottom: 1px solid black;
}
```

### 스타일 정보를 html 외부에 저장하기
* html에 스타일 정보를 하드코딩하면, 추후 디자인 변경시 html마다 변경해야 하는 불상사 발생!

#### 방법
1. style 태그를 제외한 나머지 내용을 css파일에 저장
2. html파일의 헤드에 `<link type="text/css" rel="stylesheet" href="style.css">` 를 추가해 외부 스타일시트에 연결

### 상속
* 요소 내부에 포함된 요소들은 상위 요소 스타일의 <b>일부</b>를 상속받음
* 주의) 모든 스타일이 아닌 일부(font-family, color, font-size,font-style 등)만 상속받음

#### 상속 재정의
* 상속받은 스타일 요소를 재정의
* 별도의 스타일을 지정하고 싶은 요소에 해당 속성을 기입 하면 끝!
* ex)
```html
body
{
    font-family:sans-serif;
}
em
{
    font-family:serif;
}
```

### 주석
* /* */ 사이에 작성된 내용은 주석 처리됨

### 클래스 생성
#### 생성
1. HTML의 요소에 class 속성 추가 -> 해당 요소를 클래스에 추가함
2. CSS에서 해당 클래스 선택


#### 예시
* html 파일
```html
...
<p class="greentea tea drink"> <!--요소는 1개 이상의 클래스에 속할 수 있음-->
</p>
```

* css 파일
```html
p.greentea  <!--greentea 클래스의 p요소-->
{
    color:green
}
```

### 스타일이 적용되는 방법
1. 요소를 선택한 선택자가 있는가? -> 선택자가 있고, 해당 선택자가 속성, 값을 가지고 있는 경우 해당 값이 요소의 값이 됨
2. 상속이 받는 것이 있는가? -> 1에서 선택자가 없는 경우, 부모를 탐색.
3. 기본 설정값 사용 -> 상속받는 값도 없는 경우 브라우저의 기본 설정값 사용

* 여러개의 선택자가 요소 하나를 갖는 경우: 가장 구체적인 규칙을 값으로 사용, 구체성이 동일한 경우는 가장 마지막에 나온 값을 사용

### CSS의 유효성 검사
* html과 마찬가지로 유효성 검사기(validator) 존재함
