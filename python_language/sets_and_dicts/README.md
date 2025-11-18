# SET

A set is an unordered collection of unique, hashable elements.

+ **Mutable**: You can add or remove elements from an existing set.
+ **Unordered**: A set doesn’t maintain any particular order of its elements.
+ **Unique elements**: Duplicate elements aren’t allowed.
+ **Hashable elements**: Each element must have a hash value that stays the same for its entire lifetime.

As with other mutable data types, you can modify sets by increasing or decreasing their size or number of elements.

The elements of a set must be unique. This feature makes sets especially useful in scenarios where you need to remove duplicate elements from an existing iterable, such as a list or tuple:

```python
>>> numbers = [1, 2, 2, 2, 3, 4, 5, 5]
>>> set(numbers)
{1, 2, 3, 4, 5}
```
Python sets support common set operations, such as union, intersection, difference, symmetric difference, and others. This feature makes them useful when you need to do some of the following tasks:

+ **Find common elements** in two or more sets
+ **Find differences** between two or more sets
+ **Combine multiple sets** together while avoiding duplicates

## Creating a set

1. Creating Sets Through Literals

You can define a new set by providing a comma-separated series of hashable objects within curly braces {} as shown below:

```python
l = {1, 3, 4,}
```

The elements of a set can be objects of different data types:

```python
>>> {42, "Hi!", 3.14159, None, "Python"}
{None, 42, 3.14159, 'Hi!', 'Python'}
```

It’s also important to remember that set elements must be hashable. For example, you can include a tuple in a set, as you already learned, but you can’t include a list because lists aren’t hashable:

```python
>>> rgb_colors = {
...     [51, 255, 87],  # Green
...     [51, 87, 255],  # Blue
...     [241, 196, 15],  # Yellow
...     [231, 76, 60],  # Red
... }
Traceback (most recent call last):
    ...
TypeError: unhashable type: 'list'
```

Apart from lists, you can’t use dictionaries, bytearray objects, or other sets as the elements of a set. These data types are mutable, and therefore, they can’t be hashable.

2. Using the set() Constructor

You can also build sets using the set() constructor. When would you use this approach? For example, there’s no literal for creating empty sets because an empty pair of curly braces creates an empty dictionary. If you want to create an empty set, then you have to use the constructor:

```python
>>> empty = set()
>>> empty
set()
```
The syntax to build a set using the constructor is shown below:

```python
set([iterable])
```

The argument iterable is optional and must be an iterable like a list or tuple. For example, the following code builds a set from a list:

```python
>>> set([1, 2, 2, 3, 4, 4, 5])
{1, 2, 3, 4, 5}
```

In this example, you pass a list of numbers to set(). Note how the originally duplicate values are only represented once in the resulting set.

Python strings are also iterable, so you can pass a string to set(). This will generate a set of characters in the input string:

```python
>>> language = "Python"

>>> set(language)
{'y', 'P', 'o', 't', 'n', 'h'}
```

The resulting set of characters is unordered. The original order, as specified in the string, isn’t preserved.

There’s a subtle difference between using the set() constructor and the literal syntax. Observe the difference with a quick example:

```python
>>> set("Hello!")
{'H', 'l', 'e', '!', 'o'}

>>> {"Hello!"}
{'Hello!'}
```

When you create sets using the set() constructor, the argument must be iterable. The constructor unpacks the iterable and adds its items to the resulting set as individual elements. In contrast, the set literal syntax adds the iterable as a single element to the set. It doesn’t unpack its items.

## Performing Common Set Operations

1. Union

union() is a method for sets that lets you combine two (or more) sets into a new set with all unique elements.

```python
a = {1, 2, 3}
b = {3, 4, 5}

c = a.union(b)
print(c)
```

Output (order can vary because sets are unordered):

```python
{1, 2, 3, 4, 5}
```

You can also use ```|``` oparetor

```python
c = a | b
print(c)  # {1, 2, 3, 4, 5}
```

## Intersection

The intersection of two sets is a new set containing only the elements common to both sets.

You can use the ```&``` operator or the ```.intersection()``` method to perform an intersection.

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

c = a.intersection(b)
print(c) # {3, 4}
```

```python
c = a & b
print(c)  # {3, 4}
```

Intersections can be more than two sets:

```python
x = {1, 2, 3, 4}
y = {2, 3, 4, 5}
z = {3, 4, 6}

result = x & y & z
print(result)  # {3, 4}
```

## Difference

The difference of two sets is all the elements that are in the first set but not in the second.
