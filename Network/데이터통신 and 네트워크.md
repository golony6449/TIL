# 데이터통신과 네트워크
* 데이터통신과 네트워크 - 한빛미디어
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

### 인터넷의 표준화
* 유저들의 다양한 요구 증가, 새로운 서비스의 등장으로 인터넷 관련 기술의 수정은 불가피
* 관련 회사들의 주도로 인터넷 관련기구 등장 -> 표준안 제정

* ISO, IAN(Internet Architecture Board), IESG(Internet Engineering Steering Group), IETF(Internet Engineering Task Force)

#### IETF
* 변화하는 네트워크 환경에 따라 새로운 기술 제시, 인터넷 표준안 제정을 휘한 기술 위원회
* 여려개의 워킹그룹(WG) -> 영역 형태로 구성
* WG 단위로 표준 and 절차에 관한 협의 진행

##### IETF의 표준화 절차
* 인터넷 문서 유형: 인터넷 초안(internet-draft), RFC(Request Of Comment)

* 인터넷 초안 - 작업중인 문서ㅡ 형식적 X, 언제든지 변경 삭제 가능성 있음
* RFC - IAB의 공문서 간행물. 출판된 RFC는 삭제 변경 X

##### RFC
* 인터넷 연구, 개발 공통체의 작업문서
* 인터넷 상의 기술구현에 요구되는 상세절차, 기본틀을 제공하는 기술관련 내용으로 구성됨
* 각각의 문서마다 중복, 수정 되지 않는 RFC 넘버 부여

* 상태: 4가지 상태로 분류 표준 트랙(Standard Track), 정보관련 상태(Informational), 실험관련 상태(Experimental), 개발과정 및 역사관련 상태(Historic)

* 표준 트랙: 제안단계 표준안(proposed standard) -> 표준화 전단계(drafted standard), 표준화(standard)
* 제안단계 표준안: 완전한 명세서 형태. 6개월 ~ 2년 내 다음단계 진행 or 재발행
* 표준화 전단계: 독립적, 상호동작 구현 가능. 제한된 실험 수행중
* 표준안: 실제 표준안. 신뢰성 확인 됨

### 유무선 네트워크의 발전과 변화
* internetworking: 서로 다른 종류의 네트워크를 연결시키고, 하나의 데이터 통신의 기준을 둬 다양한 하드웨어 기술의 결합을 가능케 함

* 인터넷의 기원: ARPANET(미 국방성 - 관련기관 간의 정보 공유를 위한 네트워크)
* 이후 미 국방성에서 TCP/IP 사용을 권장 -> TCP/IP를 사용하는 인터넷 등장

#### Internet, Networking 기술의 발전
* ARPANET 등장 -> TCP/IP 개발 -> 이더넷 아이디어 등장 -> TCP, IP로 분리됨 -> TCP/IP 표준지정됨 -> DNS 등장 -> WWW 등장

#### Wireless Networking의 발전
##### 1세대
* AMPS, NAMPS, ETACS

##### 2세대
* CDMA (Code Division Multiple Access)
* GSM(Global System for Mobile)
* TDMA

##### 2.5세대
* GPRS, HS CSD, EDGE

##### 3세대
* WCDMA(Wide band CDMA)
* 3세대 부터 데이터 전송단위가 Mb로 변화

##### 3.5세대
* Wibro, WiMax

##### 4세대
* OFDMA, MIMO, HD
* WiMAX / UWB
* IMT-Advanced
* Wibro-evolution

##### WLAN
* 801.11b -> a -> g -> n

#### IPv6
* IPv4의 주소길이를 4배 확장
* 초창기 IPv5의 규격검토 후, 보안, 자동 네트워킹 기능을 보완한 표준규격(RFC2460)

* 기존의 v4와 달리,단순화한 헤더정보를 제공을 위해 여러개의 독립된 헤더형태가 존재. 이를 기능에 맞도록 적절히 선택해 사용
* -> 전송되는 정보량 감소, 패킷 처리 Delay 감소

