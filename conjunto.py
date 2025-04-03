import random

class Conjunto:
    def __init__(self):
        self.__elements = []

    def add(self, element):
        if isinstance(element, (list, dict)):
            raise TypeError(f"unhashable type: {type(element)}")
        if element not in self.__elements:
            self.__elements.append(element)

    def remove(self, element):
        if element not in self.__elements:
            raise KeyError(f"not found: {element}")
        self.__elements.remove(element)

    def discard(self, element):
        if element in self.__elements:
            self.__elements.remove(element)

    def pop(self):
        if not self.__elements:
            raise IndexError("pop from empty set")
        return self.__elements.pop(random.randint(0, len(self.__elements) - 1))

    def clear(self):
        self.__elements = []

    def union(self, s2):
        new_set = Conjunto()
        for element in self.__elements:
            new_set.add(element)
        for element in s2._Conjunto__elements:
            new_set.add(element)
        return new_set

    def intersection(self, s2):
        new_set = Conjunto()
        for element in self.__elements:
            if element in s2:
                new_set.add(element)
        return new_set

    def difference(self, s2):
        new_set = Conjunto()
        for element in self.__elements:
            if element not in s2:
                new_set.add(element)
        return new_set

    def symmetric_difference(self, s2):  
        new_set = Conjunto()
        for element in self.__elements:
            if element not in s2:
                new_set.add(element)
        for element in s2:
            if element not in self.__elements:
                new_set.add(element)
        return new_set

    def __or__(self, s2):
        return self.union(s2)

    def __and__(self, s2):
        return self.intersection(s2)

    def __xor__(self, s2):
        return self.symmetric_difference(s2) 

    def __iter__(self):
        return iter(self.__elements)

    def __contains__(self, element):
        return element in self.__elements

    def __repr__(self):
        output = f"{self.__elements}"
        return output.replace("[", "{").replace("]", "}")


if __name__ == "__main__":
    s1 = Conjunto()

    s1.add(1)
    s1.add(2)
    s1.add(3)
    s1.add(4)
    print("Conjunto s1:", s1)

    s2 = Conjunto()
    for i in range(5):
        s2.add(random.randint(1, 9))

    print("Conjunto s2:", s2)

    print(
        "Unión:", s1.union(s2),
        "\nIntersección:", s1.intersection(s2),
        "\nDiferencia:", s1.difference(s2),
        "\nDiferencia simétrica:", s1.symmetric_difference(s2)
    )

    print(
        "Operadores: | (unión), & (intersección), ^ (diferencia simétrica):",
        s1 | s2, s1 & s2, s1 ^ s2
    )
