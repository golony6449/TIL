## Pandas
### Data Analyze Library
===================================
### DataFrame
* Pandas에서 사용하는 기본 데이터 형태
* `pd.DataFrame()`
* 매개변수로 2차원 리스트 사용
* `print()`로 출력시 열, 행 같이 출력됨

### Series
* 1차원 데이터형
* `pd.Series()`
* `print()`로 출력시 index 같이 출력

### 데이터 추출
* dict 형 자료를 매개변수로 만든 DataFrame의 경우 DataFrame 객체에 index로 키캆을 전달해 해당 데이터를 추출 할 수 있음
* `[['index1', 'index2']]`처럼 한번에 여러 키를 사용할 수도 있음
* 특정 위치의 값을 추출할때는 List Slicing을 이용 ex: `list[0:5000]`
* 특정 조건의 값 추출: `DF_obj[DF_obj.key >= value]`

### 정렬 and 반전
* 특정 키의 데이터를 기준으로 정렬: `DF_obj.sort_values(by='key')`
* 내림차순 정렬: `DF_obj.sort_values(by='key', ascending=False)`
* 행 - 열 반전된 값: `DF_obj.T`

### Numpy 객체로 변환
* Pandas를 지원하지 않는 라이브러리 사용 or Numpy를 이용한 데이터 처리를 위함
* `DF_obj.as_matrix()`