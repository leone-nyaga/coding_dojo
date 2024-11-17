#include "main.h"

char *_strcpy(char *dest, char *src)
{
    int i = 0;

    // Copy each character from src to dest
    while (src[i] != '\0') {
        dest[i] = src[i];  // Copy the current character
        i++;
    }

    // Don't forget to copy the null terminator
    dest[i] = '\0';

    return dest;  // Return the pointer to the destination string
}
/**
 * main - check the code
 *
 * Return: Always 0.
 */
int main(void)
{
    char s1[98];
    char *ptr;

    ptr = _strcpy(s1, "First, solve the problem. Then, write the code\n");
    printf("%s", s1);
    printf("%s", ptr);
    return (0);
}
