#include "main.h"

/**
 * createFile - function to create a file
 * @filename: name of file to be created
 *
 * Return: 0
 */

void createFile(const char *filename)
{
	FILE *file = fopen(filename, "w");

	if (file == NULL)
	{
		perror("ERROR CREATING FILE");
		return;
	}

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
