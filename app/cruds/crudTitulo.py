from neo4j import Session
from app.domain.schemas.schemas import TituloCreate, TituloUpdate
from typing import List, Dict, Any, Optional


# --- CREATE ---
def crear_titulo(session: Session, titulo: TituloCreate) -> Dict[str, Any]:
    query = """
    CREATE (t:Titulo {
        IdTitulo: $IdTitulo,
        Titulo: $Titulo,
        Rating: $Rating,
        Año: $Anio,
        Director: $Director,
        DuracionMin: $DuracionMin
    })
    RETURN t
    """
    # Renombramos 'Anio' a 'Año' para el Cypher si es necesario
    data = titulo.model_dump()
    data['Año'] = data.pop('Anio')
    
    result = session.run(query, **data)
    record = result.single()
    if record:
        return record["t"]
    return {}

# --- READ (Todos) ---
def obtener_titulos(session: Session) -> List[Dict[str, Any]]:
    query = """
    MATCH (t:Titulo)
    RETURN t.IdTitulo AS IdTitulo, t.Titulo, t.Director, t.Año
    ORDER BY t.IdTitulo
    """
    return [record.data() for record in session.run(query)]

# --- READ (Por ID) ---
def obtener_titulo_por_id(session: Session, id_titulo: int) -> Optional[Dict[str, Any]]:
    query = """
    MATCH (t:Titulo {IdTitulo: $id_titulo})
    RETURN properties(t) AS titulo
    """
    result = session.run(query, id_titulo=id_titulo).single()
    return result["titulo"] if result else None

# --- UPDATE ---
def actualizar_titulo(session: Session, id_titulo: int, datos: TituloUpdate) -> Optional[Dict[str, Any]]:
    updates = {k: v for k, v in datos.model_dump(exclude_unset=True).items()}
    
    if 'Anio' in updates:
        updates['Año'] = updates.pop('Anio')

    if not updates:
        return obtener_titulo_por_id(session, id_titulo)

    set_clauses = [f"t.{k} = ${k}" for k in updates.keys()]
    
    query = f"""
    MATCH (t:Titulo {{IdTitulo: $id_titulo}})
    SET {', '.join(set_clauses)}
    RETURN properties(t) AS titulo
    """
    
    result = session.run(query, id_titulo=id_titulo, **updates).single()
    return result["titulo"] if result else None

# --- DELETE ---
def eliminar_titulo(session: Session, id_titulo: int) -> bool:
    query = """
    MATCH (t:Titulo {IdTitulo: $id_titulo})
    DETACH DELETE t
    """
    result = session.run(query, id_titulo=id_titulo)
    return result.summary().counters.nodes_deleted > 0