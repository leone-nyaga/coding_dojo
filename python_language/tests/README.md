# UNITTESTS

The Python standard library ships with a testing framework named unittest, which you can use to write automated tests for your code. The unittest package has an object-oriented approach where test cases derive from a base class, which has several useful methods.

The framework supports many features that will help you write consistent unit tests for your code. These features include test cases, fixtures, test suites, and test discovery capabilities.

A unit is often a small part of a program that takes a few inputs and produces an output. Functions, methods, and other callables are good examples of units that you’d need to test.

The unittest package provides a unit test framework inspired by JUnit, which is a unit test framework for the Java language. The unittest framework is directly available in the standard library, so you don’t have to install anything to use this tool.

The framework uses an object-oriented approach and supports some essential concepts that facilitate test creation, organization, preparation, and automation:

+ Test case: An individual unit of testing. It examines the output for a given input set.

+ Test suite: A collection of test cases, test suites, or both. They’re grouped and executed as a whole.

+ Test fixture: A group of actions required to set up an environment for testing. It also includes the teardown processes after the tests run.

+ Test runner: A component that handles the execution of tests and communicates the results to the user.


```python
import unittest
def add(a, b):
    return a + b

class TestAdd(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(add(2, 3), 5)

if __name__ == "__main__":
    unittest.main()
```

output:

```
.
----------------------------------------------------------------------

Ran 1 test in 0.000s

OK
```

Explanation:

+ add() returns the sum of two numbers.

+ TestAdd inherits from unittest.TestCase, making it a test case class.

+ test_addition() verifies that add(2, 3) returns 5.

+ assertEqual() checks whether the actual result matches the expected value.

## Assert Methods

| Method                    | Description                                                                                 |
| ------------------------- | ------------------------------------------------------------------------------------------- |
| `.assertEqual(a, b)`      | Checks if `a` is equal to `b`, similar to the expression `a == b`.                          |
| `.assertTrue(x)`          | Asserts that the boolean value of `x` is `True`, equivalent to `bool(x) is True`.           |
| `.assertIsInstance(a, b)` | Asserts that `a` is an instance of class `b`, similar to the expression `isinstance(a, b)`. |
| `.assertIsNone(x)`        | Ensures that `x` is `None`, similar to the expression `x is None`.                          |
| `.assertFalse(x)`         | Asserts that the boolean value of `x` is `False`, similar to `bool(x) is False`.            |
| `.assertIs(a, b)`         | Verifies if `a` is identical to `b`, akin to the expression `a is b`.                       |
| `.assertIn(a, b)`         | Checks if `a` is a member of `b`, akin to the expression `a in b`.                          |



## Examples

### 1. 

This example demonstrates testing different string operations using unittest framework. The test case class TestStringMethods includes multiple tests to verify string properties and behavior.

```python
import unittest

class TestStringMethods(unittest.TestCase):

    def setUp(self):
        pass

    # Returns True if the string contains 4 a.
    def test_strings_a(self):
        self.assertEqual('a'*4, 'aaaa')

    # Returns True if the string is in upper case.
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_strip(self):
        s = 'geeksforgeeks'
        self.assertEqual(s.strip('geek'), 'sforgeeks')

    # Returns true if the string splits and matches
    # the given output.
    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()
```

Output

```
.....
----------------------------------------------------------------------
Ran 5 tests in 0.000s

OK
```

Explanation

+ assertEqual(): Checks if the result equals the expected value.

+ assertTrue() / assertFalse(): Verifies if a condition is True or False.

+ assertRaises(): Confirms a specific exception is raised.

+ test_strings_a(): Verifies character multiplication.

+ test_upper(): Checks string conversion to uppercase.

+ test_isupper(): Checks uppercase property of string.

+ test_strip(): Ensures specified characters are removed from string.

+ test_split(): Checks splitting of string and validates TypeError for invalid input.

+ unittest.main(): Runs all tests and provides a command-line interface.
