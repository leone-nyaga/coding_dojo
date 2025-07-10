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

| Type     | Size (typically) | Range                           | Description             |
| -------- | ---------------- | ------------------------------- | ----------------------- |
| `int`    | 4 bytes          | -2,147,483,648 to 2,147,483,647 | Integer numbers         |
| `char`   | 1 byte           | -128 to 127 (signed)            | Single characters       |
| `float`  | 4 bytes          | \~1.2E-38 to 3.4E+38            | Floating-point numbers  |
| `double` | 8 bytes          | \~2.2E-308 to 1.8E+308          | Double-precision floats |
| `void`   | N/A              | N/A                             | Represents “no type”    |

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

