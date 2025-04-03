from modules.hash_map import HashMap
import random
import string

familias = HashMap([
    ("PF", HashMap([
        ("KB", "Keyboards"),
        ("MS", "Headphones"),
        ("HD", "Headphones"),
        ("MO", "Monitors")
    ])),
    ("CP", HashMap([
        ("MB", "Motherboards"),
        ("CS", "Cases"),
        ("RM", "RAM"),
        ("PS", "Power Supplies")
    ])),
    ("ST", HashMap([
        ("HD", "Hard Drives"),
        ("SD", "Solid State Drives"),
        ("US", "USB Drives")
    ])),
    ("LT", HashMap([
        ("LP", "Laptops"),
        ("NB", "Notebooks")
    ]))
])

marcas = ["AK", "LG", "MS", "DE", "HP", "AS", "AC", "SA", "CR"]


def inventory_generator(file_name="inventory.txt", size=100):
    """Genera un archivo de inventario con productos aleatorios."""
    alphanumeric = string.ascii_uppercase + string.digits

    with open(file_name, "w") as file:
        for _ in range(size):
            familia_codigo, subfamilias = random.choice(familias.items())
            subfamilia_codigo, subfamilia_nombre = random.choice(subfamilias.items())
            marca = random.choice(marcas)
            clave_modelo = ''.join(random.choice(alphanumeric) for _ in range(3))
            clave_producto = f"{familia_codigo}{subfamilia_codigo}{marca}{clave_modelo}"
            qty = random.randint(0, 100)
            descripcion = f"{subfamilia_nombre} {marca} {clave_modelo}"
            file.write(f"{clave_producto} | {descripcion} | qty: {qty}\n")


if __name__ == "__main__":
    inventory_generator("example_inventory.txt", 100)
