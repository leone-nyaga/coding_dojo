#include "main.h"

int main(void)
{
	int age = 21, *pAge = &age;

	/* both will print same adress and also share the same value */
	printf("Address of age: %p\n", (void *)&age);
	printf("Value of pAge: %p\n", (void *)pAge);

	/* lets see the size of variable and pointer */
	printf("Size of Age: %lu bytes.\n", (unsigned long)sizeof(age));/* 4 bytes coz it's int */
	printf("Size of pAge: %lu bytes.\n", (unsigned long)sizeof(&age));/* 8 bytes for hexadecimal */

	return (0);

}
