## 에러발생
========================

### 개요
* 학과 커리큘럼 `영상처리(Image processing)`에서 'openCV로 배우는 영상 처리 및 응용(정성환 외 1명)'의 실습예제 5.2.1 수행중 에러발생
* 현상: split() 도중 프로그램 종료 (런타임 에러)

### 경과
* 코드리딩 3회 이상 수행
* 레퍼런스 상으로도 문제 없는 코드 (컴파일러, 인텔리센스 모두 이상 없음)
* 교수님께 여쭤본 결과, 코드 상으로는 문제 없고, <b>교수님 노트북에서는 정상 실행</b>됨을 확인함
* 교수님 노트북과 대조중 속성(.props)에서 차이를 발견, 해당부분을 확인해보라는 피드백 주심

### 결과
* 과제 수행용으로 만든 opencv_Homework 프로젝트에서는 동일 코드가 정상실행 됨을 확인
* props 설정 수정을 시도했으나, 설정 자체가 많이 꼬인 듯 함
* 새 프로젝트를 만들고, opencv_Homework의 props 파일을 로드해 실행해보니 정상 동작함

### 결론
* 라이브러리 추가 할 때, 무언가가 잘못되면, 컴파일이 되더라도 특정기능이 오작동 할 수 있다.
* 코드상의 오류가 없을때, 계속해서 비정상적 종료가 발생하면 속성값도 검토해 봐야 한다.

### 코드
```cpp
    #include <opencv2/opencv.hpp>
    #include <iostream>
    using namespace std;
    using namespace cv;

	Mat ch0(3, 4, CV_8U, Scalar(10));
	Mat ch1(3, 4, CV_8U, Scalar(20));
	Mat ch2(3, 4, CV_8U, Scalar(30));

	Mat bgr_arr[] = { ch0, ch1, ch2 };
	Mat bgr;
	merge(bgr_arr, 3, bgr);

	vector<Mat> bgr_vec;
	//Mat bgr_vec[3];
	split(bgr, bgr_vec);

	cout << "[ch0] = " << endl << ch0 << endl;
	cout << "[ch1] = " << endl << ch1 << endl;
	cout << "[ch2] = " << endl << ch2 << endl;

	cout << "[bgr] = " << endl << bgr << endl << endl;
	cout << "[bgr_vec[0]] = " << endl << bgr_vec[0] << endl;
	cout << "[bgr_vec[1]] = " << endl << bgr_vec[1] << endl;
	cout << "[bgr_vec[2]] = " << endl << bgr_vec[2] << endl;
```