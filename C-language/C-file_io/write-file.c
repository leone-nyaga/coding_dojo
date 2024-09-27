#include "main.h"

/**
 * createAndWriteFile - Creates and writes to a file
 * @filename: name of the file
 * @text: text to be written
 * Return: void
 */
void createAndWriteFile(const char *filename, const char *text)
{
	/* opens file in write mode */
	FILE *file = fopen(filename, "w");

	/* checks if file is opened successfully */
	if (file == NULL) 
	{
		perror("Error opening file");
		return;
	}

	/* write text to file */
	fprintf(file, "%s", text);

	/* closes a file */
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
