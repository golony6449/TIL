## Unpacking
=======================

### 개요
* 컬랙션(List, Dict, Tuple ...)의 원소들을 변수에 대입하거나, 함수에 전달할 때 사용

### 문자열: split(), rsplit()
* 좌측부터 or 우측부터 분리
* 분리할 기준점, 분리 횟수 지정
* `"my_photo.orig.png".split(".", 1)` => "my_photo", "orig.png"
* `"my_photo.orig.png".rsplit(".", 1)` => "my_photo.orig", "png"

### = 를 이용한 Unpacking
* 교환: `a, b = b, a`
* 중첩 Unpacking: `a, (b, c) = 1, (2, 3)`

### 확장 Unpacking (Python 3 이상)
* `a, *rest = [1, 2, 3]` ==> a = 1, rest = [2, 3]