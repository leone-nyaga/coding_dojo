#include "main.h"

/**
 * puts_half - prints the second half of a string, followed by a new line
 * @str:the string to print
 */

void puts_half(char *str)
{
    int len = strlen(str);  // Get the length of the string
    int start_index;

    // If the length is even, start from len / 2, else from (len / 2) + 1
    if (len % 2 == 0)
    {
        start_index = len / 2;  // Even length: start from middle
    }
    else
    {
        start_index = (len / 2) + 1;  // Odd length: start just after the middle
    }

    // Print the second half of the string starting from start_index
    for (int i = start_index; str[i] != '\0'; i++)
    {
        _putchar(str[i]);  // Print character
    }
    _putchar('\n');  // Print a new line after the second half
}


/**
 * main - check the code
 *
 * Return: Always 0.
 */
int main(void)
{
    char *str;

    str = "0123456789";
    puts_half(str);
    return (0);
}
