class Razas:
    def __init__(self,nombre,nomUser,vida,descrip,fuerza,defensa):
        self.NombrePersonajeRaza = nombre
        self.NombrePersonajeUser = nomUser
        self.DescripcionRaza = descrip
        self.VidaRaza = vida
        self.DefensaRaza = defensa
        self.FuerzaRaza = fuerza
       
        
class Barbaro(Razas):
    def __init__(self,nomUser):
        super().__init__(
                "Barbaro",
                nomUser,
                100,
                40,
                50,
                """ 
            El barbaro es un guerrero imponenete y muy bien armado, un nomada de la tribu que alguna vez 
            vigilo el sagrado Monte Arreat.
            * Lucha salvajemente con armas melé
            * Emplea fuerza bruta para blanadir enormes armas a dos manos, un arma en cada mano o un arma y un escudo
            * Acumula furia al causar o recibir daño y luego la descarga a través de ataques devastadores.
            """
        )

        

    """
    def getNombreBarbaro(self):
        return self.NombreBarba
            
    def getVidaBarbaro(self):
        return self.Vida

    def getFuerzaBarbaro(self):
        return self.Fuerza

    def getDefensaBarbaro(self):
         return self.Defensa

    def getDescripcionBarbaro(self):
        return self.Descripcion
        """
    


    def obtenerBarbaro(self):
        return f"""
            Nombre: {self.NombrePersonajeRaza}\n
            Vida:{self.VidaRaza}\n
            Fuerza:{self.FuerzaRaza}\n
            Defensa:{self.DefensaRaza}\n
            Descripcion Barbaro:{self.DescripcionRaza}\n"""


class GuerreroDivino(Razas):
    def __init__(self,nom:str):
            super().__init__(
                NombreGuerrero = "Guerrero Divino",
                Nombre = self.NombrePersonajeRaza(nom),
                Vida = 120,
                Fuerza = 47,
                Defensa = 40,
                Descripcion = """
                El Guerrero Divino es un campeon de la justicia,ataviado en armadura metalica y poder fulgante.
                Cuando el mal emerge de sui cubil para corromper y destruir a la humanidad, el Guerrero Divino carga.
                * Emite su veredicto con brutales manguales e imponenetes escudos.
                * Obliga a los huestes del mal a luchar cuerpo a cuerpo o a distancia media con una mirada de 
                habilidades.Asimismo, pronuncia leyes para incrementar la capacidad de combate de todos aquellos 
                que se opongan a la oscuridad.
                * Hierve de ira, un fervor que aumenta de manera constante, para descargar ataques aun mas devastadores.
                """
            )

    def getNombreGuerreroDivino(self):
        return self.NombreGuerrero
    
    def getVidaGuerreroDivino(self):
        return self.Vida

    def getFuerzaGuerreroDivino(self):
         return self.Fuerza
    
    def getDefensaGuerreroDivino(self):
         return self.Defensa

    def getDescripcionGuerreroDivino(self):
        return self.Descripcion
           

    def obtenerGuerreroDivino(self):
            return f"""
        Nombre: {self.NombreGuerrero}\n
        Vida:{self.Vida}\n
        Fuerza:{self.Fuerza}\n
        Defensa:{self.Defensa}\n
        Descripcion Guerrero Divino:{self.Descripcion}\n"""


class CazadorDeDemonios(Razas):
        def __init__(self,nom:str):
            super().__init__(
                NombreCazador = "Cazador de demonios",
                Nombre = self.NombrePersonajeRaza(nom),
                Vida = 90,
                Fuerza = 45,
                Defensa = 100,
                Descripcion = """
            La cazadora de demonios es la sobreviviente de un ataque demoniaco y se ha dedicado en cuerpo y alma
            a una gesta sin fin para librar al mundo de la influencia de las abominaciones que ponen en peligro
            al mundo de Santuario.
            * Elimina a sus enemigos con armas a distancia como granadas, arcos y ballestas.
            * Permanece movil gracias a sus habilidades de evacion e inmoviliza al enemigo con trampas bien
            colocadas.
            * Se vale de odio, fuego interno de regeneracion rapida, y disciplina, templanza que le permite hacer
            uso de habilidades tacticas.
        """
            )


        def getNombreCazadorDemonios(self):
             return self.NombreCazador
        
        def getVidaCazador(self):
             return self.Vida
        
        def getFuerzaCazador(self):
             return self.Fuerz
        
        def getDefensaCazador(self):
            return self.Defensa

        def getDescripcionCazador(self):
             return self.Descripcion

        def obtenerCazadorDeDemonios(self):
            return f"""
        Nombre: {self.NombreCazador}\n
        Vida:{self.Vida}\n
        Fuerza:{self.Fuerza}\n
        Defensa:{self.Defensa}\n
        Descripcion Cazador de Demonios:{self.Descripcion}\n"""


class Monje(Razas):
        def __init__(self,nom:str):
            super().__init__(
                NombreMonje = 'Monje',
                Nombre = self.NombrePersonajeRaza(nom),
                Vida = 105,
                Fuerza = 35,
                Defensa = 60,
                Descripcion = """
            El Monje es un guerrero sagrado, un sirviente de la divinidad cuyo cuerpo ha sido convertido 
            en un arma mortifera.
            * Acaba con el mal con sus veloces golpes y armas melé únicas como dagas de puño y bastones.
            * Invoca al poder de sus mil y un dioses para proteger, sanar y desterrar.
            * Genera espiritus durante el combate, una fuerza interna que potencia su evacion y movilidad.
            """
            )


        def getNombreMonje(self):
            return self.NombreMonje
        
        def getVidaMonje(self):
            return self.Vida
        
        def getFuerzaMonje(self):
            return self.Fuerza

        def getDefensaMonje(self):
            return self.Defensa

        def getDescripcionMonje(self):
            return self.Descripcion


        def obtenerMonje(self):
            return f"""
        Nombre: {self.NombreMonje}\n
        Vida:{self.Vida}\n
        Fuerza:{self.Fuerza}\n
        Defensa:{self.Defensa}\n
        Descripcion Monje:{self.Descripcion}\n"""

class Nigromante(Razas):
        def __init__(self,nom:str):
            super().__init__(
                NombreNigromante = 'Nigromante',
                Nombre = self.NombrePersonajeRaza(nom),
                Vida = 100,
                Fuerza = 67,
                Defensa = 80,
                Descripcion = """
            El Nigromante manipula los temibles poderes de la sangre y los huesos para restaurar el equilibrio en Santuario.
            Para ejecutar esta tarea, maldice a sus enemigos con terribles males y dirige poderosos ejercitos esqueleticos y
            gigantescos gólems.
            """
            )
            

        def getNombreNigromante(self):
             return self.NombreNigromante

        def getVidaNigromante(self):
             return self.Vida
        
        def getFuerzaNigromante(self):
            return self.Fuerza
        
        def getDefensaNigromante(self):
             return self.Defensa
        
        def getDescripcionNigromante(self):
            return self.Descripcion


        def obtenerNigromante(self):
            return f"""
        Nombre: {self.Nombre}\n
        Vida:{self.Vida}\n
        Fuerza:{self.Fuerza}\n
        Defensa:{self.Fuerza}\n
        Descripcion Nigromante:{self.Descripcion}\n"""
        

class Santero(Razas):
        def __init__(self,nom:str):
            super().__init__(
                NombreSantero = 'Santero',
                Nombre = self.NombrePersonajeRaza(nom),
                Vida = 100,
                Fuerza = 84,
                Defensa = 100,
                Descripcion = """
                El santero esgrime poder de los espiritus de la tierra inconclusa e invoca criaturas de la ultratumba.
                * Invoca espantosos muertos vivientes, alimañas y otras criaturas para la defensa y ofensa.
                * Emplea destructivos ataques con veneno,acido y fuego.
                * Lanza sus hechizos e invocaciones con mana, una reserva de enegia considerable pero de regeneracion lenta.
                """
            )

        def getNombreSantero(self):
             return self.NombreSantero

        def getVidaSantero(self):
             return self.Vida

        def getFuerzaSantero(self):
            return self.Fuerza

        def getDefensaSantero(self):
            return self.Defensa

        def getDescripcionSantero(self):
            return self.Descripcion

        def obtenerSantero(self):
            return f"""
        Nombre: {self.Nombre}\n
        Vida:{self.Vida}\n
        HabilidadesActivas:{self.habilidadesActivas}\n
        HabilidadesPasivas:{self.habilidadesPasivas}\n
        Descripcion Santero:{self.descripcion}\n"""


class Arcanista():
        def __init__(self):
            self.Nombre = 'Arcanista'
            self.Vida = 100
            self.descripcion ="""
            La arcanista es una prodigio de lo arcano que controla el tiempo y los elementos en la busqueda 
            de su destino y de el poder.
            * Controla magia arcana.
            * Congela, incinera e inmoviliza a sus adversarios.
            * Invoca magia de manera casi instantanea gracias al poder arcano, una reserva de energia que
            se genera rapidamente.
            """

        def obtenerArcanista(self):
            return f"""
        Nombre: {self.Nombre}\n
        Vida:{self.Vida}\n
        HabilidadesActivas:{self.habilidadesActivas}\n
        HabilidadesPasivas:{self.habilidadesPasivas}\n
        Descripcion Santero:{self.descripcion}\n"""
        