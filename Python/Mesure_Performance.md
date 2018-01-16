## 성능측정
* http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_core/py_optimization/py_optimization.html
===================
### timeit 모듈
* 작은 코드블럭에서의 실행시간 측정 모듈
* https://docs.python.org/3.6/library/timeit.html
* 추후 작성

### IPython에서?
* %timeit 키워드 사용
* ex) `%timeit y=x**2`

### 성능최적화 테크닉
* 간단한 방식으로 알고리즘 구현 -> 프로파일(profile) -> 병목구간 탐색 및 최적화
1. 가능한 반복문(loop) 배제 (특히 이중/삼중(double/triple))
2. 가능한 큰 규모로 알고리즘을 벡터화
3. 캐시(cache)의 일관성을 활용
4. 가능하면 Array 복사하지 않고, 열람(view) 할것
* 이러한 방법을 사용해도 느린경우(혹은, 큰 반복이 불가피한 경우)에는 `Cython`과 같은 추가적인 라이브러리 추가 

### 번외
* `y = x**2` 보다 `y = x * x`가 더 빠름 (두둥)
* 단순 값 계산(스칼라 값)의 경우 Numpy보다 openCV연산(python)연산이 더 빠름 
* ex) `%timeit z = cv2.countNonZero(img)` vs `%timeit z = np.count_nonzero(img)`
* 단, 피연산자(operand)의 크기(size)가 크면 클수록 Numpy가 강점을 가짐
* 일반적으로는 Numpy보다 openCV의 함수가 더 빠름 (특히, 값을 복사할때 보다 열람할때)