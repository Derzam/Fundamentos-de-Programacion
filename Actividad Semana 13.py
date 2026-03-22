def calcular_total(precio, cantidad):
    total = precio * cantidad
    return total


if __name__ == "__main__":
    precio_unitario = float(input("Ingrese el precio unitario del producto: "))
    cantidad = int(input("Ingrese la cantidad de productos: "))

    total_compra = calcular_total(precio_unitario, cantidad)

    print("===== RESUMEN DE COMPRA =====")
    print(f"Precio unitario: ${precio_unitario:.2f}")
    print(f"Cantidad:        {cantidad}")
    print(f"-----------------------------")
    print(f"Total a pagar:   ${total_compra:.2f}")