# Hash Table

## 저장, 검색의 복잡도
* 배열: O(n)
* BST: Omega(n), Omega(logn) (Worst Case)
* Balanced BST: Omega(logn) (Worst Case)
* B-Tree: Omega(logn)
* <b>Hash Table: Omega(1) (average) </b>

## 개요
* 원소가 저장될 자리가 <b>값에 의해</b> 결정
* 상수시간 동안 삽입, 삭제, 검색 가능
* 매우 빠른 응답을 요할때 유용
* 별도 연산(최소, 최대 값) 불가능

## 주소계산
* 검색키 -> 주소계산 -> 테이블의 인덱스 결정
* 핵심 파트

## Hash Function 
* (ex: h(x) = x mod 13)
* 입력원소가 table에 골고루 저장
* 계산이 간단해야 함
* 대표적인 방법: 나눗셈, 곱셈

### DIvision method
* h(x) = x mod m
* m: 테이블 사이즈 (보통 prime Number: 한쪽으로 몰리지 않게 하기 위함)

### Multiplication Method
* h(x) = (xA mod 1) * m
* Division의 응용
* A: 0 < A < 1인 상수
* m이 소수(prime)일 필요 없음
* p: 정수

### 예시
* M = 65536, A=0.6180339887, X=1025390
* xA = 1025390 * 0.6180339887
* xA mod 1 = 0.871673093 (정수부 삭제)
* 크누스: A = (sqrt(5) - 1 ) / 2 제안

## 충돌 (Collision)
* 한 주소에 2개의 원소 or 테이블 크기 초과
* Solution: Chaining, Open Addressing

### Chaining
* 같은 주소로 Hashing 되는 원소를 하나의 Linked List로 관리
* LL 생성 필요

### Open Addressing
* 충돌 발생시, 어떻게든 테이블 내에서 해결 => 빈자리가 생길때 까지 해시값을 계속 생성
* 추가 공간 필요 X
* Solution: Linear probing, Quadratic probing, Double hashing

### Linear probing
* 빈칸을 찾을때 까지 다음 주소로 이동
* hi(x) = (h(x) + i) mod m
* 지속적인 충돌 발생의 가능성 있음 ==> Primary Clustering(특정 영역에 원소가 몰리는 현상)

### Quadratic probing
* Primary Clustering 문제 해결
* hi(x) = (h(x) + c1i^2 + c2i) mod m
* 더 많은 주소를 이동
* 중복 충돌 발생시 마다, 점점 더 많은 주소를 이동
* Secondary Clustering 발생: 여러개의 원소가 동일한 초기 해시 함수값을 가지는 현상

### Double Hashing
* hi(x) = (h(x) + i*f(x)) mod m
* 별도의 f(x)를 통한 해결
* 군집현상 X