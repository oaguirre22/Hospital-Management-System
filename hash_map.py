class HashMap:
    def __init__(self, elements=[], capacity=10):
        self.__size = 0
        if not elements:
            self.__capacity = capacity
            self.__buckets = [[] for _ in range(self.__capacity)]
        else:
            self.__capacity = len(elements) * 2
            self.__buckets = [[] for _ in range(self.__capacity)]
            for k, v in elements:
                self.put(k, v)

    def put(self, key, value):
        if not key or not isinstance(key, str):
            raise ValueError("La clave debe ser una cadena no vacía.")
        if value is None:
            raise ValueError("El valor no puede ser nulo.")
        bucket_index = self._hash(key)
        bucket = self.__buckets[bucket_index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                print(f"[ALERTA] Clave duplicada '{key}', actualizando el valor existente.")
                bucket[i] = (key, value)
                return
        bucket.append((key, value))
        self.__size += 1
        if self.__size / self.__capacity > 0.7:
            self.__resize()

    def get(self, key):
        """
        Busca un valor por su clave en el HashMap.
        Lanza un error si la clave no existe.
        """
        if not key or not isinstance(key, str):
            raise ValueError("Clave inválida: La clave debe ser una cadena no vacía.")
        value = self.__get(key)
        if value is None:
            raise KeyError(f"Clave '{key}' no encontrada en el HashMap.")
        return value

    def __get(self, key):
        bucket_index = self._hash(key)
        bucket = self.__buckets[bucket_index]
        for k, v in bucket:
            if k == key:
                return v
        return None

    def keys(self):
        keys = []
        for bucket in self.__buckets:
            for k, v in bucket:
                keys.append(k)
        return keys

    def values(self):
        values = []
        for bucket in self.__buckets:
            for k, v in bucket:
                values.append(v)
        return values

    def items(self):
        items = []
        for bucket in self.__buckets:
            for k, v in bucket:
                items.append((k, v))
        return items

    def remove(self, key):
        """
        Elimina un valor por su clave del HashMap.
        Proporciona mensajes claros en caso de error.
        """
        if not key or not isinstance(key, str):
            raise ValueError("La clave debe ser una cadena válida.")
        bucket_index = self._hash(key)
        bucket = self.__buckets[bucket_index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self.__size -= 1
                return
        raise KeyError(f"Clave '{key}' no encontrada para eliminar.")

    def _hash(self, key, base=None):
        if not base:
            base = self.__capacity
        return hash(key) % base

    def __resize(self):
        new_capacity = self.__capacity * 2
        new_buckets = [[] for _ in range(new_capacity)]
        for bucket in self.__buckets:
            for k, v in bucket:
                new_bucket_index = self._hash(k, new_capacity)
                new_buckets[new_bucket_index].append((k, v))
        self.__capacity = new_capacity
        self.__buckets = new_buckets

    def __len__(self):
        return self.__size

    def clear(self):
        self.__capacity = 10
        self.__size = 0
        self.__buckets = [[] for _ in range(self.__capacity)]

    def __repr__(self):
        elements = [
            f"{k}: {v}" if not isinstance(v, str) else f"{k}: '{v}'"
            for bucket in self.__buckets for k, v in bucket
        ]
        return "{" + ", ".join(elements) + "}"

    def _contains__(self, key):
        return True if self.__get(key) else False

    def __iter__(self):
        for bucket in self.__buckets:
            for k, v in bucket:
                yield k, v
