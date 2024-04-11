#include "main.h"

/**
 * printArray - Prints elements of an integer array
 * @arr: Array to be printed
 * @size: size of array
 */

void printArray(int arr[], int size)

{
	int i;
	for(i = 0; i < size; i++)
	{
		printf("%d\n", arr[i]);
	}
}

/**
 * main - Entry point
 */

int main(void)
{
	int numbers[] = {1, 2, 3, 4, 5};

	printArray(numbers, sizeof(numbers) / sizeof(numbers[0]));
	return (0);
}
