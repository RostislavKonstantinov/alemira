# Alemira


##Deploy

To start project, run (from the root folder): 

    docker-compose up -d
    
If it's a first run, DB will be populated with dummy data.


##Usage


###Assignments

###Getting the list of items
`GET /api/assignment_list/`

Result is paginated, so if you want to get an exact page:
`GET /api/assignment_list/?page=2`

###Creating an item
`POST /api/assignment_list/`

Payload
```json
{ 
    "description": "str/max_2000_char/required"
 }
```

###Getting an item by pk (with all related hints)
`GET /api/assignment_details/<pk>/`

###Update an item by pk
`PUT /api/assignment_details/<pk>/`

Payload
```json
{ 
    "description": "str/max_2000_char/required"
 }
```

###Delete an item by pk
`DELETE /api/assignment_details/<pk>/`



###Hints

###Getting the list of items
`GET /api/hint_list/`

Result is paginated, so if you want to get an exact page:
`GET /api/hint_list/?page=2`

You can filter data by:
- text in description (icontains) get param: 'description'. Example `GET /api/hint_list/?description=assignment%209`
- date of creation. get param: 'lte' and 'gte'. Example `GET /api/hint_list/?lte=2021-01-26T11:26:48.272131`

Filter uses "AND" logic.

###Creating an item
`POST /api/hint_list/`

Payload
```json
{ 
    "description": "str/max_2000_char/required",
    "assignment": "int/required"
 }
```

###Getting an item by pk
`GET /api/hint_details/<pk>/`

###Update an item by pk
`PUT /api/hint_details/<pk>/`

Payload
```json
{ 
    "description": "str/max_2000_char/required",
    "assignment": "int/required"
 }
```

###Delete an item by pk
`DELETE /api/hint_details/<pk>/`



