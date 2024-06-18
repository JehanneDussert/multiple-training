# multiple-training

The different subjects I train on.

## 🛢 Database

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

## 🛠️ Backend

### File organization

#### 📁 /app

__crud.py:__ interaction functions w/ DB
__database.py:__ ORM creation (for instance: SQLAlchemy), engine & sessions creation to interact w/ DB, base classes definition
__model.py:__ SQLAlchemy classes to interact w/ DB table
__schemas.py:__ classes used to creates objects

#### 📁 /env

Project configuration.

#### 📁 /migrations

Store SQL tables & SQLite DB.

#### 📁 /tests

Using pytest to check if routes return a correct answer.

### ⛏️ Scraping

#### Override protections against scraping

- [x] User-Agent: allows you to pretend to be a browser by integrating the User-Agent in the Headers -> add User-Agent headers to your request.
- [x] Headless browsing: bypass JavaScript problems for instance with Selenium. A script will control browser activity and enable browser-server requests to be made without being detected.
- [x] Rate limit: can be solved with proxy network / paid solutions.

[Documentation](https://www.youtube.com/watch?v=HCV6nEACQo4&t=151s)

### 🏃🏻‍♀️ FastAPI

__Requests types:__ POST, GET, DELETE, PUT -> CRUD (Create, Read, Update, Delete)<br/>
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

__CORS :__ Cross-Origin Resource Sharing. This may or may not allow a site from a different origin to access our API by defining the authorized routes.

```bash
from fastapi.middleware.cors import CORSMiddleware

# For instance:
origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:5173",
    "http://localhost:3000",
    "http://localhost:4173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

[Documentation](https://www.youtube.com/watch?v=0-yncL0bqZs)

### SQLAlchemy

__SQLAlchemy__ is an __Object-Relational Mapping (ORM)__, a layer of abstraction between the code and the DB. Converts SQL queries into objects and vice versa.

__Other examples of ORM :__ Sequelize (NodeJS - MySQL, PostgreSQL, SQLite), Django ORM (same), Hibernate (Java), Ecto (Elixir - PostegreSQL)...