#include "main.h"

/**
 * findMid - Finds the integer located in the middle of an array.
 * @arr: Array of integers.
 * @size: Size of the array.
 */

int findMid(int *arr, int size)
{
	if (size == 0)
	{
		return (-1);
	}

	return (arr[size / 2]);
}

/**
 * main - Entry point.
 *
 * Return: 0
 */

int main(void)
{
	int nums[] = {10, 20, 30, 40, 75, 96};
	int size = sizeof(nums) / sizeof(nums[0]);

	int result = findMid(nums, size);

	printf("%d\n", result);

	return (0);
}
