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

## if elif else Statement

The if elif else statement allows you to check multiple expressions for TRUE and execute a block of code as soon as one of the conditions evaluates to TRUE.

Similar to the else block, the elif block is also optional. However, a program can contains only one else block whereas there can be an arbitrary number of elif blocks following an if block.

### syntax

```python
if expression1:
   statement(s)
elif expression2:
   statement(s)
elif expression3:
   statement(s)
else:
   statement(s)
```

### Example with if else

```python
amount = 2500
print('Amount = ',amount)
if amount > 10000:
   discount = amount * 20 / 100
else:
   if amount > 5000:
      discount = amount * 10 / 100
   else:
      if amount > 1000:
         discount = amount * 5 / 100
      else:
         discount = 0

print('Payable amount = ',amount - discount)
```

### Output

```bash
Amount: 800
Payable amount = 800
Amount: 2500
Payable amount = 2375.0
Amount: 7500
Payable amount = 6750.0
Amount: 15000
Payable amount = 12000.0
```

### With elif

```python
amount = 2500
print('Amount = ',amount)
if amount > 10000:
   discount = amount * 20 / 100
elif amount > 5000:
   discount = amount * 10 / 100
elif amount > 1000:
   discount = amount * 5 / 100
else:
   discount=0

print('Payable amount = ',amount - discount)
```

### output

```bash
Amount: 2500
Payable amount = 2375.0
```


