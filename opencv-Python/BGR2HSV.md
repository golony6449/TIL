## OpenCV-Python
### opencv-python-tutroals.readthedocs.io/en/latest/index.html
======================================

### 이미지
* cv2.waitKey(value): 키 입력을 기다림 (ms 단위) (0: 무한)

### 비디오 캡처 (From Camera) 및 처리
* VideoCapture 객체 사용 (para: 카메라 장치 넘버) (장치 넘버 대신 path -> 파일 로드)
* obj.read()로 프레임 단위 캡처 -> bool, frame 반환
* 객체가 초기화되지 않은 경우 .isOpen()을 이용해 장치사용여부 확인 뒤, .open()으로 장치 초기화 수행
* obj.get(propertyID)를 이용해 지정된 값, 프리셋 확인 가능
* obj.set(propertyID, value): 특정 프리셋 수치 변경
* (https://docs.opencv.org/2.4/modules/highgui/doc/reading_and_writing_images_and_video.html#videocapture-get)
* 사용후 반드시 `obj.release()` 수행!

### 비디오 저장
* VideoWriter 객체 + imwrite() 함수 사용
* VideoWriter 객체 생성시, 파일명, 코덱, FPS, Size 지정 (코덱: FourCC 형식)
* 사용후 반드시 `obj.release()` 수행

#### FourCC
* 비디오 코덱 지정을 위한 4byte 코드
* http://www.fourcc.org/codecs.php
* fourcc 객체를 만든 뒤, VideoWriter 생성자에 전달

### 그리기
#### 참고
* Thickness = -1 => 채우기 (단 닫혀있는 상태)

#### 직선
1. 그릴 캔버스 생성(np.zeros(가로, 세로, 채널), np.uint8) (2**8 = 256)
2. `cv2.line(캔버스, 시작좌표, 종료좌표, 색상, Thickness)`

#### 사각형
* `cv2.rectangle(캔버스, 시작좌표, 종료좌표, 색상, Thickness)`

#### 원
* `cv2.circle(캔버스, 중심좌표, 반지름, 색상, Thickness)`

#### 다각형(Polygon)
1. 꼭지점 좌표를 np.array로 생성
2. (ROWS, 1, 2) 형태로 크기 조정 (`npArr.reshape(-1, 1, 2)`)
3. `cv2.polylines(캔버스, [npArr], 닫힘여부, 색상, Thickness)`
* cv2.line()으로 모든 좌표를 연결한 것과 같은 효과

#### 글자 삽입
* `cv2.putText(캔버스, 텍스트, 좌표, 폰트, 크기, 색상, [cv2.LINE_AA])`
* 깔끔한 출력을 위해 AA 처리 권장

### 마우스로 그리기
#### openCV의 마우스 이벤트 확인
```python
import cv2
events = [i for i in dir(cv2) if 'EVENT' in i]
print(events)
```

#### 마우스 콜백 함수 정의
* 구체적인 형식이 정해져 있음
```python
def funcName(event, x, y, flags, param):
```

#### 정의한 함수를 콜백함수로 맵핑
`cv2.setMouseCallback(윈도우 이름, 함수명)`