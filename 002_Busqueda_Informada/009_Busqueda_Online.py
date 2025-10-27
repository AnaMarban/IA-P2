# 16_Busqueda_Online.
# El GPS explora y decide en tiempo real según lo que descubre.

from typing import Dict, List
import random

# Mapa urbano (con una sorpresa: una calle cerrada)
grafo: Dict[str, List[str]] = {
    "Casa": ["Av1", "Mercado"],
    "Av1": ["Casa", "Plaza"],
    "Plaza": ["Av1", "Parque", "Mercado"],
    "Parque": ["Plaza", "Hospital"],
    "Mercado": ["Casa", "Plaza"],
    "Hospital": ["Parque"]
}

# Heurística (estimación al hospital)
h: Dict[str, int] = {
    "Casa": 8,
    "Av1": 6,
    "Plaza": 4,
    "Parque": 2,
    "Mercado": 5,
    "Hospital": 0
}

# Calle cerrada inesperadamente
CALLE_CERRADA = ("Plaza", "Parque")

def online_search(inicio: str, destino: str, max_pasos: int = 10):
    """
    Simula una búsqueda online:
    el GPS explora paso a paso y reacciona a cambios (calles cerradas).
    """
    actual = inicio
    camino = [actual]
    descubiertos = {inicio}
    print(f"Iniciando en: {actual}")

    for paso in range(max_pasos):
        vecinos = grafo.get(actual, [])

        # Detectar si hay una calle cerrada
        if CALLE_CERRADA[0] == actual and CALLE_CERRADA[1] in vecinos:
            vecinos.remove(CALLE_CERRADA[1])
            print(f"⚠️  Calle cerrada detectada: {actual} → {CALLE_CERRADA[1]}")

        if not vecinos:
            print("🚫 Sin rutas disponibles, deteniendo búsqueda.")
            break

        # Elegir el vecino más prometedor (menor heurística)
        siguiente = min(vecinos, key=lambda n: h[n])

        print(f"→ Paso {paso+1}: {actual} → {siguiente} (h={h[siguiente]})")
        actual = siguiente
        camino.append(actual)
        descubiertos.add(actual)

        if actual == destino:
            print("✅ ¡Destino alcanzado!")
            break

        # Simular que descubre una nueva calle a mitad de camino
        if actual == "Av1" and "Mercado" not in grafo["Av1"]:
            grafo["Av1"].append("Mercado")
            print("🆕 Nueva ruta descubierta: Av1 → Mercado")

    return camino


def demo_online():
    origen, destino = "Casa", "Hospital"
    ruta = online_search(origen, destino)

    print("\nRuta recorrida en tiempo real:")
    print("  " + " → ".join(ruta))


if __name__ == "__main__":
    demo_online()
