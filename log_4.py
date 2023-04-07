import logging
import xlrd
import csv

logging.basicConfig(level=logging.ERROR)

def cargar_datos(archivo):
    try:
        # Código para cargar los datos del archivo
        with open(archivo, newline='') as archivo_csv:
            # Crear un objeto reader de csv
            csv_reader = csv.reader(archivo_csv, delimiter=',')

            # Recorrer las filas del archivo
            for fila in csv_reader:
                print(fila)
        datos= csv_reader
        return datos
    except IOError:
        logging.error(f"No se pudo cargar el archivo {archivo}")
        return None

cargar_datos("train1.csv")




