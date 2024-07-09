#include "main.h"

void swap_int(int *a, int *b)
{
	int temp = *a;
	*a = *b;
	*b = temp;
}

int main(void)
{
	int a = 98;
	int b = 42;

	printf("The former value of a=%d, b=%d\n", a, b);
	swap_int(&a, &b);
	printf("The new value is, a=%d, b=%d\n", a, b);

	return (0);
}
