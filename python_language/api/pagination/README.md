#PAGINATION
Pagination is a technique used in computing and web development to divide a large data set into smaller more manageable segaments called pages.

####syntax
```python
def paginate(items, page_size, page_number):
    start_index = (page_number - 1) * page_size
    end_index = start_index + page_size
    return items[start_index:end_index]
```
