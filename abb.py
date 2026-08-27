"""Módulo que implementa un Árbol Binario de Búsqueda (ABB) en Python.

Incluye la estructura de datos para los nodos y el árbol,
soporte para inserción, búsqueda, getters, setters, recorridos,
tamaño, altura, mínimo, máximo e impresión del árbol.
"""


class Nodo:
    """Clase que representa un nodo en un Árbol Binario de Búsqueda."""

    def __init__(self, dato):
        """Inicializa un nodo con un dato y referencias a sus hijos.

        Args:
            dato: El valor almacenado en el nodo.
        """
        self._dato = dato
        self._izquierda = None
        self._derecha = None

    # --- Getters y Setters ---

    def get_dato(self):
        """Obtiene el valor del nodo."""
        return self._dato

    def set_dato(self, dato):
        """Establece el valor del nodo."""
        self._dato = dato

    def get_izquierda(self):
        """Obtiene el hijo izquierdo del nodo."""
        return self._izquierda

    def set_izquierda(self, izquierda):
        """Establece el hijo izquierdo del nodo."""
        self._izquierda = izquierda

    def get_derecha(self):
        """Obtiene el hijo derecho del nodo."""
        return self._derecha

    def set_derecha(self, derecha):
        """Establece el hijo derecho del nodo."""
        self._derecha = derecha


class ArbolBinarioBusqueda:
    """Clase que representa un Árbol Binario de Búsqueda (ABB)."""

    def __init__(self):
        """Inicializa un árbol binario de búsqueda vacío."""
        self._raiz = None
        self._tamanio = 0

    # --- Getter y Setter para la raíz ---

    def get_raiz(self):
        """Obtiene el nodo raíz del árbol."""
        return self._raiz

    def set_raiz(self, raiz):
        """Establece la raíz del árbol."""
        self._raiz = raiz

    # --- Métodos de Estado y Tamaño ---

    def esta_vacio(self):
        """Retorna True si el árbol no tiene nodos."""
        return self._raiz is None

    def __len__(self):
        """Retorna la cantidad total de nodos en el árbol."""
        return self._tamanio

    # --- Inserción y Búsqueda ---

    def insertar(self, dato):
        """Inserta un nuevo valor en el árbol.

        Args:
            dato: El valor a insertar.
        """
        if self._raiz is None:
            self._raiz = Nodo(dato)
            self._tamanio += 1
        else:
            self._insertar(dato, self._raiz)

    def _insertar(self, dato, nodo):
        """Método auxiliar recursivo para insertar un dato."""
        if dato == nodo.get_dato():
            # No se permiten duplicados
            return  
        if dato < nodo.get_dato():
            if nodo.get_izquierda() is None:
                nodo.set_izquierda(Nodo(dato))
                self._tamanio += 1
            else:
                self._insertar(dato, nodo.get_izquierda())
        else:
            if nodo.get_derecha() is None:
                nodo.set_derecha(Nodo(dato))
                self._tamanio += 1
            else:
                self._insertar(dato, nodo.get_derecha())

    def buscar(self, dato):
        """Busca si un valor existe dentro del árbol.

        Args:
            dato: El valor a buscar.

        Returns:
            bool: True si el valor existe, False en caso contrario.
        """
        if self._raiz is None:
            return False
        return self._buscar(dato, self._raiz)

    def _buscar(self, dato, nodo):
        """Método auxiliar recursivo para buscar un dato."""
        if dato == nodo.get_dato():
            return True
        if dato < nodo.get_dato() and nodo.get_izquierda() is not None:
            return self._buscar(dato, nodo.get_izquierda())
        if dato > nodo.get_dato() and nodo.get_derecha() is not None:
            return self._buscar(dato, nodo.get_derecha())
        return False

    # --- Mínimo, Máximo y Altura ---

    def minimo(self):
        """Retorna el valor mínimo del árbol.

        El mínimo siempre es el nodo más a la izquierda.
        """
        if self.esta_vacio():
            raise ValueError("El árbol está vacío")
        return self._minimo_nodo(self._raiz).get_dato()

    def _minimo_nodo(self, nodo):
        """Retorna el nodo con el valor mínimo del subárbol."""
        actual = nodo
        while actual.get_izquierda() is not None:
            actual = actual.get_izquierda()
        return actual

    def maximo(self):
        """Retorna el valor máximo del árbol.

        El máximo siempre es el nodo más a la derecha.
        """
        if self.esta_vacio():
            raise ValueError("El árbol está vacío")
        nodo = self._raiz
        while nodo.get_derecha() is not None:
            nodo = nodo.get_derecha()
        return nodo.get_dato()

    def altura(self):
        """Calcula la altura del árbol.

        La altura de un árbol vacío es -1, la de un árbol con solo raíz es 0.
        """
        return self._altura_rec(self._raiz)

    def _altura_rec(self, nodo):
        """Método auxiliar recursivo para calcular la altura del árbol."""
        if nodo is None:
            return -1
        return 1 + max(
            self._altura_rec(nodo.get_izquierda()),
            self._altura_rec(nodo.get_derecha()),
        )
    def borrar(self, dato):
        """Borra un elemento del árbol binario de búsqueda."""
        self._raiz = self._borrar_rec(self._raiz, dato)
        return dato

    def _borrar_rec(self, nodo, dato):
        """Método auxiliar recursivo para borrar un elemento."""
        if nodo is None:
            return None

        if dato < nodo.get_dato():
            nodo.set_izquierda(self._borrar_rec(nodo.get_izquierda(), dato))
        elif dato > nodo.get_dato():
            nodo.set_derecha(self._borrar_rec(nodo.get_derecha(), dato))
        else:
            # Nodo a borrar encontrado
            if nodo.get_izquierda() is None:
                return nodo.get_derecha()
            if nodo.get_derecha() is None:
                return nodo.get_izquierda()

            # Nodo con dos hijos
            sucesor = self._minimo_nodo(nodo.get_derecha())
            nodo.set_dato(sucesor.get_dato())
            nodo.set_derecha(self._borrar_rec(nodo.get_derecha(), sucesor.get_dato()))

        return nodo
    
    # --- Recorridos del Árbol ---

    def inorden(self):
        """Realiza el recorrido inorden (Izquierda -> Raíz -> Derecha).

        Returns:
            list: Lista con los elementos recorridos en orden.
        """
        resultado = []
        self._inorden(self._raiz, resultado)
        return resultado

    def _inorden(self, nodo, resultado):
        """Método auxiliar recursivo para el recorrido inorden."""
        if nodo is not None:
            self._inorden(nodo.get_izquierda(), resultado)
            resultado.append(nodo.get_dato())
            self._inorden(nodo.get_derecha(), resultado)
    def _inordeniterativo(self,nodo,resultado):
        """Método iterativo auxiliar para el recorrido inorden."""
        if nodo is not None:
            stack = []
            current = nodo
            while stack or current:
                if current:
                    stack.append(current)
                    current = current.get_izquierda()
                else:
                    current = stack.pop()
                    resultado.append(current.get_dato())
                    current = current.get_derecha()
    def preorden(self):
        """Realiza el recorrido preorden (Raíz -> Izquierda -> Derecha).

        Returns:
            list: Lista con los elementos recorridos en preorden.
        """
        resultado = []
        self._preorden(self._raiz, resultado)
        return resultado

    def _preorden(self, nodo, resultado):
        """Método auxiliar recursivo para el recorrido preorden."""
        if nodo is not None:
            resultado.append(nodo.get_dato())
            self._preorden(nodo.get_izquierda(), resultado)
            self._preorden(nodo.get_derecha(), resultado)

    def postorden(self):
        """Realiza el recorrido postorden (Izquierda -> Derecha -> Raíz).

        Returns:
            list: Lista con los elementos recorridos en postorden.
        """
        resultado = []
        self._postorden(self._raiz, resultado)
        return resultado

    def _postorden(self, nodo, resultado):
        """Método auxiliar recursivo para el recorrido postorden."""
        if nodo is not None:
            self._postorden(nodo.get_izquierda(), resultado)
            self._postorden(nodo.get_derecha(), resultado)
            resultado.append(nodo.get_dato())

    def por_niveles(self):
        """Recorrido por niveles (BFS) usando una lista como cola."""
        if self.esta_vacio():
            return []

        resultado = []
        cola = [self._raiz]

        while cola:
            nodo = cola.pop(0)
            resultado.append(nodo.get_dato())
            if nodo.get_izquierda() is not None:
                cola.append(nodo.get_izquierda())
            if nodo.get_derecha() is not None:
                cola.append(nodo.get_derecha())

        return resultado

    # --- Visualización ---

    def imprimir(self):
        """Imprime el árbol en formato visual (rotado 90°)."""
        self._imprimir_rec(self._raiz, 0)

    def _imprimir_rec(self, nodo, nivel):
        """Método auxiliar recursivo para imprimir el árbol visualmente."""
        if nodo is not None:
            self._imprimir_rec(nodo.get_derecha(), nivel + 1)
            print("    " * nivel + f"[{nodo.get_dato()}]")
            self._imprimir_rec(nodo.get_izquierda(), nivel + 1)


def main():
    """Función principal de demostración."""
    arbol = ArbolBinarioBusqueda()
    elementos = [100,50,25,55,150,120,160]

    for el in elementos:
        arbol.insertar(el)

    print("--- Demostración Árbol Binario de Búsqueda ---")
    print("¿Está vacío?:", arbol.esta_vacio())
    print("Número de nodos (len):", len(arbol))
    print("Mínimo:", arbol.minimo())
    print("Máximo:", arbol.maximo())
    print("Altura del árbol:", arbol.altura())
    print("Recorrido Inorden:    ", arbol.inorden())
    print("Recorrido Preorden:   ", arbol.preorden())
    print("Recorrido Postorden:  ", arbol.postorden())
    print("Recorrido Por Niveles:", arbol.por_niveles())
    print("elemento borrado", arbol.borrar(40))
    print("Representación visual del árbol:")
    arbol.imprimir()


if __name__ == "__main__":
    main()



