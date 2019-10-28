# 세미콜론 in Go

## 개요

* 코드 상에서 세미콜론이 없는 것처럼 보이지만 사실은 컴파일러가 자동으로 붙임



## 문제점

* 쉼표, 연산자, 여는괄호로 끝나는 경우 세미콜론이 붙지 않음
* 반대로 말하면 닫는 괄호, 줄바꿈 기호의 경우는 세미콜론이 붙음
* 모두 휴먼에러를 발생시킬 여지 있음



## Example

```go
package main

import "fmt"

// 정상
func main(){
    fmt.Println("Hello")
}
```

```go
package main

import "fmt"

// 오류: 닫는괄호로 인해 끝나는 라인으로 간주됨
func main()
{
    // ....
}
```



## Reference

* Effective Go: Semicolons (공식문서)