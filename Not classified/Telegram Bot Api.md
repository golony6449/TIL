## 봇에서 채널로 메세지 보내기!
* sendMessage API 이용
* Telegram API를 이용, 서버에 메세지 전송 요청
* 전송에 사용한 봇은 bot api key를 이용해 구분하고, ch_id 항목은 해당 메세지를 송신 할 Target을 의미

### 주의
1. 전송 요청이 사용되는 ch_id는 해당 채널 생성시 기입한 링크를 기입해야 함 (대소문자 구분 X)
2. 채널 생성 후 링크 수정시, 변경 이후 새로운 링크로 메세지가 전송 된 이후 변경사항이 적용 되는 것으로 보임 (전송 이전에는 구 링크로도 전송 가능)

##### 비공개 채널에 메세지 전송하기
1. 해당 채널을 공개로 설정
2. 메세지 전송(내용 무관)
3. 전송에 대한 Response내의 result -> chat -> id 항목을 추출
4. 채널을 비공개로 설정하고, 추후 전송시 ch_id로 추출한 id를 지정해 전송

### reference
Telegram API Docs: https://core.telegram.org/api