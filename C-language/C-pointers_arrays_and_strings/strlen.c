#include "main.h"

int _strlen(char *s)
{
	int length = 0;

	while(*s != '\0')
	{
		length++;
		s++;
	}
	return length;
}

int main(void)
{
	char *str;
	int len;

	str = "TThis is a string";
	len = _strlen(str);
	printf("%d\n", len);

	return (0);
}
