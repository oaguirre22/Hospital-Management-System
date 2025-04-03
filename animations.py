import time
import os
from colorama import Fore, Style, init

init(autoreset=True)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

#########################
# Animaciones con extras#
#########################

def animacion_hashmap_insercion(key, value):
    """
    Animación ASCII para simular la inserción de un elemento en un HashMap.
    Muestra cálculo de hash, buckets, inserción y mensaje final.
    Incluye color, diagramas ASCII y pausas.
    """
    clear_screen()
    print("╔════════════════════════════╗")
    print("║    INSERCIÓN EN HASHMAP    ║")
    print("╚════════════════════════════╝")
    time.sleep(1)

    # Paso 1: Cálculo de hash
    clear_screen()
    print("Calculando hash para la clave:", key)
    time.sleep(1)
    input("Presione Enter para continuar...")  # Interactividad
    clear_screen()

    # Paso 2: Mostrar buckets antes de la inserción (ejemplo)
    print("Buckets del HashMap antes:")
    print("[Bucket 0] -> []")
    print("[Bucket 1] -> []")
    print("[Bucket 2] -> []")
    print("[Bucket 3] -> []")
    print("[Bucket 4] -> []")
    print("[Bucket 5] -> []   <--- Aquí insertaremos")
    time.sleep(1)
    input("Presione Enter para insertar en el Bucket...")
    clear_screen()

    # Paso 3: Insertar
    print("Insertando en Bucket 5...")
    time.sleep(1)
    clear_screen()

    # Paso 4: Mensaje final con color
    print(Fore.GREEN + "¡Guardado exitoso en el HashMap!" + Style.RESET_ALL)
    time.sleep(1)

def animacion_hashmap_eliminacion(key):
    """
    Animación ASCII para simular la eliminación de un elemento del HashMap.
    """
    clear_screen()
    print("╔════════════════════════════╗")
    print("║ ELIMINACIÓN EN HASHMAP     ║")
    print("╚════════════════════════════╝")
    time.sleep(1)
    print(f"Buscando la clave '{key}' en los buckets...")
    time.sleep(1)
    print("Clave encontrada, eliminando...")
    time.sleep(1)
    clear_screen()
    print(Fore.GREEN + f"¡El elemento con clave '{key}' ha sido eliminado con éxito!")
    time.sleep(1)

def animacion_queue_enqueue(elemento):
    """
    Animación ASCII para la inserción en la Cola (Queue).
    Muestra el proceso paso a paso con color y pausas.
    """
    clear_screen()
    print("╔════════════════════════════╗")
    print("║      ENCOLANDO EN QUEUE    ║")
    print("╚════════════════════════════╝")
    time.sleep(1)

    print("Preparando espacio en la cola...")
    time.sleep(1)
    clear_screen()

    print("Agregando '{}' a la cola...".format(elemento))
    time.sleep(1)
    clear_screen()

    print(Fore.GREEN + "¡Notificación encolada con éxito!" + Style.RESET_ALL)
    time.sleep(1)

def animacion_queue_dequeue():
    """
    Animación ASCII para la operación dequeue en la cola.
    """
    clear_screen()
    print("╔════════════════════════════╗")
    print("║      DESENCOLANDO QUEUE    ║")
    print("╚════════════════════════════╝")
    time.sleep(1)
    print("Extrayendo el primer elemento de la cola...")
    time.sleep(1)
    clear_screen()
    print(Fore.GREEN + "¡Elemento eliminado de la cola con éxito!")
    time.sleep(1)

def animacion_priorityqueue_insercion(prioridad, cita):
    """
    Animación ASCII para la inserción en la Priority Queue.
    Muestra una barra de progreso y el reordenamiento.
    """
    clear_screen()
    print("╔════════════════════════════╗")
    print("║ INSERCIÓN EN PRIORITY QUEUE║")
    print("╚════════════════════════════╝")
    time.sleep(1)

    print(f"Insertando cita con prioridad: {prioridad}")
    print(f"Detalles de la cita: {cita}")
    time.sleep(1)
    clear_screen()

    # Barra de progreso simulada
    print("Procesando: [##.......] (20%)")
    time.sleep(0.5)
    clear_screen()
    print("Procesando: [#####....] (50%)")
    time.sleep(0.5)
    clear_screen()
    print("Procesando: [########.] (80%)")
    time.sleep(0.5)
    clear_screen()

    print(Fore.GREEN + "¡Cita insertada con éxito en la cola de prioridad!" + Style.RESET_ALL)
    time.sleep(1)

def animacion_generar_reportes():
    """
    Animación ASCII para la generación de reportes.
    """
    clear_screen()
    print("╔════════════════════════════╗")
    print("║   GENERANDO REPORTES...    ║")
    print("╚════════════════════════════╝")
    for i in range(1, 6):
        print(f"Procesando sección {i}/5...")
        time.sleep(0.5)
    clear_screen()
    print(Fore.GREEN + "¡Reporte generado con éxito!")
    time.sleep(1)

def animacion_set_insercion(elemento):
    """
    Animación ASCII para agregar una especialidad al Set.
    Muestra verificación de duplicados.
    """
    clear_screen()
    print("╔════════════════════════════╗")
    print("║   AGREGANDO AL CONJUNTO    ║")
    print("╚════════════════════════════╝")
    time.sleep(1)

    print(f"Verificando duplicados para '{elemento}'...")
    time.sleep(1)
    clear_screen()

    print("Insertando en el conjunto si no existe...")
    time.sleep(1)
    clear_screen()

    print(Fore.GREEN + "¡Elemento agregado al Conjunto!" + Style.RESET_ALL)
    time.sleep(1)

def animacion_deque_insercion(registro):
    """
    Animación ASCII para insertar un registro al frente del Deque (Historial).
    """
    clear_screen()
    print("╔════════════════════════════╗")
    print("║ INSERCIÓN EN DEQUE (HIST.) ║")
    print("╚════════════════════════════╝")
    time.sleep(1)

    print(f"Agregando '{registro}' al frente del deque...")
    time.sleep(1)
    clear_screen()

    print(Fore.GREEN + "¡Registro agregado con éxito al historial!" + Style.RESET_ALL)
    time.sleep(1)

def animacion_kmp_search(patron):
    """
    Animación ASCII para simular la búsqueda con KMP.
    Agrega referencias conceptuales.
    """
    clear_screen()
    print("╔════════════════════════════╗")
    print("║      BÚSQUEDA CON KMP      ║")
    print("╚════════════════════════════╝")
    time.sleep(1)

    print("Construyendo tabla de prefijos...")
    time.sleep(1)
    clear_screen()

    print("La tabla de prefijos ayuda a retroceder eficientemente ante fallas.")
    time.sleep(1)
    clear_screen()

    print(f"Buscando el patrón '{patron}' en los datos...")
    time.sleep(1)
    clear_screen()

    print(Fore.GREEN + "Búsqueda completada con KMP." + Style.RESET_ALL)
    time.sleep(1)
