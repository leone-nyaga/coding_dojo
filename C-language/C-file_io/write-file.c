#include "main.h"

/**
 * createAndWriteFile - Creates and writes to a file
 * @filename: name of the file
 * @text: text to be written
 * Return: 0
 */
void createAndWriteFile(const char *filename, const char *text)
{
	FILE *file = fopen(filename, "w");
	if (file == NULL) 
	{
		perror("Error opening file");
		return;
	}

	fprintf(file, "%s", text);
	fclose(file);
	printf("File '%s' created and written to successfully.\n", filename);
}

/*
 * main - entry point
 *
 * Return: 0
 */

int main(void)
{
	createAndWriteFile("hello.txt", "Hello, world!");
	return (0);
}
