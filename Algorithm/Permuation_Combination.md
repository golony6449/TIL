# Permutation and Combination (순열과 조합)

## 순열

* 순서를 포함한 조합의 수

```python
items = [i for i in range(5)]
from itertools import permutations
list(permutations(items, 5))
```



## 조합

* 순서를 무시한 조합의 수

```python
items = [i for i in range(5)]
from itertools import combinations
list(permutations(items, 5))
```

