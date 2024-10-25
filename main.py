# Importar los modulos correspondientes para usar la Base de Datos
from class_BD import BaseDeDatos, Estudiante


def menu():
    bd = BaseDeDatos()  # Instancia de la base de datos

    while True:
        print("\n--- Sistema de Gestión de Estudiantes ---")
        print("1. Registrar un nuevo estudiante")
        print("2. Mostrar la lista de estudiantes")
        print("3. Actualizar el promedio de un estudiante")
        print("4. Eliminar un estudiante")
        print("5. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            try:
                nombre = input("Nombre del estudiante: ")
                edad = int(input("Edad: "))
                promedio = float(input("Promedio: "))
                estudiante = Estudiante(nombre, edad, promedio)
                estudiante.guardar_en_bd(bd)
                print("Estudiante registrado exitosamente.")
            except ValueError as e:
                print(f"Error: {e}")

        elif opcion == "2":
            estudiantes = bd.obtener_estudiantes()
            if estudiantes:
                for est in estudiantes:
                    print(
                        f"ID: {est[0]}, Nombre: {est[1]}, Edad: {est[2]}, Promedio: {est[3]}"
                    )
            else:
                print("No hay estudiantes registrados.")

        elif opcion == "3":
            try:
                id_estudiante = int(input("ID del estudiante a actualizar: "))
                nuevo_promedio = float(input("Nuevo promedio: "))
                if 0 <= nuevo_promedio <= 20:
                    bd.actualizar_promedio(id_estudiante, nuevo_promedio)
                    print("Promedio actualizado correctamente.")
                else:
                    print("El promedio debe estar entre 0 y 20.")
            except ValueError:
                print("Error: Entrada inválida.")

        elif opcion == "4":
            try:
                id_estudiante = int(input("ID del estudiante a eliminar: "))
                bd.eliminar_estudiante(id_estudiante)
                print("Estudiante eliminado correctamente.")
            except ValueError:
                print("Error: ID inválido.")

        elif opcion == "5":
            print("Saliendo del sistema...")
            bd.cerrar()
            break
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")


# Condicional para iniciar el programa
if __name__ == "__main__":
    menu()
