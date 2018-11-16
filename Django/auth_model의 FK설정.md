# User 모델을 외래키로 사용

## 개요
* 장바구니, 전적 등의 테이블에서 유저정보을 참조할 필요가 있을때 User 테이블을 참조

## 코드
### 방법 1
```python
from django.db import models
from django.conf import settings

models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
```
* 장점: 커스텀 User 모델 사용시에도, settings 파일에 설정함으로서 하드코딩을 피할 수 있음

### 방법 2
```python
from django.contrib.auth.models import User

models.ForeignKey(User, on_delete=models.CASCADE)
```

## 유의점
### 기존테이블 수정
* 기존테이블 수정시, 저장된 레코드가 존재하는 테이블의 경우 `migrate` 시점에 에러 (truncate 관련) 발생
* (보통은 디폴트로 값을 사용할지 물어봄)
* Solution: 테이블 내의 레코드를 모두 삭제 이후 `migrate` 수행