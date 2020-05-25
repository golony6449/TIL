# 자료형에 따른 시간복잡도

## 시간복잡도

* big-O 표기법
* `O(logn)`: 정렬된 상태에서 탐색
* 데이터가 늘어났을때 시간증가의 영향



## 튜플

* 둘 중 하나가 빈 경우 비지 않은 튜플을 반환
* 튜플의 덧셈(연결): `O(N+M)` N: 앞 튜플, M: 뒷 튜플



## 리스트

* 리스트는 하나가 빈 리스트라고 해도 새로운 리스트 반환
* mutable한 사용법은 `.extend()`가 적합
* pop: `Pop`한 요소의 뒷요소를 모두 이동 ==> 연산량 많음



### append

1. 빈 경우: 새 배열 생성
2. 이후는 새 메모리를 복사해서 할당 ==> 합리적인가 (실제로는 메모리 할당은 한번에 대략 10정도) (약간의 공간 낭비)
3. 크기가 작은 경우는 10배 이하의 시간차 ==> 큰 경우는 1000배 이상
4. 결론: 평균은 O(1) 가끔 O(N)
5. 리사이즈 방지시 속도 개선 가능 ==> 한번에 None으로 왕창할당에 인덱스를 이용해 직접 할당



## Dict

* Hash Table: 위치를 찾는 작업이 상수시간에 끝남
* 충돌을 고려해 2/3 수준에서 2배 크기로 리사이즈 수행
* resize: 새로운 메모리 할당 및 복사, Hash value 



## 마무리

* 내부 구조를 파악함으로서, 시간복잡도 추측 가능
* 성능을 고려할때와 하지 않을때를 구분 하는 것이 바람직해 보임