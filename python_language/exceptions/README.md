# PYTHON EXCEPTIONS

Python exceptions provide a mechanism for handling errors that occur during the execution of a program. Unlike syntax errors, which are detected by the parser, Python raises exceptions when an error occurs in syntactically correct code. Knowing how to raise, catch, and handle exceptions effectively helps to ensure your program behaves as expected, even when encountering errors.

```python
n = 10
try:
    res = n / 0
except ZeroDivisionError:
    print("Can't be divided by zero!")
```

output

```bash
Can't be divided by zero!
```

**Explanation**: Dividing a number by 0 raises a **ZeroDivisionError**. The try block contains code that may fail and except block catches the error, printing a safe message instead of stopping the program.

### Syntax

```python
try:
	#Code
except SomeException:
	#Code
else:
	#Code
finally:
	#Code
```

+ try: Runs the risky code that might cause an error.

+ except: Catches and handles the error if one occurs.

+ else: Catches and handles the error if one occurs.

+ finally: Runs regardless of what happens useful for cleanup tasks like closing files.

### Example

```python
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    print("Zero is not allowed.")
except ValueError:
    print("That’s not even a number.")
else:
    print(result)
```

1. ```try``` Block

The try block contains code that might raise an error:

+ The program asks the user to enter a number.

+ It converts the input into an integer using ```int()```.

+ It then divides ```10``` by the entered number.

If any error occurs in this block, Python immediately stops executing it and jumps to the matching ```except``` block.

2. ```except ZeroDivisionError```

This block handles the case where the user enters ```0```.

+ Dividing by zero is mathematically undefined.

+ Python raises a ```ZeroDivisionError```.

+ The program catches it and prints:

```python
Zero is not allowed.
```

3. ```except ValueError```

This block handles invalid input.

+ If the user enters something that is not a number (e.g., ```"abc"```),

+ The ```int()``` function raises a ```ValueError```.

The program catches it and prints:

```python
That’s not even a number.
```

4. ```else``` Block

The ```else``` block runs only if no exceptions occur in the ```try``` block.

+ If the user enters a valid non-zero number,

+ The result of ```10 / num``` is printed.

