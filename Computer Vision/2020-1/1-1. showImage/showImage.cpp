#include <opencv2/opencv.hpp>
#include <iostream>

using namespace cv;
using namespace std;

int main() {
	int w = 150, h = 100;
	Mat image(h, w, CV_8UC1, Scalar(255));

	// for a multi-channel image
	// Mat image(h, w, CV_8UC3, Scalar(255,0,0));
	
	cout << "SIze: " << image.size().height << "," << image.size().width << endl;
	namedWindow("image");
	imshow("image", image);

	waitKey(0);
	return 0;
}
