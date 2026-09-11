# Pagination

## Description

This project explores different techniques for paginating a dataset, a
common requirement when displaying large amounts of data across multiple
pages in an API or web application. It covers simple pagination, pagination
with hypermedia metadata, and pagination that remains stable even when data
is deleted between requests (deletion-resilient pagination).

## Learning Objectives

By the end of this project, you should be able to explain:

- How to paginate a dataset with simple `page` and `page_size` parameters
- How to paginate a dataset with hypermedia metadata (`hypermedia`)
- How to paginate a dataset when items are being deleted between requests,
  without changing the order or skipping items (deletion-resilient
  pagination)

## Requirements

- All files interpreted/compiled on Ubuntu 18.04 LTS using `python3` (version 3.7)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/env python3`
- Code should follow the `pycodestyle` style (version 2.5.\*)
- All files must be executable
- All modules, classes, and functions should have documentation
- All functions and coroutines must be type-annotated

## Files

| File                             | Description                                                                   |
| -------------------------------- | ----------------------------------------------------------------------------- |
| `0-simple_helper_function.py`    | `index_range` function that returns a tuple of start/end index for pagination |
| `1-simple_pagination.py`         | `Server` class with a `get_page` method for simple pagination                 |
| `2-hypermedia_pagination.py`     | Adds `get_hyper` method returning pagination metadata                         |
| `3-hypermedia_del_pagination.py` | Adds `get_hyper_index` method for deletion-resilient pagination               |

## Example Usage

```python
#!/usr/bin/env python3
"""Example usage of index_range."""
index_range = __import__('0-simple_helper_function').index_range

res = index_range(1, 7)
print(type(res))
print(res)
```

```
$ ./main.py
<class 'tuple'>
(0, 7)
```

## Author

Abeer Al-Saiari
