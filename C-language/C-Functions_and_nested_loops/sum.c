#include "main1.h"

int sum(int a, int b)
{
	int result = a + b;
	return (result);
}

int main(void)
{
	int c = 45, d = 55, total;
	
	total= sum(c, d);
	printf("the sum is %d\n", total);
	return (0);
}
