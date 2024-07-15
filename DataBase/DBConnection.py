import mysql.connector
from mysql.connector import errorcode
from typing import List
from Clases import *
from DataBase.Razas.clasesRazas import *

class Connection:
    def __init__(self):
        try:
            self.conec = mysql.connector.connect(
                user='DataBase',
                password='Inacap2526',
                host='127.0.0.1',
                database='usuarios'
            )
        except mysql.connector.Error as error:
            if error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                input("Usuario o contraseña incorrectos")
            elif error.errno == errorcode.ER_BAD_DB_ERROR:
                input("No existe la base de datos")
            else:
                input(error)
    
        """
        14.	Para ingresar al juego, se deberá ingresar a través de un usuario y contraseña.
                a.	El sistema deberá identificar si corresponde a un GM o jugador.
        """
    def Verificacion(self,nombre,contraseña):
        cursor = self.conec.cursor()
        query = ("SELECT * FROM usuario WHERE usuario_nombre = %s AND usuario_contraseña = %s") 
        data = (nombre,contraseña,)
        cursor.execute(query,data)
        result = cursor.fetchone()
        if result == None:
            input("Usuario o contraseña incorrectos")
        else:
            input("Usuario y contraseña correctos")
        return result
    

    def Registro(self, user:Usuario):
        try:
            cursor = self.conec.cursor()
            query = ("INSERT INTO usuario (usuario_nombre , usuario_contraseña ) VALUES(%s,%s);")
            data = (user.NombreUsuario(), user.ContraUsuario(),)
            cursor.execute(query,data)
            update = cursor.rowcount
            if update > 0:
                input("Usuario creado exitosamente")
                self.conec.commit()
            else:
                input("Error al crear el usuario")
        except Exception as error:
            input(f"Error del sistema : {error}")
            self.conec.rollback()


    def Insertar_Raza():
        rasas1 = [
              {
            "tipo": "Barbaro",
            "nombre_usuario": None,
            "vida": 100,
            "fuerza": 40,
            "defensa": 50,
            "descripcion": """
                El barbaro es un guerrero imponente y muy bien armado, un nomada de la tribu que alguna vez 
                vigilo el sagrado Monte Arreat.
                * Lucha salvajemente con armas melé
                * Emplea fuerza bruta para blanadir enormes armas a dos manos, un arma en cada mano o un arma y un escudo
                * Acumula furia al causar o recibir daño y luego la descarga a través de ataques devastadores.""",
        },
        {
            "tipo": "Guerrero Divino",
            "nombre_usuario": None,
            "vida": 120,
            "fuerza": 47,
            "defensa": 40,
            "descripcion": """
                El Guerrero Divino es un campeon de la justicia, ataviado en armadura metalica y poder fulgante.
                Cuando el mal emerge de su cubil para corromper y destruir a la humanidad, el Guerrero Divino carga.
                * Emite su veredicto con brutales manguales e imponentes escudos.
                * Obliga a las huestes del mal a luchar cuerpo a cuerpo o a distancia media con una mirada de 
                habilidades. Asimismo, pronuncia leyes para incrementar la capacidad de combate de todos aquellos 
                que se opongan a la oscuridad.
                * Hierve de ira, un fervor que aumenta de manera constante, para descargar ataques aun mas devastadores.""",
        },
        {
            "tipo": "Cazador de demonios",
            "nombre_usuario": None,
            "vida": 90,
            "fuerza": 45,
            "defensa": 100,
            "descripcion": """
                La cazadora de demonios es la sobreviviente de un ataque demoniaco y se ha dedicado en cuerpo y alma
                a una gesta sin fin para librar al mundo de la influencia de las abominaciones que ponen en peligro
                al mundo de Santuario.
                * Elimina a sus enemigos con armas a distancia como granadas, arcos y ballestas.
                * Permanece movil gracias a sus habilidades de evacion e inmoviliza al enemigo con trampas bien
                colocadas.
                * Se vale de odio, fuego interno de regeneracion rapida, y disciplina, templanza que le permite hacer
                uso de habilidades tacticas.""",
        },
        {
            "tipo":"Monje",
            "nombre_usuario": None,
            "vida": 105,
            "fuerza": 35,
            "defensa": 60,
            "descripcion": """
                El Monje es un guerrero sagrado, un sirviente de la divinidad cuyo cuerpo ha sido convertido 
                en un arma mortifera.
                * Acaba con el mal con sus veloces golpes y armas melé únicas como dagas de puño y bastones.
                * Invoca al poder de sus mil y un dioses para proteger, sanar y desterrar.
                * Genera espiritus durante el combate, una fuerza interna que potencia su evacion y movilidad.
                """ 
        },
        {
            "tipo":"Nigromante",
            "nombre_usuario": None,
            "vida": 100,
            "fuerza": 67,
            "defensa": 80,
            "descripcion": """
                El Nigromante manipula los temibles poderes de la sangre y los huesos para restaurar el equilibrio en Santuario.
                Para ejecutar esta tarea, maldice a sus enemigos con terribles males y dirige poderosos ejercitos esqueleticos y
                gigantescos gólems.
                """ 

        },
        {
            "tipo":"Santero",
            "nombre_usuario": None,
            "vida": 100,
            "fuerza": 84,
            "defensa": 100,
            "descripcion": """
                El santero esgrime poder de los espiritus de la tierra inconclusa e invoca criaturas de la ultratumba.
                * Invoca espantosos muertos vivientes, alimañas y otras criaturas para la defensa y ofensa.
                * Emplea destructivos ataques con veneno,acido y fuego.
                * Lanza sus hechizos e invocaciones con mana, una reserva de enegia considerable pero de regeneracion lenta.
                """
        },
        {
            "tipo":"Arcanista",
            "nombre_usuario": None,
            "vida": 100,
            "fuerza": 60,
            "defensa": 110,
            "descripcion": """
            La arcanista es una prodigio de lo arcano que controla el tiempo y los elementos en la busqueda 
            de su destino y de el poder.
            * Controla magia arcana.
            * Congela, incinera e inmoviliza a sus adversarios.
            * Invoca magia de manera casi instantanea gracias al poder arcano, una reserva de energia que
            se genera rapidamente.
            """
        }

    ]


    conexion = Connection()
    cursor = conexion.cursor(rass)

    for ras in rasas1:


    def CrearPersonaje(self,per:Razas,nom:str):
        cursor = self.conec.cursor()
        query = ("INSERT INTO personaje (personaje_nombre)" 
                "VALUES(%s);")
        data = (str(nom),per.DescripcionPersonaje(),per.NivelPersonaje(),per.EstadoPersonaje(),)
        cursor.execute(query,data)
        update = cursor.rowcount
        if update > 0:
            input("Personaje creado exitosamente")
            self.conec.commit()
        else:
            input("Error al crear el personaje")
            

    def VerPersonajes(self, per:Razas) -> list[Razas]:
        cursor = self.conec.cursor()
        query = ("SELECT * FROM personaje;")
        data = (per.NombrePersonaje(),per.DescripcionPersonaje(),per.NivelPersonaje(),per.EstadoPersonaje(),)
        cursor.execute(query,data)
        razas:List[Razas] = []
        for (personaje_nombre,personaje_descripcion,personaje_nivel,personaje_estado) in cursor:
            per = Razas(personaje_nombre,personaje_descripcion,personaje_nivel,personaje_estado,)
            razas.append(per)
        return razas


    def VerlistadoHabilidades(self, hab:Habilidades):
        cursor = self.conec.cursor()
        query = ("SELECT (habilidad_nombre,habilidad_desc) FROM habilidad;")
        data = (hab.NombreHabilidad(),hab.DescripcionHabilida(),)
        cursor.execute(query,data)


    def VerListadoMagia(self, mag:Magia):
        cursor = self.conec.cursor()
        query = ("SELECT (magia_nombre,magia_desc,magia_efecto) FROM magia")
        data = (mag.NombreMagia(),mag.DescripcionMagia(),mag.EfectoMagia(),)
        cursor.execute(query,data)


    def VerListadoEquipamiento(self, equi:Equipamiento):
        cursor = self.conec.cursor()
        query = ("SELECT (equipamiento_tipo) FROM equipamiento;")
        data = (equi.TipoEquipamiento(),)
        cursor.execute(query,data)  
   

    def VerlistadoArmas(self, arm:Arma):
        cursor = self.conec.cursor()
        query = ("SELECT (nombre_nombre,arma_descrip,arma_daño) FROM Armas;")
        data = (arm.Nombre(),arm.DescArma(),arm.DañoArma(),)
        cursor.execute(query,data)  



            


       

        
        

    

        


        

    