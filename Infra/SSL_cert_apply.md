# SSL 인증서 적용 on NGINX

## 개요

* 도메인을 질렀다
* 근데 이 도메인은 HTTPS가 아니면 브라우저에서 로드를 거부
* 무난한 `Let's Encrypt` or  [porkbun](porkbun.com) 제공 인증서 중 후자 선택 (둘 다 `Let's Encrypt` 기반)



## 파일 구성

* porkbun 인증서는 4개의 파일로 구성
* `domain.cert.pem`: 도메인 인증서
* `intermediate.cert.pem`: 중계 CA 인증서
* `private.cert.pem`: 서버측 비공개키
* `public.cert.pem`: CA 인증서



## 절차

1. `/etc/nginx/` 내부에 인증서 저장 폴더 생성
2. `domain` -> `intermediate` -> `public` 순으로 통합
3. 통합한 키, 비밀키를 경로로 복사
4. NGINX 설정상에 `ssl_certificate`에 통합키, `ssl_certificate_key`에 비밀키 절대경로 입력
5. SSL 활성화
6. NGINX 재시작
7. 인증서 저장폴더 권한 700로 변경



## 참고자료

* <http://dveamer.github.io/backend/SSLOnNginx.html>