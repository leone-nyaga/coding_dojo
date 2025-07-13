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

## Integer Types in C

An integer type in C represents whole numbers (no decimal points).
C offers several types of integers, giving you control over:

+ Size (how many bytes it uses in memory)

+ Sign (whether it allows negative numbers or only positives)

+ Range (based on the above two)

### Base Integer Types

The C standard defines these basic signed types:

+ short or short int

+ int

+ long or long int

+ long long or long long int

Each has a corresponding unsigned type:

+ unsigned short

+ unsigned int

+ unsigned long

+ unsigned long long

### Typical Sizes and Ranges

(Actual sizes may vary by platform — this assumes 64-bit GCC)

| Type        | Size (bytes) | Signed Range                                            | Unsigned Range                  |
| ----------- | ------------ | ------------------------------------------------------- | ------------------------------- |
| `short`     | 2            | -32,768 to 32,767                                       | 0 to 65,535                     |
| `int`       | 4            | -2,147,483,648 to 2,147,483,647                         | 0 to 4,294,967,295              |
| `long`      | 8            | -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807 | 0 to 18,446,744,073,709,551,615 |
| `long long` | 8            | Same as `long`                                          | Same as `unsigned long`         |


### Signed vs Unsigned

+ Signed

  + Default type (int = signed int)

  + Can hold both negative and positive values.

  + Example: int x = -5;

+ unsigned

  + Only positive values (including zero).

  + Has twice the positive range of the signed equivalent.

  + Useful for bitwise operations, memory sizes, array indices.

  + Example: unsigned int size = 1024;


## format specifiers 

| Format Specifier | Data Type                  | Description                                         | Example Value         |
|------------------|----------------------------|-----------------------------------------------------|------------------------|
| `%d` or `%i`     | `int`                      | Signed decimal integer                              | `-42`, `0`, `100`      |
| `%u`             | `unsigned int`             | Unsigned decimal integer                            | `42`, `4000000000`     |
| `%hd`            | `short int`                | Signed short integer                                | `-32768`, `32767`      |
| `%hu`            | `unsigned short int`       | Unsigned short integer                              | `0`, `65535`           |
| `%ld`            | `long int`                 | Signed long integer                                 | `-9223372036854775808` |
| `%lu`            | `unsigned long int`        | Unsigned long integer                               | `18446744073709551615` |
| `%lld`           | `long long int`            | Signed long long integer                            | Very large ints        |
| `%llu`           | `unsigned long long int`   | Unsigned long long integer                          | Very large ints        |
| `%x`             | `unsigned int`             | Hexadecimal (lowercase)                             | `1a3f`                 |
| `%X`             | `unsigned int`             | Hexadecimal (UPPERCASE)                             | `1A3F`                 |
| `%o`             | `unsigned int`             | Octal representation                                | `0755`, `0177`         |
| `%c`             | `char`                     | Single character                                     | `'A'`, `'z'`           |
| `%s`             | `char *` (string)          | Null-terminated string                              | `"Hello, world!"`      |
| `%p`             | `void *` (pointer)         | Memory address                                      | `0x7ffee4c3`           |
| `%f`             | `float`, `double`          | Decimal floating point (fixed-point)                | `3.14`, `0.001`        |
| `%e`             | `float`, `double`          | Scientific notation (lowercase)                     | `1.23e+10`             |
| `%E`             | `float`, `double`          | Scientific notation (uppercase)                     | `1.23E+10`             |
| `%g`             | `float`, `double`          | Auto format: `%e` or `%f`, depending on value       | `0.0001`, `100.0`      |
| `%G`             | `float`, `double`          | Auto format, uppercase (`%E` or `%F`)               | `1.23E+10`             |
| `%Lf`            | `long double`              | Long double floating point                          | Extended precision     |
| `%%`             | N/A                        | Prints a literal `%` character                      | `%`                    |


### Notes:

+ %d and %i are identical in printf(), but behave differently in scanf() (%i auto-detects base like octal/hex).

+ %p is used for pointer values — addresses in memory.

+ %f, %e, and %g are float/double, but %Lf is for long double.

+ Hexadecimal (%x, %X) and octal (%o) are often used in systems or bit-level programming.

+ You can combine specifiers with flags like width, padding, precision: Example: %.2f, %04d, %10s, etc.

## Relational Operators in C

Relational operators in C are used to compare two values or expressions.

The result of a relational operation is either:

+ 1 (true) if the relation is true

+ 0 (false) if the relation is false

They are commonly used in conditional statements like if, while, for, etc.

### List of Relational Operators

| Operator | Name                  | Description                                | Example  | Result |
| -------- | --------------------- | ------------------------------------------ | -------- | ------ |
| `>`      | Greater than          | True if left operand is greater than right | `5 > 3`  | `1`    |
| `<`      | Less than             | True if left operand is less than right    | `2 < 4`  | `1`    |
| `>=`     | Greater than or equal | True if left operand is greater or equal   | `6 >= 6` | `1`    |
| `<=`     | Less than or equal    | True if left operand is less or equal      | `3 <= 2` | `0`    |
| `==`     | Equal to              | True if both operands are equal            | `7 == 7` | `1`    |
| `!=`     | Not equal to          | True if operands are **not equal**         | `5 != 4` | `1`    |


### Example

```c
#include <stdio.h>

int main() {
    int a = 10, b = 20;

    printf("a > b: %d\n", a > b);   // 0
    printf("a < b: %d\n", a < b);   // 1
    printf("a == b: %d\n", a == b); // 0
    printf("a != b: %d\n", a != b); // 1
    printf("a >= b: %d\n", a >= b); // 0
    printf("a <= b: %d\n", a <= b); // 1

    return 0;
}
```



## if, else if and else

In C programming, conditional statements like if, else if, and else are used to make decisions based on certain conditions.

### Basic Syntax

```c
if (condition) {
    // code block executed if condition is true
} else if (another_condition) {
    // code block executed if another_condition is true
} else {
    // code block executed if none of the above conditions are true
}
```

+ EXAMPLE

```c
int temp = 10;

if (temp > 30) {
    printf("Hot\n");
} else if (temp > 20) {
    printf("Warm\n");
} else {
    printf("Cold\n");
}
```

+ Nested if

```c
int num = 10;

if (num > 0) {
    if (num % 2 == 0) {
        printf("Positive even number\n");
    }
}
```


