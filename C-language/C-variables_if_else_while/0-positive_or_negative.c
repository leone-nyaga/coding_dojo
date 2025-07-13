#include <stdlib.h>
#include <time.h>
#include <stdio.h>
/**
 * main - entry point
 *
 * Return: Zero
 */
int main(void)
{
	int n;

	srand(time(0));
	n = rand() - RAND_MAX / 2;
	
	if (n > 0) 
	{
		printf("is positive\n");
	}
	else if (n == 0)
	{
		printf("is 0\n");
	}
	else
	{
		printf("is negative\n");
	}
	return (0);
}
