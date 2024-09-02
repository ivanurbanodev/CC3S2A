def dijkstra(Grafo, salida):
    # inicializacion de los diccionarios para distancias y predecesores
    dist, prev = {}, {}
    result = []

    # establece la distancia inicial a cada vertice como infinita y sin predecesores
    for vertice in Grafo:
        dist[vertice] = float("inf")
        prev[vertice] = None
    # la distancia desde el nodo de salida a si mismo es 0
    dist[salida] = 0

    # lista de nodos no visitados
    Q = [vertice for vertice in Grafo]

    # mientras haya nodos no visitados en la lista Q
    while Q:
        # selecciona el nodo con la distancia mnima desde la salida
        u = min(Q, key=dist.get)
        Q.remove(u)  # remueve el nodo seleccionado de la lista Q
        result.append(u)  # agrega el nodo al resultado de nodos visitados en orden

        # revisa cada vecino del nodo u
        for vecino in Grafo[u]:
            # solo considera nodos que estan en Q y verificua si la nueva distancia es menor que la actual
            if vecino in Q and dist[vecino] > dist[u] + Grafo[u][vecino]:
                # actualiza la distancia para el vecino
                dist[vecino] = dist[u] + Grafo[u][vecino]
                # actualiza el predecesor para el vecino
                prev[vecino] = u

    # retorna el orden de visita de los nodos, las distancias minimas y los predecesores
    return result, dist, prev


# definicion del grafo con sus nodos y aristas 
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


s, distancia, previos = dijkstra(grafo, 'a')


print(f"{s=}")  
print(f"{distancia=}")  # Distancias mínimas desde 'a' a cada nodo
print(f"{previos=}")  
