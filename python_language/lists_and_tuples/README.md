# LISTS AND TUPLES

## LISTS

A list contains series of any data type: strings, ints, other lists. The things inside a list are generically called "elements". Unlike strings, lists are "mutable" - they can be changed.

Using the standard indexing scheme, the first element is at index 0, the next at index 1, and so on up to index length-1. 

## Basic Operations

You can get a lot done with just a few basic list features:

+ lst = [] - create an empty list

+ lst = [1, 2, 3] - create a list with data in it

+ lst.append(value) - add value to the end of a list, increasing the list's length by 1. Of all the list functions, this one is used the most.

+ len(lst) - access length of a list

+ lst[0] - access individual elements with square brackets and int index

+ for var in lst: - loop over a list. On each iteration of the loop, Python points the variable var to the next element

+ value in lst - boolean test if value is in lst (just like for string)

### Examples

```python
>>> lst = []           # Start with empty list
>>> lst.append('a')    # Add elements with lst.append()
>>> lst.append('b')
>>> lst.append('c')
>>> lst.append('d')
>>> lst
['a', 'b', 'c', 'd']
>>> len(lst)
4
>>> lst[0]              # Access element with brackets
'a'
>>> lst[2]
'c'
>>> lst[4]              # Oops, 4 is too big!
IndexError: list index out of range
>>> 
>>> lst
['a', 'b', 'c', 'd']
>>> lst[0] = 'apple'   # Change element at index 0
>>> 
>>> lst
['apple', 'b', 'c', 'd']
>>> 
>>> 'b' in lst         # "in" check
True
>>>
>>> # for-loop over list
>>> words = ['thus', 'solving', 'the', 'problem']
>>> for s in words:
      print(s)

thus
solving
the
problem
>>>
```

## List pop()

**lst.pop()** - remove the element from the end of the list and return it, decreasing the length of the list by 1. Mnemonic: the exact opposite of append().

**lst.pop(index)** - alternate version with the index to remove is given, e.g. lst.pop(0) removes the element at index 0. Raises an error if the index is not valid.

```python
>>> lst = ['a', 'b', 'c', 'd']
>>> lst.pop()   # default = remove from end
'd'
>>> lst
['a', 'b', 'c']
>>> lst.pop(0)  # can specify index to pop
'a'
>>> lst
['b', 'c']
```


