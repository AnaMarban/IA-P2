# 04_Profundidad_Limitada.py
# GPS Inteligente - Módulo 4: Búsqueda en Profundidad Limitada (DLS)
# Explora en profundidad, pero con un número máximo de pasos.

from typing import Dict, List, Optional, Tuple, Literal

Grafo = Dict[str, List[str]]
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
    if visitados is None:
        visitados = set()

    # Caso base: ¡llegamos!
    if actual == destino:
        return "success", [actual]

    # Si ya no podemos gastar más pasos
    if limite == 0:
        return "cutoff", None

    visitados.add(actual)
    hubo_cutoff = False

    for vecino in grafo.get(actual, []):
        if vecino in visitados:
            continue
        status, subcamino = dls_recursivo(grafo, vecino, destino, limite - 1, visitados)
        if status == "success":
            return "success", [actual] + subcamino
        if status == "cutoff":
            hubo_cutoff = True

    visitados.remove(actual)  # backtrack limpio para otras rutas
    return ("cutoff", None) if hubo_cutoff else ("failure", None)


def busqueda_profundidad_limitada(grafo: Grafo, inicio: str, destino: str, limite: int) -> Tuple[Status, Optional[List[str]]]:
    """
    Envoltura amigable: inicia DLS desde 'inicio' con 'limite' de profundidad.
    """
    return dls_recursivo(grafo, inicio, destino, limite, set())


def demo_ciudad_limites():
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
    limite = 2  # Casa -> Av1 -> Parque (2 pasos); falta 1 para Hospital
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
