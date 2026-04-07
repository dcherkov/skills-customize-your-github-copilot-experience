# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a RESTful API using the FastAPI framework in Python. You will create API endpoints that support creating, reading, updating, and deleting data, and use Pydantic models to validate request and response data.

## 📝 Tasks

### 🛠️ Set Up a FastAPI Application

#### Description
Install FastAPI and create a basic application with a working root endpoint that returns a welcome message.

#### Requirements
Completed program should:

- Install `fastapi` and `uvicorn` using pip.
- Create a FastAPI app instance in `starter-code.py`.
- Define a `GET /` endpoint that returns a JSON welcome message.
- Run successfully with `uvicorn starter-code:app --reload`.

Example response from `GET /`:

```json
{"message": "Welcome to the Book API!"}
```

### 🛠️ Define a Data Model and Create Items

#### Description
Define a Pydantic model for a resource of your choice (for example, a book, task, or student) and implement an endpoint to create new items.

#### Requirements
Completed program should:

- Define a Pydantic `BaseModel` class with at least three fields (e.g., `id`, `title`, `author`).
- Store created items in an in-memory list.
- Define a `POST /items` endpoint that accepts a request body matching the model and appends the item to the list.
- Return the created item as the response.

Example request body for `POST /items`:

```json
{"id": 1, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald"}
```

Example response:

```json
{"id": 1, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald"}
```

### 🛠️ Implement GET, PUT, and DELETE Endpoints

#### Description
Complete the CRUD API by adding endpoints to retrieve all items, retrieve a single item by ID, update an item, and delete an item.

#### Requirements
Completed program should:

- Define a `GET /items` endpoint that returns the full list of items.
- Define a `GET /items/{id}` endpoint that returns a single item by its ID, or returns a 404 error if not found.
- Define a `PUT /items/{id}` endpoint that updates an existing item by ID and returns the updated item.
- Define a `DELETE /items/{id}` endpoint that removes an item by ID and returns a confirmation message.

Example response from `DELETE /items/1`:

```json
{"message": "Item with id 1 has been deleted."}
```
