# 12_Busqueda_Tabu.
# El GPS recuerda caminos "malos" (tabú) para evitar ciclos y explorar alternativas.

from typing import Dict, List, Tuple
import random  # puede usarse para variar elecciones en versiones estocásticas


# Grafo urbano: cada nodo lista sus vecinos (grafo no ponderado para este ejemplo)
grafo: Dict[str, List[str]] = {
    "Casa": ["Av1", "Mercado"],
    "Av1": ["Casa", "Plaza"],
    "Plaza": ["Av1", "Parque", "Mercado"],
    "Parque": ["Plaza", "Hospital"],
    "Mercado": ["Casa", "Plaza"],
    "Hospital": ["Parque"]
}


# Heurística: estimación de distancia restante al Hospital (valores menores = mejor)
h: Dict[str, int] = {
    "Casa": 8,
    "Av1": 6,
    "Plaza": 4,
    "Parque": 2,
    "Mercado": 5,
    "Hospital": 0
}


def busqueda_tabu(
    grafo: Dict[str, List[str]],
    inicio: str,
    destino: str,
    max_iteraciones: int = 15,
    tamano_tabu: int = 3
) -> Tuple[List[str], int]:
    """
    Implementación simple de Búsqueda Tabú (tabu search) aplicada a navegación.

    Parámetros:
    - grafo: mapa de la ciudad (vecinos por nodo).
    - inicio, destino: nodos de inicio y objetivo.
    - max_iteraciones: número máximo de pasos que intentará el algoritmo.
    - tamano_tabu: cuántos movimientos recientes recordar como prohibidos.

    Retorna una tupla (camino_seguido, heuristica_mejor_encontrada).
   
    """

    # Estado inicial
    actual = inicio
    mejor = inicio
    mejor_h = h[actual]      # mejor heurística encontrada hasta ahora
    lista_tabu: List[str] = []
    camino: List[str] = [actual]

    print(f"Iniciando en: {actual} (h={mejor_h})")

    # Bucle principal: intentamos mejorar hasta max_iteraciones
    for i in range(max_iteraciones):
        vecinos = grafo.get(actual, [])
        if not vecinos:
            # Sin vecinos: punto muerto
            print("Sin vecinos para continuar.")
            break

        # Filtramos vecinos que están en la lista tabú
        vecinos_validos = [v for v in vecinos if v not in lista_tabu]
        if not vecinos_validos:
            # Si todos son tabú, detenerse (o podríamos relajar la lista tabú)
            print("Todos los vecinos son tabú, el GPS se detiene.")
            break

        # Elegimos el vecino con mejor heurística (menor h).
        # En versiones estocásticas podríamos elegir aleatoriamente entre los mejores.
        siguiente = min(vecinos_validos, key=lambda n: h[n])
        siguiente_h = h[siguiente]

        print(f"Iteración {i+1}: {actual} → {siguiente} (h={siguiente_h})")

        # Si encontramos una mejor heurística, la guardamos
        if siguiente_h < mejor_h:
            mejor = siguiente
            mejor_h = siguiente_h

        # Añadimos el paso al camino seguido
        camino.append(siguiente)

        # Actualizamos la lista tabú con el movimiento reciente (nodo 'actual')
        lista_tabu.append(actual)
        if len(lista_tabu) > tamano_tabu:
            # Mantener la lista tabú con longitud fija
            lista_tabu.pop(0)

        # Avanzamos al siguiente nodo
        actual = siguiente

        # Si alcanzamos el destino, terminamos
        if actual == destino:
            print("¡Destino alcanzado!")
            break

    # Devolvemos el camino seguido y la mejor heurística encontrada
    return camino, mejor_h


def demo_tabu():
    origen, destino = "Casa", "Hospital"
    camino, heur_final = busqueda_tabu(grafo, origen, destino)

    print("\nRuta seguida por el GPS:")
    print("  " + " → ".join(camino))
    print(f"Heurística final: {heur_final}")


if __name__ == "__main__":
    demo_tabu()
