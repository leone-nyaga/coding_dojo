#include "main.h"

/**
 * minMax - Function that finds the maximum and minimum values in an array.
 * @arr: array of integers.
 * @min: the minimum integer
 * @max: the maximum integer
 * @len: length of array.
 */
void minMax(int arr[], int *min, int *max, int len)
{
	int i;

	if (len <= 0)
	{
		return;
	}

	*min = arr[0];
	*max = arr[0];

	for (i = 0; i < len; i++)
	{
		if (arr[i] < *min)
		{
			*min = arr[i];
		}
		if (arr[i] > *max)
		{
			*max = arr[i];
		}
	}
}

/**
 * main - Entry point
 *
 * Return: 0
 */
int main(void)
{
	int data[] = {10, 5, 70, 99, 89, 1};
	int min, max, lenght;

	lenght = 6;
	minMax(data, &min, &max, lenght);

	printf("Min: %d\n", min);
	printf("Max: %d\n", max);

	return (0);
}
