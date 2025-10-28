# 16_Busqueda_Online.
# El GPS explora y decide en tiempo real según lo que va descubriendo en la calle.

from typing import Dict, List
import random  # import disponible para simulaciones estocásticas (aquí no se usa)


# Mapa urbano: lista de vecinos para cada nodo. Incluimos una "sorpresa"
# que simula una calle que puede cerrarse durante la búsqueda.
grafo: Dict[str, List[str]] = {
    "Casa": ["Av1", "Mercado"],
    "Av1": ["Casa", "Plaza"],
    "Plaza": ["Av1", "Parque", "Mercado"],
    "Parque": ["Plaza", "Hospital"],
    "Mercado": ["Casa", "Plaza"],
    "Hospital": ["Parque"]
}


# Heurística: estimación de distancia al Hospital (valores menores = mejor)
h: Dict[str, int] = {
    "Casa": 8,
    "Av1": 6,
    "Plaza": 4,
    "Parque": 2,
    "Mercado": 5,
    "Hospital": 0
}


# Ejemplo de calle que se cierra inesperadamente durante la simulación
CALLE_CERRADA = ("Plaza", "Parque")


def online_search(inicio: str, destino: str, max_pasos: int = 10):
    """
    Simula una búsqueda online (decisiones en tiempo real):

    - El GPS conoce sólo el fragmento del mapa que ha descubierto.
    - En cada paso elige el vecino más prometedor según la heurística h.
    - Si detecta eventos dinámicos (p. ej. una calle cerrada), adapta la elección.
    - max_pasos limita la longitud máxima de la simulación.
    """

    actual = inicio
    camino: List[str] = [actual]
    descubiertos = {inicio}  # nodos que el GPS ha visto hasta ahora
    print(f"Iniciando en: {actual}")

    # Simulación paso a paso
    for paso in range(max_pasos):
        vecinos = grafo.get(actual, [])

        # Detectar si la calle cerrada afecta al nodo actual; si es así la quitamos
        if CALLE_CERRADA[0] == actual and CALLE_CERRADA[1] in vecinos:
            vecinos.remove(CALLE_CERRADA[1])
            print(f"⚠️  Calle cerrada detectada: {actual} → {CALLE_CERRADA[1]}")

        # Si no quedan vecinos posibles, la búsqueda se detiene
        if not vecinos:
            print("🚫 Sin rutas disponibles, deteniendo búsqueda.")
            break

        # Elegir el vecino con menor heurística (parece más cerca del objetivo)
        siguiente = min(vecinos, key=lambda n: h[n])

        print(f"→ Paso {paso+1}: {actual} → {siguiente} (h={h[siguiente]})")

        # Avanzamos al siguiente nodo y lo registramos
        actual = siguiente
        camino.append(actual)
        descubiertos.add(actual)

        # Si alcanzamos el destino, terminamos con éxito
        if actual == destino:
            print("✅ ¡Destino alcanzado!")
            break

        # Simulación adicional: en algún punto el GPS puede 'descubrir' una nueva ruta
        # (esto demuestra que el mapa puede crecer en tiempo real).
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
