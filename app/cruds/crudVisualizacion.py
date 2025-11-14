from datetime import date, timedelta

# ========================
# CREATE - Crear Visualización
# ========================
def crear_visualizacion(session, id_afiliado: int, id_titulo: int):
    # Forzamos tipos numéricos
    id_afiliado = int(id_afiliado)
    id_titulo = int(id_titulo)

    # --- Verificar existencia de afiliado y título ---
    check_query = """
    MATCH (a:Afiliado {IdAfiliado: $id_afiliado})
    OPTIONAL MATCH (t:Titulo {IdTitulo: $id_titulo})
    RETURN a IS NOT NULL AS afiliado_existe,
           t IS NOT NULL AS titulo_existe
    """
    check = session.run(
        check_query,
        id_afiliado=id_afiliado,
        id_titulo=id_titulo
    ).single()

    if not check["afiliado_existe"]:
        raise ValueError(f"❌ Afiliado con Id {id_afiliado} no encontrado.")
    if not check["titulo_existe"]:
        # Asumiendo que cualquier título es "visualizable" si existe.
        raise ValueError(f"❌ Título con Id {id_titulo} no encontrado.")

    # --- Crear la Visualización ---
    create_query = """
    MATCH (a:Afiliado {IdAfiliado: $id_afiliado})
    MATCH (t:Titulo {IdTitulo: $id_titulo})
    CREATE (v:Visualizacion {
        IdVisualizacion: randomUUID(),
        FechaInicio: date(),
        Estado: 'INICIADA' // O 'FINALIZADA' si la creas como finalizada de inmediato
    })
    CREATE (a)-[:REALIZO_VISUALIZACION]->(v)
    CREATE (v)-[:TIENE_TITULO]->(t)
    RETURN v.IdVisualizacion AS id_visualizacion
    """

    result = session.run(
        create_query,
        id_afiliado=id_afiliado,
        id_titulo=id_titulo
    ).single()

    if not result:
        raise RuntimeError("⚠️ No se pudo crear la visualización (sin resultados).")

    return {
        "id_visualizacion": result["id_visualizacion"]
    }


# ========================
# READ - Historial de visualizaciones
# ========================
def obtener_historial_visualizaciones(session):
    query = """
    MATCH (a:Afiliado)-[:REALIZO_VISUALIZACION]->(v:Visualizacion)-[:TIENE_TITULO]->(t:Titulo)
    RETURN
        toUpper(a.Nombres) + ' ' + toUpper(a.Apellidos) AS Afiliado,
        t.Titulo AS Titulo,
        date(v.FechaInicio) AS FechaInicio,
        v.Estado AS Estado
    ORDER BY v.FechaInicio DESC
    """
    return [record.data() for record in session.run(query)]


# ========================
# READ - Estadísticas de visualizaciones
# ========================
def obtener_estadisticas_visualizaciones(session):
    # Ya que no hay un ValorRenta, las estadísticas se centran en la cantidad.
    query = """
    MATCH (v:Visualizacion)-[:TIENE_TITULO]->(t:Titulo)
    RETURN
        t.Titulo AS Titulo,
        count(v) AS CantidadVisualizaciones
    ORDER BY CantidadVisualizaciones DESC
    """
    return [record.data() for record in session.run(query)]