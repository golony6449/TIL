# NGINX 설정에서 root, alias간 차이

## 개요

* NGINX에서 정적파일 서비스를 하기 위해 `location`에 `root`나 `alias`를 설정하게 된다.
* 이번 프로젝트 세팅 중에도 아니나 다를까 햇갈려서 이 참에 정리해 볼까 한다.
* 주의) 파일을 제공할때는 둘 다 절대경로 지정



## 공통

* 요청이 들어왔을 때 제공할 파일을 탐색할 경로를 지정



## root

* `location`으로 넘어온 부분을 `root` 뒤에 추가한 뒤 접근

* 설정: `location /static { ~~~ }`, `root /app/static;`
* 탐색 위치: `/app/static/static/`



## alias

* `location`에 매칭된 부분을 제외하고 `alias`뒤에 추가한 뒤 접근

* 설정: `location /static { ~~~ }`, `alias /app/static;`
* 탐색위치: `app/static`



## 참고자료

* <https://ohgyun.com/556>