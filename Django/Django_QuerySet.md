# 쿼리셋



## 합치기 (Merge)

* 두 쿼리셋을 합집합

```python
queryset_a = queryset_a | queryset_b
```



## 특정 필드값만 추출

```python
QuerySet.values(컬럼1, 컬럼2, ...)
```



## 쿼리셋이 비어있는지 확인

```python
QuerySet.exsits()
```



## 빈 쿼리셋 생성

```python
Model.objects.none()
```



## 쿼리셋으로 필터링 수행

```python
orm.filter(컬럼명__in=쿼리셋)
```

