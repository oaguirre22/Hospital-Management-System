import random


class PQueueSimplest:
    """Cola de prioridad simple, ordena elementos de menor a mayor prioridad."""

    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        """Añade un elemento y lo ordena en la cola."""
        self.queue.append(data)
        self.queue.sort()

    def dequeue(self):
        """Elimina y devuelve el elemento con mayor prioridad (el menor valor)."""
        if not self.queue:
            raise IndexError("No se puede desencolar de una cola vacía.")
        return self.queue.pop(0)

    def peek(self):
        """Devuelve el elemento con mayor prioridad sin eliminarlo."""
        if not self.queue:
            raise IndexError("No se puede hacer peek en una cola vacía.")
        return self.queue[0]

    def size(self):
        """Devuelve el tamaño de la cola."""
        return len(self.queue)

    def empty(self):
        """Comprueba si la cola está vacía."""
        return not self.queue

    def __repr__(self):
        """Representación de la cola como lista."""
        return f"{self.queue}"


class PQueueAP:
    """Cola de prioridad avanzada con claves explícitas de prioridad."""

    def __init__(self):
        self.queue = []

    def enqueue(self, priority, data):
        """Añade un elemento con una prioridad explícita y lo ordena."""
        self.queue.append((priority, data))
        self.queue.sort(key=lambda x: x[0])

    def dequeue(self):
        """Elimina y devuelve el elemento con mayor prioridad."""
        if not self.queue:
            raise IndexError("No se puede desencolar de una cola vacía.")
        priority, data = self.queue.pop(0)
        return priority, data

    def peek(self):
        """Devuelve el elemento con mayor prioridad sin eliminarlo."""
        if not self.queue:
            raise IndexError("No se puede hacer peek en una cola vacía.")
        return self.queue[0][0], self.queue[0][1]

    def size(self):
        """Devuelve el tamaño de la cola."""
        return len(self.queue)

    def empty(self):
        """Comprueba si la cola está vacía."""
        return not self.queue

    def __repr__(self):
        """Representación de la cola como lista de tuplas (prioridad, valor)."""
        return f"{self.queue}"


#Pruebas
if __name__ == "__main__":
    print("\n--- Pruebas para PQueueSimplest ---")
    qsimple = PQueueSimplest()
    for i in range(10):
        qsimple.enqueue(random.randint(10, 99))
    print(f"Cola inicial: {qsimple}")
    print(f"Peek: {qsimple.peek()}")
    print(f"Desencolado: {qsimple.dequeue()}")
    print(f"Cola después de desencolar: {qsimple}")

    print("\n--- Pruebas para PQueueAP ---")
    qcomplex = PQueueAP()
    for i in range(10):
        qcomplex.enqueue(random.randint(0, 10), random.randint(10, 99))
    print(f"Cola inicial: {qcomplex}")
    print(f"Peek: {qcomplex.peek()}")
    print(f"Desencolado: {qcomplex.dequeue()}")
    print(f"Cola después de desencolar: {qcomplex}")

    