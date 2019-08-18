# 테스트 시간 단축

## Password Hashing

* 유저 100명 생성에 20초 걸림 ==> django의 해시 처리가 느려서.
* 해사함수를 여러번 적용 ==> 빠른속도 == 적용횟수 감소
* 키 스트레칭: 비밀번호가 맞는지 확인에 어느정도(0.2초)  걸리게 하는 것
* Django 기본: PBKDF2_SHA256(느림), 보안에는 좋지만 테스트시간은... ㅠ
* Sol: 테스트 환경에서 MD5를 `PASSWORD_HASERS`를 사용



## Mocking

* 호출에 대한 고정된 응답을 하는 가짜 객체
* 실제 객체처럼 동작, 호출 파라메터, 리턴값 검증

### 사례

* 외부 API 호출에 스로틀링
* 운영환경에는 필요하나, 테스트에서는 시간만 소모 (10초 대기를 테스트)
* `@mock.patch()` 데코레이션 사용
* 라이브러리: `freezegun`, 시간이 흐른것 **처럼** 처리



## TransactionTestCase 사용 지양

* 테스트는 다른 테스트에 영향을 받으면 안됨
* DB데이터 삭제 구현 방법 2가지: `TestCase`, `TransactionTestCase`
* TestCase: Savepoint 생성 후 Rollback
* TransactionTestCase: `TRUNCATE TABLE` 명령
* 약 3000배의 속도 차
* 단, DB Lock 관련 로직 수정시는 별도의 테스트 필요 (LOCK 관련 동작 차이 있음)
* `on_commit`: 성공시에만 실행할 함수 등록 기능(TestCase 성공여부에 무관하게 항상 롤백됨)
* 문서에서는 이런 상황에서 TransactionTestCase를 사용하도록 함
* 관련 처리를 통해 `TestCase` 사용 가능



## 병렬 테스트

* `v.1.9` 이상은 `--parallel` 추가로 간단히 가능
* 마스터 => 워커 테스트 할당, 마스터에 events 객체 전달
* 이때 프로세스간 객체 공유를 `Pickle`로 수행
* 문제: 동적으로 생성되는 `DoesNotExist`, `MultipleObjectReturned`는 피클링이 안됨
* `v.2.1` 이상은 패치된 사항
* diff를 직접 적용해 해결가능 ==> 안정성을 위해 테스트환경에서만 사용을 권장, `__qualname__` 사용 ==> py2에서는 사용 불가능



## Keepdb with mysqldump

* 프로젝트가 큰 경우 초기 마이그래이션 지연
* keepdb: 최초 테스트 DB를 재활용 (삭제 X)
* CI에서 문제 발생: 여러 브랜치가 같은 테스트 공유(원인)
* `develop`은 거의 롤백 되지 않음 => DB를 덤프 떠, CI 스크립트로 db 백업
* 4~5분 ==> 5~10초



## Disable Linter

* 30% 정도의 오버헤드
* 품질과 시간을 트레이드 오프
* 상황에 맞게 적용

