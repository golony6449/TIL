# SSH

## 개요

* Secure SHell
* 원격지에 접속해 이런저런 명령을 수행하기 위한 쉘
* <b>암호화</b>



## 설정 방법 (in Windows)

1. `PuTTYgen`에서 키 pair를 생성한다.
2. 공개키를 복사해 원격지 서버상의 `~/.ssh/authorized_keys`에 붙혀넣는다 (기본값, 수정가능)
3. 짠!



## Brute force 방어를 위한 추가 설정

1. `/etc/ssh/sshd_config` (라즈비안 기준)

* 포트 변경
* 비밀번호 로그인 불가능 설정 `PasswordAuthentication`

