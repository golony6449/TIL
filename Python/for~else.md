# for ~ else 문

## 개요

* 토이 프젝 진행중 처음보는 문법 발견
* 아무리 봐도 if와 같은 인텐트가 아니여서 설마하고 구글링
* `for ~ else 문` 이라는 것이 있었다.



## 의미

* `for`문이 `break`등의 사유로 중간에 중지되지 않고 끝까지 수행된 경우 수행되는 명령 기재
* `break`여부 확인에 유용



## 예제

```python
while True:
    for idx, row in enumerate(self.board[:-1]):
        if 0 not in row:
            self.board = remove_row(self.board, idx)
            cleared_rows += 1
            break
 	else:
 	     break
```

