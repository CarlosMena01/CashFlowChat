import os
import sys

# Obtener la ruta del directorio padre
directorio_padre = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Añadir el directorio al sys.path
sys.path.append(directorio_padre)

from categorizer import categorize_expense

def main():
    entries = [
        "6k en cerveza",
        "Pago de renta mensual 8000",
        "Compra de laptop 15000",
    ]

    for entry in entries:
        print(f"Entrada: {entry}")
        result = categorize_expense(entry)
        print("Salida:")
        print(result)
        print("-" * 40)

if __name__ == "__main__":
    main()
