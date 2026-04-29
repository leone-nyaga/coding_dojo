#include "main.h"

/**
 * writeFile - Function to write data into a file
 * @filename: name of file
 * @mode: mode
 *
 * Return: pointer to file or NULL if there's an error
 */
FILE *writeFile(const char *filename, const char *mode)
{
	FILE *fptr;

	fptr = fopen(filename, mode);

	if (filename == NULL)
	{
		perror("Error opening file");
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
	const char *zen;

	file = fopen("zen.txt", "w");

	if (file == NULL)
	{
		perror("Error opening file");
		return (1);
	}

	zen =
		"Beautiful is better than ugly.\n"
		"Explicit is better than implicit.\n"
		"Simple is better than complex.\n"
		"Complex is better than complicated.\n"
		"Flat is better than nested.\n"
		"Sparse is better than dense.\n"
		"Readability counts.\n"
		"Special cases aren't special enough to break the rules.\n"
		"Although practicality beats purity.\n"
		"Errors should never pass silently.\n";

	fprintf(file, "%s", zen);

	fclose(file);

	return (0);
}
