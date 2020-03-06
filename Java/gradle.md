# Gradle

## 개요

* Gradle을 사용해 자바 프로젝트 빌드하기



## 블록

* repositories: 의존성을 탐색할 저장소 지정 `mavenCentral()`
* dependencies: 의존하는 모듈 지정
  * compile: 컴파일시점에 필요한 모듈을 의미
  * providedCompile: 컴파일시에 필요하지만, 실행시간에 제공될 모듈 (servlet 등)
  * testCompile: 컴파일과 테스트시에 사용되는 모듈. 실행 시점에는 불필요
* jar: JAR 파일의 명명법 지정
  * baseName: 파일명
  * version: 버전명
  * 예: 'gs-gradle', '0.1.0' ==> `ga-gradle-0.1.0.jar`



## 명령

* `gradle tasks`: 수행가능한 명령 출력 (`build.gradle`파일에 따라 바뀜)
* `gradle build`: 빌드 명령어
* `./gradlew`: gradle wrapper를 이용한 빌드



## 디렉토리 구조

* build: 빌드 결과물 저장
  * classes: 컴파일된 파일
  * reports: 빌드 결과 저장
  * libs: 결합된 파일들이 저장됨 (JAR, WAR)
  * dependency-cache: 의존성 파일들의 캐시가 저장됨



## gradle wrapper

* gradle build를 시작하는 보다 나은 방법
* 이전에는 빌드파일에 추가했어야 하지만, 지금은 자체에 내장됨
* 각 운영체제 별 배치파일로 구성됨
* 스크립트 실행시 필요한 gradle을 다운받아서 수행됨 
  * => gradle이 설치되지 않은 PC에서도 구동가능
* 명령: `gradle wrapper --gradle-version 2.13`



## Example

```
apply plugin: 'java'
apply plugin: 'application'

mainClassName = 'hello.HelloWorld'

repositories {
    mavenCentral()
}

jar {
    baseName = 'gs-gradle'
    version =  '0.1.0'
}

sourceCompatibility = 1.8
targetCompatibility = 1.8

dependencies {
    compile "joda-time:joda-time:2.2"
    testCompile "junit:junit:4.12"
}
```





## Reference

*   https://spring.io/guides/gs/gradle/ 