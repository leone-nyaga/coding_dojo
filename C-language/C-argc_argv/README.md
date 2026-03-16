# Command Line Arguments in C

In any C program, there may be multiple functions, but the main() function remains the entry point from where the execution starts.
While the other functions may have one or more arguments and a return type, the main() function is generally written with no arguments.
The main() function also has a return value of "0".

```main
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
