// =========================================
// 🧹 LIMPIEZA INICIAL
MATCH (n) DETACH DELETE n;

// =========================================
// 🧍‍♂️ NODOS: AFILIADOS (con membresía)
CREATE
  (a101:Afiliado {
    IdAfiliado:101, Nombres:'Antonio', Apellidos:'Rodríguez',
    Direccion:'Calle 1', Telefono:'5512573',
    FechaVinculacion:date('2010-01-01'),
    Sexo:'M', FechaNacimiento:date('1967-04-02'),
    NivelMembresia:'PREMIUM',
    EstadoMembresia:'ACTIVA',
    FechaInicioMembresia:date('2024-01-01'),
    FechaFinMembresia:date('2025-01-01')
  }),
  (a102:Afiliado {
    IdAfiliado:102, Nombres:'Nataly', Apellidos:'Martínez',
    Direccion:'Calle 1', Telefono:'5512573',
    FechaVinculacion:date('2010-01-01'),
    Sexo:'F', FechaNacimiento:date('1967-11-20'),
    NivelMembresia:'BÁSICA',
    EstadoMembresia:'ACTIVA',
    FechaInicioMembresia:date('2024-01-01'),
    FechaFinMembresia:date('2024-06-30')
  }),
  (a103:Afiliado {
    IdAfiliado:103, Nombres:'Natalia', Apellidos:'Rodríguez',
    Direccion:'Calle 1', Telefono:'5512573',
    FechaVinculacion:date('2010-01-01'),
    Sexo:'F', FechaNacimiento:date('1998-06-20'),
    NivelMembresia:'PREMIUM',
    EstadoMembresia:'ACTIVA',
    FechaInicioMembresia:date('2024-01-01'),
    FechaFinMembresia:date('2025-01-01')
  }),
  (a104:Afiliado {
    IdAfiliado:104, Nombres:'Sofía', Apellidos:'Rodríguez',
    Direccion:'Calle 1', Telefono:'5512573',
    FechaVinculacion:date('2010-02-28'),
    Sexo:'F', FechaNacimiento:date('1998-10-08'),
    NivelMembresia:'BÁSICA',
    EstadoMembresia:'INACTIVA',
    FechaInicioMembresia:date('2023-01-01'),
    FechaFinMembresia:date('2023-12-31')
  }),
  (a105:Afiliado {
    IdAfiliado:105, Nombres:'Ricardo', Apellidos:'Ortega',
    Direccion:'Calle 2', Telefono:'4665445',
    FechaVinculacion:date('2010-01-30'),
    Sexo:'M', FechaNacimiento:date('1980-10-01'),
    NivelMembresia:'PREMIUM',
    EstadoMembresia:'ACTIVA',
    FechaInicioMembresia:date('2024-02-01'),
    FechaFinMembresia:date('2026-02-01')
  }),
  (a106:Afiliado {
    IdAfiliado:106, Nombres:'Camila', Apellidos:'Ortega',
    Direccion:'Calle 2', Telefono:'4665448',
    FechaVinculacion:date('2010-02-08'),
    Sexo:'F', FechaNacimiento:date('1990-10-20'),
    NivelMembresia:'BÁSICA',
    EstadoMembresia:'ACTIVA',
    FechaInicioMembresia:date('2024-07-01'),
    FechaFinMembresia:date('2024-12-31')
  }),
  (a107:Afiliado {
    IdAfiliado:107, Nombres:'Diego', Apellidos:'Hernández',
    Direccion:'Cra 3', Telefono:'5789779',
    FechaVinculacion:date('2010-01-01'),
    Sexo:'M', FechaNacimiento:date('1957-07-10'),
    NivelMembresia:'VIP',
    EstadoMembresia:'ACTIVA',
    FechaInicioMembresia:date('2024-01-01'),
    FechaFinMembresia:date('2030-01-01')
  });

// Relaciones familiares
MATCH (a101:Afiliado {IdAfiliado:101}), (a102:Afiliado {IdAfiliado:102})
CREATE (a101)-[:ES_PAREJA_DE]->(a102);

MATCH (a101), (a103)
CREATE (a101)-[:ES_PADRE_DE]->(a103);

MATCH (a101), (a104)
CREATE (a101)-[:ES_PADRE_DE]->(a104);

MATCH (a105), (a106)
CREATE (a105)-[:ES_PAREJA_DE]->(a106);

// =========================================
// 🎬 TÍTULOS + CATEGORÍAS
CREATE
  (catFiccion:Categoria {nombre:'Ficción'}),
  (catSuspenso:Categoria {nombre:'Suspenso'}),
  (catAccion:Categoria {nombre:'Acción'}),
  (catNiños:Categoria {nombre:'Niños'}),

  (t92:Titulo {IdTitulo:92, Titulo:'Harry Potter y la Piedra Filosofal', Rating:'Todos', Año:2001, Director:'Chris Columbus', DuracionMin:152}),
  (t93:Titulo {IdTitulo:93, Titulo:'El Señor de los Anillos', Rating:'Todos', Año:2001, Director:'Peter Jackson', DuracionMin:178}),
  (t94:Titulo {IdTitulo:94, Titulo:'Monsters Inc.', Rating:'Todos', Año:2001, Director:'Pete Docter', DuracionMin:92}),
  (t95:Titulo {IdTitulo:95, Titulo:'Insomnia', Rating:'Mayores 12', Año:2002, Director:'Christopher Nolan', DuracionMin:118}),
  (t96:Titulo {IdTitulo:96, Titulo:'Rápido y Furioso', Rating:'Mayores 18', Año:2001, Director:'Rob Cohen', DuracionMin:106}),
  (t97:Titulo {IdTitulo:97, Titulo:'Rápido y Furioso II', Rating:'Mayores 18', Año:2003, Director:'John Singleton', DuracionMin:108});

// Categorías
CREATE
  (t92)-[:PERTENECE_A]->(catFiccion),
  (t93)-[:PERTENECE_A]->(catFiccion),
  (t94)-[:PERTENECE_A]->(catNiños),
  (t95)-[:PERTENECE_A]->(catSuspenso),
  (t96)-[:PERTENECE_A]->(catAccion),
  (t97)-[:PERTENECE_A]->(catAccion);

// =========================================
// 💿 COPIAS
CREATE
  (c1t92:Copia {IdCopia:101, Estado:'DISPONIBLE'})-[:DE_FORMATO]->(:Formato {nombre:'DVD'}),
  (c1t93:Copia {IdCopia:201, Estado:'DISPONIBLE'})-[:DE_FORMATO]->(:Formato {nombre:'DVD'}),
  (c2t93:Copia {IdCopia:202, Estado:'DISPONIBLE'})-[:DE_FORMATO]->(:Formato {nombre:'BLUERAY'}),
  (c1t94:Copia {IdCopia:301, Estado:'DISPONIBLE'})-[:DE_FORMATO]->(:Formato {nombre:'DVD'}),
  (c1t95:Copia {IdCopia:401, Estado:'DISPONIBLE'})-[:DE_FORMATO]->(:Formato {nombre:'DVD'}),
  (c2t95:Copia {IdCopia:402, Estado:'DISPONIBLE'})-[:DE_FORMATO]->(:Formato {nombre:'BLUERAY'}),
  (c3t95:Copia {IdCopia:403, Estado:'DISPONIBLE'})-[:DE_FORMATO]->(:Formato {nombre:'BLUERAY'}),
  (c1t96:Copia {IdCopia:501, Estado:'DISPONIBLE'})-[:DE_FORMATO]->(:Formato {nombre:'BLUERAY'}),
  (c1t97:Copia {IdCopia:601, Estado:'DISPONIBLE'})-[:DE_FORMATO]->(:Formato {nombre:'BLUERAY'});

// Relación copia → título
MATCH (t:Titulo)
MATCH (c:Copia)
WHERE c.IdCopia STARTS WITH SUBSTRING(toString(t.IdTitulo), 0, 1)
CREATE (c)-[:COPIA_DE]->(t)

// =========================================
// 📺 VISUALIZACIÓN (antes RENTA)
// TODO 2 aplicado
CREATE
  (v1:Visualizacion {
    IdVisualizacion:1,
    FechaInicio:date('2024-11-01'),
    FechaFin:date('2024-11-03'),
    Estado:'FINALIZADA'
  });

MATCH (a101:Afiliado {IdAfiliado:101}),
      (t92:Titulo {IdTitulo:92}),
      (c1t92:Copia {IdCopia:101}),
      (v1:Visualizacion)
CREATE
  (a101)-[:REALIZO_VISUALIZACION]->(v1),
  (v1)-[:TIENE_TITULO]->(t92),
  (v1)-[:USA_COPIA]->(c1t92);

// =========================================
// 🌟 Gustos
MATCH (a103:Afiliado), (catFiccion:Categoria)
CREATE (a103)-[:LE_GUSTA]->(catFiccion);

MATCH (a106:Afiliado), (catAccion:Categoria)
CREATE (a106)-[:LE_GUSTA]->(catAccion);

MATCH (a107:Afiliado), (catSuspenso:Categoria)
CREATE (a107)-[:LE_GUSTA]->(catSuspenso);
