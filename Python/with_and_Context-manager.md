## with and Context Manager
* 참고자료: https://ddanggle.gitbooks.io/interpy-kr/content/ch24-context-manager.html
==================================
### Context Manager
* 원하는 타이밍에 리소스를 할당하고 제공하는 역할
* 가장 많이 사용되는 컨텍스트 매니저 => with
* 코드 블록 사이에서 한쌍으로 실행되어야 하는 코드 연결 가능
* ex) 파일 open - close, 소켓 open - close

#### without with
```python
file = open('somefile','w')
try:
    file.write('Hola')
finally:
    file.close()
```

#### with with
```python
with open('some_file','w') as opened_file:
    opened_file.write('Hola')
```

## Class를 이용한 Context Manager 지정
```python
class File(object):
    def __init__(self, file_name, method):
        self.file_obj = open(file_name, method)
    def __enter__(self):
        return self.file_obj 
    def __exit__(self, type, value, trace_back)
        self.file_obj.close()
```

### with 호출시의 절차
1. 해당 객체의 `__exit__` 메소드 저장
2. 해당 객체의 `__enter__` 메소드 호출
3. 코드블럭 실행
4. 코드블럭 실행 후 저장된 `__exit__` 메소드 호출

### 핸들링 중 예외발생시
* 발생한 예외의 type, value, trace_back을 `__exit__`에 전달
* `__exit__`에서 True반환시 => 적절하게 예외가 처리된 것으로 간주
* `__exit__`에서 True이외의 Something을 반환시 => with에서 예외발생 (예외가 처리되지 않음)