"""Módulo que implementa un Árbol AVL (Adelson-Velsky y Landis) en Python.

Incluye la estructura de datos para nodos balanceados y el árbol AVL,
soporte para inserción y borrado con auto-balanceo (rotaciones LL, RR, LR, RL),
búsqueda, getters, setters, recorridos (inorden, preorden, postorden, amplitud/niveles),
tamaño, altura, mínimo, máximo, árbol de expresiones matemáticas
y resolución de expresiones paso a paso en consola.
"""


class Nodo:
    """Clase que representa un nodo en un Árbol AVL."""

    def __init__(self, dato):
        """Inicializa un nodo con un dato, referencias a sus hijos y altura 1.

        Args:
            dato: El valor almacenado en el nodo.
        """
        self._dato = dato
        self._izquierda = None
        self._derecha = None
        self._altura = 1

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

    def get_altura(self):
        """Obtiene la altura del nodo."""
        return self._altura

    def set_altura(self, altura):
        """Establece la altura del nodo."""
        self._altura = altura

    def es_hoja(self):
        """Retorna True si el nodo es una hoja (no tiene hijos)."""
        return self._izquierda is None and self._derecha is None


class ArbolAVL:
    """Clase que representa un Árbol AVL (auto-balanceado)."""

    def __init__(self):
        """Inicializa un árbol AVL vacío."""
        self._raiz = None
        self._tamanio = 0

    # --- Getter y Setter para la raíz ---

    def get_raiz(self):
        """Obtiene el nodo raíz del árbol."""
        return self._raiz

    def set_raiz(self, raiz):
        """Establece la raíz del árbol."""
        self._raiz = raiz

    # --- Métodos de Estado, Tamaño y Altura AVL ---

    def esta_vacio(self):
        """Retorna True si el árbol no tiene nodos."""
        return self._raiz is None

    def cantidad(self):
        """Retorna la cantidad total de nodos en el árbol."""
        return self._tamanio

    def __len__(self):
        """Retorna la cantidad total de nodos en el árbol."""
        return self._tamanio

    def _obtener_altura(self, nodo):
        """Retorna la altura de un nodo (0 si es None)."""
        if nodo is None:
            return 0
        return nodo.get_altura()

    def _obtener_balance(self, nodo):
        """Calcula el factor de balance de un nodo (altura izq - altura der)."""
        if nodo is None:
            return 0
        return self._obtener_altura(nodo.get_izquierda()) - self._obtener_altura(nodo.get_derecha())

    def _actualizar_altura(self, nodo):
        """Actualiza la altura de un nodo basado en las alturas de sus hijos."""
        if nodo is not None:
            nodo.set_altura(1 + max(self._obtener_altura(nodo.get_izquierda()), self._obtener_altura(nodo.get_derecha())))

    def altura(self):
        """Calcula la altura del árbol (altura de la raíz - 1, o -1 si está vacío)."""
        if self.esta_vacio():
            return -1
        return self._obtener_altura(self._raiz) - 1

    # --- Rotaciones AVL ---

    def _rotacion_derecha(self, y):
        """Realiza una rotación simple a la derecha (caso Izquierda-Izquierda / LL)."""
        x = y.get_izquierda()
        t2 = x.get_derecha()

        # Realizar rotación
        x.set_derecha(y)
        y.set_izquierda(t2)

        # Actualizar alturas
        self._actualizar_altura(y)
        self._actualizar_altura(x)

        return x

    def _rotacion_izquierda(self, x):
        """Realiza una rotación simple a la izquierda (caso Derecha-Derecha / RR)."""
        y = x.get_derecha()
        t2 = y.get_izquierda()

        # Realizar rotación
        y.set_izquierda(x)
        x.set_derecha(t2)

        # Actualizar alturas
        self._actualizar_altura(x)
        self._actualizar_altura(y)

        return y

    def _rebalancear(self, nodo):
        """Rebalancea el subárbol dado y retorna la nueva raíz del subárbol."""
        if nodo is None:
            return None

        # 1. Actualizar altura de este nodo
        self._actualizar_altura(nodo)

        # 2. Obtener el factor de balance
        balance = self._obtener_balance(nodo)

        # 3. Caso Izquierda Izquierda (LL)
        if balance > 1 and self._obtener_balance(nodo.get_izquierda()) >= 0:
            return self._rotacion_derecha(nodo)

        # 4. Caso Izquierda Derecha (LR)
        if balance > 1 and self._obtener_balance(nodo.get_izquierda()) < 0:
            nodo.set_izquierda(self._rotacion_izquierda(nodo.get_izquierda()))
            return self._rotacion_derecha(nodo)

        # 5. Caso Derecha Derecha (RR)
        if balance < -1 and self._obtener_balance(nodo.get_derecha()) <= 0:
            return self._rotacion_izquierda(nodo)

        # 6. Caso Derecha Izquierda (RL)
        if balance < -1 and self._obtener_balance(nodo.get_derecha()) > 0:
            nodo.set_derecha(self._rotacion_derecha(nodo.get_derecha()))
            return self._rotacion_izquierda(nodo)

        return nodo

    # --- Inserción y Búsqueda ---

    def insertar(self, dato):
        """Inserta un nuevo valor en el árbol AVL manteniendo el balanceo.

        Args:
            dato: El valor a insertar.
        """
        self._raiz = self._insertar_rec(self._raiz, dato)

    def _insertar_rec(self, nodo, dato):
        """Método auxiliar recursivo para insertar un dato con rebalanceo AVL."""
        if nodo is None:
            self._tamanio += 1
            return Nodo(dato)

        if dato == nodo.get_dato():
            # No se permiten duplicados
            return nodo

        if dato < nodo.get_dato():
            nodo.set_izquierda(self._insertar_rec(nodo.get_izquierda(), dato))
        else:
            nodo.set_derecha(self._insertar_rec(nodo.get_derecha(), dato))

        return self._rebalancear(nodo)

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

    # --- Mínimo y Máximo ---

    def minimo(self):
        """Retorna el valor mínimo del árbol."""
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
        """Retorna el valor máximo del árbol."""
        if self.esta_vacio():
            raise ValueError("El árbol está vacío")
        nodo = self._raiz
        while nodo.get_derecha() is not None:
            nodo = nodo.get_derecha()
        return nodo.get_dato()

    # --- Borrado ---

    def borrar(self, dato):
        """Borra un elemento del árbol AVL manteniendo el balanceo.

        Args:
            dato: El elemento a borrar.

        Returns:
            El dato borrado o None si no se encontró.
        """
        if not self.buscar(dato):
            return None
        self._raiz = self._borrar_rec(self._raiz, dato)
        self._tamanio -= 1
        return dato

    def _borrar_rec(self, nodo, dato):
        """Método auxiliar recursivo para borrar un elemento con rebalanceo AVL."""
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
            elif nodo.get_derecha() is None:
                return nodo.get_izquierda()

            # Nodo con dos hijos: sucesor en inorden
            sucesor = self._minimo_nodo(nodo.get_derecha())
            nodo.set_dato(sucesor.get_dato())
            nodo.set_derecha(self._borrar_rec(nodo.get_derecha(), sucesor.get_dato()))

        return self._rebalancear(nodo)

    # --- Recorridos del Árbol ---

    def inorden(self):
        """Realiza el recorrido inorden (Izquierda -> Raíz -> Derecha)."""
        resultado = []
        self._inorden(self._raiz, resultado)
        return resultado

    def _inorden(self, nodo, resultado):
        """Método auxiliar recursivo para el recorrido inorden."""
        if nodo is not None:
            self._inorden(nodo.get_izquierda(), resultado)
            resultado.append(nodo.get_dato())
            self._inorden(nodo.get_derecha(), resultado)

    def preorden(self):
        """Realiza el recorrido preorden (Raíz -> Izquierda -> Derecha)."""
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
        """Realiza el recorrido postorden (Izquierda -> Derecha -> Raíz)."""
        resultado = []
        self._postorden(self._raiz, resultado)
        return resultado

    def _postorden(self, nodo, resultado):
        """Método auxiliar recursivo para el recorrido postorden."""
        if nodo is not None:
            self._postorden(nodo.get_izquierda(), resultado)
            self._postorden(nodo.get_derecha(), resultado)
            resultado.append(nodo.get_dato())

    def amplitud(self):
        """Recorrido por niveles (Amplitud / BFS)."""
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

    def por_niveles(self):
        """Alias de recorrido por niveles/amplitud."""
        return self.amplitud()

    def infija(self):
        """Retorna e imprime la expresión en su forma infija (inorden)."""
        elementos = self.inorden()
        exp_str = " ".join(str(e) for e in elementos)
        print(f"Forma Infija: {exp_str}")
        return exp_str

    def postfija(self):
        """Retorna e imprime la expresión en su forma postfija (postorden)."""
        elementos = self.postorden()
        exp_str = " ".join(str(e) for e in elementos)
        print(f"Forma Postfija: {exp_str}")
        return exp_str

    def prefija(self):
        """Retorna e imprime la expresión en su forma prefija (preorden)."""
        elementos = self.preorden()
        exp_str = " ".join(str(e) for e in elementos)
        print(f"Forma Prefija: {exp_str}")
        return exp_str

    # --- Árbol de Expresiones Matemáticas ---

    def _infija_a_postfija(self, expresion):
        """Convierte una expresión infija a una lista de tokens postfija (Shunting-Yard)."""
        precedencia = {'+': 1, '-': 1, '*': 2, '/': 2}
        salida, pila_op = [], []
        exp_formateada = expresion.replace('(', ' ( ').replace(')', ' ) ')
        tokens = exp_formateada.split()

        for token in tokens:
            if token == '(':
                pila_op.append(token)
            elif token == ')':
                while pila_op and pila_op[-1] != '(':
                    salida.append(pila_op.pop())
                if pila_op:
                    pila_op.pop()  # Eliminar '('
            elif token in precedencia:
                while (pila_op and pila_op[-1] in precedencia and
                       precedencia[pila_op[-1]] >= precedencia[token]):
                    salida.append(pila_op.pop())
                pila_op.append(token)
            else:
                salida.append(token)

        while pila_op:
            salida.append(pila_op.pop())

        return salida

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

    def insertarexpresion(self, expresion):
        """Construye un árbol de expresión matemática a partir de una cadena infija."""
        tokens_postfija = self._infija_a_postfija(expresion)
        self._raiz = self._postfija_a_arbol(tokens_postfija)
        self._tamanio = len(tokens_postfija)

    def result_expresion(self):
        """Evalúa la expresión matemática mostrando la resolución paso a paso en consola."""
        if self.esta_vacio():
            print("El árbol está vacío.")
            return None

        print("\n--- Resolución Paso a Paso de la Expresión ---")
        pasos = []
        resultado = self._evaluar_nodo_paso_a_paso(self._raiz, pasos)

        if isinstance(resultado, float) and resultado.is_integer():
            resultado = int(resultado)

        for i, paso in enumerate(pasos, 1):
            print(f"Paso {i}: {paso}")

        print(f"=> Resultado final: {resultado}")
        return resultado

    def _evaluar_nodo_paso_a_paso(self, nodo, pasos):
        """Método auxiliar recursivo para evaluar los nodos registrando cada paso."""
        if nodo is None:
            return 0

        if nodo.es_hoja():
            val_str = str(nodo.get_dato())
            if '.' in val_str:
                return float(val_str)
            return int(val_str)

        val_izq = self._evaluar_nodo_paso_a_paso(nodo.get_izquierda(), pasos)
        val_der = self._evaluar_nodo_paso_a_paso(nodo.get_derecha(), pasos)
        op = nodo.get_dato()

        res = 0
        if op == '+':
            res = val_izq + val_der
        elif op == '-':
            res = val_izq - val_der
        elif op == '*':
            res = val_izq * val_der
        elif op == '/':
            res = val_izq / val_der
        else:
            raise ValueError(f"Operador no soportado: {op}")

        if isinstance(res, float) and res.is_integer():
            res = int(res)

        if isinstance(val_izq, float) and val_izq.is_integer():
            val_izq = int(val_izq)

        if isinstance(val_der, float) and val_der.is_integer():
            val_der = int(val_der)

        pasos.append(f"{val_izq} {op} {val_der} = {res}")
        return res

    # --- Visualización ---

    def imprimir(self):
        """Imprime el árbol en formato visual (rotado 90°) mostrando el factor de balance."""
        self._imprimir_rec(self._raiz, 0)

    def _imprimir_rec(self, nodo, nivel):
        """Método auxiliar recursivo para imprimir el árbol visualmente."""
        if nodo is not None:
            self._imprimir_rec(nodo.get_derecha(), nivel + 1)
            fb = self._obtener_balance(nodo)
            alt = self._obtener_altura(nodo)
            print("    " * nivel + f"[{nodo.get_dato()}] (h:{alt}, fb:{fb})")
            self._imprimir_rec(nodo.get_izquierda(), nivel + 1)


# Alias para mantener compatibilidad con ArbolBinarioBusqueda
ArbolBinarioBusqueda = ArbolAVL


def main():
    """Función principal de demostración."""
    print("==================================================")
    print("--- Demostración Árbol AVL (Auto-balanceado) ---")
    print("==================================================")
    arbol = ArbolAVL()
    elementos = [100, 50, 25, 55, 150, 120, 160, 40]
    print(f"Elementos a insertar secuencialmente: {elementos}")

    for el in elementos:
        print(f"\n-> Insertando {el}...")
        arbol.insertar(el)

    print("\nEstado final del árbol AVL:")
    print("¿Está vacío?:", arbol.esta_vacio())
    print("Número de nodos (cantidad):", arbol.cantidad())
    print("Mínimo:", arbol.minimo())
    print("Máximo:", arbol.maximo())
    print("Altura del árbol:", arbol.altura())
    print("Recorrido Inorden:    ", arbol.inorden())
    print("Recorrido Preorden:   ", arbol.preorden())
    print("Recorrido Postorden:  ", arbol.postorden())
    print("Recorrido en Amplitud:", arbol.amplitud())

    print("\nRepresentación visual del árbol (rotado 90° con altura y factor de balance):")
    arbol.imprimir()

    borrado = 40
    print(f"\nBorrando elemento {borrado}:", arbol.borrar(borrado))
    print("Representación visual del árbol tras borrar:")
    arbol.imprimir()

    print("\n" + "=" * 50)
    print("--- Demostración Árbol de Expresión Matemática ---")
    print("=" * 50)

    arbol_exp = ArbolAVL()
    expresion = "3 + 5 * ( 2 + 8 )"
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