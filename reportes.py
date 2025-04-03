def gestionar_reportes(pacientes, medicos, historial):
    """
    Genera y muestra estadísticas y reportes sobre el sistema.
    """
    from colorama import Fore

    while True:
        print(Fore.CYAN + "=" * 60)
        print(Fore.YELLOW + "REPORTES Y ESTADÍSTICAS".center(60))
        print(Fore.CYAN + "=" * 60)
        print("[1] Número total de pacientes activos")
        print("[2] Especialidades más solicitadas")
        print("[3] Pacientes con más citas")
        print("[Q] Regresar al menú principal")
        print(Fore.CYAN + "=" * 60)

        opcion = input(Fore.YELLOW + "Seleccione una opción: ").strip().upper()

        if opcion == "1":
            activos = sum(1 for p in pacientes.values() if p.get("estado", "").lower() == "activo")
            print(Fore.GREEN + f"Total de pacientes activos: {activos}")
        elif opcion == "2":
            especialidades = {}
            for p in historial.values():
                especialidad = p.get("especialidad")
                if especialidad:
                    especialidades[especialidad] = especialidades.get(especialidad, 0) + 1
            print(Fore.CYAN + "Especialidades más solicitadas:")
            for esp, count in sorted(especialidades.items(), key=lambda x: x[1], reverse=True):
                print(Fore.YELLOW + f"{esp}: {count} solicitudes")
        elif opcion == "3":
            pacientes_citas = {p["nombre"]: len(p.get("citas", [])) for p in pacientes.values()}
            print(Fore.CYAN + "Pacientes con más citas:")
            for nombre, citas in sorted(pacientes_citas.items(), key=lambda x: x[1], reverse=True)[:5]:
                print(Fore.YELLOW + f"{nombre}: {citas} citas")
        elif opcion in ["Q"]:
            print(Fore.GREEN + "Regresando al menú principal...")
            break
        else:
            print(Fore.RED + "Opción no válida. Por favor, seleccione una opción de la lista.")
