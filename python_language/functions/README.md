# Functions

##  What is a function

A function is a block of reusable code that performs a specific task. It helps make your code modular, readable, and efficient.

### Defining a Python Function

+ Function blocks begin with the keyword def followed by the function name and parentheses ().

+ Any input parameters or arguments should be placed within these parentheses. You can also define parameters inside these parentheses.

+ The first statement of a function can be an optional statement; the documentation string of the function or docstring.

+ The code block within every function starts with a colon (:) and is indented.

+ The statement return [expression] exits a function, optionally passing back an expression to the caller. A return statement with no arguments is the same as return None.

### Syntax to Define a Python Function

```python
def function_name( parameters ):
   "function_docstring"
   function_suite
   return [expression]
```

By default, parameters have a positional behavior and you need to inform them in the same order that they were defined.

Once the function is defined, you can execute it by calling it from another function or directly from the Python prompt.

### Example to Define a Python Function

Here, we are defining a function greetings()

```python
def greetings():
   "This is docstring of greetings function"
   print ("Hello World")
   return
```

When this function is called, Hello world message will be printed.

### Calling a Python Function

Defining a function only gives it a name, specifies the parameters that are to be included in the function and structures the blocks of code. Once the basic structure of a function is finalized, you can call it by using the function name itself. If the function requires any parameters, they should be passed within parentheses. If the function doesn't require any parameters, the parentheses should be left empty.

Example to Call a Python Function

+ Following is the example to call printme() function −

```python
# Function definition is here
def printme( str ):
   "This prints a passed string into this function"
   print (str)
   return;

# Now you can call the function
printme("I'm first call to user defined function!")
printme("Again second call to the same function")
```

When the above code is executed, it produces the following output −


```bash
I'm first call to user defined function!
Again second call to the same function
```

