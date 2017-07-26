# threading module
* 고레벨(high level)의 thread 인터페이스
===========================
### 개요
* 멀티스레드를 구현하는데 사용 되는 모듈
* low-level의 thread모듈도 있으나, 대개는 thread 모듈 기반으로 작성된 threading 모듈을 이용

### 기본적인 구현 방법
* 객체 생성
1. threading.Thread(target=함수, args=튜플, daemon=bool형)로 thread 생성
2. 생성된 객체에 필요한 세팅 적용
3. .start() 메소드 실행

* threading.Thread를 상속받는 클래스 생성
1. 서브클래스 정의
2. 생성자 작성(생성자에서 Thread의 생성자 호출 및 기타 초기화 작업 수행)
3. run() 메소드 재정의 - 실질적인 구동 내용 작성
4. 객체 생성 후 run() 메소드 호출

### 예제 코드
* 객체 생성 방식

reference.2 참고

* 서브클래스 생성

reference.2 참고

### 기타
* start()는 내부적으로 run()을 실행
* 데몬 thread: 메인 thread가 종료되면 같이 종료되는 thread (default: false -> 메인 thread 종료 여부와 상관없이 계속 수행)

## Timer Objects
* 간단한 타이머 객체를 생성
* 지정된 시간 경과시, 사전에 지정된 함수 호출

### 사용법
1. Timer(시간, 호출함수)를 이용해 타이머 객체 생성
2. .start()메소드를 이용해 타이머 작동 시작

### 기타
1. 타이머 객체는 1회용 -> 한번 사용된 타이머 객체는 재사용 불가능(RuntimeError: threads can only be start once)
2. Qt에서의 connect 처럼 별도의 args 전달 불가능 -> 필요시 lambda식 활용해 전달

#### referencce
1. python 3.5.3 docs: https://docs.python.org/3.5/library/threading.html?highlight=threading#
2. 예제로 배우는 Python 프로그래밍: http://pythonstudy.xyz/python/article/24-%EC%93%B0%EB%A0%88%EB%93%9C-Thread