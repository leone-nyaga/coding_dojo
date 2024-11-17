#include "main.h"

int areaOfRect(int *base, int *height)
{
	int area;
	area = (*base) * (*height);
	return area;
}

int main(void)
{
	int base = 10;
	int height = 5;
	int area = areaOfRect(&base, &height);
	printf("The area is %d\n", area);
}
