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