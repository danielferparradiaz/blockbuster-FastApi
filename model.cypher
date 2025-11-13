// =========================================
// 🧹 LIMPIEZA INICIAL
MATCH (n) DETACH DELETE n;

// =========================================
// 🧍‍♂️ NODOS: AFILIADOS
CREATE
  (a101:Afiliado {
    IdAfiliado:101, Nombres:'Antonio', Apellidos:'Rodríguez',
    Direccion:'Calle 1', Telefono:'5512573', FechaVinculacion:date('2010-01-01'),
    Sexo:'M', FechaNacimiento:date('1967-04-02'), NivelMembresia:'PREMIUM'
  }),
  (a102:Afiliado {
    IdAfiliado:102, Nombres:'Nataly', Apellidos:'Martínez',
    Direccion:'Calle 1', Telefono:'5512573', FechaVinculacion:date('2010-01-01'),
    Sexo:'F', FechaNacimiento:date('1967-11-20'), NivelMembresia:'BÁSICA'
  }),
  (a103:Afiliado {
    IdAfiliado:103, Nombres:'Natalia', Apellidos:'Rodríguez',
    Direccion:'Calle 1', Telefono:'5512573', FechaVinculacion:date('2010-01-01'),
    Sexo:'F', FechaNacimiento:date('1998-06-20'), NivelMembresia:'PREMIUM'
  }),
  (a104:Afiliado {
    IdAfiliado:104, Nombres:'Sofía', Apellidos:'Rodríguez',
    Direccion:'Calle 1', Telefono:'5512573', FechaVinculacion:date('2010-02-28'),
    Sexo:'F', FechaNacimiento:date('1998-10-08'), NivelMembresia:'BÁSICA'
  }),
  (a105:Afiliado {
    IdAfiliado:105, Nombres:'Ricardo', Apellidos:'Ortega',
    Direccion:'Calle 2', Telefono:'4665445', FechaVinculacion:date('2010-01-30'),
    Sexo:'M', FechaNacimiento:date('1980-10-01'), NivelMembresia:'PREMIUM'
  }),
  (a106:Afiliado {
    IdAfiliado:106, Nombres:'Camila', Apellidos:'Ortega',
    Direccion:'Calle 2', Telefono:'4665448', FechaVinculacion:date('2010-02-08'),
    Sexo:'F', FechaNacimiento:date('1990-10-20'), NivelMembresia:'BÁSICA'
  }),
  (a107:Afiliado {
    IdAfiliado:107, Nombres:'Diego', Apellidos:'Hernández',
    Direccion:'Cra 3', Telefono:'5789779', FechaVinculacion:date('2010-01-01'),
    Sexo:'M', FechaNacimiento:date('1957-07-10'), NivelMembresia:'VIP'
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
// 🎬 NODOS: TÍTULOS + CATEGORÍAS
CREATE
  (catFiccion:Categoria {nombre:'Ficción'}),
  (catSuspenso:Categoria {nombre:'Suspenso'}),
  (catAccion:Categoria {nombre:'Acción'}),
  (catNiños:Categoria {nombre:'Niños'}),

  (t92:Titulo {IdTitulo:92, Titulo:'Harry Potter y la Piedra Filosofal', Rating:'Todos', Año:2001, Director:'Chris Columbus', DuracionMin:152}),
  (t93:Titulo {IdTitulo:93, Titulo:'El Señor de los Anillos: La Comunidad del Anillo', Rating:'Todos', Año:2001, Director:'Peter Jackson', DuracionMin:178}),
  (t94:Titulo {IdTitulo:94, Titulo:'Monsters Inc.', Rating:'Todos', Año:2001, Director:'Pete Docter', DuracionMin:92}),
  (t95:Titulo {IdTitulo:95, Titulo:'Insomnia', Rating:'Mayores 12', Año:2002, Director:'Christopher Nolan', DuracionMin:118}),
  (t96:Titulo {IdTitulo:96, Titulo:'Rápido y Furioso', Rating:'Mayores 18', Año:2001, Director:'Rob Cohen', DuracionMin:106}),
  (t97:Titulo {IdTitulo:97, Titulo:'Rápido y Furioso II', Rating:'Mayores 18', Año:2003, Director:'John Singleton', DuracionMin:108});

// Vinculamos Títulos con Categorías
CREATE
  (t92)-[:PERTENECE_A]->(catFiccion),
  (t93)-[:PERTENECE_A]->(catFiccion),
  (t94)-[:PERTENECE_A]->(catNiños),
  (t95)-[:PERTENECE_A]->(catSuspenso),
  (t96)-[:PERTENECE_A]->(catAccion),
  (t97)-[:PERTENECE_A]->(catAccion);

// =========================================
// 💿 NODOS: COPIAS y FORMATOS
CREATE
  (fDVD:Formato {nombre:'DVD'}),
  (fBlu:Formato {nombre:'BLUERAY'}),

  (c1t92:Copia {IdCopia:101, Estado:'DISPONIBLE'})-[:DE_FORMATO]->(fDVD),
  (c1t93:Copia {IdCopia:201, Estado:'DISPONIBLE'})-[:DE_FORMATO]->(fDVD),
  (c2t93:Copia {IdCopia:202, Estado:'DISPONIBLE'})-[:DE_FORMATO]->(fBlu),
  (c1t94:Copia {IdCopia:301, Estado:'DISPONIBLE'})-[:DE_FORMATO]->(fDVD),
  (c1t95:Copia {IdCopia:401, Estado:'DISPONIBLE'})-[:DE_FORMATO]->(fDVD),
  (c2t95:Copia {IdCopia:402, Estado:'DISPONIBLE'})-[:DE_FORMATO]->(fBlu),
  (c3t95:Copia {IdCopia:403, Estado:'RENTADA'})-[:DE_FORMATO]->(fBlu),
  (c1t96:Copia {IdCopia:501, Estado:'DISPONIBLE'})-[:DE_FORMATO]->(fBlu),
  (c1t97:Copia {IdCopia:601, Estado:'DISPONIBLE'})-[:DE_FORMATO]->(fBlu);


// Relación entre Copias y Títulos
CREATE
  (c1t92)-[:COPIA_DE]->(t92),
  (c1t93)-[:COPIA_DE]->(t93),
  (c2t93)-[:COPIA_DE]->(t93),
  (c1t94)-[:COPIA_DE]->(t94),
  (c1t95)-[:COPIA_DE]->(t95),
  (c2t95)-[:COPIA_DE]->(t95),
  (c3t95)-[:COPIA_DE]->(t95),
  (c1t96)-[:COPIA_DE]->(t96),
  (c1t97)-[:COPIA_DE]->(t97);

// =========================================
// 🎟️ NODO: RENTA (con duración calculada)
CREATE
  (r1:Renta {
    IdRenta:1, FechaRenta:date('2024-11-01'), FechaDevolucion:date('2024-11-03'),
    ValorRenta:5000.00, MetodoPago:'Tarjeta', Estado:'FINALIZADA'
  })
WITH r1
// La línea corregida está aquí
MATCH (a101:Afiliado {IdAfiliado:101}), (t92:Titulo {IdTitulo:92}), (c1t92:Copia {IdCopia:101}) 
CREATE
  (a101)-[:REALIZO_RENTA]->(r1),
  (r1)-[:INCLUYE_TITULO]->(t92),
  (r1)-[:INCLUYE_COPIA]->(c1t92);

// =========================================
// 🌟 BONUS: Añadimos algunos gustos
MATCH (a103:Afiliado), (catFiccion:Categoria)
CREATE (a103)-[:LE_GUSTA]->(catFiccion);

MATCH (a106:Afiliado), (catAccion:Categoria)
CREATE (a106)-[:LE_GUSTA]->(catAccion);

MATCH (a107:Afiliado), (catSuspenso:Categoria)
CREATE (a107)-[:LE_GUSTA]->(catSuspenso);
