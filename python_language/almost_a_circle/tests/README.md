# How to run

Go to the root of the project, and run:

```python
python3 -m unittest discover tests
```

Thank you for comming to my Ted talk

## Test methods used

### Base class

| Test Method                    | What it tests                                                                                  |
| ------------------------------ | ---------------------------------------------------------------------------------------------- |
| `test_id()`                    | Verifies that `Base` assigns automatic IDs correctly and uses a provided ID when one is given. |
| `test_to_json_string_normal()` | Verifies that `to_json_string()` returns a JSON string for a valid list of dictionaries.       |
| `test_to_json_string_empty()`  | Verifies that `to_json_string([])` returns `"[]"`.                                             |
| `test_to_json_string_none()`   | Verifies that `to_json_string(None)` also returns `"[]"`.                                      |

### Rectangle class

| Test Method             | What it verifies                                                                                        | Assertions Used |
| ----------------------- | ------------------------------------------------------------------------------------------------------- | --------------- |
| `test_initialization()` | Checks that a `Rectangle` object is initialized with the correct `width`, `height`, `x`, `y`, and `id`. | `assertEqual()` |
| `test_area()`           | Confirms that `area()` returns `width × height`.                                                        | `assertEqual()` |
| `test_str()`            | Verifies that `__str__()` returns the expected string representation.                                   | `assertEqual()` |
| `test_to_dictionary()`  | Confirms that `to_dictionary()` returns a dictionary with the correct keys and values.                  | `assertEqual()` |


### Square class

| Test Method            | What it tests                                                                                                                             | Assertions used |
| ---------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | --------------- |
| `test_attributes()`    | Ensures `Square` initializes attributes correctly (`width`, `height`, `x`, `y`, `id`). Also confirms that `width == height` for a square. | `assertEqual()` |
| `test_str()`           | Checks that `__str__()` returns the correct formatted string for a `Square`.                                                              | `assertEqual()` |
| `test_to_dictionary()` | Ensures `to_dictionary()` returns a dictionary with correct keys and values.                                                              | `assertEqual()` |

