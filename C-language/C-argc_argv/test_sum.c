#include "main.h"

/**
 * main - Entry point
 * @argc: Number of arguments
 * @argv: Array of arguments
 *
 * Return: 0
 */
int main(int argc, char *argv[])
{
	int sum = 0, i;

	for (i = 1; i < argc; i++)
	{
		sum = sum + str_to_int(argv[i]);
	}
	printf("%d\n", sum);

	return (0);
}
