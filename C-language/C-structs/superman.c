#include "main.h"

/**
 * superman - Displays information on the hero
 * @superman: the hero
 */

void superman(supes superman)
{
	printf("Name: %s\n", superman.name);
	printf("Power: %d\n", superman.age);
	printf("City: %s\n", superman.homeground);
}

/**
 * main - Entry point
 *
 * Return: 0
 */
int main(void)
{
	supes clark = {"Clark Kent", 35, "Metropolis"};

	superman(clark);

	return (0);
}
