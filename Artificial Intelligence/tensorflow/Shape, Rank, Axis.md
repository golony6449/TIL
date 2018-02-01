## Shape, Rank, Axis
===========================
### Shape
* 행과 열의 수
* 가장 안쪽의 값(바깐 축)의 값의 갯수 부터 Count하면 쉽게 계산 가능

```python
tf.shape(X)
>> array([4], dtype=int32) # 4개의 원소로 이루어진 1D Array
>> array([2, 2], dtype=int32) # 2개 원소를 가진 2개의 1D Array로 이루어진 Array (2차원 배열)
>> array([1, 2, 3, 4], dtype=int32) # 4D Array
```

### Rank
* 차원 수

### Axis
* 축
* 가장 바깥 축을 0부터 Count
* -1번 축: 가장 안쪽의 값들을 나타내는 축