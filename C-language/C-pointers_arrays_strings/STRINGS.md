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


