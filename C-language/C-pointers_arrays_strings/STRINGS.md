# STRINGS

A **string in C** is a one-dimensional array of char type, with the last character in the array being a "null character" represented by '\0'. Thus, a string in C can be defined as a null-terminated sequence of char type values.

## Creating a String in C

Let us create a string "Hello". It comprises five char values. In C, the literal representation of a char type uses single quote symbols such as 'H'. These five alphabets put inside single quotes, followed by a null character represented by '\0' are assigned to an array of char types. The size of the array is five characters plus the null character six.

```c
char greeting[6] = {'H', 'e', 'l', 'l', 'o', '\0'};
```

If the string is not terminated by "\0", it results in unpredictable behavior.

+ **Note**: The length of the string doesnt include the null character. The library function strlen() returns the length of this string as 5.

## Loop Through a String

You can loop through a string (character array) to access and manipulate each character of the string using the for loop or any other loop statements.

```c
#include <stdio.h>
#include <string.h>

int main (){

   char greeting[] = {'H', 'e', 'l', 'l', 'o', '\0'};

   for (int i = 0; i < 5; i++) {
      printf("%c", greeting[i]);
   }

   return 0;
}
```

The output:

```bash
Hello
```

## Printing a String (Using %s Format Specifier)

C provides a format specifier **"%s"** which is used to print a string when you're using functions like printf() or fprintf() functions.

### Example

The "%s" specifier tells the function to iterate through the array, until it encounters the null terminator (\0) and printing each character. This effectively prints the entire string represented by the character array without having to use a loop.

```c
#include <stdio.h>

int main (){

   char greeting[] = {'H', 'e', 'l', 'l', 'o', '\0'};
   printf("Greeting message: %s\n", greeting );

   return 0;
}
```

The output:

```bash
Greeting message: Hello
```

You can declare an oversized array and assign less number of characters, to which the C compiler has no issues. However, if the size is less than the characters in the initialization, you may get garbage values in the output.

## Using Pointers to Access Strings

A pointer can point to the first character of a string, and pointer arithmetic can be used to navigate through the string.

```c
char str[] = "Pointers in C";
char *ptr = str;  // Pointer to the first character

while (*ptr != '\0') {
    printf("%c", *ptr);
    ptr++;  // Move to the next character
}
```

This code prints each character of the string by dereferencing the pointer.

### How to Work with Strings and Pointers in C

1. Accessing String Elements with Pointers

You can use pointers to access individual characters in a string:

```c
char str[] = "Example";
char *ptr = str;

for (int i = 0; ptr[i] != '\0'; i++) {
    printf("%c", ptr[i]);
}
```

2. Modifying Strings with Pointers

Pointers can also be used to modify the contents of a string:

```c
char str[] = "Hello";
char *ptr = str;

ptr[0] = 'M';
printf("%s", str);  // Outputs "Mello"
```

3. Passing Strings to Functions Using Pointers

When passing strings to functions, pointers are used to avoid copying the entire array:

```c
void printString(char *str) {
    while (*str != '\0') {
        printf("%c", *str);
        str++;
    }
}

int main() {
    char msg[] = "Hello, Pointers!";
    printString(msg);
    return 0;
}
```

## String Input Using gets() and fgets() Functions

To accept a string input with whitespaces in between, we should use the gets() function. It is called an unformatted console input function, defined in the "stdio.h" header file.

### Using gets()

```c
#include <stdio.h>
#include <string.h>

int main(){

   char name[20];

   printf("Enter a name:\n");
   gets(name);

   printf("You entered: \n");
   printf("%s", name);

   return 0;
}
```

output

```bash
Enter a name:
Sachin Tendulkar

You entered: 
Sachin Tendulkar
```

In newer versions of C, gets() has been deprecated. It is potentially a dangerous function because it doesnt perform bound checks and may result in buffer overflow.

Instead, it is advised to use the fgets() function.

```c
fgets(char arr[], size, stream);
```

Parameters:

+ ```arr```: the character array (buffer) where the string will be stored.

+ ```size```: maximum number of characters to read (including the null \0).

+ ```stream```: input source (like stdin or a file pointer).

### Example

```c
#include <stdio.h>
#include <string.h>

int main(){

   char name[20];

   printf("Enter a name:\n");
   fgets(name, sizeof(name), stdin);

   printf("You entered: \n");
   printf("%s", name);

   return 0;
}
```

The ouput:

```bash
Enter a name:
Virat Kohli

You entered: 
Virat Kohli
```

## Scanf

```scanf``` is another standard input function in C, but it works quite differently from fgets.

Example

```c
#include <stdio.h>

int main() {
    int age;
    printf("Enter your age: ");
    scanf("%d", &age);

    printf("You are %d years old\n", age);
    return 0;
}
```

Reading strings

```c
char name[50];
scanf("%s", name);
```

### Key differences from fgets

+ ```scanf("%s", name)``` stops at whitespace (so it won’t read full sentences)

+ ```fgets()``` reads a whole line, including spaces

+ ```scanf``` can be unsafe if you don’t limit input size

## Printing String Using puts() and fputs() Functions

We have been using printf() function with %s specifier to print a string. We can also use puts() function (deprecated in C11 and C17 versions) or fputs() function as an alternative.

Example

```c
#include <stdio.h>
#include <string.h>

int main (){

   char name[20] = "Rakesh Sharma";

   printf("With puts(): \n");
   puts(name);

   printf("With fputs(): \n");
   fputs(name, stdout);

   return 0;
}
```

output

```c
With puts(): 
Harbhajan Singh

With fputs(): 
Harbhajan Singh
```

## String Operations

Located in the ```string.h``` file

1. strcpy

strcpy() copies one C string into another.

```c
strcpy(destination, source);
```

Example

```c
#include <stdio.h>
#include <string.h>

int main() {
    char source[] = "Beautiful";
    char dest[20];

    strcpy(dest, source);

    printf("%s\n", dest);
}
```

```c
#include <stdio.h>
#include <string.h>

char *string_copy(char *destined, char *sourced)
{
    strcpy(destined, sourced);
    return (destined);
}
int main() {
    char str1[10] = "Hello!";
    char str2[10];
    string_copy(str2, str1);
    printf("%s\n", str2);
    
    return 0;
}
```

Output:

```bash
Beautiful is better than ugly.
```
What the function looks like

```c
char *strcpy(char *dest, const char *src)
{
    int i = 0;

    while (src[i] != '\0')
    {
        dest[i] = src[i];
        i++;
    }
    dest[i] = '\0';

    return dest;
}
```

The destination array must be large enough.

2. String length

Is a function from the standard library used to find the length of a string (number of characters before the null terminator '\0').

syntax

```c
size_t strlen(const char *str);
```

Example

```c
#include <stdio.h>
#include <string.h>

int main() {
    char str[] = "Hello";
    int length = strlen(str);

    printf("Length of string: %d\n", length);
    return 0;
}
```

Output

```bash
Length of string: 5
```

NB: Return type is ```size_t``` (an unsigned integer type).

How it looks behind the scene:

```c
#include <stdio.h>

size_t strlen(const char *str)
{
    int i = 0;

    while (*str != '\0')
    {
        i++;
        str++;
    }
    return i;
}
```

3. String Concatenate

The ```strcat``` (string concatenate) function is used to append one string to the end of another.

Syntax:

```c
char *strcat(char *destination, const char *source);
```

+ ```destination```: String to append to.

```c
char dest[50] = "Hello ";
```

+ ```source```: String being appended to.

```c
char src[] = "World";
```

```Take string in source and attach it at the end of destination```

Example

```c
#include <stdio.h>
#include <string.h>

int main() {
    char greeting[20] = "Hello"; // Large enough to fit "Hello" + " World"
    char addition[] = " World";

    // Appends " World" to "Hello"
    strcat(greeting, addition);

    printf("%s", greeting); // Output: Hello World
    return 0;
}
```

how it looks behind the scenes

```c
#include <stdio.h>

char *_strcat(char *dest, const char *src)
{
    int i = 0;
    int j = 0;
    
    while (dest[i] != '\0')
    {
        i++;
    }
    while (src[j] != '\0')
    {
        dest[i] = src[j];
        i++;
        j++;
    }
    dest[i] = '\0';
    
    return (dest);
}

int main()
{
    char str1[90] = "Beautiful is ";
    char str2[90] = "better than ugly!";
    
    _strcat(str1, str2);
    
    printf("%s\n", str1);
    
    return (0);
}
```

4. String Compare

```strcmp()``` compares two strings.

Syntax

```c
int strcmp(const char *s1, const char *s2);
```


