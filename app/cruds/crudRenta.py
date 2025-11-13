from datetime import date, timedelta

# ========================
# CREATE - Crear Renta (autoasigna copia disponible)
# ========================
def crear_renta(session, id_afiliado: int, id_titulo: int):
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
        raise ValueError(f"❌ Título con Id {id_titulo} no encontrado.")

    # --- Buscar copia disponible ---
    copia_query = """
    MATCH (t:Titulo {IdTitulo: $id_titulo})<-[:COPIA_DE]-(c:Copia)
    WHERE c.Estado = 'DISPONIBLE'
    RETURN c.IdCopia AS id_copia
    LIMIT 1
    """
    copia_record = session.run(copia_query, id_titulo=id_titulo).single()

    if not copia_record:
        raise ValueError(f"⚠️ No hay copias DISPONIBLES del título {id_titulo}.")

    id_copia = copia_record["id_copia"]

    # --- Crear la renta y actualizar estado ---
    create_query = """
    MATCH (a:Afiliado {IdAfiliado: $id_afiliado})
    MATCH (t:Titulo {IdTitulo: $id_titulo})
    MATCH (c:Copia {IdCopia: $id_copia})-[:COPIA_DE]->(t)
    CREATE (r:Renta {
        IdRenta: randomUUID(),
        FechaRenta: date(),
        FechaDevolucion: date() + duration({days: 2}),
        ValorRenta: 5000.00,
        MetodoPago: 'Tarjeta',
        Estado: 'ACTIVA'
    })
    CREATE (a)-[:REALIZO_RENTA]->(r)
    CREATE (r)-[:INCLUYE_TITULO]->(t)
    CREATE (r)-[:INCLUYE_COPIA]->(c)
    SET c.Estado = 'RENTADA'
    RETURN r.IdRenta AS id_renta, c.IdCopia AS copia_usada
    """

    result = session.run(
        create_query,
        id_afiliado=id_afiliado,
        id_titulo=id_titulo,
        id_copia=id_copia
    ).single()

    if not result:
        raise RuntimeError("⚠️ No se pudo crear la renta (sin resultados).")

    return {
        "id_renta": result["id_renta"],
        "id_copia": result["copia_usada"]
    }


# ========================
# READ - Historial de rentas
# ========================
def obtener_historial_rentas(session):
    query = """
    MATCH (a:Afiliado)-[:REALIZO_RENTA]->(r:Renta)-[:INCLUYE_TITULO]->(t:Titulo)
    RETURN
        toUpper(a.Nombres) + ' ' + toUpper(a.Apellidos) AS Afiliado,
        t.Titulo AS Titulo,
        date(r.FechaRenta) AS FechaRenta,
        duration.between(r.FechaRenta, r.FechaDevolucion).days AS DuracionDias
    ORDER BY r.FechaRenta DESC
    """
    return [record.data() for record in session.run(query)]


# ========================
# READ - Estadísticas de rentas
# ========================
def obtener_estadisticas_rentas(session):
    query = """
    MATCH (r:Renta)-[:INCLUYE_TITULO]->(t:Titulo)
    RETURN
        t.Titulo AS Titulo,
        count(r) AS CantidadRentas,
        sum(r.ValorRenta) AS TotalRentas
    ORDER BY CantidadRentas DESC
    """
    return [record.data() for record in session.run(query)]
