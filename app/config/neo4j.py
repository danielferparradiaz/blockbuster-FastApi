from neo4j import GraphDatabase

# Configuración del driver de Neo4j
# (ajusta las credenciales y el URI a tu entorno)
uri = "bolt://localhost:7687"
user = "neo4j"
password = "tu_password"

driver = GraphDatabase.driver(uri, auth=(user, password))

def get_session():
    # Context manager para usar dentro de rutas
    session = driver.session()
    try:
        yield session
    finally:
        session.close()
