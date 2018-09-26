# Performance Indicator (in HTTP)

## on Network
* 지연시간: Return Trip Time(왕복시간 = 지연시간 * 2)
* 대역폭
* DNS 조회
* 연결시간: Hand Shaking에 걸리는 시간
* TLS 협상시간

## on Server
* TTFB: Time To First Byte -> `브라우저가 요청을 전송 ~ 페이지 응답의 첫번째 바이트를 수신` 까지의 시간
* 콘텐츠 다운로드 시간: 요청한 개제에 대한 TTLB(Time To Last Byte)
* 렌더링 시작 시간: 클라이언트가 화면에 무언가를 표시하기 시작할때 까지의 시간
* 문서 완성 시간: 로딩완료 까지의 시간
