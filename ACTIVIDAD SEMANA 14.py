# Funciones con parámetros y retorno de valores
# Problema: Calcular el precio total de una compra con descuento

def calcular_total(precio, cantidad, descuento):
    subtotal = precio * cantidad
    monto_descuento = subtotal * (descuento / 100)
    total = subtotal - monto_descuento
    return total

# Llamada a la función
precio_unitario = 25.50
cantidad_productos = 4
porcentaje_descuento = 10

resultado = calcular_total(precio_unitario, cantidad_productos, porcentaje_descuento)

print("=== Resumen de compra ===")
print(f"Precio unitario:  ${precio_unitario}")
print(f"Cantidad:          {cantidad_productos} unidades")
print(f"Descuento:         {porcentaje_descuento}%")
print(f"Total a pagar:    ${resultado:.2f}")