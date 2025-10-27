# 28_Iteracion_Politicas.
# Tema 28 - Iteración de Políticas (Policy Iteration)

from typing import Dict, List, Tuple

# Estados
estados = ["Casa", "Camino", "Hospital"]

# Recompensas
recompensas = {
    "Casa": 0,
    "Camino": -1,
    "Hospital": 10
}

# Transiciones por acción (probabilidad, siguiente_estado)
transiciones = {
    "Casa": {
        "IrCamino": [("Camino", 1.0)]
    },
    "Camino": {
        "IrHospital": [("Hospital", 0.8), ("Casa", 0.2)],
        "VolverCasa": [("Casa", 1.0)]
    },
    "Hospital": {
        "Quedarse": [("Hospital", 1.0)]
    }
}

GAMMA = 0.9
THETA = 0.001  # precisión mínima de mejora

def evaluar_politica(politica: Dict[str, str], utilidades: Dict[str, float]) -> Dict[str, float]:
    """Evalúa la política actual hasta que converja."""
    while True:
        delta = 0
        nuevo_u = utilidades.copy()
        for s in estados:
            a = politica[s]
            nuevo_u[s] = recompensas[s] + GAMMA * sum(
                prob * utilidades[sig] for (sig, prob) in transiciones[s][a]
            )
            delta = max(delta, abs(nuevo_u[s] - utilidades[s]))
        utilidades = nuevo_u
        if delta < THETA:
            break
    return utilidades

def mejorar_politica(utilidades: Dict[str, float], politica: Dict[str, str]) -> Tuple[Dict[str, str], bool]:
    """Mejora la política actual según las utilidades."""
    estable = True
    nueva_politica = politica.copy()
    for s in estados:
        acciones = transiciones[s].keys()
        # Evaluar qué acción da la mayor utilidad
        mejor_accion = max(
            acciones,
            key=lambda a: sum(prob * utilidades[sig] for (sig, prob) in transiciones[s][a])
        )
        if mejor_accion != politica[s]:
            estable = False
        nueva_politica[s] = mejor_accion
    return nueva_politica, estable

def iteracion_politicas():
    """Algoritmo principal de Policy Iteration."""
    # Política inicial (puede ser aleatoria)
    politica = {
        "Casa": "IrCamino",
        "Camino": "IrHospital",
        "Hospital": "Quedarse"
    }
    utilidades = {s: 0 for s in estados}

    iteracion = 1
    while True:
        print(f"\n📘 Iteración de política #{iteracion}")
        utilidades = evaluar_politica(politica, utilidades)
        politica, estable = mejorar_politica(utilidades, politica)

        print("Utilidades:", {s: round(utilidades[s], 3) for s in estados})
        print("Política:", politica)

        if estable:
            print("\n✅ Política estable: se alcanzó la política óptima.")
            break
        iteracion += 1

if __name__ == "__main__":
    iteracion_politicas()
