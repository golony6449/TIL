# 동적프로그래밍

# Longest Common Subsequence (LCS) (공통 부분 순서(문자열))
## 개요
* subsequence의 예: `<bcdb>`는 `<abcbdab>`의 subsequence
* Common Subsequence의 예: `<bca>`는 `<abcbdab>`와 `<bdcaba>`의 common subsequence
* Longest CS: Common Subsequence 중 가장 긴 것

## Optimal Substructure (부분 구조체)
* `Xm = <x1, x2, ... , xm>`
* `Yn = <y1, y2, ... , yn>`
* IF xm == yn THEN LCS(Xm, Yn) = LCS(Xm-1, Yn-1) + 1
* ELSE max(LCS(Xm, Yn-1), LCS(Xm-1, Yn))

## 방법 1: 재귀
* 함수명: LCS(m, n)

1. IF m = 0 or n = 0 THEN return 0
2. else if (xm = yn) THEN return LCS(m-1, n-1) + 1
3. else return max(LCS(m-1, n), LCS(m, n-1))

* 엄청난 중복호출 발생

## 방법 2: DP
* 함수명: LCS(m, n)
* 행렬 C: m X n 크기

1. C[i,0] <- 0 (0 ~ i ~ m)
2. C[0,j] <- 0 (0 ~ j ~ n)
3. IF xi == yj THEN C[i, j] <- C[i-1, j-1] + 1 (1 ~ i ~ m) (1 ~ j ~ n) ()
4. ELSE C[i, j] <- max(C[i-1, j], C[i, j-1])

* Complexity: Sigma(m * n)

## 정리
* 동적프로그래밍: 재귀에서 발생하는 엄청나게 많은 중복계산 문제 해결