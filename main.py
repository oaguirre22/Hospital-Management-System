from modules.hash_map import HashMap
from modules.inventarios_hash_map import inventory_generator
from modules.Colas import Queue
from modules.Colas_de_prioridad import PQueueSimplest, PQueueAP
from modules.conjunto import Conjunto
from modules.DoubleEndedQueue import MyDeque
from modules.reportes import gestionar_reportes
from modules.exportar import exportar_datos_a_csv
from modules.busquedas import buscar_pacientes_inteligente
import os
import random
from modules.animations import (
    animacion_hashmap_insercion,
    animacion_queue_enqueue,
    animacion_priorityqueue_insercion,
    animacion_set_insercion,
    animacion_deque_insercion,
    animacion_kmp_search,
    animacion_hashmap_eliminacion,
    animacion_queue_dequeue,
    animacion_generar_reportes
)



from colorama import Fore, Style, init

init(autoreset=True)


INFO = f"{Fore.GREEN}[INFO]{Style.RESET_ALL}"
ALERTA = f"{Fore.YELLOW}[ALERTA]{Style.RESET_ALL}"
ERROR = f"{Fore.RED}[ERROR]{Style.RESET_ALL}"
EXITO = f"{Fore.CYAN}[ÉXITO]{Style.RESET_ALL}"

NOMBRES = ["Juan", "María", "Carlos", "Ana", "Luis", "Laura", "Pedro", "Carmen", "José", "Sofía"]
APELLIDOS = ["García", "Pérez", "López", "Martínez", "Sánchez", "Gómez", "Fernández", "Ramírez", "Torres", "Díaz"]
ESPECIALIDADES = ["Cardiología", "Pediatría", "Dermatología", "Neurología", "Oncología", "Psiquiatría", "Traumatología"]
ALERGIAS = ["Polen", "Maní", "Lácteos", "Gluten", "Frutos rojos"]

ESPECIALIDADES_CONJUNTO = Conjunto()

def generar_pacientes_aleatorios():

    pacientes = HashMap()
    for i in range(1, 21):
        id_paciente = f"{random.randint(10000, 99999)}"
        nombre = f"{random.choice(NOMBRES)} {random.choice(APELLIDOS)}"
        edad = random.randint(1, 99)
        alergias = random.sample(ALERGIAS, random.randint(0, len(ALERGIAS)))
        pacientes.put(id_paciente, {
            "nombre": nombre,
            "edad": edad,
            "alergias": alergias
        })
    print("20 pacientes generados automáticamente.")
    return pacientes

def generar_medicos_aleatorios():

    medicos = HashMap()
    for i in range(1, 11):
        id_medico = f"M-{random.randint(100, 999)}"
        nombre = f"{random.choice(NOMBRES)} {random.choice(APELLIDOS)}"
        especialidad = random.choice(ESPECIALIDADES)
        medicos.put(id_medico, {
            "nombre": nombre,
            "especialidad": especialidad,
            "pacientes": []  
        })
    print("10 médicos generados automáticamente.")
    return medicos



def guardar_pacientes(pacientes):

    os.makedirs("data", exist_ok=True)  
    with open("data/data_pacientes.txt", "w") as file:
        for paciente_id, info in pacientes.items():
            file.write(f"{paciente_id}|{info['nombre']}|{info['edad']}|{','.join(info['alergias'])}\n")
    print("Pacientes guardados exitosamente en data_pacientes.txt.")
    

def cargar_pacientes():

    pacientes = HashMap()
    if not os.path.exists("data/data_pacientes.txt"): 
        return pacientes

    with open("data/data_pacientes.txt", "r") as file:
        for line in file:
            paciente_id, nombre, edad, alergias = line.strip().split("|")
            pacientes.put(paciente_id, {
                "nombre": nombre,
                "edad": int(edad),
                "alergias": alergias.split(",")
            })
    print("Pacientes cargados exitosamente desde data_pacientes.txt.")
    return pacientes




def guardar_citas(citas):

    os.makedirs("data", exist_ok=True)
    with open("data/data_citas.txt", "w") as file:
        for prioridad, cita in citas.queue:
            file.write(f"{cita['paciente_id']}|{cita['medico_id']}|{cita['descripcion']}|{prioridad}\n")
    print("Citas guardadas exitosamente en data_citas.txt.")


def cargar_citas():

    citas = PQueueAP()
    if not os.path.exists("data/data_citas.txt"):
        return citas

    with open("data/data_citas.txt", "r") as file:
        for line in file:
            paciente_id, medico_id, descripcion, prioridad = line.strip().split("|")
            cita = {
                "paciente_id": paciente_id,
                "medico_id": medico_id,
                "descripcion": descripcion,
                "prioridad": int(prioridad),
            }
            citas.enqueue(int(prioridad), cita)
    print("Citas cargadas exitosamente desde data_citas.txt.")
    return citas



def guardar_historiales(historial):
    os.makedirs("data", exist_ok=True)
    with open("data/data_historiales.txt", "w") as file:
        for paciente_id, registros in historial.items():
            for registro in registros:
                file.write(f"{paciente_id}|{registro}\n")
    print("Historiales médicos guardados exitosamente en data_historiales.txt.")


def cargar_historiales():
    historial = HashMap()
    if not os.path.exists("data/data_historiales.txt"):
        return historial

    with open("data/data_historiales.txt", "r") as file:
        for line in file:
            paciente_id, registro = line.strip().split("|")
            if paciente_id not in historial:
                historial.put(paciente_id, MyDeque())
            historial.get(paciente_id).insertFront(registro)
    print("Historiales médicos cargados exitosamente desde data_historiales.txt.")
    return historial



def guardar_medicos(medicos):
    os.makedirs("data", exist_ok=True)
    with open("data/data_medicos.txt", "w") as file:
        for medico_id, info in medicos.items():
            file.write(f"{medico_id}|{info['nombre']}|{info['especialidad']}\n")
    print("Médicos guardados exitosamente en data_medicos.txt.")


def cargar_medicos():
    medicos = HashMap()
    if not os.path.exists("data/data_medicos.txt"):
        return medicos

    with open("data/data_medicos.txt", "r") as file:
        for line in file:
            medico_id, nombre, especialidad = line.strip().split("|")
            medicos.put(medico_id, {
                "nombre": nombre,
                "especialidad": especialidad,
                "pacientes": [] 
            })
    print("Médicos cargados exitosamente desde data_medicos.txt.")
    return medicos



def guardar_notificaciones(notificaciones):
    os.makedirs("data", exist_ok=True)
    with open("data/data_notificaciones.txt", "w") as file:
        for notificacion in notificaciones.to_list():
            file.write(f"{notificacion}\n")
    print("Notificaciones guardadas exitosamente en data_notificaciones.txt.")


def cargar_notificaciones():
    notificaciones = Queue()
    if not os.path.exists("data/data_notificaciones.txt"):
        return notificaciones

    with open("data/data_notificaciones.txt", "r") as file:
        for line in file:
            notificaciones.enqueue(line.strip())
    print("Notificaciones cargadas exitosamente desde data_notificaciones.txt.")
    return notificaciones

def generar_datos_iniciales():

    pacientes = HashMap()
    for i in range(1, 21):
        paciente_id = str(10000 + i)
        pacientes.put(paciente_id, {
            "nombre": f"Paciente {i}",
            "edad": i + 20,
            "alergias": ["Alergia" + str(i % 5)]
        })
    
    medicos = HashMap()
    for i in range(1, 11):
        medico_id = str(20000 + i)
        medicos.put(medico_id, {
            "nombre": f"Médico {i}",
            "especialidad": f"Especialidad {i % 3 + 1}",
            "pacientes": []
        })
    
    citas = PQueueAP()
    for i in range(1, 6):
        citas.enqueue(i % 3 + 1, {
            "paciente_id": f"1000{i}",
            "medico_id": f"2000{i % 10 + 1}",
            "descripcion": f"Consulta {i}",
            "prioridad": i % 3 + 1
        })

    notificaciones = Queue()
    for i in range(1, 6):
        notificaciones.enqueue(f"Notificación {i}")

    historial = HashMap()
    for i in range(1, 21):
        paciente_id = str(10000 + i)
        historial.put(paciente_id, MyDeque())
        for j in range(1, 6):
            historial.get(paciente_id).insertFront(f"Consulta {j} para el paciente {paciente_id}")

    return pacientes, medicos, citas, notificaciones, historial




def render_menu(title, options):

    print(Fore.CYAN + "=" * 60)
    print(Fore.YELLOW + f"{title.center(60)}")
    print(Fore.CYAN + "=" * 60)
    for i, option in enumerate(options, start=1):
        print(Fore.GREEN + f"[{i}] {option}")
    print(Fore.CYAN + "=" * 60)

def render_separator():

    print(Fore.CYAN + "-" * 60)


def render_subtitle(subtitle):

    print(Fore.MAGENTA + "-" * 60)
    print(Fore.WHITE + f"{subtitle.center(60)}")
    print(Fore.MAGENTA + "-" * 60)


def simular_citas(citas):

    if citas.empty():
        print("[INFO] No hay citas para procesar. La cola está vacía.")
        return

    print("[INFO] Simulación del procesamiento de citas iniciada...")
    print("[ALERTA] Las citas se atenderán en orden de prioridad (1 = Alta, 2 = Media, 3 = Baja).")
    
    print("\nEstado inicial de la cola de citas:")
    for prioridad, cita in citas.queue:
        print(f"- Prioridad: {prioridad}, Paciente ID: {cita['paciente_id']}, Médico ID: {cita['medico_id']}, Descripción: {cita['descripcion']}")
    
    print("─" * 40)

    while not citas.empty():
        prioridad, cita = citas.dequeue() 
        print(f"[ATENDIENDO] Paciente ID: {cita['paciente_id']}, Médico ID: {cita['medico_id']}, Descripción: {cita['descripcion']}, Prioridad: {prioridad}")
    
    print("\n[INFO] Simulación completada. Todas las citas han sido atendidas.")


def menu_principal():
    pacientes = cargar_pacientes()
    medicos = cargar_medicos()
    citas = cargar_citas()
    notificaciones = cargar_notificaciones()
    historial = cargar_historiales()

    while True:
        render_menu("SISTEMA DE GESTIÓN HOSPITALARIA", [
            "Gestión de Pacientes [P]",
            "Gestión de Médicos [M]",
            "Gestión de Citas [C]",
            "Historial Médico [H]",
            "Notificaciones [N]",
            "Reportes y Estadísticas [R]",
            "Exportar datos [E]",
            "Simular generación de datos automáticos [G]",
            "Salir [Q]"
        ])

        try:
            opcion = input(Fore.YELLOW + "Seleccione una opción: ").strip().upper()

            if opcion in ["1", "P"]:
                gestionar_pacientes(pacientes)
            elif opcion in ["2", "M"]:
                gestionar_medicos(medicos)
            elif opcion in ["3", "C"]:
                gestionar_citas(citas, pacientes, medicos)
            elif opcion in ["4", "H"]:
                gestionar_historial(historial, pacientes)
            elif opcion in ["5", "N"]:
                gestionar_notificaciones(notificaciones)
            elif opcion in ["6", "R"]:
                gestionar_reportes(pacientes, medicos, historial)
            elif opcion in ["7", "E"]:
                print("Seleccione qué datos desea exportar:")
                print("[1] Pacientes\n[2] Médicos\n[3] Citas\n[Q] Regresar")
                sub_opcion = input("Seleccione una opción: ").strip().upper()
                if sub_opcion == "1":
                    exportar_datos_a_csv("pacientes.csv", pacientes.values(), ["id", "nombre", "edad", "alergias"])
                elif sub_opcion == "2":
                    exportar_datos_a_csv("medicos.csv", medicos.values(), ["id", "nombre", "especialidad", "pacientes"])
                elif sub_opcion == "3":
                    exportar_datos_a_csv("citas.csv", citas.queue, ["paciente_id", "medico_id", "descripcion", "prioridad"])
                elif sub_opcion in ["Q"]:
                    print("Regresando al menú principal...")
                else:
                    print("[ERROR]: Opción no válida.")
            elif opcion in ["8", "G"]:
                pacientes, medicos, citas, notificaciones, historial = generar_datos_iniciales()
                print(Fore.GREEN + "[SIMULACIÓN]: Datos generados automáticamente.")
            elif opcion in ["9", "Q"]:
                guardar_pacientes(pacientes)
                guardar_medicos(medicos)
                guardar_citas(citas)
                guardar_notificaciones(notificaciones)
                guardar_historiales(historial)
                print(Fore.GREEN + "¡Gracias por usar el sistema! Hasta luego.")
                break
            else:
                raise ValueError("Opción no válida. Por favor, seleccione una opción de la lista.")
        except ValueError as ve:
            print(Fore.RED + f"[ERROR]: {ve}")
        except Exception as e:
            print(Fore.RED + f"[ERROR INESPERADO]: {e}")



def gestionar_pacientes(pacientes):
    while True:
        render_menu("GESTIÓN DE PACIENTES", [
            "Registrar nuevo paciente [1]",
            "Buscar paciente por nombre o ID [2]",
            "Buscar pacientes avanzados [3]",
            "Listar todos los pacientes [4]",
            "Eliminar paciente [5]",
            "Regresar al menú principal [Q]"
        ])

        try:
            opcion = input(Fore.YELLOW + "Seleccione una opción: ").strip().upper()

            if opcion in ["1"]:
                registrar_paciente(pacientes)
            elif opcion in ["2"]:
                buscar_paciente(pacientes)
            elif opcion in ["3"]:
                buscar_pacientes_inteligente(pacientes)
            elif opcion in ["4"]:
                listar_pacientes(pacientes)
            elif opcion in ["5"]:
                eliminar_paciente(pacientes)
            elif opcion in ["Q"]:
                print(Fore.GREEN + "Regresando al menú principal...")
                break
            else:
                raise ValueError("Opción no válida. Por favor, seleccione una opción de la lista.")
        except ValueError as ve:
            print(Fore.RED + f"[ERROR]: {ve}")
        except Exception as e:
            print(Fore.RED + f"[ERROR INESPERADO]: {e}")






def validar_id_paciente():
    while True:
        id_paciente = input("Ingrese el ID del paciente (5 di­gitos numericos): ")
        if id_paciente.isdigit() and len(id_paciente) == 5:
            return id_paciente
        else:
            print("ID invalido. El ID debe tener exactamente 5 di­gitos numericos.")

def validar_nombre():
    while True:
        nombre = input("Ingrese el nombre completo del paciente (Nombre Apellido): ")
        if len(nombre.split()) >= 2 and all(c.isalpha() or c.isspace() for c in nombre):
            return nombre
        else:
            print("Nombre invalido. Debe contener al menos un nombre y un apellido, y solo letras.")

def validar_edad():
    while True:
        edad = input("Ingrese la edad del paciente (0-99): ")
        if edad.isdigit() and 0 <= int(edad) <= 99:
            return edad
        else:
            print("Edad invalida. Debe ser un numero entre 0 y 99 sin ceros al inicio.")

def validar_alergias():
    while True:
        alergias = input("Ingrese las alergias del paciente (separadas por coma y espacio): ")
        if all(c.isalpha() or c.isspace() or c == "," for c in alergias) and alergias.count(",") >= 0:
            return alergias
        else:
            print("Alergias invalidas. Ingrese solo texto, separado por coma y espacio.")

def validar_especialidad():
    while True:
        especialidad = input("Ingrese la especialidad del medico: ")
        if especialidad.isalpha():
            return especialidad
        else:
            print("Especialidad invalida. Solo se permiten letras.")

def registrar_paciente(pacientes):
    print("Por favor, siga los siguientes ejemplos de formato al registrar un paciente:")
    print("- ID del paciente: 5 dígitos numéricos (ejemplo: 12345).")
    print("- Nombre completo: Formato 'Nombre Apellido' (ejemplo: 'Juan Pérez').")
    print("- Edad: Número entre 0 y 99 (ejemplo: 25).")
    print("- Alergias: Lista separada por coma y espacio (ejemplo: 'Maní, Gluten').")
    
    id_paciente = validar_id_paciente()
    
    nombre = validar_nombre()
    
    edad = validar_edad()
    
    while True:
        alergias = validar_alergias()
        if alergias.strip():
            break
        else:
            print("Error: Las alergias no pueden estar vacías. Intente nuevamente.")
    
    alergias_set = Conjunto()
    for a in alergias.split(", "):
        animacion_set_insercion(a) 
        alergias_set.add(a)

    
    paciente_info = {
        "nombre": nombre,
        "edad": edad,
        "alergias": list(alergias_set)
    }
    
    print("\nAlergias del paciente almacenadas en un Set para evitar duplicados:", alergias_set)
    print("El Conjunto asegura que una alergia no se repita.")
    animacion_hashmap_insercion(id_paciente, paciente_info)
    pacientes.put(id_paciente, paciente_info)

    print(f"Paciente {nombre} registrado exitosamente.")
    print(f"Total de pacientes registrados: {len(pacientes)}")
    
    guardar_pacientes(pacientes)



def buscar_paciente(pacientes):
    print("Ingrese el ID o parte del nombre del paciente para buscar.")
    busqueda = input("Búsqueda: ").strip()

    if busqueda in pacientes.keys():
        info = pacientes.get(busqueda)
        print(f"\nPaciente encontrado: ID: {busqueda}, Nombre: {info['nombre']}, Edad: {info['edad']}, Alergias: {', '.join(info['alergias'])}")
        return

    print("Utilizando el algoritmo KMP para realizar la búsqueda...")
    animacion_kmp_search(busqueda)  
    resultados = pacientes.search_by_field("nombre", busqueda)

    if resultados:
        print("\nPacientes encontrados:")
        for paciente_id, info in resultados:
            print(f"ID: {paciente_id}, Nombre: {info['nombre']}, Edad: {info['edad']}, Alergias: {', '.join(info['alergias'])}")
    else:
        print("No se encontraron pacientes que coincidan con la búsqueda.")




def listar_pacientes(pacientes):
    if pacientes.__len__() == 0:
        print("No hay pacientes registrados.")
    else:
        print("\nListado de pacientes:")
        for paciente_id, info in pacientes.items():
            print(f"ID: {paciente_id}, Nombre: {info['nombre']}, Edad: {info['edad']}, Alergias: {', '.join(info['alergias'])}")

def eliminar_paciente(pacientes):
    paciente_id = input("Ingrese el ID del paciente a eliminar: ").strip()

    if not paciente_id:
        print("Error: El ID no puede estar vacío. Intente nuevamente.")
        return

    try:
        print(f"Eliminando el paciente con ID {paciente_id}...")
        pacientes.remove(paciente_id)
        animacion_hashmap_eliminacion(paciente_id)  # Animación añadida aquí
        print(f"Paciente con ID {paciente_id} eliminado exitosamente del HashMap en tiempo promedio O(1).")
    except KeyError:
        print("Paciente no encontrado. Asegúrese de ingresar un ID válido.")
        return

    print(f"Total de pacientes restantes: {len(pacientes)}")
    print("\nEstado actual de los pacientes registrados:")
    for key, value in pacientes.items():
        print(f"- ID: {key}, Nombre: {value['nombre']}, Edad: {value['edad']}")





def gestionar_medicos(medicos):
    print("\n(Uso de HashMap para almacenar médicos, permitiendo búsqueda rápida por ID.)")

    while True:
        render_menu("GESTIÓN DE MÉDICOS", [
            "Registrar nuevo médico",
            "Buscar médico por nombre o ID",
            "Listar todos los médicos",
            "Eliminar médico",
            "Regresar al menú principal"
        ])
        
        opcion = input("Seleccione una opción: ").strip()
        
        if opcion == "1":
            registrar_medico(medicos)
        elif opcion == "2":
            buscar_medico(medicos)
        elif opcion == "3":
            listar_medicos(medicos)
        elif opcion == "4":
            eliminar_medico(medicos)
        elif opcion == "5":
            break
        else:
            print("Opción no válida. Intente nuevamente.")


def registrar_medico(medicos):
    print("Por favor, siga los siguientes ejemplos de formato al registrar un médico:")
    print("- ID del médico: Prefijo 'M-' seguido de 3 dígitos (ejemplo: M-123).")
    print("- Nombre completo: Formato 'Nombre Apellido' (ejemplo: 'Dr. Juan Pérez').")
    print("- Especialidad: Solo letras (ejemplo: 'Cardiología').")
    
    id_medico = validar_id_paciente()
    
    nombre = validar_nombre()
    
    while True:
        especialidad = validar_especialidad()
        if especialidad.strip():
            break
        else:
            print("Error: La especialidad no puede estar vacía. Intente nuevamente.")
    
    animacion_set_insercion(especialidad) 

    
    medico_info = {
        "nombre": nombre,
        "especialidad": especialidad,
        "pacientes": []
    }
    
    print("\nEspecialidad añadida al conjunto de especialidades médicas:", especialidad)
    animacion_hashmap_insercion(id_medico, medico_info)
    medicos.put(id_medico, medico_info)

    print(f"Médico {nombre} registrado exitosamente.")
    print(f"Total de médicos registrados: {len(medicos)}")
    
    guardar_medicos(medicos)




def buscar_medico(medicos):

    busqueda = input("Ingrese el ID o parte del nombre/especialidad del médico: ").strip()

    if busqueda in medicos.keys():
        info = medicos.get(busqueda)
        print(f"\nMédico encontrado: ID: {busqueda}, Nombre: {info['nombre']}, Especialidad: {info['especialidad']}")
        return

    print("Utilizando el algoritmo KMP para realizar la búsqueda...")
    animacion_kmp_search(busqueda) 
    resultados_nombre = medicos.search_by_field("nombre", busqueda)


    resultados_especialidad = medicos.search_by_field("especialidad", busqueda)

    resultados = resultados_nombre + resultados_especialidad

    if resultados:
        print("\nMédicos encontrados:")
        for medico_id, info in resultados:
            print(f"ID: {medico_id}, Nombre: {info['nombre']}, Especialidad: {info['especialidad']}")
    else:
        print("No se encontraron médicos que coincidan con la búsqueda.")




def listar_medicos(medicos):
    if medicos.__len__() == 0:
        print("No hay medicos registrados.")
    else:
        print("\nListado de medicos:")
        for medico_id, info in medicos.items():
            print(f"ID: {medico_id}, Nombre: {info['nombre']}, Especialidad: {info['especialidad']}")

def eliminar_medico(medicos):
    medico_id = input("Ingrese el ID del médico a eliminar: ").strip()

    if not medico_id:
        print("Error: El ID no puede estar vacío. Intente nuevamente.")
        return

    try:
        print(f"Eliminando el médico con ID {medico_id}...")
        medicos.remove(medico_id)
        print(f"Médico con ID {medico_id} eliminado exitosamente del HashMap en tiempo promedio O(1).")
    except KeyError:
        print("Médico no encontrado. Asegúrese de ingresar un ID válido.")
        return

    print(f"Total de médicos restantes: {len(medicos)}")
    print("\nEstado actual de los médicos registrados:")
    for key, value in medicos.items():
        print(f"- ID: {key}, Nombre: {value['nombre']}, Especialidad: {value['especialidad']}")



def gestionar_citas(citas, pacientes, medicos):
    print("\n(Uso de Priority Queue para gestionar las citas, priorizando urgencias de forma eficiente.)")

    while True:
        render_menu("GESTIÓN DE CITAS", [
            "Programar nueva cita",
            "Ver lista de citas programadas",
            "Simular procesamiento de citas",
            "Regresar al menú principal"
        ])
        
        opcion = input("Seleccione una opción: ").strip()
        
        if opcion == "1":
            programar_cita(citas, pacientes, medicos)
        elif opcion == "2":
            ver_citas(citas)
        elif opcion == "3":
            simular_citas(citas)   
        elif opcion == "4":
            break
        else:
            print("Opción no válida. Intente nuevamente.")




def programar_cita(citas, pacientes, medicos):
    print("Por favor, siga los siguientes ejemplos de formato al programar una cita:")
    print("- ID del paciente: 5 dígitos numéricos (ejemplo: 12345).")
    print("- ID del médico: Prefijo 'M-' seguido de 3 dígitos (ejemplo: M-123).")
    print("- Prioridad: 1 = Alta, 2 = Media, 3 = Baja.")

    paciente_id = input("Ingrese el ID del paciente: ").strip()
    if not paciente_id in pacientes.keys():
        print("Error: El paciente con ese ID no está registrado. Intente nuevamente.")
        return

    medico_id = input("Ingrese el ID del médico: ").strip()
    if not medico_id in medicos.keys():
        print("Error: El médico con ese ID no está registrado. Intente nuevamente.")
        return

    descripcion = input("Ingrese la descripción de la cita: ").strip()

    while True:
        try:
            prioridad = int(input("Ingrese la prioridad de la cita (1 = Alta, 2 = Media, 3 = Baja): "))
            if prioridad in [1, 2, 3]:
                break
            else:
                print("Error: La prioridad debe ser 1, 2 o 3.")
        except ValueError:
            print("Error: La prioridad debe ser un número entero.")

    if citas.empty():
        print("\nEstado actual de la cola de citas: Vacía.")
    else:
        print("\nEstado actual de la cola de citas (antes de agregar la nueva cita):")
        for prioridad_actual, cita_actual in citas.queue:
            print(f"- Prioridad: {prioridad_actual}, Paciente ID: {cita_actual['paciente_id']}, Médico ID: {cita_actual['medico_id']}, Descripción: {cita_actual['descripcion']}")


    cita = {
        "paciente_id": paciente_id,
        "medico_id": medico_id,
        "descripcion": descripcion,
        "prioridad": prioridad,
    }

    print("\nAñadiendo la cita a la cola de prioridad...")
    animacion_priorityqueue_insercion(prioridad, cita)

    citas.enqueue(prioridad, cita)

    print(f"\nCita programada exitosamente para el paciente {paciente_id} con el médico {medico_id}.")
    print("Cola de citas actualizada (ordenada por prioridad):")
    for prioridad, cita in citas.queue:
        print(f"- Prioridad: {prioridad}, Paciente ID: {cita['paciente_id']}, Médico ID: {cita['medico_id']}, Descripción: {cita['descripcion']}")
    print("\nRecuerda: Las citas con prioridad más alta (1) se atenderán primero.")




def ver_citas(citas):
    if citas.empty():
        print("No hay citas programadas.")
    else:
        print("\nCitas programadas:")
        for prioridad, cita in citas.queue:
            paciente_id = cita["paciente_id"]
            medico_id = cita["medico_id"]
            descripcion = cita["descripcion"]
            print(f"Prioridad: {prioridad}, Paciente ID: {paciente_id}, Médico ID: {medico_id}, Descripción: {descripcion}")


def priorizar_citas(citas):
    if citas.empty():
        print("No hay citas para priorizar.")
    else:
        print("\nCitas urgentes:")
        for prioridad, (paciente_id, descripcion) in citas.queue:
            if prioridad == 1:  
                print(f"Paciente: {paciente_id}, Descripcion: {descripcion}, Prioridad: {prioridad}")


def gestionar_historial(historial, pacientes):
    print("\n(Uso de Deque para manejar historiales médicos, asegurando acceso rápido al registro más reciente.)")

    while True:
        render_menu("GESTIÓN DE HISTORIAL MÉDICO", [
            "Ver historial de un paciente",
            "Agregar nuevo registro médico",
            "Regresar al menú principal"
        ])
        
        opcion = input("Seleccione una opción: ").strip()
        
        if opcion == "1":
            ver_historial(historial, pacientes)
        elif opcion == "2":
            agregar_registro_medico(historial, pacientes)
        elif opcion == "3":
            break
        else:
            print("Opción no válida. Intente nuevamente.")



def ver_historial(historial, pacientes):
    paciente_id = input("Ingrese el ID del paciente: ").strip()

    if not paciente_id in pacientes.keys():
        print("El paciente con ese ID no está registrado. Intente nuevamente.")
        return

    if paciente_id not in historial.keys():
        print(f"No hay historial médico registrado para el paciente con ID {paciente_id}.")
        return

    print(f"\nHistorial médico del paciente con ID {paciente_id}:")
    for registro in historial.get(paciente_id):
        print(f"- {registro}")

def agregar_registro_medico(historial, pacientes):
    paciente_id = input("Ingrese el ID del paciente: ").strip()

    if not paciente_id in pacientes.keys():
        print("El paciente con ese ID no está registrado. Intente nuevamente.")
        return

    consulta = input("Ingrese la descripción de la consulta o tratamiento: ").strip()


    if paciente_id not in historial.keys():
        historial.put(paciente_id, MyDeque())


    animacion_deque_insercion(consulta)
    historial.get(paciente_id).insertFront(consulta)
    print(f"Registro médico agregado exitosamente para el paciente con ID {paciente_id}.")

    print("\nHistorial actualizado (mostrando los últimos 3 registros más recientes):")
    registros = historial.get(paciente_id)
    for idx, reg in enumerate(list(registros)[:3], start=1): 
        print(f"{idx}. {reg}")
    
    print("\nNota: El Deque permite agregar registros al frente, facilitando el acceso a los más recientes.")



def gestionar_notificaciones(notificaciones):
    print("\n(Uso de Cola FIFO para manejar notificaciones: el primero en entrar es el primero en salir.)")

    while True:
        render_menu("GESTIÓN DE NOTIFICACIONES", [
            "Agregar nueva notificación",
            "Ver todas las notificaciones",
            "Eliminar notificación",
            "Regresar al menú principal"
        ])
        
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            agregar_notificacion(notificaciones)
        elif opcion == "2":
            ver_notificaciones(notificaciones)
        elif opcion == "3":
            eliminar_notificacion(notificaciones)
        elif opcion == "4":
            break
        else:
            print("Opción no válida. Intente nuevamente.")




def agregar_notificacion(notificaciones):
    mensaje = input("Ingrese el mensaje de la notificación: ").strip()
    
    print("\nEstado actual de la cola de notificaciones (antes de encolar):")
    if notificaciones.empty():
        print("La cola está vacía.")
    else:
        for i, notificacion in enumerate(notificaciones.to_list(), start=1):
            print(f"{i}. {notificacion}")
    
    animacion_queue_enqueue(mensaje)
    notificaciones.enqueue(mensaje)
    
    print("\nEstado actual de la cola de notificaciones (después de encolar):")
    for i, notificacion in enumerate(notificaciones.to_list(), start=1):
        print(f"{i}. {notificacion}")
    print("Esta cola es FIFO: la primera notificación en entrar será la primera en salir.")
    
    print("Notificación agregada exitosamente.")




def ver_notificaciones(notificaciones):
    if notificaciones.empty():
        print("No hay notificaciones.")
    else:
        print("\nNotificaciones:")
        for i, notificacion in enumerate(notificaciones.to_list(), start=1):
            print(f"{i}. {notificacion}")


def eliminar_notificacion(notificaciones):
    if notificaciones.empty():
        print("No hay notificaciones para eliminar. La cola está vacía.")
    else:
        print("\nEstado actual de la cola de notificaciones (antes de desencolar):")
        for i, notificacion in enumerate(notificaciones.to_list(), start=1):
            print(f"{i}. {notificacion}")
        
        notificacion_eliminada = notificaciones.dequeue()
        animacion_queue_dequeue()  # Animación añadida aquí
        
        print("\nEstado actual de la cola de notificaciones (después de desencolar):")
        if notificaciones.empty():
            print("La cola ahora está vacía.")
        else:
            for i, notificacion in enumerate(notificaciones.to_list(), start=1):
                print(f"{i}. {notificacion}")
        
        print("Recuerda: esta es una cola FIFO, se elimina la notificación más antigua primero.")
        print(f"Notificación eliminada: {notificacion_eliminada}")


def barra_progreso():
    import time
    for i in range(1, 101, 10):
        print(f"Cargando... {i}% completado", end="\r")
        time.sleep(0.2)
    print("Carga completa. Listo para usar el sistema.\n")
    
    
    
def reportar_pacientes_por_especialidad(medicos):

    especialidades_contador = {}
    
    for medico_id, info in medicos.items():
        especialidad = info["especialidad"]
        pacientes_asignados = len(info["pacientes"])
        if especialidad not in especialidades_contador:
            especialidades_contador[especialidad] = pacientes_asignados
        else:
            especialidades_contador[especialidad] += pacientes_asignados
    
    print("\n[INFO] Cantidad de pacientes por especialidad:")
    for especialidad, cantidad in especialidades_contador.items():
        print(f"{especialidad}: {cantidad} pacientes")
    
def reportar_pacientes_por_alergia(pacientes):

    alergia = input("Ingrese la alergia a buscar: ").strip()
    contador = 0

    for paciente_id, info in pacientes.items():
        if alergia in info["alergias"]:
            contador += 1

    print(f"\n[INFO] Hay {contador} pacientes con alergia a '{alergia}'.")


def top_pacientes_por_consultas(historial):

    pacientes_consultas = []

    for paciente_id, registros in historial.items():
        pacientes_consultas.append((paciente_id, len(registros)))

    top_3 = sorted(pacientes_consultas, key=lambda x: x[1], reverse=True)[:3]

    print("\n[INFO] Top 3 pacientes con más consultas:")
    for i, (paciente_id, consultas) in enumerate(top_3, start=1):
        print(f"{i}. Paciente ID: {paciente_id}, Número de consultas: {consultas}")


    
def gestionar_reportes(pacientes, medicos, historial):
    while True:
        render_menu("REPORTES Y ESTADÍSTICAS", [
            "Cantidad de pacientes por especialidad",
            "Cantidad de pacientes con una alergia específica",
            "Top 3 pacientes con más consultas",
            "Regresar al menú principal"
        ])
        
        opcion = input("Seleccione una opción: ").strip()
        
        if opcion == "1":
            animacion_generar_reportes()  # Animación añadida aquí
            reportar_pacientes_por_especialidad(medicos)
        elif opcion == "2":
            animacion_generar_reportes()  # Animación añadida aquí
            reportar_pacientes_por_alergia(pacientes)
        elif opcion == "3":
            animacion_generar_reportes()  # Animación añadida aquí
            top_pacientes_por_consultas(historial)
        elif opcion == "4":
            break
        else:
            print("[ERROR] Opción no válida. Intente nuevamente.")

            

def simular_procesamiento_citas(citas):

    if citas.empty():
        print("[INFO] No hay citas en la cola para procesar.")
        return

    print("\n[INFO] Simulación del procesamiento de citas iniciada...")
    print("[ALERTA] Las citas se atenderán en orden de prioridad (1 = Alta, 2 = Media, 3 = Baja).\n")

    print("Estado inicial de la cola de citas:")
    for prioridad, cita in citas.queue:
        print(f"- Prioridad: {prioridad}, Paciente ID: {cita['paciente_id']}, Médico ID: {cita['medico_id']}, Descripción: {cita['descripcion']}")
    print("─" * 40)

    while not citas.empty():
        prioridad, cita = citas.dequeue()
        print(f"[ATENDIENDO] Paciente ID: {cita['paciente_id']}, Médico ID: {cita['medico_id']}, Descripción: {cita['descripcion']}, Prioridad: {prioridad}")

    print("\n[INFO] Simulación completada. Todas las citas han sido atendidas.")



if __name__ == "__main__":
    print("Modulos importados correctamente:")
    print("- HashMap")
    print("- inventory_generator")
    print("- Queue")
    print("- PQueueSimplest, PQueueAP")
    print("- Conjunto")
    print("- MyDeque")
    
    menu_principal()
    

