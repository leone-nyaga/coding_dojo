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
