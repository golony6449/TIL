# Chap 1

## 루프와 시간복잡도
* 루프의 수 만큼 n의 승수 증가

## 단! 루프의 중첩 갯수가 반드시 승수와 같지는 않음
* 슬라이드 15, Sample 4 (P.31)

## 자기호출 and 귀납적 사고
* 팩토리얼, 점화식
* 프렉탈(Fractal)(= 유사한 문양이 반복되는 것)
* Merge Sort

## 알고리즘 분석
* 이유: 무결성 확인, 자원 사용의 효율성 파악
* 크기가 작은 경우는 큰 의미 없음, but 큰 경우는 큰 차이.
* 점근적 분석: 입력의 크기가 충분히 큰 경우에 대한 분석

## 점근적 분석(Asymptotic Analysis)
* n -> 무한일때 f(n)
* big-O, theta, omega ...
* 최대, 최소, 평균적

### O 표기법 ( O(f(n)) ) (Tight or loose upper bound)
* 최대 f(n)의 비율로 증가
* 상수 비율차이 무시, 가능한 tight하게 f(n) 지정
* O(f(n^2))은 여러 제곱방정식으로 구성

### omega ( f(n) ) (Tight or loose lower bound)
* 적어도 f(n)의 비율로 증가
* O 표기법과 대칭적

### theta (Tight bound)
* f(n)의 비율로 증가하는 함수
* O, Omega의 교집합

## 분석 종류
* Worst-Case
* Average-Case (분석하기 어려움)
* Best-Case (유용 X)

## 직접 해볼것
* B-Tree??
* Merge Sort 알고리즘 찾아보기