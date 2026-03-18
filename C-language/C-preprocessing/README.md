# PREPROCESSING

The C Preprocessor is not a part of the compiler, but is a separate step in the compilation process. In simple terms, a C Preprocessor is just a text substitution tool and it instructs the compiler to do the required pre-processing before the actual compilation. We'll refer to the C Preprocessor as CPP.

In C programming, **preprocessing** is the first step in the compilation of a C code. It occurs before the **tokenization** step. One of the important functions of a preprocessor is to include the **header files** that contain the library functions used in the program. The preprocessor in C also defines the constants and expands the macros.

The preprocessor statements in C are called **directives**. A preprocessor section of the program always appears at the top of the C code. Each preprocessor statement starts with the hash (#) symbol.

## Preprocessor Directives in C

The following table lists down all the important preprocessor directives -

| Directive  | Description                                                          |
| ---------- | -------------------------------------------------------------------- |
| `#define`  | Substitutes a preprocessor macro.                                    |
| `#include` | Inserts a particular header from another file.                       |
| `#undef`   | Undefines a preprocessor macro.                                      |
| `#ifdef`   | Returns true if this macro is defined.                               |
| `#ifndef`  | Returns true if this macro is not defined.                           |
| `#if`      | Tests if a compile-time condition is true.                           |
| `#else`    | The alternative for `#if`.                                           |
| `#elif`    | Combines `#else` and `#if` in one statement.                         |
| `#endif`   | Ends a preprocessor conditional block.                               |
| `#error`   | Prints an error message to stderr.                                   |
| `#pragma`  | Issues special commands to the compiler using a standardized method. |


## Predefined Macros in C

| Macro      | Description                                                        |
| ---------- | ------------------------------------------------------------------ |
| `__DATE__` | The current date as a character literal in `"MMM DD YYYY"` format. |
| `__TIME__` | The current time as a character literal in `"HH:MM:SS"` format.    |
| `__FILE__` | Contains the current filename as a string literal.                 |
| `__LINE__` | Contains the current line number as a decimal constant.            |
| `__STDC__` | Defined as `1` when the compiler complies with the ANSI standard.  |


### Example

Let's try the following example −

```c
#include <stdio.h>

int main(){

   printf("File: %s\n", __FILE__ );
   printf("Date: %s\n", __DATE__ );
   printf("Time: %s\n", __TIME__ );
   printf("Line: %d\n", __LINE__ );
   printf("ANSI: %d\n", __STDC__ );
}
```

Output

```bash
File: main.c
Date: Mar 6 2024
Time: 13:32:30
Line: 8
ANSI: 1
```

## Macros

**Macros** in C are the names given to specific constant values or code statements which are replaced with their value/code before the compilation processor. C Macros are defined using the **#define** preprocessor directive.

**Macros** are useful for code reusability, defining constant values, defining inline functions, and conditional compilations.

The following are the different types of C macros that we are going to cover in this tutorial –

+ Object-like Macros
+ Function-like Macros
+ Chained Macros
+ Variadic Macros
+ Predefined Macros

### Syntax

```c
#define name value
```

### Example of Object-like Macros

```c
#include <stdio.h>

// Defining macros
#define PI 3.14
#define MAX 10

int main() {
   // Printing the values
   printf("Value of PI = %d\n", PI);
   printf("Value of MAX = %d\n", MAX);

   return 0;
}
```

## Function-like Macro

To define a function-like macro, you use the same "#define" directive, but you put a pair of parentheses immediately after the macro name, with one or more arguments. Such a macro is expanded only when its name appears with a pair of parentheses after it.

When the preprocessor expands such a macro, it incorporates the specified arguments in the replacement text. The function-like macros are often called Macros with parameters (or arguments).

### Syntax

```c
#define macro_name([parameter_list]) replacement_text
```

### Example of Function-like Macros

```c
#include <stdio.h>

#define square(x) ((x) * (x))

int main(){

   int x = 5;
   printf("x: %d \tSquare of x: %d", x, square(x));
   return 0;
}
```

Output

```bash
x: 5 	Square of x: 25
```

### Rules for Defining Function-like Macros

Some rules of defining a function also apply to macros −

+ A macro can be defined without arguments
+ A macro can be defined with a fixed number of arguments
+ A macro can be defined with a variable number of arguments

## Function-like Macros without Arguments

A function-like macro may also be defined without arguments.

### Example

```c
#include <stdio.h>

#define MESSAGE() printf("Hello World");

int main() {

   int x = 5;
   MESSAGE();
   return 0;
}
```

output

```bash
Hello World
```

## Chained Macros

When we have a macro nested inside another macro, they are called Chained Macros.

```c
#include <stdio.h>

#define PI 3.142
#define CIRCUMFERENCE(x) (2*PI*x)

int main(){

   int x = 5;
   printf("Circumference of a circle with radius %d is %f", x, CIRCUMFERENCE(x));
   return 0;
}
```

output

```bash
Circumference of a circle with radius 5 is 31.420000
```
