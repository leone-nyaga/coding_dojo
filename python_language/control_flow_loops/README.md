# Control flow and loops

Python program control flow is regulated by various types of conditional statements, loops, and function calls.

## Decision Making Statements
Decision making statements are used in the Python programs to make them able to decide which of the alternative group of instructions to be executed, depending on value of a certain Boolean expression.

They include: 

1. If statements

2. Match statements

## Loops or Iteration Statements

Most of the processes require a group of instructions to be repeatedly executed. In programming terminology, it is called a loop.

Instead of the next step, if the flow is redirected towards any earlier step, it constitutes a loop.

They include:

1. For loops

2. While loops

3. do - while loops


## IF statement

The if statement in Python evaluates whether a condition is true or false.

It contains a logical expression that compares data, and a decision is made based on the result of the comparison.

Syntax:

```python
if expression:
   # statement(s) to be executed
```

### Example

```python
discount = 0
amount = 1200

# Check he amount value
if amount > 1000:
   discount = amount * 10 / 100

print("amount = ", amount - discount)
```

### output

```python
amount = 1080.0
```

## If else statement

The if-else statement in Python is used to execute a block of code when the condition in the if statement is true, and another block of code when the condition is false.

Syntax:

```python
if boolean_expression:
  # code block to be executed
  # when boolean_expression is true
else:
  # code block to be executed
  # when boolean_expression is false
```

Example

```python
age=25
print ("age: ", age)
if age >=18:
   print ("eligible to vote")
else:
   print ("not eligible to vote")
```

output

```bash
age: 25
eligible to vote
```


