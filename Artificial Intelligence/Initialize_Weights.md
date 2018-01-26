## Initialize Weights (가중치의 초기값)
====================================
### 힌튼 교수님(Hinton)이 말한 뉴럴넷의 제 2 겨울(Vanishing Gradient) 원인
1. 데이터셋 부족
2. 느린 연산속도
3. 적절치 못한(멍청했던) 가중치 초기값
4. 잘못된 타입의 비선형 함수(Sigmoid) 사용

### 적절한 설정법
1. 전부 0으로 하지 말것
2. Restriected Boltzmann machine (RBM) (복잡하다는 단점)
3. Xavier initialization (노드의 input, output 갯수에 맞춰서 초기값 설정) (2010)
4. He initialization (2015)

#### 이외에도 많은 연구가 진행중인 분야


### 전부 0으로 하면?
* Back-propargation에서 W가 0이 되면 Chain-rule에 의해 이후의 모든 미분값을 0이 됨
* Vanishing Gradient 발생

### Restriected Boltzmann machine (RBM) 
* 어러개의 Layer 중 2개 씩의 Layer의 Weight 조정
* 일종의 pre-training 과정 (이 단계에서는 label 불필요)

1. 임의의 Weight 지정
2. 입력 데이터(x)를 W를 이용해 Forward(Encode) 연산 수행
3. Forward 수행 결과를 <b> 동일한 W를 이용해 반대방향으로 동일한 연산(Backward)(Decode) 수행(x')</b>
4. x와 x'의 차이가 최소가 되도록 W값 조정
5. 이후 학습 수행(Fine Tunning)

### Xavier/He initialization
* 작지도 크지도 않은 '적절한' 값을 찾고싶음
* 노드의 입력(fan_in), 출력(fan_out)의 갯수로 초기값 지정
```python
# Xavier
W = np.random.randn(fan_in, fan_out) / np.sqrt(fan_in)
# He
W = np.random.randn(fan_in, fan_out) / np.sqrt(fan_in/2)
```