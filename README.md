# switchdb_client - the Python 2.7 library for the Switch Database REST API

Switch API is the primary endpoint of data sevices and Switch DB's platform. You can do adding, editing, deleting or listing data works to your database with query operations by using this low-level API based on HTTP.

- API version: 1.2.1
- SDK version: 0.1.0
- Build date: 2017-07-04

## Installation
You can download and copy to root directory of the project.

<a name="getting-started"></a>
## Getting Started

```python
from switchdb_client import *

#
# WARNING
# This example assumes that the related database has a list named "test_2"
# 

client = SwitchClient(api_key=<KEY>,
                      api_secret=<SECRET>)

# Returns created lists in the database
client.lists()

# Add method use case example
client.add(list_name='test_2', json_data={
    "BookGuid": "2D72BCE5-2897-4C52-BD22-D5079DA5C976",
    "Title": "Lorem Ipsum Dolor",
    "Author": "Sit Amet",
    "IsActive": 1
})

# Update method use case example
client.update(list_name='test_2', list_item_id=<LIST_ITEM_ID>, json_data={
    "BookGuid": "2D72BCE5-2897-4C52-BD22-D5079DA5C976",
    "Title": "Lorem Ipsum",
    "Author": "Sit Amet",
    "IsActive": 0
})

# Delete method use case example
client.delete(list_name='test_2', list_item_id=<LIST_ITEM_ID>)

# List(select) method use case example 1
client.list(list_name="test_2", query={
    "list": "test_2",  # optional
    "count": 10,
    "page": 0,
    "where": [],
    "order": {
        "type": "DESC",
        "by": "id"
    }
})

# List(select) method use case example 2
client.list(list_name="test_2", query={
    "count": 10,
    "page": 0,
    "where": [],
    "order": {
        "type": "DESC",
        "by": "id"
    }
})
```

 ## Authors

* **[Mehmet Orkun Uçkunlar](https://github.com/morkun)** - *Initial commit*
