from neo4j import Session
from app.domain.schemas.schemas import AfiliadoCreate, AfiliadoUpdate
from typing import List, Dict, Any, Optional

def crear_afiliado(session: Session, afiliado: AfiliadoCreate) -> Dict[str, Any]:
    query = """
    CREATE (a:Afiliado {
        IdAfiliado: $IdAfiliado,
        Nombres: $Nombres,
        Apellidos: $Apellidos,
        Direccion: $Direccion,
        Telefono: $Telefono,
        FechaVinculacion: date($FechaVinculacion),
        Sexo: $Sexo,
        FechaNacimiento: date($FechaNacimiento),
        NivelMembresia: $NivelMembresia,
        EstadoMembresia: $EstadoMembresia,
        FechaInicioMembresia: date($FechaInicioMembresia),
        FechaFinMembresia: date($FechaFinMembresia)
    })
    RETURN a
    """
    result = session.run(query, **afiliado.model_dump())
    record = result.single()
    if record:
        return record["a"]
    return {}

def obtener_afiliados(session: Session) -> List[Dict[str, Any]]:
    query = """
    MATCH (a:Afiliado)
    RETURN a.IdAfiliado AS IdAfiliado, a.Nombres, a.Apellidos, a.NivelMembresia, a.EstadoMembresia
    ORDER BY a.IdAfiliado
    """
    return [record.data() for record in session.run(query)]

def obtener_afiliado_por_id(session: Session, id_afiliado: int) -> Optional[Dict[str, Any]]:
    query = """
    MATCH (a:Afiliado {IdAfiliado: $id_afiliado})
    RETURN properties(a) AS afiliado
    """
    result = session.run(query, id_afiliado=id_afiliado).single()
    return result["afiliado"] if result else None

def actualizar_afiliado(session: Session, id_afiliado: int, datos: AfiliadoUpdate) -> Optional[Dict[str, Any]]:
    # Filtrar solo los campos que no son None para generar la cláusula SET
    updates = {k: v for k, v in datos.model_dump(exclude_unset=True).items()}
    
    if not updates:
        return obtener_afiliado_por_id(session, id_afiliado)

    set_clauses = [f"a.{k} = ${k}" for k in updates.keys()]
    
    query = f"""
    MATCH (a:Afiliado {{IdAfiliado: $id_afiliado}})
    SET {', '.join(set_clauses)}
    RETURN properties(a) AS afiliado
    """
    
    result = session.run(query, id_afiliado=id_afiliado, **updates).single()
    return result["afiliado"] if result else None

def eliminar_afiliado(session: Session, id_afiliado: int) -> bool:
    query = """
    MATCH (a:Afiliado {IdAfiliado: $id_afiliado})
    DETACH DELETE a
    """
    result = session.run(query, id_afiliado=id_afiliado)
    # Verifica si se eliminó al menos un nodo
    return result.summary().counters.nodes_deleted > 0