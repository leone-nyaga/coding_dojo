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

## The Address of (&) operator and the dereference ('*') operator

1. The Address of operator (&)

The operator used to obtain the memory address of a variable in C is the address-of operator, denoted by the ampersand symbol (&).

When the & operator is placed immediately before a variable name, it returns the starting memory address (a pointer value) of that variable.

Syntax:

```c
&variable_name
```

Example:

```c
#include <stdio.h>

int main() {
    int num = 10;
    int *ptr;

    // Use the address-of operator to get the address of 'num'
    ptr = &num;

    printf("Value of num: %d\n", num);
    printf("Address of num: %p\n", &num); // Prints the address using the & operator
    printf("Value stored in ptr (address of num): %p\n", ptr); // Prints the address stored in the pointer

    return 0;
}
```

Explanation:

+ **int num = 10;** declares an integer variable **num** and assigns it a value.

+ **&num** retrieves the memory address where the value 10 is stored.

+ This address can be stored in a pointer variable (e.g., **ptr = &num;**) for later use, such as passing the variable by reference to a function or performing dynamic memory manipulation.

+ The **%p** format specifier is typically used with **printf** to display the memory address in hexadecimal format.

2. The dereference operator (*)

+ Also known as "Value at address" operator.

+ It is used to get the value stored at a memory address.

```c
int x = 10;
int *p = &x;

printf("%d", *p);
```

+ ```&x``` → gives the address of x

+ ```p``` stores that address

+ ```*p``` → gives the value at that address

OUTPUT ----> ```10```

## Application of Pointers

1. Access Array elements

Array elements can also be accessed through the pointer. You need to declare and initialize a pointer to an array and using it you can access each element by incrementing the pointer variable by 1.

The pointer to an array is the address of its 0th element. When the array pointer is incremented by 1, it points to the next element in the array.

### Example

```c
#include <stdio.h>

int main(){

   int arr[] = {1,2,3,4,5};
   int *ptr = arr;

   for(int i = 0; i <= 4; i++){
      printf("arr[%d]: %d\n", i, *ptr);
      ptr++;
   }
   
   return 0;
}
```

Output

```bash
arr[0]: 1
arr[1]: 2
arr[2]: 3
arr[3]: 4
arr[4]: 5
```

2. For Allocating Memory Dynamically

One of the most important applications of C pointers is to declare memory for the variables dynamically. There are various situations, where static memory allocation cannot solve the problem, such as dealing with large size of arrays, structures having n numbers of students and employees, etc.

Thus, whenever you need to allocate memory dynamically, pointers play an important role in it. C language provides some of the functions to allocate and release the memory dynamically. The functions are:

```
**malloc()** function
Allocates an array of num elements each of which size in bytes will be size.
**calloc()** function
Allocates an array of num bytes and leaves them uninitialized.
**realloc()** function
Reallocates memory extending it up to newsize.
```

### The malloc() Function

This function is defined in the "stdlib.h" header file. It allocates a block memory of the required size and returns a **void** pointer.

```c
void *malloc (size)
```

The size parameter refers to the block of memory in bytes. To allocate the memory required for a specified data type, you need to use the typecasting operator. For example, the following snippet allocates the memory required to store an int type.

```c
int *ptr;
ptr = (int * ) malloc (sizeof (int));
```

Here we need to define a pointer to character without defining how much memory is required and later, based on requirement, we can allocate memory.

In this example, we use the malloc() function to allocate the required memory to store a string (instead of declaring a char array of a fixed size) −

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(){

   char *name;
   name = (char *) malloc(strlen("TutorialsPoint"));

   strcpy(name, "TutorialsPoint");
   
   if(name == NULL) {
      fprintf(stderr, "Error - unable to allocate required memory\n");
   } else {
      printf("Name = %s\n", name );
   }
}
```

When the above code is compiled and executed, it produces the following output −

```bash
Name = TutorialsPoint
```


