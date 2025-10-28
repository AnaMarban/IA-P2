# Q_Learning.
# GPS Inteligente - Enfoque 5: Aprendizaje por Refuerzo
# Tema - Q-Learning

import random
from typing import Dict, Tuple

# Estados y acciones
estados = ["Casa", "Camino", "Hospital"]
acciones = {"Casa": ["Avanzar"], "Camino": ["Avanzar", "Volver"], "Hospital": []}

# Recompensas
recompensas: Dict[Tuple[str, str], float] = {
    ("Casa", "Avanzar"): 0,
    ("Camino", "Avanzar"): -1,
    ("Camino", "Volver"): -2
}

# Transiciones aleatorias simuladas (el GPS no las conoce, solo las experimenta)
def mover(estado: str, accion: str) -> str:
    if estado == "Casa" and accion == "Avanzar":
        return "Camino"
    elif estado == "Camino" and accion == "Avanzar":
        return random.choices(["Hospital", "Casa"], weights=[0.8, 0.2])[0]
    elif estado == "Camino" and accion == "Volver":
        return "Casa"
    return "Hospital"

# Parámetros
ALFA = 0.1      # tasa de aprendizaje
GAMMA = 0.9     # descuento futuro
EPSILON = 0.2   # probabilidad de explorar
EPISODIOS = 40  # cantidad de viajes

# Tabla Q (estado, acción) → valor
Q: Dict[Tuple[str, str], float] = { (s,a): 0 for s in estados for a in acciones.get(s, []) }

def elegir_accion(estado: str) -> str:
    """Estrategia epsilon-greedy: a veces explora, a veces aprovecha."""
    if random.random() < EPSILON:
        return random.choice(acciones[estado])  # exploración
    # explotación: elige la mejor acción conocida
    return max(acciones[estado], key=lambda a: Q[(estado, a)])

def q_learning():
    """Entrenamiento del GPS mediante Q-Learning."""
    for episodio in range(EPISODIOS):
        estado = "Casa"
        print(f"\n📘 Episodio {episodio + 1}")
        while estado != "Hospital":
            accion = elegir_accion(estado)
            siguiente = mover(estado, accion)
            recompensa = recompensas.get((estado, accion), 0 if siguiente != "Hospital" else 10)

            # Actualización Q (regla de Bellman)
            if acciones.get(siguiente):
                mejor_q_futuro = max(Q[(siguiente, a)] for a in acciones[siguiente])
            else:
                mejor_q_futuro = 0

            Q[(estado, accion)] += ALFA * (
                recompensa + GAMMA * mejor_q_futuro - Q[(estado, accion)]
            )

            print(f"  {estado} → {accion} → {siguiente} | R={recompensa} | Q={Q[(estado, accion)]:.2f}")
            estado = siguiente

    print("\n🔹 Q-Table final:")
    for (s,a), q in Q.items():
        print(f"  ({s}, {a}): {q:.2f}")

    # Construir política óptima
    print("\n🚗 Política aprendida:")
    for s in estados:
        if acciones.get(s):
            mejor = max(acciones[s], key=lambda a: Q[(s,a)])
            print(f"  En {s}, elige: {mejor}")

if __name__ == "__main__":
    q_learning()
