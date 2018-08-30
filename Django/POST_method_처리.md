# Post method processing

## POST method를 반드시 사용해야 하는 상황
1. 제출된 폼을 이용해 서버의 모델(데이터)를 조작하는 경우
* 인덱싱, 검색봇(bot), 새로고침 등등의 이유로 URL 상에 값이 그대로 고정(노출) 되면 예상치 못한 상황 발생 가능성 존재

2. 폼에 개인정보등의 포함된 경우
* 최근 본 목록(recent) 등에 개인정보(ID, PW 등)가 그대로 노출됨

## POST method의 처리 이후
* 적절한 웹페이지로 Redirect Code를 이용해 사이트 이동