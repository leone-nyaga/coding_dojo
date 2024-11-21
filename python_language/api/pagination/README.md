# PAGINATION

Pagination is a technique used in computing and web development to divide a large data set into smaller more manageable segaments called pages.

#### syntax
```python
def paginate(items, page_size, page_number):
    start_index = (page_number - 1) * page_size
    end_index = start_index + page_size
    return items[start_index:end_index]
```

#### Example

Let's have a list of numbers from 0 - 15
```python
num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
```
And, let's assume you want to paginate this list into 3 pages with each page containing 5 items (i.e., page_size = 5).
The goal is to split it into 3 pages with 5 items on each page.

1. The first page(page_number = 1)
start index: (1 - 1) * 5 = 0
end index: 0 + 5 = 5
This means the function will slice the list from index 0 to 5 (not including index 5):
page 1 will contain ```[ 0, 1, 2, 3, 4]```
Calling the function:
```python
paginate(num, 5, 1)  # returns [0, 1, 2, 3, 4]
```

2. The second page(page_number = 2)
start index: (2 - 1) * 5 = 5
end index: 5 + 5 = 10
this means the function will slice the list from index 5 to 10 (not including index 10):
page 2 will contain ```[ 5, 6, 7, 8, 9]```
Claaing the function:
```python
paginate(num, 5, 2) # returns [ 5, 6, 7, 8, 9 ]
```

3. The third page(page_number  = 3)
start index: (3 - 1) * 5 = 10
end index: 10 + 5 = 15
this means the function will slice the list from index 10 to 15 (not including index 15):
page 3 will contain ```[ 10, 11, 12, 13, 14 ]```
Calling the function:
```python
paginate(num, 5, 3) # return [ 10, 11, 12, 13, 14 ]
```
