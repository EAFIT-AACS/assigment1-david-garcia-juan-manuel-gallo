# *Equipo*
      - David Garcia
      - Juan Manuel Gallo

---

# Minimización de Autómatas Finitos Deterministas (DFA)

## 📌 Descripción
Este proyecto implementa el **algoritmo de minimización de un DFA** usando el método de llenado de tabla. El programa lee un archivo de entrada que describe el autómata y luego imprime, en orden lexicográfico, los pares de estados equivalentes. Se asume que los estados son números naturales y que el estado inicial siempre es `0`.

---

# Minimización de Autómatas Finitos Deterministas (DFA)

## 📌 Descripción
Este proyecto implementa el **algoritmo de minimización de un DFA** usando el método de llenado de tabla. El programa lee un archivo de entrada que describe el autómata y luego imprime, en orden lexicográfico, los pares de estados equivalentes. Se asume que los estados son números naturales y que el estado inicial siempre es `0`.

---

## 📂 Estructura del Proyecto
mi_proyecto/
        ─ minimizar_dfa.py  # Código fuente en Python.
        ─ input.txt         # Archivo de entrada con la descripción del DFA
        ─ README.md          # Esta documentación



---

## 📥 Entrada
El archivo de entrada debe seguir este formato:
1. **Número de casos de prueba**  
2. Para cada caso:
   - Número de estados del DFA.
   - Alfabeto (símbolos separados por espacios).
   - Estados finales (separados por espacios).
   - Transiciones (una línea por cada estado; cada línea contiene el estado de origen y, a continuación, el destino para cada símbolo del alfabeto, en el mismo orden).

### Ejemplo de `input.txt`
1 6 a b 3 4 1 2 3 4 3 5 3 4 4 5 3 4


---

## 📤 Salida
El programa imprime en la consola los pares de estados equivalentes en **orden lexicográfico**.  
  
### Ejemplo de salida:
(1,2) (3,4) (3,5) (4,5)


---

## 🚀 Cómo Ejecutarlo
### **Desde la Terminal**
1. Asegúrate de tener **Python 3.x** instalado.
2. Coloca el archivo `input.txt` en el mismo directorio que `minimizar_dfa.py`.
3. Abre la terminal en ese directorio y ejecuta:
python minimizar_dfa.py input.txt

---

## 📝 Explicación del Algoritmo
1. **Lectura de la Entrada:**  
Se extraen los casos de prueba que incluyen el número de estados, el alfabeto, los estados finales y la tabla de transiciones.

2. **Inicialización de la Tabla de Indistinguibilidad:**  
Se crea una matriz triangular inferior donde cada celda representa un par de estados:
- Se marca "0" (sin distinguir) en cada celda.
- En la diagonal se pone el número del estado.
- Se marca con "x" los pares en los que un estado es final y el otro no (ya que son inmediatamente distinguibles).

3. **Proceso Iterativo:**  
Se recorre la matriz y, para cada par sin marcar, se comprueba si, para algún símbolo del alfabeto, las transiciones conducen a un par ya marcado. Si es así, se marca el par actual.

4. **Determinación de Estados Equivalentes:**  
Los pares que permanecen sin marcar son considerados equivalentes y se imprimen en orden lexicográfico.

---

## 🛠️ Requisitos y Herramientas
- **Lenguaje:** Python 3.x  
- **Editor de Código:** VSCode, PyCharm, o el de tu preferencia  
- **Terminal o Línea de Comandos:** Para ejecutar el programa

---

## 🎯 Ejemplos de Casos de Prueba

### Caso 1
- **Descripción:** DFA con 4 estados (0, 1, 2, 3), alfabeto `{a, b}` y estados finales `{1, 3}`.
- **Entrada:**
1 4 a b 1 3 0 1 2 1 1 3 2 1 2 3 1 3

- **Salida Esperada:**  
(0,2) (1,3)


### Caso 2
- **Descripción:** DFA con 5 estados (0, 1, 2, 3, 4), alfabeto `{a, b}` y estados finales `{2, 4}`.
- **Entrada:**
1 5 a b 2 4 0 1 2 1 1 3 2 1 4 3 1 3 4 1 4

- **Salida Esperada:**  
(1,3) (2,4)


### Ambos Casos Juntos
Si deseas probar ambos casos en un solo archivo, el contenido de `input.txt` debe ser:

2 4 a b 1 3 0 1 2 1 1 3 2 1 2 3 1 3 5 a b 2 4 0 1 2 1 1 3 2 1 4 3 1 3 4 1 4

Y la salida esperada será:
(0,2) (1,3) (1,3) (2,4)

---




