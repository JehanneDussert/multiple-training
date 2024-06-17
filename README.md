# multiple-training

The different subjects I train on.

## Database

### SQL

__Relational database:__ system that saves information in the form of a two-dimensional table called a table or relationship.

__SQL :__ standard used by PostgreSQL, MySQL, MariaDB, SQL Server, SQLite, Oracle...

__Table creation & handling:__
```bash
# CREATE TABLE
CREATE TABLE recipes (
    title VARCHAR(150),
    slug VARCHAR(50),
    content TEXT,
    duration SMALLINT,
    online BOOLEAN,
    created_at DATETIME
);

# INSERT new element
INSERT INTO recipes (
    title, 
    slug, 
    content, 
    duration, 
    online, 
    created_at
) VALUES (
    'Soupe',
    'soupe',
    'Contenu de test',
    10,
    FALSE,
    1718616853
);

# GET element: expressions
SELECT * 
FROM recipes
WHERE slug = 'soup'

SELECT * 
FROM recipes
WHERE duration BETWEEN 0 and 20

SELECT * 
FROM recipes
WHERE slug IN ('soup')

# DELETE element
DELETE from recipes WHERE title = 'Soupe'

# UPDATE element
UPDATE recipes SET title = 'Soupe de légume' WHERE title = 'Soupe'
```

## Backend

### Scraping

#### Override protections against scraping

- [x] User-Agent: allows you to pretend to be a browser by integrating the User-Agent in the Headers -> add User-Agent headers to your request.
- [x] Headless browsing: bypass JavaScript problems for instance with Selenium. A script will control browser activity and enable browser-server requests to be made without being detected.
- [x] Rate limit: can be solved with proxy network / paid solutions.

[Documentation](https://www.youtube.com/watch?v=HCV6nEACQo4&t=151s)

### FastAPI

__Requests types:__ POST, GET, DELETE, PUT -> CRUD (Create, Read, Update, Delete)
__Decorators:__ with FastAPI, enables to define routes.

Command line:
```
uvicorn main:app --reload
```

__Routes definition:__
```bash

# GET an object
@app.get("/my_route")
def get_my_route() -> dict:
    return { "key": value }

# POST/CREATE new object
@app.post("/my_route")
def create_my_route(my_object: Object) -> Object:
    if my_object.id in list_objects:
        raise HTTPException(status_code=404, detail=f"L'objet {my_object.id} existe déjà")
    
    list_objects[my_object.id] = asdict(my_object)

    return my_object

# PUT/MODIFY an object
@app.put("/my_route")
def update_my_route(my_object: Object, id: int = Path(ge=1)) -> Object:
    if id not in list_objects:
        raise HTTPException(status_code=404, detail=f"L'objet n'existe pas")

    list_objects[id] = asdict(my_object)

    return my_object

# DELETE an object
@app.delete("/my_route/{id}")
def delete_object(id: int = Path(ge=1)) -> Object:
    if id in list_objects:
        object = Object(**list_objects[id])
        del list_objects[id]
        
        return object
    
    raise HTTPException(status_code=404, detail=f"L'objet n'existe pas")

# GET all types
@app.get("/types")
def get_all_types() -> list[str]:
    types = []

    for object in list_objects:
        for type in object["types"]:
            if type not in types:
                types.append(types)

    types.sort()

    return types
```

__CORS :__ Cross_Origin Resource Sharing.

[Documentation](https://www.youtube.com/watch?v=0-yncL0bqZs)