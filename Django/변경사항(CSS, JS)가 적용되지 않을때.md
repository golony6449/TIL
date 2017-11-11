#변경사항(CSS, JS)가 적용되지 않을때
-----------------
### Django 문제 X
### 브라우저가 캐시해 둔 Static파일을 사용하기 때문
* Chrome: Ctrl + F5

### F5 vs Ctrl + F5
#### F5
* 화면의 컨텐츠 새로고침
* 내용(HTML)만을 새로고침 함 -> 새로고침 되지 않는 부분 존재

#### Ctrl + F5
* 관련된 모든 Cache등을 모두 새로고침
* Icon, CSS, JS등 모든 내용 새로고침 됨

### 그 외
* IE, Chrome, Safari, FF등 다양한 브라우저에서 제공하는 기능임
* 단 OS별로 단축키가 다름
* Win: Ctrl + F5
* Mac: Apple + R (Command + R)
* Linux: F5