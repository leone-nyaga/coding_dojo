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


