# Lombok

## 개요

* 생성자, Getter, Setter 작성을 간단하게 할 수 있는 라이브러리



## 의존성

```
buildscript {
	repositories{
    	maven {
            url "https://plugins.gradle.org/m2/"
        }
	}
	
	dependencies {
		classpath "io.freefair.gradle:lombok-plugin:4.1.6"
	}
}
apply plugin: 'io.freefair.lombok'

dependencies{
    compile('org.projectlombok:lombok')
}
```



### 인텔리제이 설정

* 관련 플러그인 (`Lombok`) 설치
* 설정에서 어노테이션 프로세싱 (Annotation Processing) 활성화



## 사용

`@Getter`

`@Setter`

`@Builder`



## Trobleshooting

* `cannot find symbol` 오류 발생
  * `build.gradle`의 Dependency에 `annotationProcessor 'org.projectlombok:lombok'` 추가

* `error: constructor Code in class Code cannot be applied to given types` 오류 발생
  * `@Builder` 와 `@oArgsConstructor` 동시적용시 발생
  * Solution: `@AllArgsConstructor ` 적용
  * https://yuja-kong.tistory.com/m/99

