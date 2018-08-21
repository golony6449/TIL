# switch in Python

## 문법변경
1. 소스코드
2. 어휘분석
3. 구문분석
4. 바이트코드

## VS에서 컴파일하기
* PCBuild안의 솔루션파일 Open
* 그 중 python, pythoncore, pgen

## Parser
* 어휘분석 + 구문분석을 1개의 도구로
* Grammar/Grammar (EBNF로 작성됨)

* compound_stmt에 switch_stmt 추가

* switch_stmt 작성

## 컴파일 이후
* 생성된 h, c 파일을 덮어쓰기

## 구문트리(AST) 작성
* ast 모듈 사용
* /Parser 폴더 안에 추가(덮어쓰기)

## 구문트리 생성


## 심볼테이블 작성
* symboltable.c 파일 주성

## 바이트코드 생성
* .pyc: 바이트코드 (159개의 바이트코드 명령어)
* dis(assemble) 모듈을 이용해 조작 가능
* compile.c 수정