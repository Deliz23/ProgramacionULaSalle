class Node:
    def __init__(self, valor):
        self.valor = valor
        self.next = None
# Se inicializa el nodo con un valor
class Pila:  # la clase representa la estructura de la pila
    def __init__(self):
        self.last = None

    def push(self, valor): # metodo push para poder agregar un valor a la pila
        nodo = Node(valor)
        if self.last is not None:
            nodo.next = self.last
        self.last = nodo

    def pop(self): #  # Metodo para eliminarel valor del ultimo nodo de la pila
        if self.last is not None:
            ultimo = self.last.valor
            self.last = self.last.next
            return ultimo
        return None

    def show(self): # Metodo para mostrar todos los valores de la pila
        actual = self.last
        while(actual):
            print(actual.valor) # imprime el valor del nodo actual
            actual = actual.next # avanza al siguiente nodo 
    #Ejemplo de la pila
pila = Pila()
numeros =[1,2,4,5,7,5,10]

for n in numeros:
    pila.push(n)

    print("El contenido de la pila final es: ")
    pila.show() 