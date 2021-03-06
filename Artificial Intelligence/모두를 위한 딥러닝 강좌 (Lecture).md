# 모두를 위한 딥러닝 강좌 by Kim SungHun
* https://www.youtube.com/playlist?list=PLlMkM4tgfjnLSOjrEJN31gZATbcj_MpUm
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

## Linear Regression (선형 회귀)
### 모델
* <b>H(x) = Wx + b</b>

* 평면좌표계에서 적절한 직선(Linear)의 방정식 찾기! 
### 목표
* Cost 함수(손실함수)가 최소가 되는 W, b 찾기!

* 좋은 가설: H(x)에 x를 대입해서 나온 결과를 y(실제 값)와 비교했을때 차이가 적은 것

### Cost Function(= Loss function)
* 계산: (H(x) - y)**2 

#### 제곱을 하는 이유
1. 항상 양수의 값을 얻기 위해
2. 차이의 기하급수적인 증가를 표현 하기 위해

#### 입력값이 여러개일때?
* cost(W) = (1/m) * sum((Wxi - yi)**2)

### 우리의 목표 - Cost function 값을 줄이자!
* cost함수를 W,b에 대해 미분하면 해당 W, b를 변화 시켰을때 cost함수의 변화량을 추측할 수 있음

* 단, convex function일 경우에 한해.
* 이외의 함수는 cost 함수 값을 줄이는 것은 가능하나, GD를 통해 얻은 최솟값이 진정한 최솟값이라는 보장은 없음

### Multi Variable
* 입력 데이터가 여러개일때의 경우
* Matrix를 이용해  여러개의 input의 case들을 묶어서 한번에 일관 처리

#### h(x)
* h(x1,x2,x3) = w1x1 + w2x2 + w3x3 + b

#### cost function
* 어찌됬든 cost function은 (예측값 - 정답) 간의 차이를 계산
* cost(W, b) = (1/m) * sum(H(x1, x2, x3) - y)

####  WX vs XW
* Theory: H(x) = Wx + b

* Tensorflow: H(X) = XW <-Matrix 곱 만을 이용해서 바로 처리 가능

* 수학적 의미는 동일

### Logistic Classification
* Regession과의 차이점: Classification은 여러개 중 1개로 분류 (특히 Binary Classification은 2개 중 1개로 분류)

* One-hot encoding 된 상황에서 Linear Regression의 문제점을 해결하기 위해 사용 -> 결과값(Y)이 0 ~ 1이 아닌 다른 값이 나오는 경우 발생.

#### Logistic Classification의 Hypothesis
* sigmoid (=logistic function) = 1/(1 + exp(-x))

#### Cost function for logistic classification
* cost(W) = (1/m) * sum(c(H(x), y))

* if y=1 -> c(H(x), y) = -log(H(x))
* if y=0 -> c(H(x), y) = -log(1 - H(x))

* case 1. y=1: H(x)가 작으면 작을 수록 cost 값 증가
* case 2. y=0: H(x)가 크면 클수록 cost 값 증가

* 2개의 식을 합치면? -> C(H(x), y) = -ylog(H(x)) - (1-y)log(1-H(x))

#### Minimize cost with Gradient Decent Algorithm for logistic classification
* 미분을 이용해 경사하강법 적용

### Lec 11
#### Conv 연산에서 Output size 계산방법
* ((N - F) / Stride) + 1
* 입력 size: N, 필터 size: F 
* 점점 size가 작아짐 -> 정보손실 문제 ==> padding으로 해결(보완) 및 모서리 임을 알릴 수 있음

#### 연산
* 필터 마다 Conv 연산 수행 => Activation map 생성 ==> 필터 수 만큼의 채널이 생성됨
* 대개 마지막 Layer에서 Pooling 수행 (그 외에는 NN 만들기 나름)
* 이후 Pooling의 결과값을 FCN(일반적인 NN)의 입력으로 전달 ==> 최종 결과 도출

### Pooling Layer (Sampling)
1. Conv 층의 결과에서 각각의 Layer를 추출 => 작은 크기로 Resize(=Sampling)
2. (Max pooling의 경우) 1의 결과를 일정 크기의 필터로 마스킹 => 큰 값을 추출해 출력값으로 사용 

### Lec-11-2 복습!!

### Case
#### LeNet-5
#### AlexNet
#### GoogLeNet
* Inception module
#### ResNet
* 깊은층 but 값을 건너 뜀으로서 적은 층 처럼 학습되는 특징

### Demo
* https://cs.stanford.edu/people/karpathy/convnetjs/demo/cifar10.html

### Lec 12
## RNN - Recurrent Neural Network
* Neural Network의 꽃!
* Sequence data 처리를 위해, 각 뉴런의 결과(state)를 다음 뉴런에 전달
* 이전의 연산이 다음 연산에 영향을 줌

### 활용처
* <b> Sequence Data </b> (time series)
* Language Model -> 연관어 (다음에 올 글자(Charactor) 예측)
* Speech Recognition
* Machine Translation
* Conversasion Modeling / Question Answering
* Image/Video Captioning
* Image/Music/Dance Generation

### RNN의 flexibility
1. 1 -> 1 : ex: Vanila
2. 1 -> N : ex: Image captioning
3. N -> 1 : ex: Sentiment Classification
4. N -> N : ex: Machine Translation
5. N -> N : ex: Video captioning (on frame level)

### 수식
* ht = fw(ht-1, xt)
* ht: New state, fw: some function with parameters W, ht-1: Old state(이전 값), xt: input vector at some time step
* 이때, RNN 전체에서 같은 fw()를 사용(<b>즉, 동일한 weighs(가중치) 사용</b>) -> 그림으로 표시할때 재귀적으로 표시

* 첫 뉴런은 ht-1이 존재하지 않음 -> 0 벡터 사용

### 기본적인 RNN - Vanilla Recurrent Neural Network
* `ht = fw(ht-1, xt)` -> `ht = tanh(Whh*ht-1 + Wxh*xt)`
* `yt = Why*ht`

* yt의 size는 Why의 size에 따라 결정됨!

### Character -> vector 변환
* 많은 방법이 있음

#### One-Hot encoding (ex: 'hello')
* 가장 간단한 인코딩 방법
* Voca = [h,e,l,o]

* 변환
| h | e | l | o |
|---|---|---|---|
| 1 | 0 | 0 | 0 |
| 0 | 1 | 0 | 0 |
| 0 | 0 | 1 | 0 |
| 0 | 0 | 0 | 1 |

### Multi-Layer RNN

### RNN의 학습모델
* 계속 발전되는 중
* 연산 문제때문에 RNN 자체 대신 아래의 2개의 모델을 사용
* LSTM (Long Short Term Memory)
* GRU

### Sequence data
* NLP(Natural Language Processing), SR(Speech Recognition)에서 자연어, 음성
* 각각의 데이터(문자 등)뿐만 아닌, 이전 데이터(나아가 데이터 전체)를 같이 이해해야 의미파악 가능