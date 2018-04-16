## filter2D 함수
======================
### 개요
* Conv연산을 수행하는 함수
* Kernel(일종의 필터)을 사용해 연산 수행

### 정의
`filter2D(inputMat, outputMat, <b>depth</b>, kernel);`

### depth
* 출력의 depth 결정
* 입력 Matrix와 동일한 Depth를 사용하면 됨 (-1: 입력과 동일한 depth 값)
* 지원되는 depth 조합
| 입력의 depth | 사용가능한 파라메터(= 출력의 depth) |
|-------------|------------------------------------|
| CV_8U | -1, CV_16S, CV_32F, CV_64F |
| CV_16U, CV_16S | -1, CV_32F, CV_64F |
| CV_32F | -1, CV_32F, CV_64F |
| CV_64F | -1, CV_64F |
 
### 예시
```cpp
    Mat image = imread("...", IMREAD_GRAYSCALE);
    CV_Assert(image.data);
    
	float blurVal[] = {
		1 / 9., 1 / 9., 1 / 9.,
		1 / 9., 1 / 9., 1 / 9.,
		1 / 9., 1 / 9., 1 / 9.,
	};

	float blurVal2[] = {
		1 / 25., 1 / 25., 1 / 25., 1 / 25., 1 / 25.,
		1 / 25., 1 / 25., 1 / 25., 1 / 25., 1 / 25.,
		1 / 25., 1 / 25., 1 / 25., 1 / 25., 1 / 25.,
		1 / 25., 1 / 25., 1 / 25., 1 / 25., 1 / 25.,
		1 / 25., 1 / 25., 1 / 25., 1 / 25., 1 / 25.,
	};

	Mat blurDst, blurDst2;
	Mat blurMask(3, 3, CV_32F, blurVal);
	Mat blurMask2(5, 5, CV_32F, blurVal2);

	filter2D(image, blurDst, CV_32F, blurMask);
	filter2D(image, blurDst2, CV_32F, blurMask2);

	blurDst.convertTo(blurDst, CV_8U);
	blurDst2.convertTo(blurDst2, CV_8U);

	imshow("3x3 blur", blurDst);
	imshow("5x5 blur", blurDst2);
	waitKey();
```

### 참고자료
* https://blog.iwanhae.ga/introduction-to-opencv/
* https://docs.opencv.org/2.4/modules/imgproc/doc/filtering.html#filter2d