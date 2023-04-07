import logging

logging.basicConfig(level=logging.WARNING)

def dividir(a, b):
    if b == 0:
        logging.warning("Intentando dividir por cero")
        return None
    else:
        resultado = a / b
        return resultado

print(dividir(10, 0))
