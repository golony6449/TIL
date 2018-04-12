## calcHist
=====================
### 개요
* 히스토그램 작성을 위한 값 계산 함수

### 형태
`calcHist(Mat *img, int nimgs, const int *channels, InputArray mask, OutputArray hist, int dims, const int *histSize, const float **ranges)`
* img : 히스토그램을 계산할 이미지 배열
* nimgs: 이미지 갯수
* channels: 히스토그램을 계산할 채널 (배열)   ex) 2장의 이미지에서 첫 이미지의 B, 두번째의 G를 계산하려면? ==> { 0, 4 }
* mask: 히스토그램을 계산할 범위
* hist: 히스토그램 값을 저장할 Mat
* dims: 계산 결과의 차원 수
* histSize: 히스토그램의 계급수 (배열)
* range: 계급의 범위(시작값, 최대값) (배열)

### 예제
```cpp
#include <opencv2/opencv.hpp>
#include <iostream>
using namespace cv;
using namespace std;

void calc_Histo(const Mat& img, Mat& hist, int bins, int range_max = 256) {
	int histSize[] = { bins };
	float range[] = { 0, (float)range_max };
	int channels[] = { 0 };
	const float* ranges[] = { range };

	//cout << hist.dims << endl;
	calcHist(&img, 1, channels, Mat(), hist, 1, histSize, ranges);
}

void draw_histo(Mat hist, Mat &hist_img, Size size = Size(256, 200)) {
	hist_img = Mat(size, CV_8U, Scalar(255));
	float bin = (float)hist_img.cols / hist.rows; //계급 너비 계산
	normalize(hist, hist, 0, hist_img.rows, NORM_MINMAX);

	//cout << hist << endl;

	for (int i = 0; i < hist.rows; i++) {
		float start_x = i * bin;
		float end_x = (i + 1) * bin;
		Point2f pt1(start_x, 0);
		Point2f pt2(end_x, hist.at<float>(i));

		if (pt2.y > 0)
			rectangle(hist_img, pt1, pt2, Scalar(0), -1);

	}
	flip(hist_img, hist_img, 0);
}

void first() {
	Mat image = imread("img.jpg", CV_LOAD_IMAGE_GRAYSCALE);
	CV_Assert(!image.empty());

	Mat hist, hist_image;

	calc_Histo(image, hist, 256);
	//cout << hist.rows << "  " << hist.cols << endl;
	draw_histo(hist, hist_image);

	imshow("histo", hist_image);
	imshow("결과", image);
	waitKey();
}
```

### 참고자료
* http://swprog.tistory.com/entry/OpenCV-histogram