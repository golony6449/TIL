# 데이터통신과 네트워크
---------------------------
## 데이터통신과 네트워크
### 데이터 통신, 네트워크의 개념
#### 데이터통신
* 데이터 + 통신
* (사실, 개념, 명령) + (정보의 공유)

* 통신: 두 사람 or 장치 사이에서 정보공유를 위해 정한 규칙(프로토콜)에 따라 Symbols, Signs등을 이용해 다른 지점으로 정보를 전달하는 과정

##### 그럼 데이터 통신은?
* 컴퓨터, 통신장치 간에 유무선의 전송매체를 사용해 정해진 규칙(통신 프로토콜)에 따라 데이터로 표현된 정보를 교환하는 과정
* 데이터 처리장치 뿐 아니라, 정보전송, 교환장치도 필요함 -> 상호연결 시스템(데이터통신 네트워크) 구축 필요 -> 분산된 source로 부터 정보의 전송, 공유를 위해 설계된 상호연결 시스템

* Data Communication Network -> Computer Network (= Network) 라고 표현

* 즉, Computer Network = 데이터 처리, 통신장치 간에 통신 매체를 통해 통신규칙(protocol)에 따라 데이터의 전송 및 수신 과정을 포함하는 시스템

#### 데이터 통신 네트워크 시스템의 구성요소
* Message(메시지): 통신하고자 하는 정보 (텍스트, 이미지 등)
* Transmission Equipment(전송장치): Message를 전송하는 장치 (컴퓨터, 워크스테이션, 전화기 등)
* Receiving Equipment(수신장치): Message 수신
* Transmission Media(전송 매체): Message가 전송되는 실제 전송로
* Protocol(프로토콜): 데이터 통신과 관련된 규칙

* 물리적인 연결이외에도 다양한 Device들이 정보를 주고받을 수 있도록 일관성있는 개방형 구조 가짐
* ex: ISO - 개방형 시스템 상호접속(Open Systems Interconnection), IBM - 시스템 네트워크 구조 (System Network Achitecture)

### 네트워크 유형
* 네트워크 참조 모델: 네트워크 내 or 네트워크간 정보교환을 위한 프로토콜을 표준화한 모델

#### LAN - Local Area Network
* 건물, 캠퍼스등 일정지역 내의 네트워크 구성형태
* 대역폭: 10~1000Mbps
* 구조: Star, Bus, Ring

#### MAN - Metropolitan Area Network
* LAN의 확장개념
* 10 ~ x00 KM 범위를 수용하는 네트워크 시스템
* ex: DOCSIS(케이블 TV 네트워크), Wibro, Wi-Max

#### WAN - Wide Area Network
* 광범위한 지역(도시, 국가)을 수용
* x00 ~ x000 KM 범위 포함
* 전송매체, 교환장치로 구성된 Sub Network로 구분
* 흔히 가정에서 사용되는 네트워크 개념 (댁내 장비, 라우터 등으로 구성)

#### PAN - Personal Area Network
* 10m 이내의 단거리
* IEEE 802.15 에서 표준화
* ex: Bluetooth, Zigbee

#### BAN - Body Area Network
* 인체중심 네트워크
* 신체에 부착된 여러장치로 구성된 네트워크
* 현재는 의료(임플란트, 원격제어 등)/비의료용(엔터테인먼트, 제어, 식별정보 송수신등)으로 구분됨

### 네트워크 표준화
* 표준화의 정의: 작업방법, 시간, 공구, 설비에 대한 과학적 조사를 통해 <br>하나의 최선의 방법을 발견</br> 이를 모든 작업자에게 적용

* 개방경쟁시장, 국제적인 통신에 있어서 제조사, 판매자, 정부, 서비스 provider 간 상호 연동성 보장 -> 호환성유지를 가능도록 함

* de facto(by fact): 일반에 널리 사용되는 표준 (사실상 표준)
* de jure(by law): 공식적이고 권위있는 기관, 단체에서 제정된 표준

#### 데이터통신, 네트워크에서의 표준화 기구, 단체
##### ITU
* UN 산하기관, 3개의 주요 섹션(ITU-R,T,D) 으로 구성. 
* 이중 ITU-T(Telecommunication)에서 전송, 교환, 신호방법등에 대한 표준 권고중 
* (직접적인 연관성으로는 V, X series 있음)
* 4개의 클래스로 회원구성됨 -> Government members(정부기관), Sector members(제조사), Associate members(연구그룹), Regulatory agencies(규제기관 (FCC등))

##### ISO - International Standard Organization
* 국제적인 표준기구
* 통신관련 위원회로 TC(Techical Commitee) 97 존재
* OSI를 제정했음

##### ANSI - American National Standard Institute
* 미국의 표준 제정기구
* IEEE, EIA와 함께 표준 제정

##### EIA - Electronic Industries Association
* RS-232, RS-449 규격 제정

##### NIST - National Institute Standard and Technology
* 미연방정부가 구입하는 장비에 대한 정보처리 표준안(FIPS) 발간
* DES 알고리즘 제정

