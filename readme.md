# 🚀 FastAPI & PostgreSQL REST API

[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white)](https://www.sqlalchemy.org/)
[![Pydantic](https://img.shields.io/badge/Pydantic-E92063?style=for-the-badge&logo=pydantic&logoColor=white)](https://docs.pydantic.dev/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Uvicorn](https://img.shields.io/badge/Uvicorn-4053D6?style=for-the-badge&logo=uvicorn&logoColor=white)](https://www.uvicorn.org/)

A RESTful Web API for product inventory management built with **FastAPI**, **SQLAlchemy ORM**, **PostgreSQL**, **Pydantic v2**, and **Uvicorn**.

---

## 📌 Features

- **RESTful API Architecture:** Clean and modular backend API designed for handling product resource endpoints.
- **Complete CRUD Functionality:** Full Create, Read, Update, and Delete operations for managing product inventories.
- **Relational Data Persistence:** PostgreSQL integration using **SQLAlchemy ORM** for database interaction and session management.
- **Data Validation & Aliasing:** Strict schema validation with **Pydantic v2**, supporting field aliases (`qty` / `quantity`) and custom response serialization.
- **Automatic DB Seeding:** Automated table creation and default database seeding upon application launch.
- **CORS Enabled:** Cross-Origin Resource Sharing middleware configured for client integrations.
- **Interactive Documentation:** Auto-generated OpenAPI documentation via Swagger UI (`/docs`) and ReDoc (`/redoc`).

---

## 🛠️ Tech Stack

- **Framework:** [FastAPI](https://fastapi.tiangolo.com/)
- **ORM:** [SQLAlchemy](https://www.sqlalchemy.org/)
- **Data Validation:** [Pydantic v2](https://docs.pydantic.dev/)
- **Database:** [PostgreSQL](https://www.postgresql.org/) (`psycopg2`)
- **ASGI Server:** [Uvicorn](https://www.uvicorn.org/)
- **Language:** Python 3.x

---

## 📂 Project Structure

```text
Flask-API/
├── main.py              # FastAPI application entry point, route handlers, & CORS configuration
├── database.py          # PostgreSQL connection engine and SessionLocal setup
├── database_models.py   # SQLAlchemy ORM database models (Products table schema)
├── models.py            # Pydantic data schemas, validation aliases, & serialization
├── readme.md            # Project documentation
└── .gitignore           # Git ignore rules
```

---

## ⚙️ Getting Started

### **Prerequisites**

Ensure you have the following installed on your system:
- **Python 3.8+**
- **PostgreSQL Database Server**

---

### **Setup & Execution**

1. **Activate Virtual Environment:**
   ```bash
   source myenv/bin/activate    # On macOS/Linux
   # myenv\Scripts\activate     # On Windows
   ```

2. **Install Dependencies:**
   ```bash
   pip install fastapi uvicorn sqlalchemy psycopg2-binary pydantic
   ```

3. **Configure Database Connection:**
   Update the PostgreSQL connection string in `database.py`:
   ```python
   db_url = "postgresql://<username>:<password>@localhost:5432/<database_name>"
   ```

4. **Run the API Server:**
   ```bash
   uvicorn main:app --reload
   ```
   - **Base URL:** `http://127.0.0.1:8000`
   - **Interactive API Docs (Swagger UI):** `http://127.0.0.1:8000/docs`
   - **Alternative API Docs (ReDoc):** `http://127.0.0.1:8000/redoc`

---

## 📡 API Endpoints Reference

| Method | Endpoint | Description | Status Code |
| :--- | :--- | :--- | :--- |
| `GET` | `/` | API welcome greeting | `200 OK` |
| `GET` | `/products` or `/products/` | Retrieve all products | `200 OK` |
| `GET` | `/products/{id}` or `/product/{id}` | Retrieve a specific product by ID | `200 OK` / `404 Not Found` |
| `POST` | `/products` or `/product` | Create a new product | `201 Created` / `409 Conflict` |
| `PUT` | `/products/{id}` or `/product/{id}` | Update an existing product by ID | `200 OK` / `404 Not Found` |
| `DELETE` | `/products/{id}` or `/product/{id}` | Delete a product by ID | `200 OK` / `404 Not Found` |

---

## 📦 Data Schema Example

**Product Payload (JSON):**
```json
{
  "id": 1,
  "name": "Asus Vivobook S14",
  "description": "Windows Laptop",
  "price": 60000.0,
  "qty": 10
}
```

---

## 🙏 Acknowledgements & Learning Resource

Special thanks to **Navin Reddy** and the **[Telusko](https://www.youtube.com/@Telusko)** YouTube channel! 🎓

I learned REST API development, FastAPI backend design, PostgreSQL database integration, and SQLAlchemy ORM through Telusko's beginner-friendly tutorials, which made complex API concepts very easy to understand and implement.

---

## 📜 License

This project is created for educational and practice purposes.