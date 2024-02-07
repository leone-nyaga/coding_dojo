#include <stdlib.h>
#include <time.h>
#include <stdio.h>

/**
 * main - entry point
 * description - checks the last digit
 * Return: 0(positive)
 */

int main(void)
{
	int n;

	srand(time(0));
	n = rand() - RAND_MAX / 2;
	if (n % 10 > 5)
		printf("%d and is greater than 5\n", n);
	else if (n % 10 == 0)
		printf("%d and is zero\n", n);
	else
		printf("%d and is less than 6 and not zero\n", n);

	return (0);
}
