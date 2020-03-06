# Spring Security

## 개요

* 스프링 프로젝트에서 URL에 대한 접근제어, 로그인 처리를 하는 모듈



## 의존성

```
implementation 'org.springframework.boot:spring-boot-starter-security'
```



## 접근제어 (HttpSecurity)

### 기본 틀

```java
@Configuration
@EnableWebSecurity
@RequiredArgsConstructor
public class WebSecurityConfiguration extends WebSecurityConfigurerAdapter {

    @Override
    protected void configure(HttpSecurity http) throws Exception {
        http
                .authorizeRequests()
                    .antMatchers("/member/new").permitAll()
                    .antMatchers("/admin").hasRole("ADMIN")
                    .anyRequest().authenticated()
                    .and()
                .formLogin()
                    .defaultSuccessUrl("/main")
                    .permitAll()
                    .and()
                .logout();
    }
}
```

* `antMatchers(URL).permitAll()`: 해당 URL은 권한없이 접근 가능
* `antMatchers(URL).hasRole(권한)`: 해당 URL은 특정 권한을 가진 사람만 접근 가능
* `anyRequest().authenticated()`: 그 외의 요청은 인증된 사용자만 접근 가능
* `formLogin()` 과 하위 설정, 로그아웃: 폼 로그인, 로그아웃을 사용할 수 있음, `login`페이지는 권한없이 접근 가능, 성공하면 지정된 URL 요청



## 참고자료

* [Spring Security](https://velog.io/@hellozin/Spring-Security-Form-Login-간단-사용-설명서-f2jzojj8bj)
* 