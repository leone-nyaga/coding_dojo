# 0x01-variables_if_else_while

## VARIABLES

A variable is a named storage location in memory that holds a value of a specific type.
You can think of variables as labeled boxes where you store data that your program can manipulate.

### Why use Variables?

+ To store data temporarily.

+ To refer to values by name rather than by memory address.

+ To change data throughout the execution of a program.

## Variable Declaration and Definition

```c
int age;
```

+ int is the type (integer).

+ age is the variable name.

+ This declaration reserves space for an integer in memory.

You can declare multiple variables of the same type on one line:

```c
int x, y, z;
```

## Variable Initialization

You can declare and initialize a variable at the same time:

```c
int score = 10;
```

+ This sets score to 10 at the moment of creation.

+ Initialization is optional, but using uninitialized variables is undefined behavior and can cause bugs.

## Variable Types in C

C is a statically typed language — every variable must have a type.

Common primitive types:

| Type              | Size (bytes) | Range (Approximate)                        | Description                                   |
|-------------------|--------------|--------------------------------------------|-----------------------------------------------|
| `char`            | 1            | -128 to 127                                | Stores characters or small integers           |
| `unsigned char`   | 1            | 0 to 255                                   | Characters or bytes, no negative values       |
| `short` or `short int` | 2      | -32,768 to 32,767                          | Shorter-range integers                        |
| `unsigned short`  | 2            | 0 to 65,535                                | Only positive short integers                  |
| `int`             | 4            | -2,147,483,648 to 2,147,483,647            | Default integer type                          |
| `unsigned int`    | 4            | 0 to 4,294,967,295                         | Default unsigned integer                      |
| `long` or `long int` | 8         | -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807 | Larger integers               |
| `unsigned long`   | 8            | 0 to 18,446,744,073,709,551,615            | Large unsigned integers                       |
| `long long` or `long long int` | 8 | Same as `long`                            | Used for even larger numbers                  |
| `unsigned long long` | 8        | Same as `unsigned long`                    | Unsigned variant                              |
| `float`           | 4            | ~1.2E-38 to ~3.4E+38                        | Single-precision floating point               |
| `double`          | 8            | ~2.2E-308 to ~1.8E+308                      | Double-precision floating point               |
| `long double`     | 16 (varies)  | Greater precision than `double`            | Extended precision floats (platform-specific) |
| `void`            | N/A          | N/A                                        | Represents "no value"                         |


Note: Sizes can vary based on platform and compiler.

## Variable Naming Rules
+ Must start with a letter (A-Z, a-z) or underscore _.

+ Can contain letters, digits (0-9), and underscores.

+ Case sensitive (age and Age are different).

+ Cannot use C keywords like int, if, while, etc.

+ Avoid starting names with _ followed by uppercase letters — reserved for system.

## Variable Scope

The scope of a variable is the part of the program where the variable is visible and accessible.

+ Local variables: Declared inside a function or block { ... }. Only accessible there.

+ Global variables: Declared outside all functions. Accessible throughout the file (and possibly other files if declared extern).

+ Static variables: Can be local or global, but keep their value between function calls and have limited visibility.

## Examples of Variable Scope

```c
int global_var = 5; // global

void func() {
    int local_var = 10; // local to func
    printf("%d\n", global_var); // accessible here
}
```

## Variable Storage Classes

Variables in C can have storage classes which affect lifetime and visibility.

| Storage Class | Scope        | Lifetime                     | Default Initialization       |
| ------------- | ------------ | ---------------------------- | ---------------------------- |
| `auto`        | Local        | Automatic (until block ends) | Garbage (uninitialized)      |
| `register`    | Local        | Automatic                    | Garbage                      |
| `static`      | Local/Global | Program lifetime             | Zero initialized             |
| `extern`      | Global       | Program lifetime             | Depends on external variable |

Note: auto is default for local variables, so usually omitted.

## Constants

Variables declared with const cannot be changed after initialization.

```c
const int DAYS_IN_WEEK = 7;
```

## Important Notes

+ Using an uninitialized variable causes undefined behavior — the variable contains garbage value.

+ Variables can be reassigned new values anytime within their scope.

+ C does not check for overflow or type mismatch at runtime — be careful!

## Example — Putting it all together

```c
#include <stdio.h>

int global_counter = 0; // global variable

int main() {
    const float PI = 3.14159;  // constant variable
    int age = 25;              // local variable, initialized
    int score;                 // local variable, uninitialized (bad!)

    score = 100;               // assigned later

    printf("Age: %d\n", age);
    printf("Score: %d\n", score);
    printf("PI: %.5f\n", PI);
    printf("Global counter: %d\n", global_counter);

    return 0;
}
```

## Summary

| Topic          | Key Point                                           |
| -------------- | --------------------------------------------------- |
| Declaration    | Telling the compiler variable name and type         |
| Initialization | Assigning an initial value at declaration           |
| Types          | `int`, `char`, `float`, `double`, etc.              |
| Scope          | Where variable can be accessed: local vs global     |
| Storage Class  | Lifetime and visibility: `auto`, `static`, `extern` |
| Constants      | `const` variables cannot be changed                 |


