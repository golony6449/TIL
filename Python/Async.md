# 비동기 프로그래밍

## 개요

* Python에서 제공하는 비동기 프로그래밍에 대한 정리
* 키워드: `async`, `await`, `async with`, `async for`
* 네이티브 코루틴: `async def`로 생성된 함수



## 구성

1. 네이티브 코루틴 작성(`async def`)
2. loop 생성 (`asyncio.get_event_loop`)
3. 실행 (`loop.run_until_complete`)
4. loop 종료 (`loop.close()`)



* 이때, 코루틴에서의 반환값은 실행 단계에서 받을 수 있음
* `value = loop.run_until_complete(코루틴)`



## await

* 코루틴을 실행하는 방법 중 하나
* 코루틴, 퓨처, 테스트 객체를 실행하고 종료될때 까지 대기
* 주의: 네이티브 코루틴 내에서만 사용 가능

## 참고자료

* [Wikidocs 자료](https://wikidocs.net/21046)
* [파이썬의 await vs return vs return await](https://winterj.me/python-await-vs-return/)
* [코딩도장 자료](https://dojang.io/mod/page/view.php?id=2469)