#include "main.h"

/**
 * main - Entry point
 *
 * Return: 0
 */
int main(void)
{
	supes batman;

	strcpy(batman.name, "Bruce Wayne");
	batman.age = 35;
	strcpy(batman.homeground, "Gotham City");

	printf("Hero name: %s, Hero age: %d, Hero home %s\n",
			batman.name,
			batman.age,
			batman.homeground);
	return (0);
}
