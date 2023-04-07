import logging

# Configuración básica del logger
logging.basicConfig(level=logging.INFO)

def calcular_precio(producto, cantidad):
    precio_unitario = 10
    logging.info(f"Calculando precio de {cantidad} unidades de {producto}")
    precio_total = cantidad * precio_unitario
    logging.info(f"Precio total de {cantidad} unidades de {producto}: {precio_total}")
    return precio_total

# Ejemplo de uso de la función
calcular_precio("Camisa", 3)



