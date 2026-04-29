#include "main.h"

/**
 * openFile - Function that opens a file or
 * creates a file if it doesn't exist
 * @filename: name of the file
 * @mode: Mode in which the file will be opened
 *
 * Return: pointer to file or Null if it fails
 */
FILE *openFile(const char *filename, const char *mode)
{
	FILE *fptr = fopen(filename, mode);

	if (fptr == NULL)
	{
		printf("Error: could not open %s\n", filename);
	}
	else
	{
		printf("Successfully opened %s\n", filename);
	}

	return (fptr);
}

/**
 * main - Entry point
 *
 * Return: 0
 */
int main(void)
{
	FILE *file;

	file = openFile("zen.txt", "w");

	if (file == NULL)
	{
		return (1);
	}

	fclose(file);

	return (0);
}
