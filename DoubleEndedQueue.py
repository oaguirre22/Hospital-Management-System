class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None
        self.anterior = None


class MyDeque:
    def __init__(self):
        self.frente = None
        self.rear = None

    def insertFront(self, valor):
        """
        Inserta un valor en la parte frontal del deque.
        """
        if valor in self:
            raise ValueError(f"Valor duplicado detectado: {valor}")
        nuevo_nodo = Nodo(valor)
        if self.frente is None:
            self.frente = nuevo_nodo
            self.rear = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.frente
            self.frente.anterior = nuevo_nodo
            self.frente = nuevo_nodo

    def insertRear(self, valor):
        """
        Inserta un valor en la parte trasera del deque.
        """
        if valor in self:
            raise ValueError(f"Valor duplicado detectado: {valor}")
        nuevo_nodo = Nodo(valor)
        if self.rear is None:
            self.frente = nuevo_nodo
            self.rear = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.rear
            self.rear.siguiente = nuevo_nodo
            self.rear = nuevo_nodo

    def removeLeft(self):
        """
        Elimina y devuelve el valor del nodo frontal del deque.
        """
        if self.frente is None:
            raise IndexError("Operación inválida: No se puede eliminar desde un deque vacío.")
        valor = self.frente.valor
        self.frente = self.frente.siguiente
        if self.frente is not None:
            self.frente.anterior = None
        else:
            self.rear = None
        return valor

    def removeRight(self):
        """
        Elimina y devuelve el valor del nodo trasero del deque.
        """
        if self.rear is None:
            raise IndexError("Operación inválida: No se puede eliminar desde un deque vacío.")
        valor = self.rear.valor
        self.rear = self.rear.anterior
        if self.rear is not None:
            self.rear.siguiente = None
        else:
            self.frente = None
        return valor

    def remove(self, valor):
        """
        Elimina un nodo con el valor especificado.
        """
        if self.frente is None:
            raise ValueError(f"Valor {valor} no encontrado en el deque.")
        if self.frente.valor == valor:
            return self.removeLeft()
        if self.rear.valor == valor:
            return self.removeRight()
        nodo_actual = self.frente.siguiente
        while nodo_actual is not None:
            if nodo_actual.valor == valor:
                if nodo_actual.anterior is not None:
                    nodo_actual.anterior.siguiente = nodo_actual.siguiente
                if nodo_actual.siguiente is not None:
                    nodo_actual.siguiente.anterior = nodo_actual.anterior
                return valor
            nodo_actual = nodo_actual.siguiente
        raise ValueError(f"Valor {valor} no encontrado en el deque.")

    def isEmpty(self):
        """
        Verifica si el deque está vacío.
        """
        return self.frente is None

    def peekFront(self):
        """
        Devuelve el valor del nodo frontal sin eliminarlo.
        """
        if self.frente is None:
            return None
        return self.frente.valor

    def peekRear(self):
        """
        Devuelve el valor del nodo trasero sin eliminarlo.
        """
        if self.rear is None:
            return None
        return self.rear.valor

    @staticmethod
    def merge_into(deque1, deque2):
        """
        Combina dos deques. El deque2 se vacía y se añade al final de deque1.
        """
        if deque2.isEmpty():
            return deque1
        if deque1.isEmpty():
            deque1.frente = deque2.frente
            deque1.rear = deque2.rear
        else:
            deque1.rear.siguiente = deque2.frente
            deque2.frente.anterior = deque1.rear
            deque1.rear = deque2.rear
        deque2.frente = None
        deque2.rear = None
        return deque1

    def size(self):
        """
        Devuelve el tamaño del deque.
        """
        count = 0
        current = self.frente
        while current:
            count += 1
            current = current.siguiente
        return count

    def __iter__(self):
        self._current = self.frente
        return self

    def __next__(self):
        if self._current is not None:
            valor = self._current.valor
            self._current = self._current.siguiente
            return valor
        raise StopIteration
