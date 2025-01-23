class Nodo:
    def __init__(self, valor):
        self.izq = None
        self.der = None
        self.valor = valor

class ArbolBinario: # el arbol comienza estando vacio
    def __init__(self):
        self.root = None

    def insertar(self, valor):  # metodo para insertar un valor en el arbol
        if self.root is None:
            self.root = Nodo(valor)
        else:
            self._insertar_recursivo(self.root, valor)

    def _insertar_recursivo(self, nodo, valor): # Funcion recursiva para insertar el valor
        if valor < nodo.valor:
            if nodo.izq is None:
                nodo.izq = Nodo(valor)
                print(f"Valor {valor} insertado a la izquierda de {nodo.valor}")
            else:
                self._insertar_recursivo(nodo.izq, valor)
        elif valor > nodo.valor:
            if nodo.der is None:
                nodo.der = Nodo(valor)
                print(f"Valor {valor} insertado a la derecha de {nodo.valor}")
            else:
                self._insertar_recursivo(nodo.der, valor)
        else:
            print(f"El valor {valor} ya existe en el arbol.")

    def eliminar(self, valor):  # Metodo para eliminar un nodo
        print(f"Eliminando el valor {valor}...")
        self.root = self._eliminar_recursivo(self.root, valor)

    def _eliminar_recursivo(self, nodo, valor):   # Funcion recursiva para eliminar un nodo
        if nodo is None:
            return nodo
        
        if valor < nodo.valor:
            nodo.izq = self._eliminar_recursivo(nodo.izq, valor)
        elif valor > nodo.valor:
            nodo.der = self._eliminar_recursivo(nodo.der, valor)
        else:
            if nodo.izq is None:
                return nodo.der
            elif nodo.der is None:
                return nodo.izq
            temp = self._minimo(nodo.der)
            nodo.valor = temp.valor
            nodo.der = self._eliminar_recursivo(nodo.der, temp.valor)

        return nodo

    def _minimo(self, nodo):
        actual = nodo
        while actual.izq is not None:
            actual = actual.izq
        return actual

    def inorden(self):   # Recorrido inorden 
        print("Recorrido Inorden (izquierda, raiz, derecha):")
        self._inorden(self.root)

    def _inorden(self, raiz):
        if raiz is not None:
            self._inorden(raiz.izq)
            print(raiz.valor, end=" ")
            self._inorden(raiz.der)

    def preorden(self): # Recorrido preorden 
        print("Recorrido Preorden (raiz, izquierda, derecha):")
        self._preorden(self.root)

    def _preorden(self, raiz):
        if raiz is not None:
            print(raiz.valor, end=" ")
            self._preorden(raiz.izq)
            self._preorden(raiz.der)

    def postorden(self):  #REcorrido postorden
        print("Recorrido Postorden (izquierda, derecha, raiz):")
        self._postorden(self.root)

    def _postorden(self, raiz):
        if raiz is not None:
            self._postorden(raiz.izq)
            self._postorden(raiz.der)
            print(raiz.valor, end=" ")

    def mostrar_arbol(self):  # Mostrar el arbol de manera visual
        print("Visualizacion del arbol:")
        if self.root is not None:
            self._mostrar_arbol(self.root, 0)
        else:
            print("El arbol esta vacio.")

    def _mostrar_arbol(self, nodo, nivel):
        if nodo is not None:
            self._mostrar_arbol(nodo.der, nivel + 1)
            print("    " * nivel + f"->{nodo.valor}")
            self._mostrar_arbol(nodo.izq, nivel + 1)

# Ejemplo de uso
lista = [32, 45, 2, 6, 3, 864, 23, 24, 12]
arbol = ArbolBinario()

# Insertando elementos
for i in lista:
    arbol.insertar(i)

# Mostramos el árbol
arbol.mostrar_arbol()

arbol.inorden()
print("\n")
arbol.preorden()
print("\n")
arbol.postorden()
print("\n")

# Eliminamos un nodo
arbol.eliminar(45)
arbol.mostrar_arbol()