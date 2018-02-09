## Tensor Manipulation
======================

### Reduce mean
* `tf.reduce_mean()`
* 평균 계산
* 주의: Array 내부의 값의 자료형으로 연산 수행 => float를 사용해야 소수점까지 계산됨
* axis: 0 -> 세로방향, 1 -> 가로방향, -1 -> 가장 안쪽의(축 번호가 작은) arr
* (추가 정리 필요)

### Reduce sum
* `tf.reduce_sum()`
* 합 계산
* axis별 계산 가능
* reduce_mean, reduce_sum의 조합해서 사용하기도 함

### Argmax
* `tf.argmax()`
* 해당 축에서 가장 큰 값의 Index 도출
* axis별 계산 가능

### Reshape
* `tf.reshape()`
* Array의 shape 변경 (Rank 등)
* -1 -> 적절한 값을 자동으로 사용
* 값이 섞일까에 대한 우려 => 보통은 가장 안쪽 축의 size는 조작하지 않음 => 데이터 조합의 변형 없음

### Squeeze, Expand
* Reshape의 특수한 형태
* `tf.squeeze()`, `tf.expand_dims()`
* squeeze: Rank(차원) 감소
* expand: Rank(차원) 증가
```python
tf.squeeze([[0], [1], [2]]).eval()
# >>> array([0, 1, 2], dtype=int32)
```
```python
tf.expand_dims([0, 1, 2], 1).eval()
# >>> array([[0],
#            [1],
#            [2]], dtype=int32)
```

### One hot
* 수치가 아닌 Array에서 1의 값을 가지는 원소의 Index로 값을 표현
* 주의: Rank가 1 증가됨 => 필요시 reshape(or squeeze) 수행
```python
tf.one_hot(arr, depth=int)
```

### Casting
* int <-> float
* boolean(True, False) => 1 or 0
* `tf.cast(arr, dtype=datatype)`

### Stack
* Python List => tf Array(numpy)로 쌓아주는 역할
* 쌓아주는 역할 => Rank 증가
* axis 옵션을 이용해 여러가지 방법으로 쌓을 수 있음

### Ones
* `tf.ones_link(arr)`
* 매개변수로 들어온 arr과 Size가 동일한 1로 채워진 tf.Array() 생성

### Zeros line
* `tf.zeros_like(arr)`
* 매개변수로 들어온 arr과 Size가 동일한 0으로 채워진 tf.Array() 생성

### Zip
* python Keyword
* 여러개의 List를 묶어 한번에 처리할 수 있도록 해줌
```python
# example
for x, y in zip([1, 2, 3], [4, 5, 6]):
    print(x, y)
# >>> 1 4
# >>> 2 5
# >>> 3 6
`