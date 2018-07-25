# 도메인 and URL
## 개요
* 과거의 hosts 방식의 문제점을 개선한 URL -> IP의 변환
* 과거의 행정적인 부분을 자동화

## Domain VS URL
### 도메인
* 해당서버의 주소
* ex) docs.python.org

### URL
* Uniform Resource Location
* 프로토콜, 컴퓨터 이름, 디렉터리 경로를 포함하는 파일 위치의 표기법
* ex) https://docs.python.org/index.html

## 구성
| docs | python | org | |
|------|--------|-----|-|
| sub | Second-Level | Top-Level | Root |

* 각각의 Level을 담당하는 독자적인 DNS 서버 존재
* 상위 Level의 서버는 자식 레벨의 서버를 알고 있어야 함

## DNS의 동작(변환) 과정
1. Root 네임서버에 요청 -> 일치 X -> 해당하는 Top-Level의 목록 전달
2. Top-Level의 서버에 요청 -> 일치 X -> 해당하는 Second-Level의 목록 전달
3. 일치할때 까지 반복

## 도메인의 등록과정
| 등록자(Registrant) | 등록대행자(Registrar) | 등록소 (Registry) | ICANN |
|-------------------|----------------------|-------------------|------|
| 서버의 관리자 | 중간대행자 | Top-Level 도메인 관리 | Root 도메인 관리 |

* Root Name Server: 전세계의 Top-Level 서버의 목록 관리
* Top-Level Server: KISA에서 관리 (kr의 경우)
* Second-Level Server: 등록대행자의 서버 사용 or 직접 구축 가능 (등록대행자: KISA에 등록된 중간대행자)

1. 서버의 관리자는 도메인 구매 후, 등록대행자(의 서버에)에 등록
2. 등록대행자는 등록소의 서버에 도메인과 등록대행자의 서버주소를 등록

## TODO
* 등록소의 DNS 서버에도 도메인이 등록되는데, 그럼 등록대행자의 DNS 서버의 존재 의의는 무엇일까?