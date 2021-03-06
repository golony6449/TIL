## 만화로 쉽게 배우는 CPU
=============================
## Chapter 1. CPU?
* 정보의 디지털화: 음성, 화상, 동영상등을 모두 수치화해 0, 1로 표현 => 모든 정보를 디지털 통신 회선, 매체로 전송, 저장 가능. 연산(분석, 가공) 가능
* 정보: 우리 주변을 둘러싸고 있는 모든 것

### 디지털 vs 아날로그
| 디지털 | 아날로그 |
|-------|----------|
| 불연속적 값 | 연속적 값 |
* 최소단위를 줄임으로서 아날로그에 근접할수는 있지만, 어느정도의 손실은 발생
* => 없어도 무방한 정보를 생략함으로서 압축

* 이미지, 음성: 비가역적 압축(영구적인 데이터 손실 발생)
* 텍스트: 가역적 압축(원본 데이터 복원 가능)


* CPU - Central Processing Unit(중앙연산처리장치)
* 제어장치 + 연산장치로 구성
* CPU가 처리하는 연산: 산술연산(덧셈, 뺄셈) + 논리연산(AND, OR, NOT)
* 단, 최근의 CPU에는 FPU(Float Processing Unit, 부동소수점 연산기)이 포함 => 곱셈, 나눗셈도 가능

### 컴퓨터의 5대 장치
1. 제어장치: 프로그램을 해석해 다른 4개의 장치를 제어.
2. 연산장치: 연산을 수행. <b>메모리에서 데이터를 가져와 연산 수행</b>
3. 기억장치: 연산을 수행할 대상(데이터, 프로그램)을 저장. 주기억장치 + 보조기억장치
4. 입력장치: 외부에서 데이터 입력
5. 출력장치: 외부로 데이터 출력

* CPU를 이해하는데는 데이터, 제어의 흐름을 파악하는 것이 중요!

### ALU - Arithmetic Logic Unit (산술 연산 장치)
* CPU의 핵심
* 산술연산 수행
* 입력: A,B(대상), F(명령어)
* 출력: Y, S(스테이터스)

#### CPU는 연산과 판단을 수행
* ALU에서 S(Status)가 필요한 이유
* 연산의 출력인 Status를 이용해 주어진 조건 충족 여부를 판단 => 이후의 행동 변화
* 이러한 연산, 판단을 반복함으로서 여러가지 일을 수행할 수 있게 함 (이를 위해서는 정확한 프로그램 작성이 필요)

## Chapter 2. 디지털 연산
* 0,1로 표현 => 상반되는 2가지 상태로 표현
* 내부적으로는 전압이 기준보다 높다(High), 낮다(Low)로 구분
* 다만 High가 1에 대응 될지(Positive) 0에 대응될지(Negative)는 설계자가 정함

### 고정소수점, 부동소수점
* 고정소수점: 일상적으로 사용하는 표기법. 소수점 위치를 고정시킨 뒤, 정수부, 소수부 표현
* 부동소수점: 숫자를 가수부, 지수부로 분리 => x.xx * 2^n 형태로 표시

### 보수
* 덧셈기를 이용한 뺄셈연산 방법
* 즉, 원래 수에 더하면 자리넘침이 발생하는 수 (보충하는 수) => 보수
* 자리넘침수는 무시 => 덧셈 결과: 0 => 음수표현 가능

* 15-15 = 15+(-15)
* 2가지의 보수가 존재: r의 보수, r-1의 보수 => ex) 10진수 => 10의 보수, 9의 보수

#### 15-15 => 15 + (-15) => 15 + 85 = (1)00 => 자리넘침은 무시

#### r의 보수
* r-1에 각각의 자리수를 뺄셈
* 결과에 +1

#### r-1의 보수
* r-1에 각각의 자리수를 뺄셈

#### 컴퓨터는 내부적으로 2의 보수를 사용해 음수 표현

### 논리회로
* IC(Integrated Circuit): 0,1을 이용해 논리 연산을 수행하는 장치(부품). 내부에 논리회로가 구성되어 있음
* 3가지 기본 논리회로: AND, OR, NOT
* 이 외의 회로: XOR, NAND, NOR, XNOR => 몇가지의 기본 회로를 연결한 것과 같은 작용

* 진리표(진리값 표): 모든 입출력 패턴을 표기한 표

#### 드모르간 정리: OR, AND를 변환!

#### 반가산기
* 덧셈연산을 수행하는 회로
* Carry: X and Y, 결과: X xor Y 이므로, 1개의 AND, XOR 게이트를 이용해 설계 가능

#### 전가산기
* 여러자리의 덧셈 연산 수행
* 반가산기를 2개 연결해 구성 가능
* 전가산기 여러개를 연결함으로서 한번에 여러자리의 2진수를 덧셈할 수 있는 가산기 구성 가능
* 이때 한 자리의 계산결과, 자리올림이 다음 자리수의 입력으로 전달

#### 순차 자리올림 가산기 and 자리 올림 션견 가산기
* 순차 자리올림 가산기: Carry의 전파지연 문제 -> 앞자리의 계산이 끝나야 다음 자리 계산 가능
* 자리 올림 선견 가산기: Carry를 미리 준비된 논리회로로 계산 상위의 자리도 기다림 없이 계산 가능

#### 기억하는 회로 - 플립플롭
* 과거의 상태를 기억 => 과거 상태도 연산의 대상이 될 수 있음
* ex) 메모리, CPU 내부의 레지스터
* 래치(Latch): 0 or 1인 상태를 '유지'하는 것
* 종류: RS, D, T 플립플롭

* RS플립플롭의 구성: 2개의 NAND, or 2개의 NOR 게이트
* 주의) 절대 R, S가 동시에 1이 되면 안됨

* 8자 형태: 기억 회로의 특징

* D 플립플롭: 입력 - D, C(Clock)
* 클록의 상승신호(상승 Edge)를 매개로 동작

#### 최근의 회로 설계
* HDL(Hardware Description Language) - 하드웨어 기술언어, 회로를 생성하는 기술
* CAD: Computer Aided Desing

* 초기에는 기본 게이트(AND, OR, XOR 등)을 결선해 회로 구성
* FPGA: Field Programable Gate Array: 내부에 4~6입력의 룹업 테이블 내장, 외부에서 결선을 프로그램할수 있도록 한 IC => 동일한 FPGA도 전혀 다른 IC로서 사용 가능
*                       => 대량 생산을 통해 원가 절감 가능


## Chapter 3. CPU의 구조
* 어드레스 공간: CPU가 직접 관리하고 있는 공간
* 어드레스: 저장장소에 할당된 번호 => 원하는 데이터를 번호로 불러오거나 저장 할 수 있음
* 버스: 데이터의 통로(신호선의 묶음), 어드레스, 데이터, 외부(CPU - 외부장치), 내부(CPU 내부) 3가지 존재
* (데이터) 버스 폭: 신호선의 가닥 수 = 한번에 다룰수 있는 비트 수 ex) 64bit CPU => 버스 폭 = 64 => ALU의 처리 폭 = 64bit
* 외부의 데이터 버스 폭: 한번에 메모리와 주고 받을 수 있는 비트 수
* 내부의 데이터 버스 폭: 한 번에 연산 할 수 있는 비트 수
* 어드레스 버스 폭: 취급 가능한 어드레스 수 ex) 32bit => 2^32 공간 크기를 가짐

### 제어 버스
| Read/Write | Load/Store |
|------------|------------|
| HW 관점 | SW 관점 |

* 제어 신호를 전하는 버스
* 제어신호: 데이터를 꺼내라, or 저장하라 (R/W 제어신호)
#### 83번 데이터가 필요 => 어드레스 버스: 83, 제어 버스: Read
* I/O 제어: 외부 장치를 작동 시키기 위한 제어 신호

### 명령
* CPU가 이해하기 쉬운 형태의 작업
* 프로그램: 명령의 연속
* 오퍼랜드(대상), 오퍼레이터(명령코드)로 구성
* 주의) 오퍼랜드는 어드레스로 지정가능
* 연산할때는 레지스터를 이용
* 레지스터 종류: 어큐물레이터(누적기), 범용 레지스터, 명령 레지스터(명령 저장 목적)
* 명령 예시) 2개의 데이터를 어큐물레이터, 범용 레지스터에 저장 => ALU에서 덧셈 연산 수행 => 결과를 어큐물레이터에 저장
* 즉, 명령을 해독 한 뒤, 연산 수행

### 명령의 처리
* PC의 내용 => 어드레스 레지스터에 저장 => 메모리에 전달(명령의 어드레스 지정)
* 어드레스가 지정된 명령을 메모리에서 CPU로 전달 => 명령레지스터에 저장 => 명령 디코더에서 해독
* 해독된 명령(오퍼랜드 + 명령코드)을 ALU로 연산

* <b>1. 명령읽기(Fetch) => 2. 명령 해독(디코드) => 3. 명령 실행 => 4. 결과 쓰기</b>

#### 프로그램 카운터 (PC)
* 다음에 실행할 명령의 어드레스 기억
* 현재 명령이 레지스터에 저장되었을 때 다음 명령으로 전환
* 조건 판단에 따른 분기, 반복 => 순차적으로 이동하지 않을 수도 있음
* PC의 비트수 = 어드레스 버스의 비트수 = 어드레스 공간의 비트 수
* MMU(Memory Mapping Unit): 가상 메모리와 실제 메모리를 대응시키는 HW

#### 명령 디코더
* 메모리에서 호출된 명령코드로 연산 처리를 위한 기능을 작동 시킬 수 있도록 하드웨어를 내부에서 접속하는 동작 수행
* 메모리상의 명령 != CPU의 제어신호

### 여러가지 기억장치
* 종류: 주기억장치, 보조기억장치
* 보조기억장치는 CPU가 직접 접근 할 수 없음 => CPU의 어드레스 공간에 존재하지 않음
* 어드레스 공간: CPU가 직접 관리하고 있는 공간, RAM영역 + ROM 영역 + IO영역
*                                                                    => CPU와 외부장치가 직접 연결되어 있음 (단, 디스플레이 처럼 직접 연결되지 않고 중간에 별도의 컨트롤러가 존재하는 경우도 있음)
* 용량: 하드디스크 > 디스크 캐시 > 메인 메모리 > 캐시 메모리 > 레지스터

### 인터럽트 (Interrupt)
* 현재 진행중인 작업을 일시중지(방해) 하는 역학
* 우선적인 이벤트를 먼저 수행 => 여러가지 작업을 효율적으로 진행 할 수 있음 (주기적인 확인 불필요, 우선순위가 높은 작업을 먼저 수행)
* 스택을 이용해 계산도중의 값, PC의 값 등을 저장 => 원래 작업으로 돌아갈 수 있도록 함

#### 인터럽트 마스크
* 인터럽트를 받아들이지 않도록 하는 기능
* 단, 리셋, 우선순위가 가장 높은 인터럽트(NMI)는 마스크 불가능
* 리셋: 기기 초기화, 전원을 켤때도 실행됨 => 정상적인 동작 개시 가능
*       => 전압이 안정화 되기까지 CPU 동작 개시 X => 안정화 이후 리셋 입력에 H(High) 입력해 리셋 해제
*               => 필요시 리셋의 전압 강하 수행 => 강제 리셋

#### 타이머 인터럽트
* CPU 내부의 감산카운터를 이용 => 카운터가 0이 되었을때, 인터럽트 발생
* 절차: 마스터 클럭 주기의 몇 배를 기준으로 할지 결정 => 타이머 기준 클럭 몇회에 인터럽트 발생할지 레지스터에 저장 => 리셋을 명령으로 해제

### 클록
* 일정 주기로 H, L 상태를 반복하는 신호
* 단위: Hz(1초에 몇번 반복하는가?)

#### 정확도
* 주파수가 얼마나 정확한지 정도를 나타낸 것

#### 클록 제너레이터
* 클록을 만들기 위한 발진기
* 일반적으로는 CPU에 내장, 외부에서 발생시킨 신호를 입력할 수도 있음
* 내장: 발진회로 => 여러가지 부품을 조합 => 각각의 부품의 품질이 균일해야 함
* 외부: 발진'기'에서 만들어 진 클록 => 정확

### FLOPS
* CPU의 능력 수치
* CPU의 클록속도(얼마나 빨리 작동), 연산속도에 의해 결정(얼마만큼의 속도로)
* MIPS(Million Instructions Per Seconds): 1초당 실행할 수 있는 명령 수
* CPU가 부동소수점 연산 HW를 내장 => MFLOPS(Million Floating Point Operations Per Seconds): 1초당 얼마만큼의 부동소수점 연산을 실행 할 수 있는가?
