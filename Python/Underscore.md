# Underscore (_) in Python
* 참고자료: https://mingrammer.com/underscore-in-python
------------------------------
## 타 언어에서의 용도
* 스네이크(Snake) 표기법의 변수, 함수명에 사용

## Python에서의 사용법
### 1. 인터프리터에서의 사용
* 마지막 실행 결과값 저장
```python
>>> 10
10
>>> _ #1개의 언더바(Underbar)
10
```

### 2. (튜플등의 언패킹(Unpacking)시의) 값을 무시
* 특정 값을 무시하기 위한 용도로 사용
* 필요하지 않을 값을 _에 할당하는 방법으로 사용
```python
x, _, y = (1,2,3) # x = 1, y = 3

x, *-, y = (1,2,3,4,5) # x = 1, y = 5

for _ in range(10): # Index 무시
    do_something()
```

### 3. 특별한 의미의 네이밍
* 언더스코어가 사용되는 가장 많은 방법

#### 1. `_single_leading_underscore`
* 주로 한 모듈 내부에서만 사용되는 private요소를 선언할때 사용되는 Convention(관례)
* `from (module_name) import *`로 임포트 하는 경우 _로 시작하는 것들은 임포트에서 제외
* 단, python은 진정한 의미의 private는 지원하지 않음 -> 직접 가져와 사용 or 호출하는 경우는 사용 가능 (Weak Internal Use Indicator)

```python
class _Base: # private 클래스
    _hidden = 2 # private 변수

    def _hiddenFunc(self): # private Method
        pass
```

#### 2. `single_trailing_underscore_`
* 파이썬 키워드와 출동을 피하기 위해 사용되는 Convention
```python
Tkinter.Toplevel(master, class_='ClassName')
list_ = List.objects.get(1)
```

#### 3. `__double_leading_underscores`
* Convention보다는 문법적 요소
* 클래스 속성명을 맹글링하여 상속과 같은 상황에서, 클래스 속성명의 충돌 방지목적으로 사용
* 맹글링?: Compiler, Intereter에서 변수명(or 함수명)을 그대로 사용하지 않고, 일정한 규칙에 의해 변형시키는 것을 의미함
* 규칙: `ClassName 클래스의 __method라는 메소드` -> `_ClassName(클래스명)__method()`
* 상속시에 함수명이 같아도 Override 되지않음
* 맹글링되기 때문에, 일반적인 접근(`ClassName.__method`)로는 접근 불가능

```python
class A:
    def __double_method(self):
        pass

class B(A):
    def __double_method(self): 
        pass

# dir(): 해당 클래스의 함수 리스트 출력
print(dir(A())) # ['_A__double_method' ....]
print(dir(B())) # ['_A__doubled_method', '_B__doubled_method', .....] 
```

#### 4. `__double_leading_and_trailing_underscores__`
* Special한 변수, 메소드에 사용
* ex: `__init__`(생성자), `__len__`, `__str__`, `__eq__`(==연산자 대응)

### 4. 국제화(i18n), 지역화(l10n) 함수로 사용되는 경우
* Convention으로서 사용 (_가 국제화/지역화 함수라는 의미 X)
* i18n, l10n 함수를 _로 바인딩하는 C의 Convention에서 유래

### 5. 숫자 리터럴 값의 자리수 구분자로 사용
* 3.6버전에서 추가된 문법
* 숫자값을 쉽게 읽기위한 자릿수 구분

```python
dec=1_000_000
bin=0b_1111_0000
hex=0x_1234_abcd

print(dec) # 1000000
print(bin) # 240
print(hex) # 305441741
```