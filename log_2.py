import logging

logging.basicConfig(level=logging.DEBUG)

def dividir(a, b):
    logging.debug(f"Dividiendo {a} entre {b}")
    resultado = a / b
    logging.debug(f"Resultado de la división: {resultado}")
    return resultado

print(dividir(10, 2))