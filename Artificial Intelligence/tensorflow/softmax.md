## Softmax
=========================
## Softmax
### 역할
* NN의 마지막 층 (출력층) 으로 사용
* Hypothesis의 값(Score)을 입력으로 받아 Probabilities(확률, 가능성)을 출력하는 층 => 각 출력일 확률 계산

## softmax_cross_entropy_with_logits
### 개요
* 좀 더 간단한 softmax 함수 사용을 위한 TF 내장 함수

### 기존의 코드
```python
logits = tf.matmul(X, W) + b
hypothesis = tf.nn.softmax(logits)
cost = tf.reduce_mean(-tf.reduce_sum(Y * tf.log(hypothesis), axis=1))
```

### 새로운(Fancy)한 코드 - softmax_cross_entropy_with_logits
* logits: X * W + b

```python
logits = tf.matmul(X, W) + b
cost_i = tf.nn.softmax_cross_entropy_with_logits(logits=logits, labels=Y_one_hot)
cost = tf.reduce_mean(cost_i)
```

### one-hot 인코딩
* label을 1 or 0으로 표현
* N차원 입력시 => 출력: N+1 차원 ex) [[0], [3]] ==> [[[1, 0, 0, 0], [0, 0, 0, 1]]]
* reshape 반드시 수행 해야함 ex) `tf.reshape(Y_one_hot, [-1, nb_classes]) # -1: 전부를 의미`
`tf.one_hot(Y, nb_classes)`
* nb_classes: 분류할 class의 수를 의미