# OBJECT ORIENTED PROGRAMMING

Object-oriented programming (OOP) in Python helps you structure your code by grouping related data and behaviors into objects. You start by defining classes, which act as blueprints, and then create objects from them.
OOP simplifies modeling real-world concepts in your programs and enables you to build systems that are more reusable and scalable.

## What is object oriented programming in Python?

Object-oriented programming is a [programming paradigm](https://en.wikipedia.org/wiki/Programming_paradigm) that provides a means of structuring programs so that properties and behaviors are bundled into individual objects.

For example, an object could represent a person with properties like a name, age, and address and behaviors such as walking, talking, breathing, and running. Or it could represent an email with properties like a recipient list, subject, and body and behaviors like adding attachments and sending.

Put another way, object-oriented programming is an approach for modeling concrete, real-world things, like cars, as well as relations between things, like companies and employees or students and teachers. OOP models real-world entities as software objects that have some data associated with them and can perform certain operations.

OOP also exists in other programming languages and is often described to center around the four pillars, or four tenants of OOP:

1. **Encapsulation** allows you to bundle data (attributes) and behaviors (methods) within a class to create a cohesive unit. By defining methods to control access to attributes and its modification, encapsulation helps maintain data integrity and promotes modular, secure code.

2. **Inheritance** enables the creation of hierarchical relationships between classes, allowing a subclass to inherit attributes and methods from a parent class. This promotes code reuse and reduces duplication.

3. **Abstraction** focuses on hiding implementation details and exposing only the essential functionality of an object. By enforcing a consistent interface, abstraction simplifies interactions with objects, allowing developers to focus on what an object does rather than how it achieves its functionality.

4. **Polymorphism** allows you to treat objects of different types as instances of the same base type, as long as they implement a common interface or behavior. Python’s duck typing make it especially suited for polymorphism, as it allows you to access attributes and methods on objects without needing to worry about their actual class.

## How to define a class

In Python, you define a class by using the class keyword followed by a name and a colon. Then you use .__init__() to declare which attributes each instance of the class should have:

```python
class Employee:
    def __init__(self, name, age):
        self.name =  name
        self.age = age
```

While the class is the blueprint, an **instance** is an object that’s built from a class and contains real data. An instance of the Dog class is not a blueprint anymore. It’s an actual dog with a name, like Miles, who’s four years old.

Put another way, a class is like a form or questionnaire. An instance is like a form that you’ve filled out with information. Just like many people can fill out the same form with their own unique information, you can create many instances from a single class.

```python
class Dog:
    pass
```

The Dog class isn’t very interesting right now, so you’ll spruce it up a bit by defining some properties that all Dog objects should have.

You define the properties that all Dog objects must have in a method called ```.__init__()```. Every time you create a new Dog object, ```.__init__()``` sets the initial state of the object by assigning the values of the object’s properties. That is, .```__init__()``` initializes each new instance of the class.

You can give ```.__init__()``` any number of parameters, but the first parameter will always be a variable called self. When you create a new class instance, then Python automatically passes the instance to the self parameter in ```.__init__()``` so that Python can define the new attributes on the object.

Update the Dog class with an .__init__() method that creates .name and .age attributes:

```python
# dog.py

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

In the body of .__init__(), there are two statements using the self variable:

1. self.name = name creates an attribute called name and assigns the value of the name parameter to it.
2. self.age = age creates an attribute called age and assigns the value of the age parameter to it.

Attributes created in ```.__init__()``` are called instance attributes. An instance attribute’s value is specific to a particular instance of the class. All Dog objects have a name and an age, but the values for the name and age attributes will vary depending on the Dog instance.

On the other hand, class attributes are attributes that have the same value for all class instances. You can define a class attribute by assigning a value to a variable name outside of ```.__init__()```.
