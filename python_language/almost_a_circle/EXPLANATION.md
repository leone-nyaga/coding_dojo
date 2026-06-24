# Explanation of Python Almost A Circle

## 0. If it's not tested it doesn't work

Create a ```tests``` folder that holds all the unnittests.

## 1. Base class

Create a class named ```Base``` that will give every object a unique ID automatically, unless the user provides one.

```python
class Base:
```

An empty init file will be needed to convert the ```models``` folder in to a package.

```python
__nb_objects = 0
```

This means:

+ private class variable

+ counts how many objects have been created

+ helps generate automatic IDs

Think of it like: "internal counter that no one outside should touch"

Constructor:

```python
def __init__(self, id=None):
```

Every time you create an object:

```python
b = Base()
```

Python runs this function.

### What you must do inside it

1. In the case that a user gives an ID:

```python
Base(10)
```

Use it directly:

```python
self.id = id
```

2. In the case that a user doesn't give an ID

```python
Base()
```

One will be auto-generate:

```python
Base.__nb_objects += 1
self.id = Base.__nb_objects
```

Think of it like this:

+ Give me an ID. If you don't have one, i'll create one for you.

+ Like a ticket system ? You bring your own ticket → use it : No ticket → system gives you next number.


# 2. First Rectangle

Write the class Rectangle that inherits from Base:

```python
def __init__(self, width, height, x=0, y=0, id=None):
```

This ```super().__init__(id)``` calls the parent class's constructor and passes the argument id to it.

Private instance attributes, each with its own public getter and setter:

```python
# width getter and setter
self.width = width

@property
def width(self):
    """
    Width of the rectangle.
    """
    return self.__width

@width.setter
def width(self, value):
    """
    Setter to width.
    """
    self.__width = value
```


