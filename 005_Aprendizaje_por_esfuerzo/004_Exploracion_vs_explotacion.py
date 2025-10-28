# Exploracion_Explotacion.py
# GPS Inteligente - Enfoque 5: Aprendizaje por Refuerzo
# Tema - Exploración vs Explotación (ε-greedy)

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

# Transiciones (simuladas)
def mover(estado: str, accion: str) -> str:
    if estado == "Casa" and accion == "Avanzar":
        return "Camino"
    elif estado == "Camino" and accion == "Avanzar":
        return random.choices(["Hospital", "Casa"], weights=[0.8, 0.2])[0]
    elif estado == "Camino" and accion == "Volver":
        return "Casa"
    return "Hospital"

# Parámetros
ALFA = 0.1
GAMMA = 0.9
EPSILON = 0.2  # 20% de exploración
EPISODIOS = 30

# Q-Table
Q: Dict[Tuple[str, str], float] = { (s,a): 0 for s in estados for a in acciones.get(s, []) }

def elegir_accion(estado: str) -> str:
    """Estrategia epsilon-greedy: explora o explota."""
    if random.random() < EPSILON:
        accion = random.choice(acciones[estado])
        print(f"   Explorando: {accion}")
        return accion
    accion = max(acciones[estado], key=lambda a: Q[(estado,a)])
    print(f"   Explotando: {accion}")
    return accion

def entrenamiento():
    """Entrena al GPS equilibrando exploración y explotación."""
    for episodio in range(EPISODIOS):
        estado = "Casa"
        print(f"\n Episodio {episodio + 1}")
        while estado != "Hospital":
            accion = elegir_accion(estado)
            siguiente = mover(estado, accion)
            recompensa = recompensas.get((estado, accion), 0 if siguiente != "Hospital" else 10)

            # Actualización Q
            if acciones.get(siguiente):
                mejor_q = max(Q[(siguiente, a)] for a in acciones[siguiente])
            else:
                mejor_q = 0

            Q[(estado, accion)] += ALFA * (recompensa + GAMMA * mejor_q - Q[(estado, accion)])
            print(f"  {estado} → {accion} → {siguiente} | R={recompensa} | Q={Q[(estado,accion)]:.2f}")
            estado = siguiente

    print("\n Q-Table final:")
    for (s,a), v in Q.items():
        print(f"  ({s}, {a}): {v:.2f}")

if __name__ == "__main__":
    entrenamiento()
