import sqlite3
import os


class BaseDeDatos:

    def __init__(self):
        self.__conexion = None

    @property
    def conexion(self):
        return self.__conexion

    @conexion.setter
    def conexion(self, valor):
        if isinstance(valor, sqlite3.Connection) or valor is None:
            self.__conexion = valor
        else:
            raise ValueError("El valor debe ser una conexión de base de datos o None.")

    # Método para conectar la base de dato
    def conectar(self):
        bd_nom = "db_estudiantes.db"
        bd_ruta = os.path.join(os.getcwd(), "database", bd_nom)

        try:

            if not os.path.exists(bd_ruta):
                if bd_nom.endswith(".db"):
                    self.__conexion = sqlite3.connect(bd_ruta)
                    print(f"La base de datos '{bd_nom}' se creó correctamente...")
                else:
                    print(f"La base de datos '{bd_nom}' ya existe...")

            if self.__conexion is None:
                self.__conexion = sqlite3.connect(bd_ruta)
                print(f"Se conecto correctamente a la base de datos '{bd_nom}'")
            else:
                print("Ya hay una conexión activa.")

        except sqlite3.OperationalError:
            print(
                "Ocurrió un error al crear la base de datos, revise la ruta del archivo."
            )

    # Método para desconectar la base de dato
    def cerrar(self):
        if self.__conexion is not None:
            self.__conexion.close()
            self.conexion = None
            print("La base de datos se cerró correctamente.")
        else:
            print("No hay ninguna conexión abierta para cerrar.")

    # Método para crear la tabla Estudiantes
    def crear_tabla(self):
        try:
            self.conectar()
            cur = self.conexion.cursor()
            cur.execute(
                """CREATE TABLE estudiantes(
                            id integer primary key autoincrement,
                            nombre text not null,
                            edad integer not null,
                            promedio decimal not null
                        )"""
            )
            print("La tabla 'estudiantes' se creo correctamente.")

        except sqlite3.OperationalError:
            print("La tabla de 'estudiantes' ya existe.")
        finally:
            self.cerrar()

    # Método para insertar un estudiante
    def insertar_estudiante(self, nombre, edad, promedio):
        try:
            self.conectar()
            cur = self.conexion.cursor()
            cur.execute(
                "INSERT INTO estudiantes(nombre, edad, promedio) values(?,?,?)",
                (nombre, edad, promedio),
            )
            self.conexion.commit()
            print("Los datos se insertaron de manera correcta.")
        except sqlite3.OperationalError:
            print("Ocurrió un Error: Los datosno se insertaron correctamente")
        finally:
            self.cerrar()

    # Método para obtener una lista de los estudiantes
    def obtener_estudiantes(self):
        try:
            self.conectar()
            cur = self.conexion.cursor()
            cur.execute("SELECT * FROM estudiantes")
            lis_estu = cur.fetchall()
            for i in lis_estu:
                print(i)
        except sqlite3.OperationalError:
            print("Ocurrió un Error: No se pudieron extraer los datos correctamente.")
        finally:
            self.cerrar()

    # Método para poder actualizar el promedio de un estudiante por su ID
    def actualizar_promedio(self, id_estudiante, nuevo_promedio):
        try:
            self.conectar()
            cur = self.conexion.cursor()
            cur.execute(
                """UPDATE estudiantes set promedio=? WHERE id=?""",
                (nuevo_promedio, id_estudiante),
            )
            self.conexion.commit()
            print("Datos Actualizados correctamente")
        except sqlite3.OperationalError:
            print("Ocurrió un Error: No se pudo actualizar el promedio del alumno.")
        finally:
            self.cerrar()

    # Método para eliminar un estudiante mediante su ID
    def eliminar_estudiante(self, id_estudiante):
        try:
            self.conectar()
            cur = self.conexion.cursor()
            cur.execute("""DELETE FROM estudiantes WHERE id=?""", (id_estudiante,))
            self.conexion.commit()
            print("Dato eliminado correctamente")
        except sqlite3.OperationalError:
            print("Ocurrió un Error: No se pudo eliminar al alumno.")
        finally:
            self.cerrar()


bd = BaseDeDatos()
# bd.conectar()
# bd.cerrar()
# bd.crear_tabla()
# bd.obtener_estudiantes()
# bd.actualizar_promedio(4, 20)
# bd.obtener_estudiantes()
# bd.eliminar_estudiante(4)
# bd.obtener_estudiantes()
