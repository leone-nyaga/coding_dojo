#include "main.h"

/**
 * readFile - function to read file
 * @filename: pointer to the filename
 * Return: void
 */
void readFile(const char *filename)
{
	FILE *file = fopen(filename, "r");

	/* check if file opens successfully */
	if (file == NULL)
	{
		perror("Error opening file");
		return;
	}
	
	/* Buffer that stores each line from the file */
	char buffer[200];

	/* reads file line by line and prints the content */
	while (fgets(buffer, sizeof(buffer), file) != NULL)
	{
		printf("%s", buffer);
	}
	
	/* closes a file */
	fclose(file);

	printf("\nFile '%s' read successfully.\n", filename);
}

/**
 * main - entry point
 *
 * Return: 0
 */
int main(void)
{
	readFile("hello.txt");

	return (0);
}
