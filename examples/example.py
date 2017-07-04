from switch_client import *

#
# WARNING
# This example assumes that the related database has a list named "test_2"
# 

client = SwitchClient(api_key=<KEY>,
                      api_secret=<SECRET>)

# Returns created lists in the database
print client.lists()

# Add method use case example
print client.add(list_name='test_2', json_data={
    "BookGuid": "2D72BCE5-2897-4C52-BD22-D5079DA5C976",
    "Title": "Lorem Ipsum Dolor",
    "Author": "Sit Amet",
    "IsActive": 1
})

# Update method use case example
print client.update(list_name='test_2', list_item_id=<LIST_ITEM_ID>, json_data={
    "BookGuid": "2D72BCE5-2897-4C52-BD22-D5079DA5C976",
    "Title": "Lorem Ipsum",
    "Author": "Sit Amet",
    "IsActive": 0
})

# Delete method use case example
print client.delete(list_name='test_2', list_item_id=<LIST_ITEM_ID>)

# List(select) method use case example 1
print client.list(list_name="test_2", query={
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
print client.list(list_name="test_2", query={
    "count": 10,
    "page": 0,
    "where": [],
    "order": {
        "type": "DESC",
        "by": "id"
    }
})
