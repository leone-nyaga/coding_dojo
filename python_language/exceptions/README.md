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


