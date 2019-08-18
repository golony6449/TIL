# Async I/O

## sync, async, blocking, non-blocking

* 실행흐름을 멈추지 않고 진행할수 있는가? 에 따른 구분
* `Future`, `Promise`, `Coroutine`
* sync, blocking은 구분되어야 함
* blocking: IO 작업과 연관



## aync vs non-blocking

* Blocking IO 사용해도, 주 실행흐름에 대한 방해 없으면 비동기 프로그래밍
* (==별도의 채널로 작업 처리)



## 비동기 프레임워크

* Quart(프로덕션 수준 사용 불가), Growler(얘도), FastAPI
* Vibora: Flask와 유사, 빠른 웹서버, 멀티코어 지원, uvloop
* AIOHTTP: asyncio 기반 비동기 HTTP 클라/서버
* sanic
* tornado: py2에서 많이 쓰임, 웹 - 비동기 네트워크 프레임워크



## 비동기 라이브러리

* ayncio: async / await 구문으로 동시성 코드 작성 라이브러리
* 코루틴 제어, 자식 제어, 동시성 코드 동기화 (고수준)
* 저수준도 제공



## uvloop

* asyncio의 이벤트 루프를 대체
* Cython으로 개발
* `asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())`
* libuv 기반



## libuv

* 크로스 플랫폼. Node.js 위해 작성됨
* 이벤트 드리븐 비동기 IO
* kqueue(BSD), epoll(LINUX), IOCP(Win) 추상화



## IO Loop

* libuv의 경우 언급되어있지 않으면 안전하지 않은 쓰레드
* 루프 활성 상태 여부에 따라 반복 여부 결정



## sync vs async

* 이벤트 루프 대체시에 큰 성능차



## asyncio vs uvloop

* asyncio: 비동기코드가 python으로 작성
* uvloop: cython, C로 구현됨



## Django

* 2019년 12월 `v.3.0` 에서 완전한 비동기 방식 지원 예정
* 단, 동기방식 코드를 그대로 사용하면 `SynchronousOnlyOperation` 에러 발생
* ==> 거대한 마이그레이션 필요로 예상

