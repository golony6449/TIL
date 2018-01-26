## 학습률, 데이터 전처리, 오버피팅
===================================
### 학습률
* cost함수에 곱해지는 하이퍼파라메터
* 보통 0.0001 으로 시작
* Cost값의 추이를 보고, 사람이 직접 조정

#### 학습률이 적정치 보다 큰 경우
* Cost값이 발산 => Cost값이 숫자가 아닌 수치가 나타나게 됨 (범위 초과)
* 학습률을 감소시킨 뒤 다시 학습 시도

#### 학습률이 적정치 보다 작은 경우
* 학습시간이 길어짐
* local minimum에서의 학습 종료
* Cost 값이 무의미한 정도의 차이인 경우 학습률 증가 후 다시 학습

### 데이터 전처리
* 데이터 각각의 차이가 큼 => 왜곡된 형태의 그래프 => Cost 값이 발산할 위험 존재
* 학습률이 적절하다고 생각되는데도 Cost값이 발산, 학습이 되지 않을때 => 데이터 중 차이가 크게 나는 값이 존재하는지, 정규화 수행여부 확인

* 종류: Zero-centered data, Normalized data(특정 범위 안에 모든 값이 위치 하도록 함)

* Normalize(정규화) = (x-뮤)/분산 (통계학에서의 정규화와 동일)

### 오버피팅(Overfitting)
* 가장 큰 문제
* 모델이 학습데이터에 너무 최적화 => 훈련데이터, 실제데이터를 제대로 대응 할 수 없는 상태
* 층이 깊을 수록 발생하기 쉬워짐 (그래프 상에서 번곡점 수 증가)

#### Solution
* 가장 좋은 해결법: 훈련데이터의 증가!
* 중복된 Feature 제거(Deep Learning에서는 불필요), <b>Regularization</b>

#### Regularization - 일반화
* Weight 값을 너무 크게 하지 않도록 함
* Dicision Boundary가 구부러진 상황 => 특정 Weight가 큰 상황 => 오버피팅
* 구부러진 선을 펴는 것! => Weight에 큰 값이 없도록!

* `cost Funtion = 기존의 cost 함수 + sum(W^2) * 람다`
* 이때 W^2은 각각의 요소들의 제곱을 의미
* 람다: Regulation Strength => 일반화를 중요하게 여기는 정도 (1: 중요, 0: 무관심)

### Dropout
* Neural Net에서의 Regularization 방법
* `Dropout: A Simple Way to Prevent Neural Networks from Overfitting [Srivastava et al. 2014]`
* forward연산 -> 이후 Backprop 연산에서 랜덤하게 일부 뉴런을 0으로 설정 => 일부 뉴런을 kill 하는 역할
* 주의점: 학습시에만 비활성화 해야함 => 평가(Evaluation)시에는 dropout_rate: 1로 할 것