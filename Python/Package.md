## Package
====================
### 개요
* 파이썬 모듈을 계층적 구조로 관리 할 수 있도록 도와줌
* 코드를 모듈별로 분리함으로서 협업, 유지보수에 유리함
* ex) `game.sound`: game 패키지의 sound 모듈

### 작성
1. 디렉토리를 이용해 계층적 구조 생성
2. 각 디렉토리에 `__init__.py` 파일 생성 (내용은 empty)
3. 하부 모듈 작성

* `interactive shell`에서 사용을 위해 `PYTHONPATH`에 디렉토리 추가

### 사용
* 함수를 모듈로 사용 가능
* ex) `import game.sound.echo` or `from game.sound import echo` or `from game.sound.echo import func`
* 에러: `import game`(함수 호출 불가능), `import game.sound.echo.func`(No such module)
* 결론: 마지막 항목은 반드시 모듈 or 패키지

* 모듈내에서는 상대 경로를 이용해 다른 모듈을 import 할 수 있음. ex) `from game.graphic.render import func` == `..graphic.render import func`
* 여러개의 깊은 계층으로 이루어진 경우 유용

### __init__.py
* 해당 디렉토리가 패키지 또는 패키지의 일부임을 알려주는 역할
* 3.3버전부터 없이도 패키지로 인식, but 하위 호환을 위해 생성해주는 것이 바람직

### __all__ = []
* `*`을 이용한 import 시에 import 할 모듈 정의 
* `__all__` 내부에 정의된 모듈만 import 됨 (단, 마지막이 패키지인 경우)
* `from`키워드의 마지막이 모듈인 경우 모듈 내부의 모든 함수, 클래스가 import 됨

### 참고자료
* https://wikidocs.net/1418