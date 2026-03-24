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

### The calloc() Function

The C library function **"calloc"** (stands for contiguous allocation) allocates the requested memory and returns a pointer to it.

```c
void *calloc(n, size);
```

Where **"n"** is the number of elements to be allocated and "size" is the byte size of each element.

The following snippet allocates the memory required to store 10 integer types.

```c
int *ptr;
ptr = (int *) calloc(25, sizeof(int));
```

### The realloc() Function

The **realloc()** function in C is used to dynamically change the memory allocation of a previously allocated memory. You can increase or decrease the size of an allocated memory block by calling the **realloc()** function.

```c
void *realloc(*ptr, size);
```

The first parameter **"ptr"** is the pointer to a memory block previously allocated with **malloc**, **calloc** or **realloc** to be reallocated.

Dynamic memory allocation technique is extensively used in complex linear and non−linear data structures such as linked lists and trees, which are employed in operating system software.

3. For Passing Arguments as Reference

When a function is called by reference, the address of the actual argument variables passed, instead of their values.

Passing a pointer to a function has two advantages −

+ First, it overcomes the limitation of pass by value. Changes to the value inside the called function are done directly at the address stored in the pointer. Hence, we can manipulate the variables in one scope from another.

+ Second, it also overcomes the limitation of a function in that it can return only one expression. By passing pointers, the effect of processing a function takes place directly at the address. Secondly, more than one value can be returned if we return the pointer of an array or struct variable.

### Example

The following function receives the reference of two variables whose values are to be swapped.

```c
/* function definition to swap the values */

int swap(int *x, int *y){
   int z;
   z = *x;    /* save the value at address x */
   *x = *y;   /* put y into x */
   *y = z;    /* put z into y */
  
   return 0;
}
```

### Example

The main() function has two variables "a" and "b", their addresses are passed as arguments to the swap() function.

```c
#include <stdio.h>

int swap(int *x, int *y);

int main(){

   /* local variable definition */
   int a = 10;
   int b = 20;
 
   printf("Before swap, value of a : %d\n", a);
   printf("Before swap, value of b : %d\n", b);
 
   /* calling a function to swap the values */
   swap(&a, &b);
 
   printf("After swap, value of a: %d\n", a);
   printf("After swap, value of b: %d\n", b);
 
   return 0;
}
```

Output

```bash
Before swap, value of a: 10
Before swap, value of b: 20
After swap, value of a: 20
After swap, value of b: 10
```

4. For Passing an Array to Function

Let us use these characteristics for passing the array by reference. In the main() function, we declare an array and pass its address to the **max()** function.

The **max()** function traverses the array using the pointer and returns the largest number in the array, back to the main() function.

### Example

Take a look at the following example −

```c
#include <stdio.h>

int max(int *arr, int length);

int main(){
    
   int arr[] = {10, 34, 21, 78, 5};
   int length = sizeof(arr)/sizeof(int);

   int maxnum = max(arr, length);
      printf("max: %d", maxnum);
}

int max(int *arr, int length){

   int max = *arr;
        
   for (int i = 0; i < length; i++){   
      printf("arr[%d]: %d\n", i, (*arr));
        
      if ((*arr)>max)
         max = (*arr);
      arr++;
   }
   return max;
}
```

Output

```bash
arr[0]: 10
arr[1]: 34
arr[2]: 21
arr[3]: 78
arr[4]: 5
max: 78
```

5. For Returning Multiple Values from a Function

In the C language, the functions can have only one return statement to return one value at a time. With the help of C pointers, you can return multiple values from a function by passing arguments as references.

### Example

The following example demonstrates how you can return multiple values with the help of C pointers.

```c
#include <stdio.h>

// Creating a function to find
// addition and subtraction
// of two numbers
void funAddSub(int a, int b, int* add, int* sub) {
  *add = a + b;
  *sub = a - b;
}

int main() {
  int num1 = 10;
  int num2 = 3;

  // Variables to store results
  int res1, res2;

  // Calling function to get add and sub
  // by passing the address of res1 and res2
  funAddSub(num1, num2, &res1, &res2);

  // Printing the result
  printf("Addition is %d and subtraction is %d", res1, res2);

  return 0;
}
```

Output

```bash
Addition is 13 and subtraction is 7
```
