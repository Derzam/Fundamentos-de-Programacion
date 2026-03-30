
#   AGENDA ESTUDIANTIL - Colecciones de Datos en Python
#   Usa: diccionario, lista y conjunto


def mostrar_menu():
    print("\n" + "="*45)
    print("     AGENDA ESTUDIANTIL")
    print("="*45)
    print("  1. Agregar estudiante y nota")
    print("  2. Mostrar todos los estudiantes")
    print("  3. Buscar estudiante")
    print("  4. Eliminar estudiante")
    print("  5. Mostrar materias registradas")
    print("  6. Salir")
    print("="*45)

def agregar_estudiante(estudiantes, materias):
    nombre = input("  Nombre del estudiante: ").strip()
    if not nombre:
        print(" El nombre no puede estar vacío.")
        return
    nota = input("  Nota (0-10): ").strip()
    try:
        nota = float(nota)
        if not (0 <= nota <= 10):
            raise ValueError
    except ValueError:
        print("   Nota inválida. Debe ser un número entre 0 y 10.")
        return
    materia = input("  Materia: ").strip()
    if not materia:
        print("   La materia no puede estar vacía.")
        return

    # Diccionario: relaciona nombre → {nota, materia}
    estudiantes[nombre] = {"nota": nota, "materia": materia}

    # Conjunto: guarda materias sin repetir
    materias.add(materia)

    print(f"   {nombre} agregado correctamente.")

def mostrar_estudiantes(estudiantes):
    if not estudiantes:
        print("\n    No hay estudiantes registrados.")
        return
    print("\n  {:<20} {:<10} {}".format("Nombre", "Nota", "Materia"))
    print("  " + "-"*42)
    for nombre, datos in estudiantes.items():
        estado = " Aprobado" if datos["nota"] >= 6 else " Reprobado"
        print("  {:<20} {:<10} {:<15} {}".format(
            nombre, datos["nota"], datos["materia"], estado))

def buscar_estudiante(estudiantes):
    nombre = input("  Nombre a buscar: ").strip()
    if nombre in estudiantes:
        datos = estudiantes[nombre]
        print(f"\n   Estudiante encontrado:")
        print(f"      Nombre : {nombre}")
        print(f"      Nota   : {datos['nota']}")
        print(f"      Materia: {datos['materia']}")
        print(f"      Estado : {'Aprobado ' if datos['nota'] >= 6 else 'Reprobado '}")
    else:
        print(f" '{nombre}' no está en la agenda.")

def eliminar_estudiante(estudiantes):
    nombre = input("  Nombre a eliminar: ").strip()
    if nombre in estudiantes:
        del estudiantes[nombre]
        print(f"  🗑️  '{nombre}' eliminado correctamente.")
    else:
        print(f"  '{nombre}' no encontrado.")

def mostrar_materias(materias):
    if not materias:
        print("\n   No hay materias registradas.")
        return
    print("\n  Materias registradas (sin repetir):")
    for m in sorted(materias):
        print(f"      • {m}")

# ── Programa principal ────────────────────────────────────────

def main():

    historial = []


    estudiantes = {}


    materias = set()

    # Datos
    estudiantes["Ana Torres"]   = {"nota": 9.0, "materia": "Matemáticas"}
    estudiantes["Luis Mora"]    = {"nota": 5.5, "materia": "Historia"}
    estudiantes["Sofía Reyes"]  = {"nota": 8.2, "materia": "Matemáticas"}
    materias.update(["Matemáticas", "Historia"])

    print("\n  Bienvenido a la Agenda Estudiantil ")
    print("  (Se cargaron 3 estudiantes de ejemplo)")

    while True:
        mostrar_menu()
        opcion = input("  Elige una opción: ").strip()

        if opcion == "1":
            agregar_estudiante(estudiantes, materias)
            historial.append("Agregar estudiante")
        elif opcion == "2":
            mostrar_estudiantes(estudiantes)
            historial.append("Mostrar estudiantes")
        elif opcion == "3":
            buscar_estudiante(estudiantes)
            historial.append("Buscar estudiante")
        elif opcion == "4":
            eliminar_estudiante(estudiantes)
            historial.append("Eliminar estudiante")
        elif opcion == "5":
            mostrar_materias(materias)
            historial.append("Mostrar materias")
        elif opcion == "6":
            print(f"\n  📋  Acciones realizadas en esta sesión:")
            for i, accion in enumerate(historial, 1):
                print(f"      {i}. {accion}")
            print("\n  ¡Hasta luego! \n")
            break
        else:
            print(" Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()