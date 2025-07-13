#include <stdio.h>

/**
 * main - Entry point
 *
 * Return: 0
 */

#include <stdio.h>

int main(void)
{
    int i = 0;

    /* Print digits 0-9 */
    while (i < 10)
    {
        putchar(i + '0'); /*convert 0-9 to '0'-'9'*/
        i++;
    }

    /* Print letters a-f */
    i = 0;
    while (i < 6)
    {
        putchar(i + 'a'); /* convert 0-5 to 'a'-'f' */
        i++;
    }

    putchar('\n');

    return 0;
}

