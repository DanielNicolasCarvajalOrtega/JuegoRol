
class Usuario:
    def __init__(self,id_,nom,contr) -> None:
        self.__Id_user = id_
        self.__Username = nom
        self.__Password = contr

    def IdentUsuario(self):
        return self.__Id_user
    
    def NombreUsuario(self):
        return self.__Username
    
    def ContraUsuario(self):
        return self.__Password


class GameMaster(Usuario):
    def __init__(self, id_, nom, contr):
        super().__init__(id_, nom, contr)
        

    
class Habilidades:
    def __init__(self,_id,nom,ni,est,desc):
        self.__Id = _id
        self.__Nombre = nom
        self.__Nivel = ni
        self.__Estado = est
        self.__Descripcion = desc

    def IdHabilidad(self):
        return self.__Id
    
    def NombreHabilidad(self):
        return self.__Nombre
    
    def NivelHabilidad(self):
        return self.__Nivel
    
    def EstadoHabilidad(self):
        return self.__Estado
    
    def DescripcionHabilida(self):
        return self.__Descripcion

class Magia:
    def __init__(self,id_,nom,desc,efec):
        self.__Id = id_
        self.__Nombre = nom
        self.__Descripcion = desc
        self.__Efecto = efec
    
    def IdMagia(self):
        return self.__Id
    
    def NombreMagia(self):
        return self.__Nombre

    def DescripcionMagia(self):
        return self.__Descripcion

    def EfectoMagia(self):
        return self.__Efecto


class Equipamiento:
    def __init__(self,id_,nom,est):
        self.__Id = id_

    def IdEquipamiento(self):
        return self.__Id
    
    
class Arma:
    def __init__(self,id_,nom,desc,daño):
        self.__Id = id_
        self.__Nombre = nom
        self.__Daño = daño
        self.__Descripcion = desc
        
    def IdArma(self):
        return self.__Id
    
    def NombreArma(self):
        return self.__Nombre
    
    def DañoArma(self):
        return self.__Daño
    
    def DescArma(self):
        return self.__Descripcion