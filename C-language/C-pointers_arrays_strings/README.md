# POINTERS

In C programming, a pointer is a variable that stores the memory address of another variable.

Instead of holding an actual value, it holds the location in the computer's memory where that value is stored

This allows for direct manipulation of data in memory, which can be crucial for tasks like dynamic memory allocation, efficient array traversal, and passing arguments by reference to functions.

```c
/*
Pointer Basics Example

Goal:
Understand the relationship between:
- a variable
- a pointer
- the value stored in memory
- the addresses involved

Key ideas:
ptr   -> stores an address
*ptr  -> accesses the value stored at that address
&var  -> gives the address of a variable
*/

#include <stdio.h>

int main() {

    /* Step 1: Create a normal integer variable */
    int x = 5;

    /* Step 2: Declare a pointer that can store the address of an int */
    int *ptr;

    /* Step 3: Make the pointer point to x */
    ptr = &x;

    /*
    Memory idea (conceptual):

        ptr --------> x
                     5
    */

    printf("Value stored in x: %d\n", x);

    /* Dereferencing the pointer */
    printf("Value accessed through pointer (*ptr): %d\n", *ptr);

    /* Address of the pointer variable itself */
    printf("Address of ptr (&ptr): %p\n", (void *)&ptr);

    /* Address of x */
    printf("Address of x (&x): %p\n", (void *)&x);

    /* Value stored in ptr (which is the address of x) */
    printf("Value stored in ptr (ptr): %p\n", (void *)ptr);

    /*
    Important relationships:

    ptr  == &x
    *ptr == x

    ptr  -> address
    *ptr -> value at that address
    */

    return 0;
}
```

### What is **(void *)** ????

+ It's a type cast.

+ It's called a **generic pointer** "convert this pointer to a void pointer."

syntax
```c
void *p;
```

This pointer can store any address:

```c
int x = 5;
char c = 'A';

p = &x;
p = &c;
```

It can also work without it

```c
printf("%p\n", &x);
```

It works because most compilers automatically convert pointer types.

But according to the C standard, the correct type for %p is:

```c
printf("%p\n", (void *)&x);
```


