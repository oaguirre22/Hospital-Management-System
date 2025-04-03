import csv
from colorama import Fore

def exportar_datos_a_csv(filename, data, fieldnames):
    try:
        with open(filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for row in data:
                filtered_row = {key: row[key] for key in fieldnames if key in row}
                writer.writerow(filtered_row)
        print(Fore.GREEN + f"Datos exportados exitosamente a '{filename}'.")
    except Exception as e:
        print(Fore.RED + f"[ERROR]: No se pudo exportar el archivo. {e}")
