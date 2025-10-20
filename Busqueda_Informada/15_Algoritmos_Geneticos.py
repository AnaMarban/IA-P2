# 15_Algoritmos_Geneticos.py
# GPS Inteligente - Módulo 15: Algoritmos Genéticos
# Evoluciona rutas mediante selección, cruce y mutación.

import random
from typing import List, Dict, Tuple

# Grafo urbano (rutas posibles)
grafo: Dict[str, List[str]] = {
    "Casa": ["Av1", "Mercado"],
    "Av1": ["Plaza"],
    "Plaza": ["Parque", "Mercado"],
    "Parque": ["Hospital"],
    "Mercado": ["Parque"],
    "Hospital": []
}

# Heurística: distancia estimada al Hospital (menor = mejor)
h: Dict[str, int] = {
    "Casa": 8,
    "Av1": 6,
    "Plaza": 4,
    "Parque": 2,
    "Mercado": 5,
    "Hospital": 0
}

# =====================================================
# Funciones del algoritmo genético
# =====================================================

def generar_ruta_aleatoria(inicio: str, destino: str, max_pasos: int = 5) -> List[str]:
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
    """La 'aptitud' de la ruta es la heurística del último nodo."""
    return h.get(ruta[-1], 999)

def cruzar_rutas(r1: List[str], r2: List[str]) -> List[str]:
    """Cruza dos rutas (intercambia partes)."""
    corte = min(len(r1), len(r2)) // 2
    nueva = r1[:corte] + [n for n in r2 if n not in r1[:corte]]
    return nueva

def mutar_ruta(ruta: List[str], probabilidad: float = 0.2) -> List[str]:
    """A veces cambia un tramo de la ruta al azar."""
    if random.random() < probabilidad and len(ruta) > 2:
        i = random.randint(1, len(ruta) - 2)
        vecinos = grafo.get(ruta[i - 1], [])
        if vecinos:
            ruta[i] = random.choice(vecinos)
    return ruta

def algoritmo_genetico(inicio: str, destino: str, poblacion_inicial: int = 6, generaciones: int = 6) -> Tuple[List[str], int]:
    """Evoluciona rutas usando principios genéticos."""
    poblacion = [generar_ruta_aleatoria(inicio, destino) for _ in range(poblacion_inicial)]

    print(f"Generación inicial ({len(poblacion)} rutas):")
    for r in poblacion:
        print("  ", " → ".join(r))

    for gen in range(generaciones):
        print(f"\n== Generación {gen+1} ==")
        # Evaluar todas las rutas
        evaluadas = [(evaluar_ruta(r), r) for r in poblacion]
        evaluadas.sort(key=lambda x: x[0])

        # Mostrar las mejores
        print("Mejores rutas actuales:")
        for val, r in evaluadas[:3]:
            print(f"  ({val}) {' → '.join(r)}")

        # Selección: mejores 3 sobreviven
        mejores = [r for _, r in evaluadas[:3]]

        # Reproducción: cruces entre las mejores
        hijos = []
        while len(hijos) < poblacion_inicial:
            p1, p2 = random.sample(mejores, 2)
            hijo = cruzar_rutas(p1, p2)
            hijo = mutar_ruta(hijo)
            hijos.append(hijo)

        poblacion = hijos

    # Resultado final
    mejor_val, mejor_ruta = min([(evaluar_ruta(r), r) for r in poblacion], key=lambda x: x[0])
    return mejor_ruta, mejor_val

def demo_genetico():
    ruta, valor = algoritmo_genetico("Casa", "Hospital")
    print("\nRuta evolucionada final:")
    print("  " + " → ".join(ruta))
    print(f"Heurística final: {valor}")

if __name__ == "__main__":
    demo_genetico()
