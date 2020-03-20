# AJP 보안 관련 오류 발생시

* 톰켓 v9에서 바뀐 정책 때문에 발생하는 에러

* 오류 메시지

` java.lang.IllegalArgumentException: The AJP Connector is configured with secretRequired="true" but the secret attribute is either null or "". This combination is not valid.`

## Solution

* `secretRequired="false"` 추가

```xml
    <Connector address="0.0.0.0" port="8009" protocol="AJP/1.3" redirectPort="8443" secretRequired="false"/>
```



## Ref

* https://nirsa.tistory.com/131
* https://okky.kr/article/687011