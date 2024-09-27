#include "main.h"

/**
 * createFile - function to create a file
 * @filename: name of file to be created
 *
 * Return: void
 */

void createFile(const char *filename)
{
	/* Opens file in write mode */
	FILE *file = fopen(filename, "w");

	/* Checks if ile was opened successfully */
	if (file == NULL)
	{
		perror("ERROR CREATING FILE");
		return;
	}

	/* closes a file */
	fclose(file);

	printf("File '%s' opened successfully\n", filename);
}

/**
 * main - entry point
 *
 * Return: 0
 */

int main(void)
{
	createFile("hello.txt");
	return (0);
}
