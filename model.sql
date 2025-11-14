CREATE DATABASE IF NOT EXISTS blockbuster_db;
USE blockbuster_db;

CREATE TABLE AFILIADO (
    IdAfiliado INT PRIMARY KEY,
    Nombres VARCHAR(50) NOT NULL,
    Apellidos VARCHAR(50) NOT NULL,
    Direccion VARCHAR(100),
    Telefono VARCHAR(20),
    FechaVinculacion DATE NOT NULL,
    Sexo CHAR(1) CHECK (Sexo IN ('M', 'F')),
    FechaNacimiento DATE,
    IdPrincipal INT,
    FOREIGN KEY (IdPrincipal) REFERENCES AFILIADO(IdAfiliado)
);


CREATE TABLE TITULO (
    IdTitulo INT PRIMARY KEY,
    Titulo VARCHAR(100) UNIQUE NOT NULL,
    Descripcion VARCHAR(255),
    Rating VARCHAR(30),
    Categoria VARCHAR(50),
    FechaLiberacion DATE
);

CREATE TABLE COPIA_TITULO (
    IdCopia INT,
    IdTitulo INT,
    Estado ENUM('DISPONIBLE','RENTADA','DAÑADA') DEFAULT 'DISPONIBLE',
    Formato ENUM('DVD','BLUERAY','VHS') NOT NULL,
    PRIMARY KEY (IdCopia, IdTitulo),
    FOREIGN KEY (IdTitulo) REFERENCES TITULO(IdTitulo)
);


CREATE TABLE RENTA (
    IdRenta INT AUTO_INCREMENT PRIMARY KEY,
    IdAfiliado INT NOT NULL,
    IdCopia INT NOT NULL,
    IdTitulo INT NOT NULL,
    FechaRenta DATE NOT NULL DEFAULT (CURRENT_DATE),
    FechaDevolucion DATE,
    ValorRenta DECIMAL(10,2) DEFAULT 5000,
    ValorRecargo DECIMAL(10,2),
    FOREIGN KEY (IdAfiliado) REFERENCES AFILIADO(IdAfiliado),
    FOREIGN KEY (IdCopia, IdTitulo) REFERENCES COPIA_TITULO(IdCopia, IdTitulo)
);


CREATE TABLE USUARIO (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    rol ENUM('ADMIN','USER') DEFAULT 'USER'
);


INSERT INTO AFILIADO VALUES
(101, 'Antonio', 'Rodríguez', 'Calle 1', '5512573', '2010-01-01', 'M', '1967-04-02', NULL),
(102, 'Nataly', 'Martínez', 'Calle 1', '5512573', '2010-01-01', 'F', '1967-11-20', 101),
(103, 'Natalia', 'Rodríguez', 'Calle 1', '5512573', '2010-01-01', 'F', '1998-06-20', 101),
(104, 'Sofía', 'Rodríguez', 'Calle 1', '5512573', '2010-02-28', 'F', '1998-10-08', 101),
(105, 'Ricardo', 'Ortega', 'Calle 2', '4665445', '2010-01-30', 'M', '1980-10-01', NULL),
(106, 'Camila', 'Ortega', 'Calle 2', '4665448', '2010-02-08', 'F', '1990-10-20', 105),
(107, 'Diego', 'Hernández', 'Cra 3', '5789779', '2010-01-01', 'M', '1957-07-10', NULL);

INSERT INTO TITULO VALUES
(92, 'Harry Potter 1', 'Película de Acción', 'Todos', 'Ficción', '2000-01-01'),
(93, 'El Señor de los Anillos', 'Película de Acción', 'Todos', 'Ficción', '2000-01-01'),
(94, 'Mousters Inc.', 'Película de Aventuras para Niños', 'Todos', 'Niños', '2001-08-01'),
(95, 'Insomnia', 'Película de Suspenso', 'Mayores 12', 'Suspenso', '2002-12-01'),
(96, 'Rápido y Furioso', 'Acción en autos', 'Mayores 18', 'Acción', '2002-12-01'),
(97, 'Rápido y Furioso II', 'Acción en autos', 'Mayores 18', 'Acción', '2003-02-01');

INSERT INTO COPIA_TITULO VALUES
(1, 92, 'DISPONIBLE', 'DVD'),
(1, 93, 'DISPONIBLE', 'DVD'),
(2, 93, 'DISPONIBLE', 'BLUERAY'),
(1, 94, 'DISPONIBLE', 'DVD'),
(1, 95, 'DISPONIBLE', 'DVD'),
(2, 95, 'DISPONIBLE', 'BLUERAY'),
(3, 95, 'RENTADA', 'BLUERAY'),
(1, 96, 'DISPONIBLE', 'BLUERAY'),
(1, 97, 'DISPONIBLE', 'BLUERAY');


