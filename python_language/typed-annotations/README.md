TYPED ANNOTATIONS
==================
Python is a statically typed language, meaning there is no need to declare the datatype e.g. x = 10
Languages like C, C++, Java are statically typed, meaning types are checked at compile-time, e.g. int num = 10;

Normal python code
===================
def greet(name):
    return f"Hello {name}"
print (greet("John")) // output "Hello John"

Python code with type hints
============================
def greet(name: str) -> str:
   return f"Hello {name}"
print (greet("John")) // output "Hello John"
