## 컴파일러에서의 프론트엔드 and 백엔드
* special thanks to GNUxer
-----------------------------------------
* 사진자료: https://www.cse.iitb.ac.in/grc/intdocs/gcc-basic-info_files/gcc-cgf-fig.png
* 원문: https://www.cse.iitb.ac.in/grc/intdocs/gcc-basic-info.html (fig. 2.1)

### 이해를 돕기위한 웹의 프론트엔드(FE), 백엔드(BE)
* 사용자는 FE를 통해 서버에 정보(html 문서, 각종 Request) 요청
* 서버는 이를 받아들여 BE에서 처리
* 처리, 생성된 자료를 FE로 전송
* 출력

### 프론트엔드 백엔드는 웹에만 있는게 아니였다!
* 컴파일러에도 프론트엔드, 백엔드가 존재
* 컴파일러의 FE에서는 입력받은 소스코드를 파서를 이용해 기계종속적이지 <br>않은</br> 코드를 생성하고 최적화 수행
* 이후 이를 이용해 BE에서 특정 아키텍처(x86, CUDA, ARM 등의 구조, 명령어집합)를 위한 기계어 생성

### 예시 - GCC
* GCC는 백엔드, 프론트엔드 모두를 제공
* 초기에는 Gnu C Compiler로 불림
* 이후 다양한 언어를 프론트엔드에서 제공하고, 다양한 아키텍처를 백엔드에서 지원
* Gnu Compiler Collection으로 불리게 됨