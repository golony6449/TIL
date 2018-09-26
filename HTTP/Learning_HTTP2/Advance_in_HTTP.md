# Advance in HTTP
## HTTP 0.9
* `GET` method만 존재
* HTML만 로드 가능

## HTTP 1.0
* Header, Response Code, Redirect, Conditional Request, Encoding, Method 개념 도입
* RFC 1945

## HTTP 1.1
* Host Header의 필수화 ==> 가상호스팅(1개의 IP -> 다수의 웹 Property 제공)
* 세션 유지 ==> TCP 요청에 횟수 감소
* New Method(OPTIONS), Upgrade Header, Pipelining
* RFC 2068, 2616, 7230 ~ 7235

## SPDY

## HTTP 2
* HTTP 1.1의 체계를 유지하면서, 체감지연시간을 획기적으로 개선
* HOL 블로킹 해결