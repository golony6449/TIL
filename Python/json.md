# JSON

## 개요

* Python의 내장모듈 `json`을 사용하면서 발생한 이슈 정리



## dump 그리고 한글

* 저장한 파일의 한글이 유니코드 형태(`u3141`)로 저장됨
* `file.write(json.dumps())`도 동일 증상
* `json.dump()` 또는 `json.dumps()`의 매개변수로 `ensure_ascii=False`를 전달
* 참고자료: https://datamod.tistory.com/104

