# 테스트 자동화 도구: JUnit

## 개요

* 테스트 자동화 도구
* 테스트 케이스 생성 ==> 확인

## 예제 코드

```java
package calculator;

public class Calculator {
	int add(int i, int j) {
		return i + j;
	}
	int sub(int i, int j) {
		return i - j;
	}
	int multiply(int i, int j) {
		return i * j;
	}
	int divide(int i, int j) {
		return i / j;
	}

	public static void main(String[] args) {
		Calculator cal = new Calculator();
		System.out.println(cal.add(1,  2));
		System.out.println(cal.sub(1,  2));
		System.out.println(cal.multiply(1,  2));
		System.out.println(cal.divide(4, 2));
	}
}
```



## 테스트 케이스: JUnit 3

```java
package calculator;

import junit.framework.TestCase;

public class CalculatorTest extends TestCase {
//	초기화 코드 중복 제거
	Calculator cal;
	
//	setUp + Ctrl + Space
	@Override
	protected void setUp() throws Exception {
		cal = new Calculator();
		// TODO Auto-generated method stub
		super.setUp();
	}

	public void testAdd() {
		int result = cal.add(2, 1);
		assertEquals(3, result);
	}
	
	public void testSub() throws Exception {
		int result = cal.sub(2, 1);
		assertEquals(1, result);
	}
	
	public void testMul() throws Exception {
		int result = cal.multiply(3,  2);
		assertEquals(6, result);
	}
	
	public void testDiv() throws Exception {
		int result = cal.divide(4, 2);
		assertEquals(2, result);
	}
	
//	종료시 마무리 작업
// teardown + Ctrl + Space
	@Override
		protected void tearDown() throws Exception {
			// TODO Auto-generated method stub
			super.tearDown();
		}

}

```



## 테스트 케이스: JUnit4

```java
package calculator;

import static org.junit.Assert.*;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;

public class Calculator4Test {
	private Calculator cal;
	
	@Before
	private void setup() {
		// TODO Auto-generated method stub
		cal = new Calculator();

	}

	@Test
	public void add() {
		cal = new Calculator();
		assertEquals(3, cal.add(2, 1));
	}
	
	@Test
	public void sub() {
		cal = new Calculator();
		assertEquals(3, cal.sub(2, 1));
	}
	
	@After
	private void teardown() {
		// TODO Auto-generated method stub
		
	}
}

```





## 참고사항

* 실행순서: Setup => 테스트 케이스 1개 => Teardown (반복) (이전 작업이 )
* 각 테스트의 이름의 접두사는 반드시 `test`
* 테스트 케이스 이름 클릭 후 실행시, 해당 테스트 케이스만 실행