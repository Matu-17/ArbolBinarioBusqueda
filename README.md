# Árbol Binario de Búsqueda (ABB) y Árbol de Expresiones Matemáticas

Este proyecto implementa en **Python** una estructura de datos de **Árbol Binario de Búsqueda (ABB)** y un **Árbol de Expresiones Matemáticas**, siguiendo los principios de la Programación Orientada a Objetos (POO) y el estándar de codificación **PEP 8**.

---

## 📌 Descripción del Proyecto

El proyecto se divide en dos capacidades principales:

1. **Árbol Binario de Búsqueda (ABB)**: Permite almacenar, buscar, borrar y recorrer elementos ordenados.
2. **Árbol de Expresiones Matemáticas**: Permite parsear cadenas de operaciones matemáticas infijas (por ejemplo `"3 + 5 * 2"`), representarlas visualmente como un árbol binario de expresión, obtener sus notaciones **Infija**, **Postfija** y **Prefija**, y calcular el resultado de la operación.

---

## ⚙️ ¿Cómo funciona el Árbol de Expresiones?

El procesamiento de una expresión matemática se realiza en los siguientes pasos:

1. **Conversión Infija a Postfija (Algoritmo Shunting-Yard)**:
   - Una expresión como `"3 + 5 * 2"` se pasa a notación postfija / Notación Polaca Inversa (`"3 5 2 * +"`).
   - Esto garantiza que se respete la jerarquía de operadores (`*` y `/` tienen mayor prioridad que `+` y `-`) sin necesidad de paréntesis.

2. **Construcción del Árbol (`_postfija_a_arbol`)**:
   - Se utiliza una **pila (stack)** de nodos.
   - Los números (operandos) se almacenan como **nodos hoja** (sin hijos).
   - Los operadores (`+`, `-`, `*`, `/`) se almacenan como **nodos internos** cuyos hijos izquierdo y derecho son los operandos o subárboles correspondientes.

3. **Recorridos de la Expresión**:
   - **Infija (Inorden)**: Recorre `Izquierda ➔ Raíz ➔ Derecha` para reconstruir la expresión matemática en su forma infija habitual.
   - **Postfija (Postorden)**: Recorre `Izquierda ➔ Derecha ➔ Raíz` para obtener la representación postfija.
   - **Prefija (Preorden)**: Recorre `Raíz ➔ Izquierda ➔ Derecha` para obtener la representación prefija (Notación Polaca).

4. **Evaluación de la Expresión (`result_expresion`)**:
   - Evalúa el árbol recursivamente desde las hojas hacia la raíz realizando las operaciones aritméticas correspondientes.

---

## 🚀 Funcionalidades Principales

### Clase `Nodo`
- `get_dato()`, `set_dato()`: Obtiene o modifica el valor del nodo.
- `get_izquierda()`, `set_izquierda()`: Referencia al hijo izquierdo.
- `get_derecha()`, `set_derecha()`: Referencia al hijo derecho.
- `es_hoja()`: Retorna `True` si el nodo no tiene hijos.

### Clase `ArbolBinarioBusqueda`
- **Operaciones de ABB**:
  - `insertar(dato)`: Inserta un nuevo valor en el ABB.
  - `buscar(dato)`: Verifica si un dato existe en el árbol.
  - `borrar(dato)`: Elimina un elemento del árbol manteniendo la estructura ABB.
  - `minimo()`, `maximo()`: Obtiene los valores gramos.
  - `altura()`: Calcula la altura del árbol.
  - `cantidad()`: Retorna el número total de nodos.
  - `esta_vacio()`: Indica si el árbol carece de elementos.

- **Recorridos del Árbol**:
  - `inorden()`: Recorrido Inorden.
  - `preorden()`: Recorrido Preorden.
  - `postorden()`: Recorrido Postorden.
  - `amplitud()`: Recorrido por niveles (BFS).

- **Operaciones de Expresión Matemática**:
  - `insertarexpresion(expresion)`: Carga una cadena matemática (ej: `"3 + 5 * 2"`) en el árbol.
  - `infija()`: Muestra la forma infija.
  - `postfija()`: Muestra la forma postfija.
  - `prefija()`: Muestra la forma prefija.
  - `result_expresion()`: Retorna y muestra el resultado numérico final.

- **Visualización**:
  - `imprimir()`: Muestra la representación gráfica del árbol rotado 90° en la consola.

---

## 📋 Requisitos del Sistema

- **Python**: Versión 3.8 o superior.
- **Git**: Para clonar el repositorio.
- **Librerías**: Ninguna externa (utiliza únicamente la librería estándar de Python).

---

## 📥 Clonación e Instalación

1. **Clonar el repositorio**:
   Abre una terminal y ejecuta el siguiente comando:
   ```bash
   git clone <URL_DE_TU_REPOSITORIO>
   ```

2. **Acceder al directorio del proyecto**:
   ```bash
   cd ABB
   ```

---

## ▶️ Cómo Ejecutar el Proyecto

Para ejecutar la demostración completa del proyecto (que incluye tanto el ABB como el Árbol de Expresiones Matemáticas):

### En Windows (PowerShell o CMD):
```bash
py abb.py
```
*o también:*
```bash
python abb.py
```

### En Linux / macOS:
```bash
python3 abb.py
```

---

## 💡 Ejemplo de Salida en Consola

```text
--- Demostración Árbol Binario de Búsqueda ---
Elementos insertados: [100, 50, 25, 55, 150, 120, 160, 40]
¿Está vacío?: False
Número de nodos (cantidad): 8
Mínimo: 25
Máximo: 160
Altura del árbol: 3
Recorrido Inorden:     [25, 40, 50, 55, 100, 120, 150, 160]
Recorrido Preorden:    [100, 50, 25, 40, 55, 150, 120, 160]
Recorrido Postorden:   [40, 25, 55, 50, 120, 160, 150, 100]
Recorrido en Amplitud: [100, 50, 150, 25, 55, 120, 160, 40]
Elemento borrado: 40
Representación visual del árbol:
        [160]
    [150]
        [120]
[100]
        [55]
    [50]
        [25]

==================================================
--- Demostración Árbol de Expresión Matemática ---
==================================================
Expresión ingresada: '3 + 5 * 2'

Representación visual del árbol de expresión:
        [2]
    [*]
        [5]
[+]
    [3]

Forma Infija: 3 + 5 * 2
Forma Postfija: 3 5 2 * +
Forma Prefija: + 3 * 5 2
Resultado de la expresión: 13
```
