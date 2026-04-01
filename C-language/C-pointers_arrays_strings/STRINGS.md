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


