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

    def es_hoja(self):
        """Retorna True si el nodo es una hoja (no tiene hijos)."""
        return self._izquierda is None and self._derecha is None


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

    def cantidad(self):
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
    def es_hoja(self, dato):
        """Verifica si el nodo que contiene el dato especificado es una hoja.

        Args:
            dato: El valor del nodo a consultar.

        Returns:
            bool: True si el nodo existe y no tiene hijos, False en caso contrario.
        """
        nodo = self._buscar_nodo(dato, self._raiz)
        if nodo is not None:
            return nodo.es_hoja()
        return False

    def _buscar_nodo(self, dato, nodo):
        """Método auxiliar recursivo que retorna el objeto Nodo correspondiente al dato."""
        if nodo is None:
            return None
        if str(dato) == str(nodo.get_dato()):
            return nodo
        if self._es_comparable(dato, nodo.get_dato()):
            if dato < nodo.get_dato():
                return self._buscar_nodo(dato, nodo.get_izquierda())
            return self._buscar_nodo(dato, nodo.get_derecha())
        # Búsqueda general no ordenada (para árboles de expresión)
        izq = self._buscar_nodo(dato, nodo.get_izquierda())
        if izq is not None:
            return izq
        return self._buscar_nodo(dato, nodo.get_derecha())

    def _es_comparable(self, a, b):
        """Retorna True si dos elementos se pueden comparar por orden de magnitud (<, >)."""
        try:
            return (isinstance(a, (int, float)) and isinstance(b, (int, float))) or (type(a) == type(b))
        except TypeError:
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
    def _preordeniterativo(self,nodo,resultado):
        if nodo is not None:
            stack = [nodo]
            while stack:
                current = stack.pop()
                resultado.append(current.get_dato())
                if current.get_derecha() is not None:
                    stack.append(current.get_derecha())
                if current.get_izquierda() is not None:
                    stack.append(current.get_izquierda())
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
    def _postordeniterativo(self,nodo,resultado):
        if nodo is not None:
            stack = []
            last_visited = None
            current = nodo
            while stack or current:
                if current:
                    stack.append(current)
                    current = current.get_izquierda()
                else:
                    peek_node = stack[-1]
                    if peek_node.get_derecha() and last_visited != peek_node.get_derecha():
                        current = peek_node.get_derecha()
                    else:
                        resultado.append(peek_node.get_dato())
                        last_visited = stack.pop()
    def amplitud(self):
        """Recorrido por niveles (Amplitud/BFS) usando una lista como cola."""
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
    def infija(self):
        """Retorna e imprime la expresión en su forma infija (inorden)"""
        elementos = self.inorden()
        exp_str = " ".join(str(e) for e in elementos)
        print(f"Forma Infija: {exp_str}")
        return exp_str

    def postfija(self):
        """Retorna e imprime la expresión en su forma postfija (postorden)"""
        elementos = self.postorden()
        exp_str = " ".join(str(e) for e in elementos)
        print(f"Forma Postfija: {exp_str}")
        return exp_str
    def prefija(self):
        """Retorna e imprime la expresion en su forma prefija"""
        elementos = self.preorden()
        exp_str = " ".join(str(e) for e in elementos)
        print(f"Forma Prefija: {exp_str}")
        return exp_str
        
    # --- Árbol de Expresiones Matemáticas ---

    def _infija_a_postfija(self, expresion):
        """Convierte una expresión infija a una lista de tokens postfija (Shunting-Yard)."""
        precedencia = {'+': 1, '-': 1, '*': 2, '/': 2}
        salida, pila_op = [], []
        for token in expresion.split():
            if token in precedencia:
                while (pila_op and pila_op[-1] in precedencia and
                       precedencia[pila_op[-1]] >= precedencia[token]):
                    salida.append(pila_op.pop())
                pila_op.append(token)
            else:
                salida.append(token)
        return salida + pila_op[::-1]

    def _postfija_a_arbol(self, tokens):
        """Construye la estructura de árbol a partir de una lista de tokens en postfija."""
        operadores = {'+', '-', '*', '/'}
        pila = []
        for token in tokens:
            nodo = Nodo(token)
            if token in operadores:
                nodo.set_derecha(pila.pop())
                nodo.set_izquierda(pila.pop())
            pila.append(nodo)
        return pila[-1] if pila else None

    def _insertar_expresion(self, expresion):
        """Construye un árbol de expresión matemática a partir de una cadena infija."""
        tokens_postfija = self._infija_a_postfija(expresion)
        self._raiz = self._postfija_a_arbol(tokens_postfija)
        self._tamanio = len(expresion.split())

    def insertarexpresion(self, expresion):
        """Alias para insertar_expresion."""
        self._insertar_expresion(expresion)

    def result_expresion(self):
        """Evalúa la expresión matemática del árbol y muestra la resolución directamente."""
        if self.esta_vacio():
            print("El árbol está vacío.")
            return None

        resultado = self._evaluar_nodo(self._raiz)
        if isinstance(resultado, float) and resultado.is_integer():
            resultado = int(resultado)
        print(f"Resultado de la expresión: {resultado}")
        return resultado

    def _evaluar_nodo(self, nodo):
        """Método auxiliar recursivo para evaluar un nodo del 
        árbol de expresión."""
        if nodo is None:
            return 0
        if nodo.es_hoja():
            val_str = str(nodo.get_dato())
            if '.' in val_str:
                return float(val_str)
            return int(val_str)
        val_izq = self._evaluar_nodo(nodo.get_izquierda())
        val_der = self._evaluar_nodo(nodo.get_derecha())
        op = nodo.get_dato()

        if op == '+':
            return val_izq + val_der
        elif op == '-':
            return val_izq - val_der
        elif op == '*':
            return val_izq * val_der
        elif op == '/':
            return val_izq / val_der
        else:
            raise ValueError(f"Operador no soportado: {op}")

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
    print("--- Demostración Árbol Binario de Búsqueda ---")
    arbol = ArbolBinarioBusqueda()
    elementos = [100, 50, 25, 55, 150, 120, 160, 40]
    print(f"Elementos insertados: {elementos}")
    for el in elementos:
        arbol.insertar(el)

    print("¿Está vacío?:", arbol.esta_vacio())
    print("Número de nodos (cantidad):", arbol.cantidad())
    print("Mínimo:", arbol.minimo())
    print("Máximo:", arbol.maximo())
    print("Altura del árbol:", arbol.altura())
    print("Recorrido Inorden:    ", arbol.inorden())
    print("Recorrido Preorden:   ", arbol.preorden())
    print("Recorrido Postorden:  ", arbol.postorden())
    print("Recorrido en Amplitud:", arbol.amplitud())
    print("Elemento borrado:", arbol.borrar(40))
    print("Representación visual del árbol:")
    print("Es hoja?:", arbol.es_hoja(100))
    arbol.imprimir()

    print("\n" + "=" * 50)
    print("--- Demostración Árbol de Expresión Matemática ---")
    print("=" * 50)

    arbol_exp = ArbolBinarioBusqueda()
    expresion = "3 + 5 * 2"
    print(f"Expresión ingresada: '{expresion}'")

    arbol_exp.insertarexpresion(expresion)

    print("\nRepresentación visual del árbol de expresión:")
    arbol_exp.imprimir()

    print()
    arbol_exp.infija()
    arbol_exp.postfija()
    arbol_exp.prefija()
    arbol_exp.result_expresion()


if __name__ == "__main__":
    main()
