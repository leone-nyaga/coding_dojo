#include "main.h"

void print_rev(char *s)
{
	int length = 0;

	while (*s != '\0')
	{
		length++;
		s++;
	}

	for (int i = length - 1; i >= 0; i--)
	{
		putchar(s[i]);
	}
	putchar('\n');
}

int main(void)
{
	char sentence[] = "Hello guys, I am learning C";
	print_rev(sentence);

	return (0);
}
