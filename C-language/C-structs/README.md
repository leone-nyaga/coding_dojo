# STRUCTURES

C structures are special, large variables which contain several named variables inside. Structures are the basic foundation for objects and classes in C. Structures are used for:

+ Serialization of data
+ Passing multiple arguments in and out of functions through a single argument
+ Data structures such as linked lists, binary trees, and more

## Declaration

You can create (declare) a structure by using the **"struct"** keyword followed by the structure_tag (structure name) and declare all of the members of the structure inside the curly braces along with their data types.

```c
struct [structure tag]{
   member definition;
   member definition;
   ...
   member definition;
} [one or more structure variables];
```

The **structure tag** is optional and each member definition is a normal variable definition, such as "int i;" or "float f;" or any other valid variable definition.

At the end of the structure's definition, before the final semicolon, you can specify one or more structure variables but it is optional.

### Example

```c
struct book{
   char  title[50];
   char  author[50];
   double price;
   int   pages;
} book1;
```

Here, we declared the structure variable book1 at the end of the structure definition. However, you can do it separately in a different statement.
