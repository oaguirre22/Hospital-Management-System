Introducción
El Sistema de Gestión Hospitalaria es un proyecto diseñado como una solución innovadora para los desafíos administrativos que enfrentan los entornos hospitalarios modernos. Este sistema no solo organiza y procesa grandes volúmenes de información sobre pacientes, médicos, citas y notificaciones, sino que también aprovecha las ventajas de estructuras de datos avanzadas para garantizar eficiencia y precisión.
En un mundo donde la gestión de datos es esencial para mejorar la experiencia del paciente y optimizar los recursos médicos, este proyecto propone una herramienta robusta y escalable. A través de su implementación, se busca integrar algoritmos eficientes y técnicas de almacenamiento adecuadas para reducir tiempos de espera, evitar errores humanos y proporcionar una plataforma centralizada para las operaciones cotidianas.
Desarrollado como parte del curso de Estructuras de Datos 2, este sistema sirve no solo como una herramienta funcional, sino también como un ejercicio educativo para demostrar cómo las estructuras de datos avanzadas, como tablas hash, colas de prioridad y conjuntos, pueden transformar problemas complejos en soluciones prácticas.


Inspiración
 El desarrollo del Sistema de Gestión Hospitalaria nació de la necesidad de abordar problemas recurrentes en la administración de hospitales, clínicas y centros de atención médica. La inspiración principal fue crear una herramienta que, mediante estructuras de datos avanzadas, permitiera gestionar de manera eficiente tareas esenciales como el registro de pacientes, asignación de citas y almacenamiento de historiales médicos.
Además, el proyecto refleja el desafío constante de aplicar teorías aprendidas en el aula a problemas del mundo real. Este sistema busca simular un entorno hospitalario para ofrecer soluciones tangibles y escalables, demostrando cómo la correcta elección de estructuras de datos puede simplificar procesos complejos.
Objetivos Educativos
 Este proyecto no solo tiene fines prácticos, sino que también está diseñado para cumplir con objetivos educativos clave, tales como:
Comprensión y Aplicación de Estructuras de Datos Avanzadas: El sistema utiliza HashMaps para búsquedas rápidas, Priority Queues para manejar citas médicas urgentes y Deques para gestionar historiales médicos, entre otras estructuras.
Desarrollo de Habilidades de Programación Compleja: Integra módulos, algoritmos personalizados y técnicas de animación ASCII para crear una experiencia interactiva.
Optimización de Procesos: A través de la implementación de estructuras como tablas hash y colas, se busca reducir la complejidad temporal de las operaciones y demostrar su eficiencia en escenarios reales.
Colaboración entre Diferentes Áreas de la Computación: Este proyecto combina la teoría de estructuras de datos, algoritmos avanzados y habilidades prácticas de desarrollo de software, fomentando una visión integral.


Objetivo del Proyecto
El Sistema de Gestión Hospitalaria tiene como objetivo principal el desarrollo de una herramienta que permita administrar de manera eficiente los procesos esenciales en un entorno hospitalario. Este proyecto busca automatizar tareas que, en muchos casos, se realizan manualmente y pueden estar sujetas a errores humanos, como la gestión de citas, el registro de pacientes y el almacenamiento de historiales médicos.
Objetivos Principales
Implementar Soluciones de Alto Desempeño: Utilizar estructuras de datos avanzadas, como tablas hash, colas de prioridad y conjuntos, para garantizar que las operaciones del sistema sean rápidas y escalables.
Optimizar la Asignación de Recursos: Diseñar algoritmos que aseguren una asignación eficiente de citas médicas y la correcta priorización de pacientes en función de la urgencia de su atención.
Proveer una Experiencia de Usuario Intuitiva: Ofrecer un sistema con menús claros y animaciones interactivas que guíen al usuario durante la operación del software.
Facilitar el Análisis de Datos: Incorporar herramientas para generar reportes estadísticos útiles, como la distribución de pacientes por especialidad médica o el análisis de historiales médicos.
Asegurar la Persistencia de Datos: Implementar mecanismos para guardar y recuperar información en archivos, asegurando que los datos no se pierdan entre sesiones.



Desarrollo
El desarrollo del Sistema de Gestión Hospitalaria se basa en la aplicación de estructuras de datos avanzadas, diseñadas para optimizar el manejo de información médica en un entorno hospitalario. A continuación, se detallan los componentes principales del sistema, las estructuras utilizadas, y cómo cada módulo contribuye al cumplimiento de los objetivos.
1. Componentes del Sistema
El sistema se organiza en módulos especializados, cada uno con una funcionalidad clara y definida:
Gestión de Pacientes: Registro, búsqueda y eliminación de pacientes utilizando tablas hash para garantizar búsquedas rápidas y efectivas.
Gestión de Médicos: Administración de información sobre médicos, incluyendo especialidades y pacientes asignados, también mediante tablas hash.
Gestión de Citas: Uso de colas de prioridad para ordenar y procesar citas según la urgencia, asegurando una atención eficiente.
Historial Médico: Manejo de historiales médicos mediante deques (colas de doble extremo), permitiendo un acceso rápido a registros recientes.
Notificaciones: Uso de colas tradicionales para implementar un sistema FIFO (First In, First Out) que gestiona recordatorios y alertas.
Reportes y Estadísticas: Herramientas para analizar datos y generar informes útiles sobre el funcionamiento hospitalario.
2. Estructuras de Datos Implementadas
Cada módulo está diseñado para aprovechar las ventajas de diferentes estructuras de datos:
HashMap (Tabla Hash): Almacena datos de pacientes, médicos e historiales, permitiendo operaciones de inserción, búsqueda y eliminación con un costo promedio de O(1).
PQueueAP (Cola de Prioridad): Ordena las citas médicas según su prioridad, con un costo de O(log⁡n) para inserciones y eliminaciones.
Deque (Cola de Doble Extremo): Almacena historiales médicos, facilitando el acceso rápido a registros recientes y soporte para operaciones FIFO y LIFO.
Queue (Cola Simple): Maneja notificaciones en orden de llegada, con un costo de O(1) para inserciones y eliminaciones.
Set (Conjunto): Almacena especialidades médicas y alergias, garantizando unicidad y búsquedas eficientes.
3. Persistencia de Datos
El sistema implementa un mecanismo robusto para guardar datos en archivos de texto. Esto permite:
Recuperar información entre sesiones.
Exportar datos en formato CSV para análisis externo.
Garantizar la integridad y accesibilidad de la información médica.
4. Interfaz del Usuario
El sistema incluye menús interactivos y animaciones que guían al usuario a través de las funcionalidades. Estas animaciones hacen uso de la biblioteca colorama para enriquecer la experiencia visual.
5. Algoritmos Específicos
Algunos de los algoritmos diseñados específicamente para este sistema incluyen:
Algoritmo KMP (Knuth-Morris-Pratt): Para realizar búsquedas avanzadas de patrones en cadenas, como nombres de pacientes o médicos.
Gestión de Prioridades: Basado en estructuras de montículo para ordenar y procesar citas según su urgencia.
Generación de Reportes: Análisis estadístico de datos médicos para detectar tendencias y áreas de mejora.
6. Flujo de Trabajo
El sistema comienza cargando los datos guardados previamente desde archivos. Posteriormente, los usuarios interactúan con el menú principal para realizar diversas operaciones. Al cerrar la sesión, toda la información actualizada se guarda automáticamente, asegurando la persistencia de datos.



¿Cómo funciona el SISTEMA DE GESTIÓN HOSPITALARIA?
El Sistema de Gestión Hospitalaria opera como una solución integral para automatizar los procesos administrativos de un entorno hospitalario, implementando estructuras de datos avanzadas y algoritmos eficientes que garantizan el manejo óptimo de información. Cada componente del sistema está diseñado para cumplir una función específica, aprovechando las propiedades inherentes de las estructuras de datos empleadas.
A continuación, se detalla el funcionamiento de cada módulo y cómo contribuye al sistema en su conjunto:
1. Gestión de Pacientes
La gestión de pacientes es uno de los pilares fundamentales del sistema, ya que garantiza un manejo eficiente de la información relacionada con los individuos atendidos en el hospital.
Estructura utilizada:


Una tabla hash (HashMap) almacena los datos de cada paciente, permitiendo búsquedas, inserciones y eliminaciones en tiempo promedio O(1). Cada entrada de la tabla hash se asocia a un ID único que identifica al paciente.
Conjuntos (Set) se utilizan para almacenar alergias específicas, evitando duplicados.
Funciones principales:


Registro de Pacientes: Los pacientes son registrados con información clave como su nombre, edad y alergias. La función valida que no existan duplicados en el registro.
Búsqueda de Pacientes: La búsqueda puede realizarse por ID o mediante algoritmos avanzados como Knuth-Morris-Pratt (KMP) para encontrar coincidencias parciales en nombres.
Eliminación de Pacientes: Los pacientes pueden eliminarse rápidamente gracias a las propiedades de la tabla hash.
Flujo de datos: Al agregar un nuevo paciente, la tabla hash asigna un bucket (compartimiento) basado en un valor hash calculado a partir del ID del paciente. Esto asegura una distribución uniforme y eficiente de los datos.


2. Gestión de Médicos
Este módulo organiza la información de los médicos registrados, incluyendo su especialidad y pacientes asignados.
Estructura utilizada:


Similar al módulo de pacientes, se utiliza una tabla hash para almacenar los datos de los médicos, con su ID como clave principal.
Conjuntos (Set): Se emplean para gestionar las especialidades médicas disponibles.
Funciones principales:


Registro y Eliminación de Médicos: Permite añadir y remover médicos del sistema.
Búsqueda por Especialidad o Nombre: Utiliza la tabla hash para búsquedas directas y el algoritmo KMP para búsquedas avanzadas.
Gestión de Especialidades: Asegura que las especialidades médicas estén organizadas sin duplicados mediante conjuntos.
Relación con otros módulos: Los médicos están relacionados directamente con las citas médicas y los pacientes que atienden, estableciendo conexiones dinámicas dentro del sistema.


3. Gestión de Citas Médicas
El módulo de citas es crítico para la funcionalidad del sistema, ya que organiza y prioriza las consultas médicas en función de su gravedad.
Estructura utilizada:


Una cola de prioridad gestiona las citas, donde las consultas con mayor prioridad (gravedad) son atendidas primero. La implementación asegura que las operaciones de inserción y extracción se realicen en tiempo O(log n).
Se emplea una cola FIFO para simular el flujo de citas.
Funciones principales:


Programación de Citas: Las citas se registran con información como el ID del paciente, el médico asignado, la descripción y la prioridad.
Simulación de Procesamiento: Procesa las citas en orden de prioridad, generando una lista clara de las consultas atendidas.
Listar Citas Programadas: Permite visualizar todas las citas ordenadas por prioridad.
Ventajas del sistema: El uso de colas de prioridad asegura que los casos urgentes sean atendidos inmediatamente, mientras que los casos de menor prioridad se mantienen en espera de manera organizada.


4. Historial Médico
El historial médico de cada paciente se gestiona mediante una estructura de deque, la cual permite acceder y actualizar los registros más recientes con rapidez.
Estructura utilizada:


Una deque (Double-Ended Queue) almacena los registros médicos de cada paciente. Esta estructura permite añadir registros al frente o al final, ofreciendo flexibilidad para manejar datos cronológicos.
Funciones principales:


Consulta del Historial: Permite al usuario visualizar los registros médicos asociados a un paciente.
Añadir Nuevos Registros: Agrega un registro al frente de la deque, garantizando que las consultas recientes sean las primeras en mostrarse.
Ventajas del sistema: La deque proporciona un acceso eficiente tanto a los registros más antiguos como a los más recientes, lo cual es esencial en entornos médicos donde la información cronológica es crucial.


5. Gestión de Notificaciones
Este módulo utiliza una cola FIFO para manejar las notificaciones generadas por el sistema.
Estructura utilizada:


Una cola se emplea para gestionar las notificaciones de manera que las más antiguas se eliminen primero, siguiendo el principio "Primero en entrar, primero en salir" (FIFO).
Funciones principales:


Agregar Notificaciones: Genera nuevos mensajes que se encolan en la estructura.
Visualización: Permite listar todas las notificaciones pendientes.
Eliminación: Extrae la notificación más antigua de la cola.
Aplicaciones en el sistema: Las notificaciones se utilizan para informar al usuario sobre eventos importantes, como nuevas citas, actualizaciones de pacientes y reportes generados.


6. Reportes y Estadísticas
Este módulo analiza los datos almacenados en el sistema para generar reportes informativos.
Estructura utilizada:


Se combinan estructuras como tablas hash, listas y conjuntos para compilar estadísticas clave.
Funciones principales:


Pacientes por Especialidad: Genera un conteo de pacientes por cada especialidad médica.
Pacientes por Alergia: Busca pacientes que comparten una alergia específica.
Top 3 Pacientes con Más Consultas: Ordena y muestra los pacientes que más consultas médicas han registrado.
Relevancia: Este módulo permite obtener una visión general del funcionamiento hospitalario, identificando áreas críticas y patrones de atención.


7. Persistencia de Datos
Para garantizar que los datos se conserven entre sesiones, el sistema utiliza archivos de texto para almacenar información.
Estructura utilizada:


Los datos de pacientes, médicos, citas, historiales y notificaciones se guardan en archivos planos (.txt) en la carpeta data.
Proceso:


Cada vez que se realiza una operación, los datos son automáticamente guardados en los archivos correspondientes.
Al iniciar el programa, el sistema carga estos datos para restaurar el estado anterior.
Flujo General del Sistema
El sistema inicia cargando datos almacenados previamente en archivos.
El usuario interactúa con el menú principal, seleccionando una funcionalidad específica.
Cada acción seleccionada ejecuta funciones específicas que utilizan estructuras de datos para realizar operaciones rápidas y eficientes.
Se garantiza la retroalimentación visual mediante animaciones ASCII y mensajes en pantalla.
Al cerrar el sistema, los datos se guardan automáticamente en los archivos correspondientes.

Optimización Mediante Estructuras de Datos
El uso de estructuras de datos avanzadas es clave para el rendimiento del sistema:
Tablas Hash: Acceso directo a datos mediante claves únicas.
Colas de Prioridad: Procesamiento eficiente de elementos según su urgencia.
Deque: Gestión dinámica y cronológica de registros.
Conjuntos: Eliminación automática de duplicados y búsquedas rápidas.
Requisitos Previos
Para ejecutar el SISTEMA DE GESTIÓN HOSPITALARIA, es necesario cumplir con ciertos requisitos previos para garantizar su correcto funcionamiento. A continuación, se detallan los elementos necesarios:
Software Requerido
Python 3.9 o superior: Lenguaje de programación utilizado para el desarrollo del sistema.
Editor de texto o IDE: Es preferible usar herramientas como Spyder (parte de Anaconda) o Visual Studio Code, ya que facilitan la gestión y depuración del código.
Sistema Operativo: Este proyecto es compatible con Windows, macOS y distribuciones de Linux.
Bibliotecas Esenciales:
colorama: Utilizada para la personalización del texto en la consola con colores.
os: Para la manipulación de archivos y directorios.
random: Usada en la generación de datos ficticios para pruebas.
Ejemplos de Uso
A continuación, se presentan algunos casos de uso representativos del sistema:
Caso de Uso 1: Registro de Pacientes
El sistema permite registrar pacientes nuevos a través del menú interactivo:
Seleccione la opción Gestión de Pacientes.
Dentro de esta sección, elija Registrar nuevo paciente.
Proporcione los datos requeridos:
ID del paciente: Un identificador único de 5 dígitos.
Nombre completo.
Edad: Un valor entre 0 y 99 años.
Lista de alergias: Ingrese las alergias separadas por comas.
Resultado esperado:
El sistema registra al paciente y lo almacena en el HashMap correspondiente, mostrando un resumen del registro.
Caso de Uso 2: Programación de Citas
Las citas se gestionan mediante una Priority Queue para priorizar la urgencia:
Acceda a Gestión de Citas en el menú principal.
Seleccione Programar nueva cita.
Proporcione la información solicitada:
ID del paciente.
ID del médico.
Descripción de la cita.
Nivel de prioridad: 1 (Alta), 2 (Media), o 3 (Baja).
Resultado esperado:
La cita se agrega a la cola de prioridades y el sistema actualiza el estado de la misma.
Caso de Uso 3: Generación de Reportes
Se puede generar un análisis detallado de datos almacenados en el sistema:
Elija Reportes y Estadísticas en el menú.
Seleccione uno de los reportes disponibles:
Pacientes por especialidad.
Pacientes con alergias específicas.
Top 3 pacientes con mayor número de consultas.
Resultado esperado:
El sistema genera un reporte detallado en consola, presentando la información solicitada con claridad.
Áreas de Mejora
Nuevas Funcionalidades: Agregar soporte para la gestión de inventarios médicos o medicamentos.
Interfaz Mejorada: Optimizar la experiencia de usuario mediante una interfaz gráfica o mejoras en la consola.
Ampliación del Modelo: Implementar análisis avanzados con datos masivos utilizando estructuras de datos adicionales como grafos.





4. Metodología de Desarrollo y Flujo de Trabajo
El SISTEMA DE GESTIÓN HOSPITALARIA fue desarrollado siguiendo una metodología estructurada que abarcó desde la planificación inicial hasta la implementación y pruebas finales. Este enfoque metódico aseguró que el sistema cumpliera tanto con los requerimientos funcionales como con los objetivos educativos. A continuación, se detallan las etapas principales del desarrollo y el flujo de trabajo implementado.
Etapa 1: Identificación de Requisitos
En esta fase, se definieron claramente las funcionalidades esenciales que el sistema debía cubrir:
Gestión eficiente de pacientes, médicos, citas, historiales y notificaciones.
Priorización de citas según la urgencia médica.
Persistencia de datos entre sesiones.
Implementación de reportes estadísticos relevantes.
Interfaz interactiva y de fácil uso en consola.
Además, se seleccionaron las estructuras de datos más adecuadas para cada funcionalidad, considerando factores como eficiencia, escalabilidad y facilidad de implementación.
Etapa 2: Diseño del Sistema
Con los requisitos claros, se diseñó una arquitectura modular para el sistema, asegurando que cada componente tuviera una funcionalidad específica y que fuera fácil de mantener y extender.
 Decisiones clave en el diseño:
Uso de HashMaps para búsquedas rápidas.
Empleo de colas de prioridad para manejar urgencias en citas.
Implementación de deques para gestionar historiales médicos cronológicamente.
Separación de lógica de negocios y persistencia de datos en módulos independientes.
Se desarrolló un diagrama de flujo para representar cómo interactuarían los usuarios con el sistema y cómo se manejarían las operaciones internas.
Etapa 3: Desarrollo
El desarrollo del sistema se realizó en Python, utilizando un enfoque iterativo:
Estructuras de datos: Se desarrollaron e implementaron clases personalizadas para las estructuras utilizadas (HashMap, Priority Queue, Deque, etc.), asegurando que cumplieran con los requisitos de eficiencia.
Funcionalidades principales: Cada módulo del sistema (gestión de pacientes, médicos, citas, etc.) fue implementado de manera individual, probándose de forma aislada antes de integrarse.
Persistencia de datos: Se diseñaron funciones para guardar y cargar datos en archivos .txt, garantizando la integridad de la información.
Interfaz interactiva: Se desarrollaron menús dinámicos y animaciones ASCII para guiar al usuario, utilizando la biblioteca colorama.
Etapa 4: Pruebas y Optimización
Una vez implementadas todas las funcionalidades, el sistema pasó por una serie de pruebas exhaustivas:
Pruebas de funcionalidad: Validación de cada operación, desde el registro de pacientes hasta la generación de reportes.
Pruebas de estrés: Evaluación del desempeño del sistema con grandes volúmenes de datos.
Pruebas de integridad de datos: Comprobación de que la información almacenada en archivos se recuperaba correctamente.
Flujo de Trabajo del Sistema
Carga Inicial: El sistema comienza cargando los datos almacenados en archivos para restaurar el estado anterior.
Interacción del Usuario: A través de menús interactivos, el usuario realiza operaciones específicas, como registrar pacientes, programar citas o generar reportes.
Ejecución de Operaciones: Cada operación ejecuta funciones internas que utilizan estructuras de datos avanzadas para garantizar eficiencia y precisión.
Persistencia de Datos: Los cambios realizados se guardan automáticamente en archivos al finalizar la sesión.

6. Preguntas Frecuentes (FAQ)
P: ¿Qué hacer si el sistema no carga los datos al iniciar?
 R: Asegúrese de que los archivos necesarios (data_pacientes.txt, data_medicos.txt, etc.) existan en la carpeta data. Si los archivos no están presentes, el sistema generará estructuras vacías al iniciar.
P: ¿Cómo puedo extender el sistema para manejar inventarios médicos?
 R: Puede añadir un nuevo módulo que utilice una tabla hash para almacenar información sobre medicamentos o suministros. Además, se puede integrar con las funciones de reportes para analizar el uso de inventarios.
P: ¿Es posible cambiar el diseño del sistema para usar una base de datos en lugar de archivos de texto?
 R: Sí, el sistema está diseñado de manera modular, lo que facilita la sustitución del almacenamiento en archivos por una base de datos como SQLite o PostgreSQL. Simplemente tendría que reescribir las funciones de persistencia.
P: ¿Puedo agregar más campos a los registros de pacientes o médicos?
 R: Claro. Puede modificar las estructuras de datos en el módulo correspondiente para incluir los nuevos campos, así como actualizar las funciones de guardado y carga para reflejar estos cambios.
P: ¿Qué sucede si dos pacientes tienen el mismo nombre?
 R: Los pacientes se identifican de forma única mediante su ID. Aunque puedan compartir nombres, el sistema garantiza que cada registro sea único gracias a este identificador.
P: ¿Qué hago si quiero priorizar automáticamente todas las citas de una especialidad médica?
 R: Puede modificar el módulo de citas para incluir una función que ajuste las prioridades en base a criterios específicos, como la especialidad médica.

7. Limitaciones Actuales del Sistema
Aunque el SISTEMA DE GESTIÓN HOSPITALARIA cumple con sus objetivos principales, existen ciertas limitaciones técnicas y de diseño que se deben considerar para futuras mejoras:
Almacenamiento en Archivos de Texto:


Los datos se guardan en archivos planos (.txt), lo que limita la capacidad de manejar grandes volúmenes de información de manera eficiente.
No hay soporte para transacciones o concurrencia en el acceso a datos.
Interfaz Basada en Consola:


La interacción con el usuario se realiza exclusivamente a través de la consola, lo que puede no ser ideal para usuarios no técnicos.
No hay soporte para interfaces gráficas o aplicaciones web.
Capacidad Escalable Limitada:


Aunque las estructuras de datos utilizadas son eficientes, el diseño actual no está optimizado para manejar datos masivos en tiempo real.
La persistencia basada en archivos no es adecuada para sistemas hospitalarios con múltiples usuarios simultáneos.
Falta de Personalización en Reportes:


Los reportes generados están predefinidos y no permiten filtros personalizados o análisis avanzados.
Gestión de Seguridad:


No hay mecanismos de autenticación o autorización, lo que podría ser un problema en entornos reales donde la privacidad de los datos es crítica.
Soporte Multilenguaje:


Actualmente, el sistema solo opera en español, lo que limita su aplicabilidad en entornos internacionales.
