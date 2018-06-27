## Closure (클로저)
==================================

### Preface
* 함수 내부에 함수를 정의 할 수 있음 (지원되는 언어에 한해서)
* 이때, 내부에 정의된 함수를 `내부함수`, 내부함수를 가지고 있는 함수를 `외부함수` 라고 함
* 내부함수는 외부함수의 지역변수에 접근 할 수 있음

### 정의
* 외부함수의 실행이 끝나서 외부함수가 <b>소멸</b>한 경우에도 내부함수가 외부함수의 변수에 접근할 수 있도록 하는 매커니즘

### Example
* 외부함수가 내부함수를 반환했을 때, 반환된 내부함수가 외부함수 밖에서 사용된 경우
```javascript
function outter(){
    var title = 'coding everybody';  
    return function(){        
        alert(title);
    }
}
inner = outter();
inner();
```

### reference
* 생활코딩 (https://opentutorials.org/course/743/6544)