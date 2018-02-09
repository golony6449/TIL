## Matmul VS Multifly
============================================
### Matmul
* 행렬곱
* 피연산자 2개의 Size가 일정 규칙을 충족해야 함
* 앞의 피연산자의 열의 수 == 뒤의 피연산자의 행의 수
* 결과: [앞의 피연산자의 행의 수, 뒤의 피연산자의 열의 수]
* tf(or np).matmul() 사용

### Multifly
* 원소간의 단순 곱
* 결과: 앞의 피 연산자의 크기(Sizw)
* *기호 사용

### ex
```python
matrix1 = tf.constant([[1., 2.], [3., 4.]])
matrix2 = tf.constant([[1.], [2.]]))
tf.matmul(matrix1, matrix2).eval()
# >>> array([[5. ],
#            [11.]])
matrix1 * matrix2
# >>> array(([[1., 2.]
#             [6., 8.]]))
```

### Broadcast 기능
* 유용하지만 실수(오류)가능성 높음
* 원소수(Shape, Rank)가 동일하지 않은 경우, 각각의 원소끼리 연산하는 방법
```python
matrix1 = tf.constant([[1., 2.]])
matrix2 = tf.constant(3.)
# >>> array([[4., 5.]])
```

```python
matrix1 = tf.constant([[1., 2.]])
matrix2 = tf.constant([3., 4.])
# >>> array([[4., 6.]])
```

```python
matrix1 = tf.constant([[1., 2.]])
matrix2 = tf.constant([[3.], [4.]])
# >>> array([[4., 5.],
#            [5., 6.]])
```