# golbal keyword in python
## 개요
* Python에서 사용되는 키워드중 하나
* 파이썬은 기본적으로는 <b>함수 밖의 변수를 호출</b> 할 수 없음
* 해당 변수가 전역변수임을 지정하는 키워드
* 변수 사용 전에 사용

## 전역변수의 사용
```python
value = 10

def func():
	print(value) # 전역변수 사용
```


## 문제 발생
```python
value = 0 # 전역변수

def func():
	value = value + 10
	print(value)
```

* ERROR: value가 할당 전에 참조됨


## Solution
```python
value = 0 # 전역변수

def func():
	global value	# 사용전에 전역변수임을 지정
	value = value + 10
	print(value)

```