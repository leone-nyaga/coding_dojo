# Hello World

## :snake: What is Python?

Python is a programming language that's:

+ High-level – Easy to read and write (close to human language)

+ Interpreted – You don’t need to compile it; just run it directly

+ Dynamically typed – You don’t have to declare variable types

+ Open-source – Free and supported by a huge community

Python is one of the most popular programming languages in the world.

## :fire: What Can You Do with Python?

Here are just some of the things people use Python for:

| Field                   | What You Can Do                                                       |
| ----------------------- | --------------------------------------------------------------------- |
| **Web Development**     | Build websites and APIs (with Flask, Django)                          |
| **Data Science**        | Analyze and visualize data (with pandas, matplotlib, seaborn)         |
| **Machine Learning**    | Build AI models (with scikit-learn, TensorFlow, PyTorch)              |
| **Automation**          | Automate tasks like sending emails, renaming files                    |
| **Scripting**           | Write short programs to solve daily problems                          |
| **Cybersecurity**       | Analyze malware, scan networks                                        |
| **Game Development**    | Build games (with Pygame)                                             |
| **Robotics & IoT**      | Control hardware with Python on Raspberry Pi                          |
| **App Development**     | Make desktop apps (with Tkinter, Kivy)                                |
| **APIs & Web Scraping** | Collect and use data from the internet (with requests, BeautifulSoup) |

### python hello world

```python
# This will print 'Hello, World!' as the output
print("Hello, World!")
```

## Characteristics of Python

+ It supports functional and structured programming methods as well as OOP.
+ It can be used as a scripting language or can be compiled to byte-code for building large applications.
+ It provides very high-level dynamic data types and supports dynamic type checking.
+ It supports automatic garbage collection.
+ It can be easily integrated with C, C++, COM, ActiveX, CORBA, and Java.

## Who Invented Python?

Python was invented by a Dutch Programmer Guido Van Rossum in the late 1980s. He began working on Python in December 1989 as a hobby project while working at the Centrum Wiskunde & Informatica (CWI) in the Netherlands. Python's first version (0.9.0) was released in 1991.

![guido van rossum](https://github.com/leone-nyaga/coding_dojo/blob/main/images/guido%20van%20rossum.jpg)


## Syntax

The Python syntax defines a set of rules that are used to create a Python Program.

### Python - Interactive Mode Programming

We can invoke a Python interpreter from command line by typing python at the command prompt as following −

```bash
$ python3
Python 3.10.6 (main, Mar 10 2023, 10:55:28) [GCC 11.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

Here `>>>` denotes a Python Command Prompt where you can type your commands. Let's type the following text at the Python prompt and press the Enter −

```bash
>>> print ("Hello, World!")
```

If you are running older version of Python, like Python 2.4.x, then you would need to use print statement without parenthesis as in print "Hello, World!". However in Python version 3.x, this produces the following result −

```bash
Hello, World!
```

### Python - Script Mode Programming

We can invoke the Python interpreter with a script parameter which begins the execution of the script and continues until the script is finished. When the script is finished, the interpreter is no longer active.

Let us write a simple Python program in a script which is simple text file. Python files have extension .py. Type the following source code in a test.py file −

```python
print ("Hello, World!")
```

We assume that you have Python interpreter path set in PATH variable. Now, let's try to run this program as follows −

```bash
$ python3 test.py
```

This produces the following result −

```bash
Hello, World!
```

Let us try another way to execute a Python script. Here is the modified test.py file −

```python
#!/usr/bin/python3

print ("Hello, World!")
```
We assume that you have Python interpreter available in /usr/bin directory. Now, try to run this program as follows −

```bash
$ chmod +x test.py     # This is to make file executable
$./test.py
```

This produces the following result −

```bash
Hello, World!
```

### Python Identifiers

A Python identifier is a name used to identify a variable, function, class, module or other object. An identifier starts with a letter A to Z or a to z or an underscore (_) followed by zero or more letters, underscores and digits (0 to 9).

Python does not allow punctuation characters such as &commat;, $, and % within identifiers.

Here are naming conventions for Python identifiers −

+ Python Class names start with an uppercase letter. All other identifiers start with a lowercase letter.
+ Starting an identifier with a single leading underscore indicates that the identifier is private identifier.
+ Starting an identifier with two leading underscores indicates a strongly private identifier.
+ If the identifier also ends with two trailing underscores, the identifier is a language-defined special name.

### Python Lines and Indentation

Python programming provides no braces to indicate blocks of code for class and function definitions or flow control. Blocks of code are denoted by line indentation, which is rigidly enforced.

The number of spaces in the indentation is variable, but all statements within the block must be indented the same amount. For example −

```python
if True:
   print ("True")
else:
   print ("False")
```

However this is incorrect

```python
def greet(name):
print("Hello,", name)  # ❌ This will cause an IndentationError
```


