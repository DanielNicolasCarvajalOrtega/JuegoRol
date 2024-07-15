-- SQLBook: Code

CREATE DATABASE Usuarios;

Use Usuarios;

DROP TABLE Poder;
DROP TABLE DatosUsuarios;
DROP TABLE Habilidades;

DROP TABLE Equipamiento;

DROP TABLE Poder;


CREATE TABLE DatosUsuarios(
    IdPersonaje INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    NombreJugador VARCHAR(150) NOT NULL,
    NombrePersonaje VARCHAR(150) NOT NULL,
    Raza VARCHAR(50) NOT NULL,
    Nivel INT NOT NULL,
    Estado VARCHAR(50) NOT NULL,
    IdHabilidad INT NOT NULL,
    IdEquipamiento INT NOT NULL,
    IdPoder INT NOT NULL,
    Rol VARCHAR(50) NOT NULL,
    Contrasena VARCHAR(100) NOT NULL,
    Gmail VARCHAR(100) NOT NULL,
    NombreUsuario VARCHAR(100) NOT NULL,
    FOREIGN KEY (IdHabilidad) REFERENCES Habilidades(IdHabilidad),
    FOREIGN KEY (IdEquipamiento) REFERENCES Equipamiento(IdEquipamiento),
    FOREIGN KEY (IdPoder) REFERENCES PODER(IdPoder)
);

CREATE TABLE Habilidades(
    IdHabilidad INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    Nombre VARCHAR(150) NOT NULL,
    Nivel INT NOT NULL,
    CodPersonaje INT NOT NULL
);
    

CREATE TABLE Equipamiento(
    IdEquipamiento INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    Nombre VARCHAR(150) NOT NULL,
    CodPersonaje INT NOT NULL
    
);

CREATE TABLE Poder(
    IdPoder INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    Nombre VARCHAR(150) NOT NULL,
    Nivel INT NOT NULL,
    CodPersonaje INT NOT NULL
);



ALTER TABLE Habilidades
ADD CONSTRAINT fk_Habi_
FOREIGN KEY (CodPersonaje) REFERENCES DatosPersonaje(IdPersonaje);

ALTER TABLE Equipamiento
ADD CONSTRAINT fk_Equi
FOREIGN KEY (CodPersonaje) REFERENCES DatosPersonaje(IdPersonaje);

ALTER TABLE Poder
ADD CONSTRAINT fk_Pod
FOREIGN KEY (CodPersonaje) REFERENCES DatosPersonaje(IdPersonaje);

RENAME TABLE DatosPersonaje TO DatosUsuarios;




ALTER TABLE DatosUsuarios
ADD NombreUsuario VARCHAR(100) NOT NULL;
