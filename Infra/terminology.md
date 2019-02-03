# 용어 (Terminology)

## 인프라

* Immutable Infrastructure: 이미지 기반의 인프라스트럭처, 이미지는 변경불가능하기 때문에 `Immutable`이라 칭하는 듯
* Infrastructure as Code: 인프라 구성을 코드로서 관리, Docker: `Dockerfile`
* Bootstrapping: OS의 시작을 자동화
* Configuration: OS, 미들웨어의 설정을 자동화, Ansible(Python), Puppet
* <b>Orchestration</b>: 여러 서버의 관리를 자동화, Kubernetes
* Continuous Integration: 코드가 추가/수정될 때 마다 테스트 수행 ==> 확실하게 동작하는 코드를 지속적으로 유지, 테스트 자동화 도구(Jenkins, Trevis) 사용
* Coutinuous Delivery: 인프라 환경까지 포함된 테스트를 수행 ==> 제품 환경에 그대로 전개, 지속적인 서비스를 가능하도록 함
* Blue Green Deployment: 현재 동작중인 시스템(Blue), 버전업 이후의 시스템(Green)을 동시에 작동시킨 상태에서 시스템 전환, 문제 발생시 이전 시스템으로 롤백
* 스테이징 환경(Staging Env): CD가 일어나는 환경에서, 릴리즈 전에 확인하는 테스트 환경

