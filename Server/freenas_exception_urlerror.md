# FreeNAS Trouble Shooting

## 개요

* 발생: 플러그인 설치 시도시, 50 ~ 75 퍼센트 지점에서 오류 발생
* 메시지: `exception urlerror occurred destroyed XXX`
* 결과: 플러그인 설치 실패



## 자료수집

1. https://forums.freenas.org/index.php?threads/11-2-plug-ins-problem.71773/
2. https://forums.freenas.org/index.php?threads/efault-exception-urlerror-occured-destroyed-plex.72981/



## 분석

### 1번 자료

* 네트워크 상의 오류일 가능성이 크다는 의견
* 설정 초기화, 여러번의 재부팅으로 해결



### 2번 자료

* 검색당시 가장 최근 포럼 자료
* 현재 서버와 동일버전, 동일한 문제 발생
* 답변대로 로그(`/var/log/message`) 확인 
* ==> 동일 로그 확인 (설치중 Link state 가 down으로 변경)
* 결론: 온보드 내장 랜카드의 문제