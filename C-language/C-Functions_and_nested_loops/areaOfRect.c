#include "main1.h"

int areaOfRect(int length, int width)
{
	int area;
	area = length * width;
	return area;
}

int main(void)
{
	int a = 50;
	int b = 25;
	int area = areaOfRect(a, b);
	printf("%d\n", area);
	return (0);
}
