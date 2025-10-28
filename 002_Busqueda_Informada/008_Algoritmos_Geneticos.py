# 15_Algoritmos_Geneticos.
# Evoluciona rutas mediante selección, cruce y mutación (versión simple).

import random
from typing import List, Dict, Tuple


# Grafo urbano (rutas posibles): cada nodo lista sus vecinos posibles
grafo: Dict[str, List[str]] = {
    "Casa": ["Av1", "Mercado"],
    "Av1": ["Plaza"],
    "Plaza": ["Parque", "Mercado"],
    "Parque": ["Hospital"],
    "Mercado": ["Parque"],
    "Hospital": []
}


# Heurística: estimación de la distancia al Hospital (menor = mejor)
h: Dict[str, int] = {
    "Casa": 8,
    "Av1": 6,
    "Plaza": 4,
    "Parque": 2,
    "Mercado": 5,
    "Hospital": 0
}


# =====================================================
# Funciones del algoritmo genético (simples y explicadas)
# =====================================================


def generar_ruta_aleatoria(inicio: str, destino: str, max_pasos: int = 5) -> List[str]:
    """Genera una ruta aleatoria siguiendo vecinos hasta max_pasos o el destino.

    - Empieza en 'inicio' y en cada paso elige aleatoriamente un vecino.
    - Se detiene al alcanzar 'destino' o al no tener más vecinos.
    """
    ruta = [inicio]
    actual = inicio
    for _ in range(max_pasos):
        vecinos = grafo.get(actual, [])
        if not vecinos:
            break
        actual = random.choice(vecinos)
        ruta.append(actual)
        if actual == destino:
            break
    return ruta


def evaluar_ruta(ruta: List[str]) -> int:
    """La 'aptitud' (fitness) de la ruta: usamos la heurística del último nodo.

    - Cuanto menor sea el valor devuelto, mejor se considera la ruta.
    - Si la ruta termina en un nodo desconocido, devolvemos 999 como penalización.
    """
    return h.get(ruta[-1], 999)


def cruzar_rutas(r1: List[str], r2: List[str]) -> List[str]:
    """Cruza dos rutas intercambiando partes para crear un nuevo individuo.

    Estrategia simple: tomamos la mitad de r1 y completamos con nodos de r2
    que no estén repetidos en la primera parte.
    """
    corte = min(len(r1), len(r2)) // 2
    nueva = r1[:corte] + [n for n in r2 if n not in r1[:corte]]
    return nueva


def mutar_ruta(ruta: List[str], probabilidad: float = 0.2) -> List[str]:
    """Aplica una mutación aleatoria: cambia un nodo interior por un vecino.

    - Con probabilidad 'probabilidad' se elige un índice interior y se reemplaza
      por un vecino válido del nodo anterior.
    """
    if random.random() < probabilidad and len(ruta) > 2:
        i = random.randint(1, len(ruta) - 2)
        vecinos = grafo.get(ruta[i - 1], [])
        if vecinos:
            ruta[i] = random.choice(vecinos)
    return ruta


def algoritmo_genetico(inicio: str, destino: str, poblacion_inicial: int = 6, generaciones: int = 6) -> Tuple[List[str], int]:
    """Evoluciona rutas usando un bucle genético simple:
    - Generación inicial aleatoria
    - Evaluación por aptitud
    - Selección de los mejores
    - Cruce y mutación para crear nueva población
    """
    # Crear población inicial
    poblacion = [generar_ruta_aleatoria(inicio, destino) for _ in range(poblacion_inicial)]

    print(f"Generación inicial ({len(poblacion)} rutas):")
    for r in poblacion:
        print("  ", " → ".join(r))

    # Bucle de generaciones
    for gen in range(generaciones):
        print(f"\n== Generación {gen+1} ==")

        # Evaluar todas las rutas y ordenarlas por aptitud (menor es mejor)
        evaluadas = [(evaluar_ruta(r), r) for r in poblacion]
        evaluadas.sort(key=lambda x: x[0])

        # Mostrar las mejores rutas actuales
        print("Mejores rutas actuales:")
        for val, r in evaluadas[:3]:
            print(f"  ({val}) {' → '.join(r)}")

        # Selección: los mejores sobreviven (por simplicidad, tomamos top-3)
        mejores = [r for _, r in evaluadas[:3]]

        # Reproducción: cruzamos padres seleccionados para producir hijos
        hijos: List[List[str]] = []
        while len(hijos) < poblacion_inicial:
            p1, p2 = random.sample(mejores, 2)
            hijo = cruzar_rutas(p1, p2)
            hijo = mutar_ruta(hijo)
            hijos.append(hijo)

        poblacion = hijos

    # Elegir la mejor ruta final y su valor
    mejor_val, mejor_ruta = min([(evaluar_ruta(r), r) for r in poblacion], key=lambda x: x[0])
    return mejor_ruta, mejor_val


def demo_genetico():
    ruta, valor = algoritmo_genetico("Casa", "Hospital")
    print("\nRuta evolucionada final:")
    print("  " + " → ".join(ruta))
    print(f"Heurística final: {valor}")


if __name__ == "__main__":
    demo_genetico()
