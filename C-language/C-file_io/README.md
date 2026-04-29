# C FILE IO

A single C file can read, write, move, and create files in our computer easily using a few functions and elements included in the C File I/O system. We can easily manipulate data in a file regardless of whether the file is a text file or a binary file using functions like fopen(), fclose(), fprintf(), fscanf(), getc(), putc(), getw(), fseek(), etc.

C Files can perform multiple useful operations:

+ Creation of a new file (fopen with attributes as “a” or “a+” or “w” or “w+”).

+ Opening an existing file (fopen).

+ Reading from file (fscanf or fgets).

+ Writing to a file with fprintf or fputs.

+ Moving file pointer associated with a given file to a specific position. (fseek, rewind).

+ Closing a file (fclose).

## File Pointer declaration

For performing operations on the file, a special pointer called File pointer is used that can be declared as:

```c
FILE *file_ptr;
```

We can open the file as

```c
file_ptr = fopen("fileName.txt", "w");
```

| Mode          | Description                                                                                                         |
| ------------- | ------------------------------------------------------------------------------------------------------------------- |
| `r`           | Open for reading. File must exist. Pointer starts at the beginning.                                                 |
| `rb`          | Open for reading in binary mode. File must exist.                                                                   |
| `w`           | Open for writing. Overwrites file if it exists, otherwise creates a new file.                                       |
| `wb`          | Open for writing in binary mode. Overwrites file if it exists, otherwise creates a new file.                        |
| `a`           | Open for appending. Writes go to the end of the file. Creates file if it doesn’t exist.                             |
| `ab`          | Open for appending in binary mode. Writes go to the end. Creates file if it doesn’t exist.                          |
| `r+`          | Open for reading and writing. File must exist. Pointer starts at the beginning.                                     |
| `rb+` / `r+b` | Open for reading and writing in binary mode. File must exist.                                                       |
| `w+`          | Open for reading and writing. Overwrites file if it exists, otherwise creates a new file.                           |
| `wb+` / `w+b` | Open for reading and writing in binary mode. Overwrites file if it exists, otherwise creates a new file.            |
| `a+`          | Open for reading and appending. Writing always happens at the end. Creates file if it doesn’t exist.                |
| `ab+` / `a+b` | Open for reading and appending in binary mode. Writing always happens at the end. Creates file if it doesn’t exist. |

## Opening a file in C

To perform the opening and creation of a file in c we can use the fopen() function which comes under stdio.h header file.

```c
p = fopen("fileopen", "mode");
```

Example

```c
p = fopen("Hello.txt", r);
```

## Creating a File in C

As now we know how to open a file using fopen() now the question arises about creation. The creation of a file is as simple as opening a file. As, if the while opening a file for writing or appending is done with either write("w") or append("a") mode then in the case where the file doesn't exist a new file is created.

```c
// C program to Create a file
#include <stdio.h>
#include <stdlib.h>

// Driver code
int main()
{
    // File Pointer declared
    FILE* ptr;

      // File opened
    ptr = fopen("./Hello.txt", "w");

      // Failed Condition
    if (ptr == NULL) {
        printf("Error Occurred While creating a "
               "file !");
        exit(1);
    }

      // File closed
    fclose(ptr);

      // Data is finally Inserted
    printf("File created\n\n");

    return 0;
}
```

## Writing a File in C

fprintf() and fscanf() are used to read and write in a text file in C programming. They expect a pointer to the structure FILE since they are file versions of print() and scanf().

```c
// C program to write contents
// to the file
#include <stdio.h>
#include <stdlib.h>

// Driver code
int main()
{
    // File Pointer declared
    FILE* ptr;

      // File opened
    ptr = fopen("./Hello.txt", "w+");

      // Failed Condition
    if (ptr == NULL) {
        printf("Error Occurred While writing to a text "
               "file !");
        exit(1);
    }

      // Data to be inserted
    char str[] = "This is all the Data to be inserted in "
                 "File by GFG.";

      // Puts data inside the file
    fputs(str, ptr);
  
      // File closed
    fclose(ptr);

      // Data is finally Inserted
    printf("Data Written Inside the file\n\n");

    return 0;
}
```

## Reading File in C

```c
// C program to read contents
// from the file
#include <stdio.h>
#include <stdlib.h>

// Driver code
int main()
{
  char str[80];
  FILE* ptr;

  ptr = fopen("Hello.txt", "r");

  if (ptr == NULL) 
  {
    printf("Error While opening file");
        
    // if the pointer returns NULL 
    // program will exit
    exit(1);
  }
  
  if(fgets(str, 80, ptr) != NULL)
  {
    puts(str);
  }
  fclose(ptr);

  return 0;
}
```


# File Descriptor

In Unix type systems, a file descriptor ( fd for short) is a small positive integer used as reference to an open file in a process. A process is a currently running program.

However, from the operating system’s point of view, a file is not only a text file as we might think of it as a user. A file can also be a directory or even another type of input/output resource such as a keyboard, a screen, a pipe or a network socket.

By default, each process systematically inherits three open file descriptors :

| File Descriptor | Name            | `<unistd.h>`    | `<stdio.h>` |
| --------------- | --------------- | --------------- | ----------- |
| 0               | Standard Input  | `STDIN_FILENO`  | `stdin`     |
| 1               | Standard Output | `STDOUT_FILENO` | `stdout`    |
| 2               | Standard Error  | `STDERR_FILENO` | `stderr`    |


