# app/cruds/crudVisualizacion.py

from app.auth.membership import validate_membership


def crear_visualizacion(session, id_afiliado: int, id_titulo: int, user: dict):

    # Se valida membresía ANTES de crear visualización
    validate_membership(user)

    # --- resto igual ---
    id_afiliado = int(id_afiliado)
    id_titulo = int(id_titulo)

    # verificar existencia
    check_query = """
    MATCH (a:Afiliado {IdAfiliado: $id_afiliado})
    OPTIONAL MATCH (t:Titulo {IdTitulo: $id_titulo})
    RETURN a IS NOT NULL AS afiliado_existe,
           t IS NOT NULL AS titulo_existe
    """
    check = session.run(check_query,
        id_afiliado=id_afiliado,
        id_titulo=id_titulo
    ).single()

    if not check["afiliado_existe"]:
        raise ValueError(f"❌ Afiliado con Id {id_afiliado} no encontrado.")

    if not check["titulo_existe"]:
        raise ValueError(f"❌ Título con Id {id_titulo} no encontrado.")

    # crear visualización
    query = """
    MATCH (a:Afiliado {IdAfiliado: $id_afiliado})
    MATCH (t:Titulo {IdTitulo: $id_titulo})
    CREATE (v:Visualizacion {
        IdVisualizacion: randomUUID(),
        FechaInicio: date(),
        Estado: 'INICIADA'
    })
    CREATE (a)-[:REALIZO_VISUALIZACION]->(v)
    CREATE (v)-[:TIENE_TITULO]->(t)
    RETURN v.IdVisualizacion AS id_visualizacion
    """

    result = session.run(query,
        id_afiliado=id_afiliado,
        id_titulo=id_titulo
    ).single()

    return {
        "id_visualizacion": result["id_visualizacion"]
    }


# app/cruds/crudVisualizacion.py

from app.auth.membership import validate_membership


def crear_visualizacion(session, id_afiliado: int, id_titulo: int, user: dict):
    validate_membership(user)

    id_afiliado = int(id_afiliado)
    id_titulo = int(id_titulo)

    check_query = """
    MATCH (a:Afiliado {IdAfiliado: $id_afiliado})
    OPTIONAL MATCH (t:Titulo {IdTitulo: $id_titulo})
    RETURN a IS NOT NULL AS afiliado_existe,
           t IS NOT NULL AS titulo_existe
    """
    check = session.run(check_query,
        id_afiliado=id_afiliado,
        id_titulo=id_titulo
    ).single()

    if not check["afiliado_existe"]:
        raise ValueError(f"❌ Afiliado con Id {id_afiliado} no encontrado.")

    if not check["titulo_existe"]:
        raise ValueError(f"❌ Título con Id {id_titulo} no encontrado.")

    query = """
    MATCH (a:Afiliado {IdAfiliado: $id_afiliado})
    MATCH (t:Titulo {IdTitulo: $id_titulo})
    CREATE (v:Visualizacion {
        IdVisualizacion: randomUUID(),
        FechaInicio: date(),
        Estado: 'INICIADA'
    })
    CREATE (a)-[:REALIZO_VISUALIZACION]->(v)
    CREATE (v)-[:TIENE_TITULO]->(t)
    RETURN v.IdVisualizacion AS id_visualizacion
    """

    result = session.run(query,
        id_afiliado=id_afiliado,
        id_titulo=id_titulo
    ).single()

    return {
        "id_visualizacion": result["id_visualizacion"]
    }


def obtener_historial_visualizaciones(session):
    query = """
    MATCH (a:Afiliado)-[:REALIZO_VISUALIZACION]->(v:Visualizacion)-[:TIENE_TITULO]->(t:Titulo)
    RETURN a.IdAfiliado AS afiliado,
           v.IdVisualizacion AS id_visualizacion,
           v.FechaInicio AS fecha_inicio,
           v.Estado AS estado,
           t.IdTitulo AS titulo,
           t.Nombre AS nombre
    ORDER BY fecha_inicio DESC
    """

    result = session.run(query)
    return [record.data() for record in result]


def obtener_estadisticas_visualizaciones(session):
    query = """
    MATCH (v:Visualizacion)-[:TIENE_TITULO]->(t:Titulo)
    RETURN t.Nombre AS titulo,
           COUNT(v) AS total_visualizaciones
    ORDER BY total_visualizaciones DESC
    """

    result = session.run(query)
    return [record.data() for record in result]
