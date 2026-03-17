# Command Line Arguments in C

In any C program, there may be multiple functions, but the main() function remains the entry point from where the execution starts.
While the other functions may have one or more arguments and a return type, the main() function is generally written with no arguments.
The main() function also has a return value of "0".

```c
int main(void)
{
    return 0;
}
```

## What are Command Line Arguments?

Instead of invoking the input statement from inside the program, it is possible to pass data from the command line to the main() function when the program is executed. These values are called **command line arguments**.

Command line arguments are important for your program, especially when you want to control your program from outside, instead of hard coding those values inside the code.

Let us suppose you want to write a C program "hello.c" that prints a "hello" message for a user. Instead of reading the name from inside the program with scanf(), we wish to pass the name from the command line as follows −

```c
C:\users\user>hello Leone
```

The string will be used as an argument to the main() function and then the "Hello Leone" message should be displayed.

## argc and argv

To facilitate the main() function to accept arguments from the command line, you should define two arguments in the main() function **argc** and **argv[]**.

**argc** refers to the number of arguments passed and **argv[]** is a pointer array that points to each argument passed to the program.

```c
int main(int argc, char *argv[])
{
	...
	return (0);
}
```

The **argc** argument should always be non-negative. The **argv** argument is an array of character pointers to all the arguments, argv[0] being the name of the program. After that till **"argv [argc - 1]"**, every element is a command-line argument.

Open any text editor and save the following code as "hello.c" −

```c
#include <stdio.h>

int main (int argc, char * argv[]){
   printf("Hello %s", argv[1]);
   return 0;
}
```

The program is expected to fetch the name from argv[1] and use it in the printf() statement.

Compile it and build the excecutable

```bash
C:\Users\user>gcc -c hello.c -o hello.o

C:\Users\user>gcc -o hello.exe hello.o
```

Pass the name as a command line argument −

```bash
C:\Users\user>hello Leone
Hello Leone
```

### Example

```c
#include <stdio.h>

int main (int argc, char *argv[]) {

   if(argc == 2) {
      printf("The argument supplied is %s\n", argv[1]);
   }
   else if(argc > 2) {
      printf("Too many arguments supplied.\n");
   }
   else {
      printf("One argument expected.\n");
   }
}
```

When the above code is compiled and executed with a single argument, it produces the following output −

```bash
$./a.out testing
The argument supplied is testing.
```

When the above code is compiled and executed with two arguments, it produces the following output −

```bash
$./a.out testing1 testing2
Too many arguments supplied.
```

When the above code is compiled and executed without passing any argument, it produces the following output −

```bash
$./a.out
One argument expected
```

It should be noted that **argv[0]** holds the name of the program itself and **argv[1]** is a pointer to the first command line argument supplied, and **(*)argv[n]** is the last argument. If no arguments are supplied, then **argc** will be set at **"1"** and if you pass one argument, then argc is set at **"2"**.

## Void

Sometimes **argc** and **argv** are required by the function signature but not used in the program.

To prevent compiler warnings:

```c
int main(int argc, char *argv[]) {
    (void)argc;
    (void)argv;
    return 0;
}
```

+ ```(void)argc;``` and ```(void)argv;``` explicitly mark the parameters as intentionally unused.

+ This is commonly used to suppress compiler warnings.


## Passing Numeric Arguments from the Command Line

Let us write a C program that reads two command line arguments, and performs the addition of argv[1] and argv[2].

### Example

Start by saving the code below −

```c
#include <stdio.h>

int main (int argc, char * argv[]) {

   int c = argv[1] + argv[2];
   printf("addition: %d", c);
   
   return 0;
}
```

When we try to compile, you get the error message −

```bash
error: invalid operands to binary + (have 'char *' and 'char *')
 int c = argv[1]+argv[2];
         ~~~~~~~~~~~~~~
```

This is because the "+" operator cannot have non-numeric operands.

To solve this issue, we need to use the library function **atoi()** that converts the string representation of a number to an integer.

```c
#include <stdio.h>
#include <stdlib.h>

int main (int argc, char * argv[]) {

   int c = atoi(argv[1]) + atoi(argv[2]);
   printf("addition: %d", c);
   
   return 0;
}
```

Compile and build an executive from "add.c" and run from the command line, passing numeric arguments −

```bash
C:\Users\user>add 10 20
addition: 30
```

### Example

You pass all the command line arguments separated by a space, but if the argument itself has a space, then you can pass such arguments by putting them inside double quotes (" ") or single quotes (' ').

In this example, we will pass a command line argument enclosed inside double quotes −

```c
#include <stdio.h>

int main(int argc, char *argv[]) {

   printf("Program name %s\n", argv[0]);

   if(argc == 2) {
      printf("The argument supplied is %s\n", argv[1]);
   }
   else if(argc > 2) {
      printf("Too many arguments supplied.\n");
   }
   else {
      printf("One argument expected.\n");
   }
}
```

When the above code is compiled and executed with a single argument separated by space but inside double quotes, it produces the following output −

```bash
$./a.out "testing1 testing2"

Program name ./a.out
The argument supplied is testing1 testing2
```


## NB

+ ```argc``` (argument count) represents the number of arguments passed to the program, including the program name itself.

+ ```argv``` (argument vector) is an array of strings (```char *argv[]```) that stores the arguments passed via the command line.

+ ```argv[0]``` always contains the name (or path) used to execute the program.

+ All command-line arguments are passed as strings, even if they look like numbers.

+ To use numeric values, arguments must be converted from strings to integers using functions like ```atoi()``` (from ```stdlib.h```) or by manual conversion.

+ ```argv``` can also be treated as a pointer to pointers (```char **argv```), meaning:

  + ```argv[i]``` is equivalent to ```*(argv + i)```

  + ```argv[i][j]``` accesses individual characters within each argument

+ Always validate input when working with command-line arguments to avoid unexpected behavior.
