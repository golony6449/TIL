# PPO: Proximal Policy Optimization
* 키워드: 정책망, 강화학습
------------------------------------
## 개요
* 강화학습에서 정책망 설정을 통한 학습 최적화 알고리즘
* ex) 바둑: 수행할 수 있는 경우의 수에 따른 승리 확률 계산 후, 높은 확률을 선택 -> 반복
* 학습 수행시, 가장 승리 확률이 높았던 경우의 Learning_rate를 높게 함 => 시간연관성 있음

* 현재 강화학습 분야에서 baseline 알고리즘으로 적용중