def dijkstra(grafo, salida):
    # inicializa los diccionarios para almacenar distancias minimas y predecesores
    dist, prev = {}, {}
    visitados = []  # lista para rastrear el orden en que se visitan los nodos

    # establece todas las distancias a infinito inicialmente y sin predecesores
    for vertice in grafo:
        dist[vertice] = float("inf")
        prev[vertice] = None
    dist[salida] = 0  # la distancia al nodo de salida es 0

    # inicializa la lista de nodos no visitados
    no_visitados = list(grafo.keys())

    # mientras haya nodos no visitados
    while no_visitados:
        # selecciona el nodo no visitado con la distancia minima
        u = min(no_visitados, key=dist.get)
        no_visitados.remove(u)  # marca el nodo como visitado
        visitados.append(u)  # agrega el nodo a la lista de nodos visitados

        # revisa cada vecino del nodo actual
        for vecino, peso in grafo[u].items():
            # solo considera vecinos no visitados y actualiza la distancia si es más corta
            nueva_distancia = dist[u] + peso
            if vecino in no_visitados and nueva_distancia < dist[vecino]:
                dist[vecino] = nueva_distancia  # actualiza la distancia mínima
                prev[vecino] = u  # actualiza el predecesor

    # retorna el orden de visita de los nodos, las distancias mínimas y los predecesores
    return visitados, dist, prev


# definición del grafo con sus nodos y aristas ponderadas
grafo = {
    'a': {'b': 4, 'c': 3},
    'b': {'d': 5},
    'c': {'b': 2, 'd': 3, 'e': 6},
    'd': {'f': 5, 'e': 1},
    'e': {'g': 5},
    'g': {'z': 4},
    'f': {'g': 2, 'z': 7},
    'z': {}
}

# ejecución del algoritmo de Dijkstra desde el nodo 'a'
visitados, distancias, predecesores = dijkstra(grafo, 'a')

# imprime los resultados
print(f"Orden de nodos visitados: {visitados}")
print(f"Distancias mínimas desde 'a': {distancias}")
print(f"Predecesores en el camino más corto: {predecesores}")
