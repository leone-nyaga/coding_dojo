# HELLO WORLD

C is a general-purpose programming language.
It was created in the 1970s by Dennis Ritchie and remains very widely used and influential.
By design, C's features cleanly reflect the capabilities of the targeted CPUs.
It has found lasting use in operating systems code (especially in kernels), device drivers, and protocol stacks, but its use in application software has been decreasing.

## stages of compilation

1. Preprocessing

What happens here:

+ The preprocessor handles all directives that begin with #, like:

  + #include

  + #define

  + #ifdef, #ifndef, etc.

+ Tasks:

  + Replaces macros (#define) with their values.

  + Replaces #include <file> with the actual content of the file.

  + Removes comments (//, /* ... */).

  + Processes conditional compilation (#if, #endif, etc.).

+ command

```bash
gcc -E source.c -o source.i
```

  + -E: Stop after preprocessing and output the result.

  + Output: source.i (a text file containing the preprocessed code)

+ Notes:

  + The output is still C code, but now it has no macros or includes — everything is "flattened".

2. Compilation (proper)

+ What happens here:

  + The compiler takes the preprocessed code and translates it into assembly code.

  + Syntax checking, semantic analysis, optimization of expressions, etc.

  + Variables are assigned memory locations (at least conceptually at this point).

  + Functions are converted to low-level instructions.

+ Command

```bash
gcc -S source.i -o source.s
```

  + -S: Stop after compilation, output assembly code.

  + Output: source.s

+ Notes:

  + This stage is where actual C-to-ASM translation happens.

  + You’ll see mov, call, etc. in the output — raw CPU instructions in human-readable form.

3. Assembly

+ What happens here:

  + The assembler takes the assembly code (.s) and turns it into machine code (binary) — but not yet a complete program.

  + Produces an object file: a partially compiled file with placeholders for unresolved symbols.

+ Command:

```bash
gcc -c source.s -o source.o
```

  + -c: Compile/assemble without linking.

  + Output: source.o (object file)

+ Notes:

+ .o files are machine-readable, but still incomplete — think of them like puzzle pieces.

4. Linking
+ What happens here:

  + The linker takes your .o file and links it with:

    + Standard libraries (like libc)

    + Other .o or .a files (like your own compiled modules)

  + Resolves all function calls, global variables, etc.

  + Produces the final executable binary.

+ Command:

```bash
gcc source.o -o program
```

  + Output: program (executable)

+ Notes:

  + This is where errors like "undefined reference to printf" occur if the linker can't find the needed function.

## summary table

| Stage         | File Extension | Flag      | Output         | Description                           |
|---------------|----------------|-----------|----------------|---------------------------------------|
| Preprocessing | `.i`           | `-E`      | Preprocessed C | Handles `#include`, `#define`, etc.   |
| Compilation   | `.s`           | `-S`      | Assembly code  | Converts C to assembly                |
| Assembly      | `.o`           | `-c`      | Object file    | Converts assembly to machine code     |
| Linking       | (none)         | (default) | Executable     | Combines all `.o` into a program      |


## Full Example (with all flags)

```c
#include <stdio.h>
int main() {
    printf("Hello, World!\n");
    return 0;
}
```

You could run the whole compilation process like this:

```bash
gcc -E main.c -o main.i        # Preprocess
gcc -S main.i -o main.s        # Compile to Assembly
gcc -c main.s -o main.o        # Assemble to Object File
gcc main.o -o main             # Link to Executable
```


