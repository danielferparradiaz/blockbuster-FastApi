from datetime import date, timedelta

# ========================
# CREATE - Crear Renta
# ========================
def crear_renta(session, id_afiliado: int, id_copia: int, id_titulo: int):
    query = """
    MATCH (a:Afiliado {IdAfiliado: $id_afiliado})
    MATCH (t:Titulo {IdTitulo: $id_titulo})
    MATCH (c:Copia {IdCopia: $id_copia})-[:COPIA_DE]->(t)
    CREATE (r:Renta {
        IdRenta: randomUUID(),
        FechaRenta: date(),
        FechaDevolucion: date() + duration({days: 2}),
        ValorRenta: 5000.00,
        Estado: 'ACTIVA'
    })
    CREATE (a)-[:REALIZO_RENTA]->(r)
    CREATE (r)-[:INCLUYE_TITULO]->(t)
    CREATE (r)-[:INCLUYE_COPIA]->(c)
    SET c.Estado = 'RENTADA'
    RETURN r.IdRenta AS id_renta
    """
    result = session.run(query, id_afiliado=id_afiliado, id_copia=id_copia, id_titulo=id_titulo)
    return result.single()["id_renta"]


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
