# Callback Function

## 개요
* 동작이 수행이 끝났을때 동작되는 함수
* 함수자체를 매개변수로서 전달하는 방식으로 구현

## Anonymous Fucntion
* 익명 함수
* 이름이 없는 함수를 의미

```javascript
/* 동일한 역할
fucntion a () {
    console.log('a');
}
*/

var a = function(){
    console.log('a');
}
```

* JS에서 함수는 값으로 볼수 있음 ==> 인자로서 전달할 수 있음
* 호출할때는 값 뒤에 소괄호 기입