# Chapter 12 상태공간 트리의 탐색

## 용어
* 백트래킹: 탐색 실패시, 이전단계로 이동
* 한정분기: 진행했을때 절대 좋은 해가 나올 수 없는 경우 진행하지 않음 ==> 불필요한 연산, 후보에서 제외

## State-Space-Tree
* 문제 해결 과정의 중간 상태를 각각 한 노드로 나타낸 트리
* 탐색기법: Backtracking, Branch-and-bound(한정분기), A*

## TSP의 예
* 상태 공간 트리: Week 11-3 슬라이드 6 참고

## Backtracking
* DFS와 유사한 스타일의 탐색의 총칭
* 가능한 지점까지 탐색, 막히면 되돌아감(Backtracking)
* Maze(미로), 8-Queens Problem, Map coloring(색칠 문제)

## Maze
* 벽에 도달해야만 막혀있는지 판단 가능한 미로

### 구현
* visited, prev 2개의 배열로 운용

``` 
# maze 함수
1. visited[v] = YES
2. if v == T THEN 성공
3. for each x in v에 인접한 정접
4. if visited[x] == NO THEN prev[x] = v, maze(x)
```

## 색칠문제 (Coloring Problem)
* 인접한 영역들의 Vertex를 그렸을때 인접한 Vertex는 같은 색을 칠할 수 없음
* k개의 색상을 사용해서 전체 그래프를 칠할 수 있는가?

### Map Coloring
1. 지도에서 구역간 인접관계 파악
2. 연결관계를 정점, 간선으로 표현
3. 보기 쉽게 그래프 화

### 알고리즘 - kColoring
```
# i: 정점, c: 색상
# 정점 i-1 까지는 제대로 칠이 된 상태에서 
# 정점 i를 c로 칠하려면 k개(고정)의 색으로 충분한가?
kColoring(i, c)
if (valid(i, c)) then {
    color[i] <- c;
    if (i = n) then {return TRUE;}
    else {
        result <- FALSE;
        d <- 1;
        while(result = FALSE and d<= k){
            result <- kCOloring(i+1, d);
            d++;
        }
    }
    return result;
} else {return FALSE;}
```

```
# i: 정점, c: Color
# 질문: 정점 i-1까지는 제대로 칠이 된 상태에서 정점 i를 색 c로 칠하면 색이 곂치지 않는가?
valid(i, c)
{
    for j<-1 to i-1{
        # 정점 i와 j 사이에 간선이 있고 and 두 정점이 같은색이면 
        # 안됨(return FALSE)
        if ((i, j) in E and color[j] = c) THEN return FALSE;
    }
    return TRUE;
}
```

* 직접 돌려보기!
* 작업 완료 후, (6, 3) -> (5, 1) -> (4, 2) -> (3, 2) -> (2, 2) -> (1, 1) 순으로 호출종료
* 슬라이드 7 보고 실습해보기! (Week 12.1)

## 한정 분기(Branch-and-Bound)
* 분기 + 한정
* 분기를 한정시켜 시간절약
* Backtracking과 공통점: 경우들을 차례로 나열
* Backtracking과 차이점: 최적해를 찾을 가능성이 없으면 분기하지 않음 
* (Backtracking은 진행불가능 전까지 진행)

### TSP와 BnB
* `(   )`: 최소한의 비용 추정치, 현재까지의 가중치 + 나머지 노드에서 나가는  최소한의 가중치 값의 합
* Week 12.2 슬라이드 4 해보기!


## A* 알고리즘
* Best First Search의 목적점에 이르는 잔여 추정거리를 고려하는 알고리즘
* 정점 x로 부터 목적점에 이르는 잔여거리 추정치(h(x))는 실제치 보다 크면 안됨
* 단점: 미래의 h(x)를 정해야 함 (있다고 간주하고 알고리즘 수행)

### Best First Search (최적의 길 선택)
* 최적의 길 선택 알고리즘
* 각 정점이 매력함수(g(x)) 값을 가지고 있음 ==> 가장 매력적인 점 부터 방문 (다익스트라와의 차이점)

### 다익스트라의 차이점
* 다익스트라: 하나의 시작점으로 부터 모든 정점에 이르는 최단경로 계산
* A* 알고리즘: 목적점이 <b>하나!</b>
* 다익스트라 알고리즘은 h(x)=0인 특수한 경우의 A* 알고리즘으로 볼수도 있음

### 알고리즘
* s: 시작점
* t: 목적지
* G: 주어진 그래프
* h: 추정거리 (h(x) 값)
* g: 각 노드의 값(가중치)
* w[u, v]: u에서 v로 가는 가중치

```
A*(G, s, t){
    Q <- V;
    foreach u in Q{
        g[u] <- f[u] <- inf.
        h[u] <- u에서 t까지의 추정거리
    }
    
    g[s] <- 0;
    f[s] <- h[s]
    while(Q is not Empty){
        u <- deleteMin(Q, f)
        if (u = t) return;
        else for each v in u와 인접한 정점 리스트
        	if (v in Q and g[u] + w(u, v) < g[v]){
                g[v] <- g[u] + w[u, v]	// 가중치 갱싱
                prev[v] <- u			// 백트래킹을 위한 정보
                f[v] <- g[v] + h[v]		// 지금까지 온 거리 + 추정거리
        	}
    }
}
```

* 슬라이드 8, 9 해보기!!

### A * 알고리즘이 첫 리프노드 방문시 종료되는 이유
* 한정분기와 유사