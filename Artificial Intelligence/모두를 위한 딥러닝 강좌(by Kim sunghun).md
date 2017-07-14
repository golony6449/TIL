# 모두를 위한 딥러닝 강좌 by Kim SungHun
----------------------

## ML - Machine Learning
* 프로그램(컴퓨터)이 데이터를 보고 학습해서 무언가를 학습

### 종류
| Supervised | Unsupervised |
|------------|--------------|
| 라벨(Label)이 있는 데이터 | 라벨이 없는 데이터 |
| = Training Set |   |
| ex) 고양이 사진 모음 |   |


### 머신러닝 모델
1. Train data set을 학습
2. 모델 생성
3. 데이터 입력
4. 결과값 출력

### Type of Supervised learning
1. regression(회귀) : ex) 점수예측
2. binary classification(2진 분류) : ex) Pass, Unpass
3. multiLabel classification(다중 분류) : ex) A,B,C,D,E,F

## Tensorflow
* data flow graph를 이용해 수치계산을 하는 라이브러리

data flow graph - node, edge로 구성
* node: 작업(함수)을 의미
* edge: 데이터(tensor(벡터, 행렬))를 의미

### Tensorflow의 메커니즘
1. 그래프(노드, 간선) 생성
2. 세션을 이용해 그래프 실행
3. 출력

### node를 변수로 생성하기 (= 실행시점에 값 지정)
* placeholder 함수를 이용해 노드 생성

#### 사용법
* 정의
tf.placeholder(자료형)

* 실행시
session객체.run(노드명, feed_dict={노드명:값})

### Tensor
배열(array)을 의미

#### 구성요소
1. Ranks : 차원 수

| Ranks | 수학적 의미 |
|-------|------------|
| 0 | Scalar |
| 1 | Vector |
| 2 | Matrix |
| 3 | 3-Tensor |
| n | n-Tensor |

2. Shapes : 각각의 차원의 원소 수
3. Types : 자료형

| 자료형 | 지정 방법 |
|-------|-----------|
| float | tf.float32 |
| int32 | tf.int32 |
| double | tf.float64 |
| int8 | tf.int8 |
| int16 | tf.int16 |
| int64 | tf.int64 |


## Linear Regression (선형 회귀)

### 모델
* <b>H(x) = Wx + b</b>

### 목표
* Cost 함수(손실함수)가 최소가 되는 W, b 찾기!

좋은 가설: H(x)에 x를 대입해서 나온 결과를 y(실제 값)와 비교했을때 차이가 적은 것

### Cost Function(= Loss function)
계산: (H(x) - y)**2

#### 제곱을 하는 이유
1. 항상 양수의 값을 얻기 위해
2. 차이의 기하급수적인 증가를 표현 하기 위해

* session.run(node명) 실행시

해당 노드 부터 그래프 처음으로 역추적 -> 그래프 처음부터 해당 노드까지 수행

### 1 변수 선형 회귀 구현
* 모델
1. 데이터셋 생성
2. 기울기를 tf.Variable()로 생성
3. h(x) 정의
4. cost함수 정의
5. optimizer 생성
6. session 생성
7. 변수 초기화 (session.run(tf.global_variables_initializer()))
8. session 실행


* 한번에 여러 세션 실행

sess.run(cost);sess.run(W);sess.run(b);sess.run(train) -> sess.run([cost,W,b,train])

* cost 함수 값 최소화 - Gradient Descent Algorithm
1. 랜덤한 값에서 시작
2. W를 약간 변경(learning_rate로 조절)
3. W가 바뀔때 마다, 기울기가 줄어들 확률이 가장 높은 방향 다시 계산 -> 약간 이동
4. 2,3 반복

* 수식: W-(학습 데이터에서의 기울기 * 학습률)

-인 이유? -> 기울기 +: W 감소해야함, 기울기-: W 증가해야함

* <b>Convex function</b> - 2차 함수 그래프 형태의 함수

어느 지점에서 학습을 시작해도 수식 반복시 최소점을 찾을수 있음을 보장할 수 있음

-> 선형회귀를 적용한 Cost function 설계할때, 함수 모양이 Convex function인지 확인해야 할 필요 있음


* 기울기는 미분을 이용해서 구함

미분방법
1. 프로그래머가 직접 미분해 미분방정식 계산 후 노드로 구현
2. optimizer 사용

```python
optimizer=tf.train.GradientDescentOptimizer(learning_rate=0.01) #optimizer 생성
train=optimizer.minimize(cost) #최소화 수행
```

* 프로그래머가 직접 기울기 조작하는 방법?

```python
gradvar=optimizer.compute_gradient(cost) #기울기 계산 후 반환
# gradvar을 직접 조작
optimizer.apply_gradient(gradvar) # 기울기 적용
```


## 여러가지 Tensorflow 객체
* 변수 생성
```python
W=tf.Variable(값, name='이름') #텐서플로우가 변경하는 변수(학습중 변경)
```

* 랜덤한 값을 가지는 배열 생성
```python
tf.random_normal([n]) # Ranks(차원)가 n이고 랜덤한 값을 가지는 배열 반환
```

* 평균계산
```python
tf.reduce_mean() #평균 계산
```

* 제곱
```python
tf.square(x) #x를 제곱하는 tensor,sparetensor 반환
```

* tensorflow 변수에 값 대입
```python
TFvariable.assign(k) #변수에 k 대입
```