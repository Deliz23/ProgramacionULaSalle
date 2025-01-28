class Node:
    def __init__(self, valor):
        self.valor = valor
        self.next = None

class ListaEnlazada: # Clase que representa una lista 
    def __init__(self):   # se inicializa la lista con el head
        self.head = None

    def insertar(self, valor): # # metodo para insertar un valor al final de la lista
        nodo = Node(valor)
        if self.head is None:
            self.head = nodo
        else:
            actual = self.head
            while actual.next:
                actual = actual.next
            actual.next = nodo

    def eliminar(self, valor):  # metodo para eliminar un valor especifico de la lista
        actual = self.head
        previo = None
        while actual and actual.valor != valor:
            previo = actual
            actual = actual.next
        if actual is None:
            return
        if previo is None:
            self.head = actual.next
        else:
            previo.next = actual.next

    def mostrar(self):  # metodo para mostrar los elementos de la lista
        actual = self.head
        while actual:
            print(actual.valor, end=" -> ")
            actual = actual.next
        print("None")

lista = ListaEnlazada()
for n in [10, 8, 3, 12, 45]:
    lista.insertar(n)

print("Lista enlazada:")
lista.mostrar()
lista.eliminar(3)
print("Despues de eliminar 3:")
lista.mostrar()