#include <stdio.h>

/**
 * main - Prints a greeting with the first command-line argument
 * @argc - argument count
 * @argv - argument vector
 * Return 0
 */

int main(int argc, char *argv[])
{
	(void) argc;
	printf("Hello %s\n", argv[1]);
	return (0);
}
