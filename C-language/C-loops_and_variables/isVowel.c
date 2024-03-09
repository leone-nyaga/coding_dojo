#include  <stdio.h>

/**
 * main - Entry point
 * Description - Checks if is a vowel
 * Return: 0 if success
 */

int main(void)
{
	char vowel;

	printf("Please enter a Letter...\n");
	scanf("%c", &vowel);

	switch (vowel)
	{
		case 'A':
		case 'a':
			printf("A\n");
			printf("That's a vowel\n");
			break;

		case 'E':
		case 'e':
			printf("E\n");
			printf("That's a vowel\n");
			break;

		case 'I':
		case 'i':
			printf("I\n");
			printf("That's a vowel\n");
			break;

		case 'O':
		case 'o':
			printf("O\n");
			printf("That's a vowel\n");
			break;

		case 'U':
		case 'u':
			printf("U\n");
			printf("That's a vowel\n");
			break;

		default:
			printf("That's a Consonant\n");
			break;
	}

	return (0);
}


