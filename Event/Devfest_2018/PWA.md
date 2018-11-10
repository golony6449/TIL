# Isomorphic PWA
* = SPA + PWA + Server rendering + code splitting

## Performance
* 5초 이내의 TTI(모든 레이아웃 안정, 모든 글꼴 표시)
* 2초 이내의 나머지 로드

## SPA
* 서버 부담 감소
* 앱과 유사한 UX
* 모듈화, 재사용 가능 코드
* 엄청 느린 초기구동속도

### JS
* 메인쓰레드에서 동작해야 하는것, 할 필요 없는 것을 구분 ==> 병렬화

## PRPL 패턴:
* 구글 웹팀에서 발표 = UX를 극대화 하는 예시
* Push, Render, Pre-cache, Lazy-load
* 요구사항 많음

## Dynamic Code splitting + Lazy loading
* webpack ==> 큰 크기의 JS, 폰트 파일 생성 ==> 
* React-Loadable

## Minfy + compress
* Minify: webpack Uglifier
* compress: nginx 설정 (gzip)

## 평가도구
* chrome aduit

## 사용자가 많이 사용하는 패턴을 파악, 이를 최적화 하는 것이 중요
* ex: 정보 Read 페이지 => 유저 인터렉션보다, 렌더링에 집중

## SSR -  Isomorphic (Universial) Web App
* 첫페이지: SSR ==> 빠름
* 이후 페이지: CSR ==> SPA의 사용자 경험
* Client <-> nginx  <-> ssr <-> 캐시
* 		<-> API server


## Next.js
* 이게 뭘까?
* 수정해야 하는 코드 양이 너무 많음


## 그 외
* 렌더링 순서는 굉장히 중요 (window 객체 등등)
* Life cycle cavet
* offline caching
* service worker (=workbox(모듈화된 서비스 워커))