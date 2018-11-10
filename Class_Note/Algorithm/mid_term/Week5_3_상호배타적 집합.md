# Chap 7 상호 배타적 집합
* 집합생성, 집합판단, 합집합

## 상호 배타적 Set의 처리
* 교집합 X
* 연산: Make-Set(x), FInd-Set(x), Union(x, y)
* 자료형: Linked List, Tree

## Linked List를 이용한 처리
* 1개의 집합 = 1 Linked List
* 대표원소: 맨 앞의 원소
* Node: 대표원소링크(=부모링크 (HEAD)), 다음원소링크, tail(마지막 노드를 가리키는 포인터)

### 합집합
* 기존의 원소의 마지막원소 --> 대상 집합의 대표원소 를 가리키도록 함
* 대상 집합의 HEAD 포인터를 기존 집합의 HEAD를 가리키도록 함

#### Weight를 고려한 합집합(Union)
* 두 집합중 작은 집합을 큰 집합 뒤에 붙임
* HEAD 수정 횟수 감소 ==> 속도 향상

#### 수행시간 (정리 2)
* 조건: Weight를 고려한 합집합을 사용할때
* m번의 Make-Set, Union, Find-Set 중 n번이 Make-Set ==> 원소수 n개
* 총 수행시간: O(m + nlog(n))
* Make-Set, Find-Set: 상수(1)
* Union: n log(n) (데이터를 가공했을때, 그냥 합하면 n^2) (정렬과 유사)

## Tree를 이용한 집합표현
* 1개의 집합 = 1개의 트리
* child는 parent를 가리킴 (<b>HEAD 아님</b>)
* 대표원소: 루트

### 합집합
* 기존 트리의 루트를 대상 루트가 가리키도록 수정

### 알고리즘
* p[x]: 부모 노드

* Make-Set: 리스트 생성
* Union: p[FInd-Set(y)] <- Find-Set(x)
* Find-Set(x): 리프노드 부터 루트노드 까지 탐색

## 연산의 효율 향상
#### Rank를 이용한 Union
* Rank = 트리의 깊이
* 합집합 결과의 깊이가 얕도록 합집합
* 기준: 깊이가 깊은 트리
* 대상: 깊이가 얕은 트리
* 깊이가 같은 경우, 합집할 결과의 깊이는 1 증가

#### 알고리즘
* Make-Set(x): p[x] <- x, rank[x] <- 0
* Union(x, y): 깊이를 비교

#### 수행시간 (정리 5)
* Tree로 표현되는 배타 집합에서
* 조건: m번의 Make-Set, Union, FInd-Set 중 n번이 Make-Set
* 수행시간: O(mlog*(n))
* log*(n) = loglogloglong ...... log(n)  (1에 수렴)
* 즉, 사실상 Linear time (O(n))

* Tree 기반 배타적 집합에서는 Make, Union, FInd 모두 상수 (1)

#### Path Compression
* FInd-Set 과정에서 만나는 모든 노드들이 직접 Root를 가리키도록 포인터