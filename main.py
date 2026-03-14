print("Matriz 3x4")
matrizAsientos = [[0 for _ in range(4)] for _ in range(3)]
f = int(input("Ingrese el numero de fila (0-2): "))
c = int(input("Ingrese el numero de columna (0-3): "))
matrizAsientos[f][c] = 1


print("Estado de la sala:")
for i in range(3):
    for j in range(4):
        print(matrizAsientos[i][j], end=" ")
    print()
