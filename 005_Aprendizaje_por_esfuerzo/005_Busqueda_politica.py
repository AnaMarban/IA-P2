# Busqueda_Politica.
# GPS Inteligente - Enfoque 5: Aprendizaje por Refuerzo
# Tema - Búsqueda de la Política

import random
from typing import Dict

# Estados y acciones
estados = ["Casa", "Camino", "Hospital"]
acciones = {"Casa": ["Avanzar"], "Camino": ["Avanzar", "Esperar"], "Hospital": []}

# Recompensas
recompensas: Dict[str, float] = {"Casa": 0, "Camino": -1, "Hospital": 10}

# Política inicial (probabilidades)
politica = {
    "Casa": {"Avanzar": 1.0},
    "Camino": {"Avanzar": 0.5, "Esperar": 0.5},
}

# Parámetros
ALFA = 0.05      # tasa de aprendizaje
EPISODIOS = 40
GAMMA = 0.9

def mover(estado: str, accion: str) -> str:
    """Simula el movimiento del GPS."""
    if estado == "Casa" and accion == "Avanzar":
        return "Camino"
    if estado == "Camino" and accion == "Avanzar":
        return random.choices(["Hospital", "Casa"], weights=[0.8, 0.2])[0]
    if estado == "Camino" and accion == "Esperar":
        return "Camino"
    return "Hospital"

def elegir_accion(estado: str) -> str:
    """Elige una acción según las probabilidades de la política."""
    probs = politica[estado]
    return random.choices(list(probs.keys()), weights=list(probs.values()))[0]

def actualizar_politica(estado: str, accion: str, recompensa: float):
    """Ajusta la política según la recompensa (gradiente de política simple)."""
    for a in politica[estado]:
        if a == accion:
            politica[estado][a] += ALFA * recompensa * (1 - politica[estado][a])
        else:
            politica[estado][a] -= ALFA * recompensa * politica[estado][a]
    # Normalizar para mantener suma = 1
    total = sum(politica[estado].values())
    for a in politica[estado]:
        politica[estado][a] /= total

def busqueda_politica():
    """Entrena al GPS mejorando directamente su política."""
    for episodio in range(EPISODIOS):
        estado = "Casa"
        total_r = 0
        print(f"\n📘 Episodio {episodio + 1}")
        while estado != "Hospital":
            accion = elegir_accion(estado)
            siguiente = mover(estado, accion)
            r = recompensas.get(siguiente, 0)
            total_r += r

            actualizar_politica(estado, accion, r)
            print(f"  {estado} → {accion} → {siguiente} | R={r:.1f} | Política[{estado}]={politica[estado]}")
            estado = siguiente

        print(f"🏁 Recompensa total: {total_r:.1f}")

    print("\n🚗 Política final aprendida:")
    for s in politica:
        print(f"  {s}: {politica[s]}")

if __name__ == "__main__":
    busqueda_politica()
