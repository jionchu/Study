#include <opencv2/opencv.hpp>
#include <iostream>

using namespace cv;
using namespace std;

int main() {
	Mat gray_image, color_image;

	// 0 on the 2nd parameter means read image in grayscale
	gray_image = imread("lena.jpg", 0);

	// blank 2nd parameter means 1, which means read image in colors
	color_image = imread("lena.jpg");

	imshow("gray image", gray_image);
	imshow("color image", color_image);

	waitKey(30000);
	return 0;
}
