#include "main.h"

void _puts(char *str)
{
	while(*str != '\0')
	{
		putchar(*str);
		str++;
	}
	putchar('\n');
}

int main(void)
{
	char sng[] = "Hello Friend";
	_puts(sng);

	return (0);
}
