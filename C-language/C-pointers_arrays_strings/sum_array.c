#include "main.h"

/**
 * sum_array - Finds the sum of numbers in an array
 * @arr: Array of integers
 * @size: Size of array
 *
 * Return: The sum of integers in an Array
 */

int sum_array(int arr[], int size)
{
	int sum = 0;
	int i;

	for (i = 0; i < size; i++)
	{
		sum = sum + arr[i];
	}

	return (sum);
}

/**
 * main - Entry point
 *
 * Return: 0
 */

int main(void)
{
	int arr[] = {1, 3, 4, 7, 9};
	int result = sum_array(arr, 5);

	printf("Sum = %d\n", result);

	return (0);
}
