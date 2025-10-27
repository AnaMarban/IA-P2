# 27_Iteracion_Valores.
# Tema 27 - Iteración de Valores (Value Iteration)

from typing import Dict, Tuple

# Estados del GPS
estados = ["Casa", "Camino", "Hospital"]

# Recompensas inmediatas
recompensa: Dict[str, float] = {
    "Casa": 0,
    "Camino": -1,
    "Hospital": 10
}

# Transiciones (probabilidad, siguiente_estado)
# Ejemplo: desde "Camino", 0.8 de prob a "Hospital", 0.2 a "Casa"
transiciones: Dict[str, list] = {
    "Casa": [("Camino", 1.0)],
    "Camino": [("Hospital", 0.8), ("Casa", 0.2)],
    "Hospital": [("Hospital", 1.0)]  # estado terminal
}

# Parámetros de aprendizaje
GAMMA = 0.9  # factor de descuento (importancia del futuro)
ITERACIONES = 10

def iteracion_valores():
    """Implementación simple del algoritmo de Value Iteration."""
    utilidades = {s: 0 for s in estados}

    for i in range(ITERACIONES):
        nuevo_valor = {}
        print(f"\n📘 Iteración {i+1}:")
        for s in estados:
            # Si es terminal, su utilidad es su recompensa
            if s == "Hospital":
                nuevo_valor[s] = recompensa[s]
                continue

            # Calcular utilidad esperada
            total = 0
            for (sig, prob) in transiciones[s]:
                total += prob * utilidades[sig]
            nuevo_valor[s] = recompensa[s] + GAMMA * total
            print(f"  U({s}) = {nuevo_valor[s]:.3f}")

        utilidades = nuevo_valor

    print("\n🔹 Utilidades finales:")
    for s, u in utilidades.items():
        print(f"  {s}: {u:.3f}")

if __name__ == "__main__":
    iteracion_valores()
