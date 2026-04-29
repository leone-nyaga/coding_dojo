#include "main.h"

/**
 * readFile - Function that reads content of a file
 * @filename: name of the file
 * @mode: the set mode
 *
 * Return: pointer to the file, NULL if error
 */

FILE *readFile(const char *filename, const char *mode)
{
	FILE *fptr = fopen(filename, mode);

	if (filename == NULL)
	{
		perror("Error opening File!");
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
	char line[256];
	FILE *file = readFile("zen.txt", "r");

	if (file == NULL)
	{
		perror("Error opening File");
		return (1);
	}


	while (fgets(line, sizeof(line), file) != NULL)
	{
		printf("%s", line);
	}

	fclose(file);

	return (0);
}
