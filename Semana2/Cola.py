class Nodo:
    def __init__(self, valor): # se inicializa el nodo con un valor
        self.valor = valor
        self.siguiente = None

class Cola: # esta clase  representa la estructura de una cola
    def __init__(self):
        self.frente = None
        self.final = None
        self._tamanio = 0  # Contador de elementos en la cola

    def esta_vacia(self):  # metodo para verificar si la cola esta vacia
        return self.frente is None

    def encolar(self, valor):  # metodo para agregar un valor a la cola
        nodo = Nodo(valor)
        if self.esta_vacia():
            self.frente = self.final = nodo
        else:
            self.final.siguiente = nodo
            self.final = nodo
        self._tamanio += 1  # aumenta el contador de elementos

    def eliminar(self): # metodo para eliminar un elemento de la cola 
        if self.esta_vacia():
            print("La cola esta vacia, no se puede eliminar.")
            return None
        valor = self.frente.valor
        self.frente = self.frente.siguiente
        if self.frente is None:
            self.final = None
        self._tamanio -= 1  # disminuye el contador de elementos
        return valor

    def mostrar(self):
        if self.esta_vacia():
            print("La cola esta vacia.")
            return
        actual = self.frente
        print("Frente -> ", end="")
        while actual:
            print(actual.valor, end=" ")
            if actual.siguiente:
                print("->", end=" ")
            actual = actual.siguiente
        print(" <- Final")

    def tamaño(self):
        return self._tamanio


cola = Cola()
for n in [1, 2, 3, 4, 5]:
    cola.encolar(n)

print("Cola inicial:")
cola.mostrar()
print("Tamanio de la cola:", cola.tamaño())

print("\nEliminando un elemento...")
cola.eliminar()
cola.mostrar()
print("Tamanio de la cola:", cola.tamaño())

print("Vaciando la cola:")
while not cola.esta_vacia():
    cola.eliminar()
    cola.mostrar()

print("La cola esta vacia?", cola.esta_vacia())