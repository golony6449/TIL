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