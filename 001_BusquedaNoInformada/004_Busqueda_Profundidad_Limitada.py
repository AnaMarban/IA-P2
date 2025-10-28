# 04_Profundidad_Limitada.
# Explora en profundidad, pero con un número máximo de pasos.

from typing import Dict, List, Optional, Tuple, Literal  # anotaciones de tipos

# Un grafo simple: nodo -> lista de vecinos
Grafo = Dict[str, List[str]]

# Estado que puede devolver la búsqueda limitada:
# - "success": encontró el destino dentro del límite
# - "cutoff": se alcanzó el límite antes de encontrarlo (posible continuar con más profundidad)
# - "failure": no hay camino por este rumbo
Status = Literal["success", "cutoff", "failure"]


def dls_recursivo(
    grafo: Grafo,
    actual: str,
    destino: str,
    limite: int,
    visitados: Optional[set] = None
) -> Tuple[Status, Optional[List[str]]]:
    """
    Búsqueda en Profundidad Limitada (recursiva).
    Devuelve:
      - ("success", camino) si encontró destino dentro del límite.
      - ("cutoff", None) si se alcanzó el límite antes de encontrarlo.
      - ("failure", None) si no hay camino por este rumbo.
    Nota: usamos 'visitados' para evitar ciclos simples.
    """

    # Inicializamos el conjunto de visitados si no se proporcionó
    if visitados is None:
        visitados = set()

    # Caso base 1: ya estamos en el destino
    if actual == destino:
        return "success", [actual]

    # Caso base 2: no nos quedan niveles para explorar -> cutoff
    if limite == 0:
        return "cutoff", None

    # Marcamos el nodo actual como visitado para evitar ciclos
    visitados.add(actual)

    # Señalamos si alguna rama alcanzó el límite (cutoff)
    hubo_cutoff = False

    # Recorremos vecinos del nodo actual
    for vecino in grafo.get(actual, []):
        # Si ya visitamos el vecino, lo omitimos
        if vecino in visitados:
            continue

        # Llamada recursiva con límite reducido en 1
        status, subcamino = dls_recursivo(grafo, vecino, destino, limite - 1, visitados)

        # Si una rama encontró el destino, construimos y devolvemos el camino completo
        if status == "success":
            return "success", [actual] + subcamino

        # Si una rama no pudo terminar por límite, lo anotamos para devolver "cutoff" si no hay success
        if status == "cutoff":
            hubo_cutoff = True

    # Hacemos backtrack: desmarcamos 'actual' para permitir otras rutas que lo visiten por distinto camino
    visitados.remove(actual)

    # Si alguna rama fue 'cutoff', devolvemos 'cutoff', si no, es 'failure'
    return ("cutoff", None) if hubo_cutoff else ("failure", None)


def busqueda_profundidad_limitada(grafo: Grafo, inicio: str, destino: str, limite: int) -> Tuple[Status, Optional[List[str]]]:
    """
    Envoltura sencilla que inicia la búsqueda limitada desde 'inicio' con el 'limite' dado.
    """
    # Inicializamos el conjunto de visitados vacío y llamamos a la función recursiva
    return dls_recursivo(grafo, inicio, destino, limite, set())


def demo_ciudad_limites():
    # Grafo de ejemplo (ciudad) con vecinos para cada nodo
    ciudad: Grafo = {
        "Casa":    ["Av1", "Mercado"],
        "Av1":     ["Plaza", "Parque"],
        "Plaza":   ["Escuela"],
        "Parque":  ["Hospital"],
        "Mercado": [],
        "Escuela": [],
        "Hospital": []
    }

    origen, destino = "Casa", "Hospital"

    print("== DEMO 1: Límite insuficiente ==")
    limite = 2  # Casa -> Av1 -> Parque (2 pasos); hace falta 1 paso más para Hospital
    status, ruta = busqueda_profundidad_limitada(ciudad, origen, destino, limite)
    print(f"Límite = {limite} | Estado: {status}")
    if ruta:
        print("Ruta:", " → ".join(ruta))
    print()

    print("== DEMO 2: Límite suficiente ==")
    limite = 3  # Casa -> Av1 -> Parque -> Hospital (3 pasos)
    status, ruta = busqueda_profundidad_limitada(ciudad, origen, destino, limite)
    print(f"Límite = {limite} | Estado: {status}")
    if ruta:
        print("Ruta:", " → ".join(ruta))


if __name__ == "__main__":
    demo_ciudad_limites()
