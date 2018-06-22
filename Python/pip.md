## pip
=================
### 개요
* Python의 패키지 매니저
* PYPI를 패키지 저장소로 사용

### pip freeze
* Output installed packages in requirements format (in help)
* 설치된 패키지들의 목록을 `requirements` 형식에 맞게 출력
* 배포할 때 여러 패키지들의 의존성을 기록, 다른 사용자가 큰 어려움 없이 환경을 설정할 수 있도록 도움
* `pip freeze > requirements.txt` : 패키지 목록을 파일로 출력
* `pip install -r requirements.txt` : 파일에 기록된 패키지들을 설치 (주의: 충돌시, requirements에 있는 버전이 우선시 됨)