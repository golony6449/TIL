## SuppressWarning
#### 직역하면 `경고를 억누른다`
=================================

### 개요
* 컴파일러가 경고하는 내용중 일부를 무시(제외)하는 어노테이션(annotation)
* 제외할 옵션을 ()안에 지정
* 예시: `@SuppressWarnings("unused")`

### 종류
| 이름 | 의미 |
|------|------|
| all | 모든 경고를 억제 |
| cast | 캐스트 연산자 관련 경고 억제 |
| dep-ann | 사용하지 말아야 할 주석 관련 경고 억제 |
| deprecation | 사용하지 말아야 할 (= 더 이상 지원되지 않는) 메소드 관련 경고 억제 |
| fallthrough | switch문에서의 break 누락 관련 경고 억제 |
| finally | 반환하지 않는 finally 블럭 관련 경고 억제 |
| null | null 분석 관련 경고 |
| rawtypes | 제네릭을 사용하는 클래스 매개변수가 불특정일 때의 경고 억제 |
| unchecked | 검증되지 않은 연산자 관련 경고 억제 |
| unused | 사용하지 않는 코드 관련 경고 억제 |

### 참고자료
* http://jinwoonote.tistory.com/entry/SuppressWarnings-%EC%9D%B4%EA%B1%B4-%EB%AD%90%EC%A7%80