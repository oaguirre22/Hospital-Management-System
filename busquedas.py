def buscar_pacientes_inteligente(pacientes):
    """
    Realiza búsquedas avanzadas combinando filtros.
    """
    from colorama import Fore

    try:
        edad_min = int(input(Fore.YELLOW + "Ingrese la edad mínima: "))
        especialidad = input(Fore.YELLOW + "Ingrese la especialidad (opcional): ").strip().lower()
        
        resultados = [
            p for p in pacientes.values()
            if (p.get("edad", 0) >= edad_min) and 
               (especialidad in p.get("especialidad", "").lower() if especialidad else True)
        ]

        if resultados:
            print(Fore.GREEN + "Resultados encontrados:")
            for r in resultados:
                print(Fore.CYAN + f"{r}")
        else:
            print(Fore.YELLOW + "No se encontraron pacientes que coincidan con los filtros.")
    except ValueError as ve:
        print(Fore.RED + f"[ERROR]: {ve}")
    except Exception as e:
        print(Fore.RED + f"[ERROR INESPERADO]: {e}")
