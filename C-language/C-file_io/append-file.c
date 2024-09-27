#include "main.h"

/**
 * appendToFile - Function that appends to a file
 * @filename: pointer to filename
 * @text: pointer to the text being appended
 * Return: 0
 */

void appendToFile(const char *filename, const char *text)
{
	/* Opens file in append mode */
	FILE *file = fopen(filename, "a");

	/* check if file is opened successfully */
	if (file == NULL)
	{
		perror("Error in opening file");
		return;
	}

	/* Appends to a file */
	fprintf(file, "%s", text);

	/* close file */
	fclose(file);

	printf("Text appended to file '%s' successfully.\n", filename);
}

/**
 * main - Entry point
 *
 * Return: 0
 */
int main(void)
{
	appendToFile("hello.txt", "/nThis is an appended text");
	return(0);
}
