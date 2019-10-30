# Heap

## 개요

* 완전 이진 트리
* 우선순위 큐를 구현하는 방법 중 하나 (Array, Linked List로도 구현가능)
* 부모 노드는 자식노드 보다 작거나(최소 힙) 큼(최대 힙)
  * **루트 노드가** 삽입된 값 중 **최소(최소 힙) 또는 최대(최대 힙)**인 트리
* 힙에 사용되는 큐는 보통 리스트로 구현
* 종류: 최대 힙, 최소 힙



## Method

### 삽입

1. 리스트의 마지막에 삽입 될 원소 추가
2. 해당 원소와 부모가 힙 구성요건을 만족하는지 확인
   1. 만족한다면 삽입 끝
   2. 만족하지 않는 경우 위치 교환
3. 반복



### 삭제

1. 루트 노드 값을 백업하고 노드 삭제
2. 마지막 자식 노드를 루트로 이동
3. 힙 구성요건을 충족하도록 재구성
   1. 두 자식중 더 큰 값과 교환 (최대힙의 경우)
   2. 교환 후 해당 자식 방향으로 순회하면서 조건 충족 여부 확인



## C++ with STL

* STL 내의 `queue` 헤더에 포함된 `priority_queue`를 불러와 사용할 수 있음

```c++
#include <queue>
using namespace std;

priority_queue<int> max_heap1;
priority_queue<int, vector<int>, less<int>> max_heap2;
priority_queue<int, vector<int>, greater<int>> min_heap;

max_heap.push(1);	// 삽입
max_heap.top();		// 루트 값 반환 (삭제는 하지 않음)
max_heap.size();	// 원소 수 확인
max_heap.empty();	// Empty 여부 확인 (비어 있는경우 false 반환)
max_heap.pop();		// 루트 값 반환 후 내부에서 삭제
```





## Python

* 내장 모듈 중 `heapq`를 불러와서 사용할 수 있음
* 주의 1) 최소힙만 구현되어 있음
* 주의 2) 리스트를 힙처럼 다룰수 있게 해주는 모듈: 자료구조 자체는 아님
  * ==> 관련 메서드에 매개변수로 리스트를 전달해서 사용해야 함

```python
import heapq

heap = []
temp_list = [1, 3, 56, 2, 3, 45, 123]

heapq.heapify(heap, temp_list)	# 리스트를 힙으로 변환
heapq.heappush(heap, 4) 	# 삽입
heap.heappop(heap)			# 삭제
heap[0]						# 원소 중 최솟값
```



### Max Heap in Python

* `heappush`를 호출할때, 매개변수로 튜플을 전달하면, 튜플의 0번 인덱스를 기준으로 최소힙이 구성되는 것을 응용
* 매개변수로 `(-value, value)`를 전달
* 값이 큰 만큼, 사용되는 값(우선순위)가 낮아지므로 가장 큰 값이 루트(0번 원소)에 위치하게 됨
* 짠, 최대 힙 완성
* Example: `heapq.heappush(heap, (-value, value))`



## Reference

* [Datastructure: Heap](https://gmlwjd9405.github.io/2018/05/10/data-structure-heap.html)
* [python-heapq](https://www.daleseo.com/python-heapq/)
* [C++ STL: Priority Queue](https://dyngina.tistory.com/24)