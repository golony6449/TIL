# sys Module
=====================

### sys.path
* 경로와 관련된 모듈

#### 예시
* `__file__`: 각각의 py 파일의 경로 (절대경로 아님, /(프로젝트상위), \(프로젝트 내부) 혼용된 경로)

* `sys.path.abspath(프로젝트 내 파일)` : 해당 파일의 절대경로 반환

* `sys.path.dirname(경로)`: 해당 경로의 상위디렉토리 경로 반환