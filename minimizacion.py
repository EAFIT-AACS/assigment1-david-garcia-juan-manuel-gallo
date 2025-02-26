# Función opcional para visualizar la matriz de minimización (útil para depuración)
def mostrar_tabla(tabla, total_estados):
    for fila in range(total_estados):
        for col in range(fila + 1):
            print(tabla[fila][col], end=" ")
        print()

def main():
    # Abrir y leer el archivo de entrada
    with open('Input.txt', 'r') as entrada:
        contenido = entrada.readlines()

    # Número de casos de prueba
    num_casos = int(contenido[0].strip())
    
    # Listas para almacenar la información de cada caso
    lista_estados  = []   # Número de estados por caso
    lista_alfabetos = []  # Alfabeto (lista de símbolos) por caso
    lista_finales  = []   # Estados finales por caso
    lista_transiciones = []  # Tabla de transiciones por caso

    indice = 1
    for _ in range(num_casos):
        # Leer el número de estados y agregarlo a la lista
        n_estados = int(contenido[indice].strip())
        lista_estados.append(n_estados)
        indice += 1

        # Leer el alfabeto (separado por espacios)
        simbolos = contenido[indice].strip().split()
        lista_alfabetos.append(simbolos)
        indice += 1

        # Leer los estados finales y convertirlos a enteros
        finales = list(map(int, contenido[indice].strip().split()))
        lista_finales.append(finales)
        indice += 1

        # Leer la tabla de transiciones para cada estado
        transiciones_caso = []
        for _ in range(n_estados):
            fila_trans = contenido[indice].strip().split()
            transiciones_caso.append(fila_trans)
            indice += 1
        lista_transiciones.append(transiciones_caso)

    # Procesamiento de cada caso
    for caso in range(num_casos):
        n = lista_estados[caso]
        alfabeto = lista_alfabetos[caso]
        finales = lista_finales[caso]
        tabla_trans = lista_transiciones[caso]

        # Construir el diccionario de transiciones (delta)
        # La estructura es: delta[(estado, símbolo)] = estado_destino
        delta = {}
        for i in range(n):
            # Se asume que cada línea inicia con el estado y luego los destinos para cada símbolo
            for pos, simbolo in enumerate(alfabeto):
                estado_actual = int(tabla_trans[i][0])
                destino = int(tabla_trans[i][pos + 1])
                delta[(estado_actual, simbolo)] = destino

        # Inicializar la matriz (tabla triangular inferior) para el algoritmo de minimización.
        # Se llena inicialmente con "0" y en la diagonal se coloca el número del estado.
        tabla_min = [["0"] * n for _ in range(n)]
        for i in range(n):
            tabla_min[i][i] = str(i)

        # Paso 1: Marcar con "x" aquellos pares (i,j) en que uno es estado final y el otro no.
        for i in range(1, n):
            for j in range(i):
                if (i in finales) ^ (j in finales):
                    tabla_min[i][j] = "x"

        # Paso 2: Realizar el marcado iterativo de la tabla
        cambio = True
        while cambio:
            cambio = False
            for i in range(1, n):
                for j in range(i):
                    if tabla_min[i][j] == "0":
                        for simbolo in alfabeto:
                            destino_j = delta[(j, simbolo)]
                            destino_i = delta[(i, simbolo)]
                            # Acceder a la celda correspondiente (ordenada de menor a mayor)
                            a, b = min(destino_j, destino_i), max(destino_j, destino_i)
                            if tabla_min[b][a] == "x":
                                tabla_min[i][j] = "x"
                                cambio = True
                                break

        # Paso 3: Imprimir los pares equivalentes (aquellos que no fueron marcados)
        for i in range(1, n):
            for j in range(i):
                if tabla_min[i][j] == "0":
                    print(f"({j},{i})", end=" ")
        print()

if __name__ == "__main__":
    main()