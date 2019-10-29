# Spring's Annotations

## Annotation

* 소스코드에 메타데이터를 표현하는 방법
* 메타데이터: 데이터에 대한 설명을 의미하는 데이터
* 데이터의 유효성검사, 간결한 코드 작성 가능
* 리플렉션을 이용해 어노테이션 지정만으로 필요한 클래스 주입 가능



## 종류

* `RestController`: 해당 객체가 HTTP 요청을 핸들링하는 컨트롤러임을 의미하는 어노테이션
  * `@Controller` + `@ResponseBody`
* `RequestMapping(path, method=??)`: 메서드와 path를 맵핑(method 옵션으로 특정 요청만 맵핑 가능)
* `GetMapping(path)`: GET Method와 함수를 맵핑
* `RequestParam(value=?, defaultValue=?)`: value로 지정한 쿼리 매개변수를 변수에 저장
  * `public Greeting greeting(@RequestParam(value="name", defaultValue="World") String name)`
* `Autowired`: Spring에 의해 생성되는 객체임을 표기.
* `Service`: 해당 클래스를 스프링 컴포넌트 스캐너가 감지하고, 어플리케이션 컨텍스트에 추가.
* `Async`: 해당 메서드가 분리된 Thread에서 실행되어야 함을 표기. 해당 메서드는 Future 객체 반환
* `EnableAsync`: `Async` 메서드를 Thread pool에서 실행할수 있도록 하는 마킹
* `MessageMapping(Path)`: 해당 경로로 메시지가 도달했을 때, 해당 메서드가 실행됨을 표기 (웹소켓)
* `SendTo(Path)`: 해당 경로를 구독(Subscribe) 중인 모든 사람에게 메서드 반환값을 브로드캐스트함을 표기(웹소켓)
* `Configuration`: Spring configuration 클래스임을 명시
* `EnableWebSocketMessageBroker`: 메시지 브로커를 기반으로 웹소켓 메시지 핸들링 활성화
* 