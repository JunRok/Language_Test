#include<stdio.h>
#define PI 3.141592
double cal_area(double x);

int main()
{
	double radius;
	printf("원의 반지름을 입력하시오 : ");
	scanf("%lf", &radius);

	double area = cal_area(radius);
	printf("원의 면적은 %lf입니다.\n", area);

	return 0;
}

double cal_area(double x)
{
	return x * x * PI;
}