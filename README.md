# 🚀 Blockbuster API – FastAPI + Neo4j  
API para gestionar afiliados, títulos, copias y rentas usando **FastAPI** y **Neo4j**.

---

## 📌 Requisitos previos

Asegúrate de tener instalado:

- **Python 3.10+**
- **Neo4j Desktop o Neo4j Server**
- **pip** o **conda**
- **Driver Neo4j Bolt en ejecución**
- **Uvicorn** (se instala automáticamente)

---

## 🗂️ Estructura del proyecto

blockbuster-python/
│
├── app/
│ ├── cruds/
│ │ ├── crudRenta.py
│ │ ├── crudTitulo.py
│ │ └── crudAfiliado.py
│ ├── routes/
│ │ ├── renta_routes.py
│ │ ├── titulo_routes.py
│ │ └── afiliado_routes.py
│ ├── database.py
│ ├── main.py
│ └── models.py
│
├── requirements.txt
└── README.md


## Instalar dependencias
pip install -r requirements.txt


## Configurar Neo4j

Edita tu archivo app/database.py y coloca tus credenciales:

NEO4J_URI = "bolt://localhost:7687"
NEO4J_USER = "neo4j"
NEO4J_PASSWORD = "tu_password"


## Probar el proyecto con:
uvicorn app.main:app --reload
