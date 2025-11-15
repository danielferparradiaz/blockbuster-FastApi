# app/cruds/crudVisualizacion.py

from app.auth.membership import validate_membership


def crear_visualizacion(session, id_afiliado: int, id_titulo: int, user: dict):

    # 🔒 validar membresía ANTES de crear visualización
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
