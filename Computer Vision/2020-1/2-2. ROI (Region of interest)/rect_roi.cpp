#include <opencv2/opencv.hpp>
#include <iostream>

using namespace cv;
using namespace std;

int main() {
	Mat image = imread("lena.jpg");
	Rect rect(100, 30, 300, 400);
	Mat rect_roi = image(rect);

	imshow("rectROI", rect_roi);

	waitKey(0);
	return 0;
}
