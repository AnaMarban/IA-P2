
from typing import Dict, List, Tuple

# Lista de estados posibles
estados = ["Casa", "Camino", "Hospital"]

 # Diccionario de recompensas inmediatas para cada estado
recompensas = {
    "Casa": 0,
    "Camino": -1,
    "Hospital": 10
}

 # Diccionario de transiciones: para cada estado y acción, lista de (siguiente_estado, probabilidad)
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

# Parámetros del algoritmo
GAMMA = 0.9         # Factor de descuento: importancia del futuro
THETA = 0.001       # Precisión mínima para considerar convergencia

def evaluar_politica(politica: Dict[str, str], utilidades: Dict[str, float]) -> Dict[str, float]:
    """
    Evalúa la política actual: calcula las utilidades de cada estado siguiendo la política dada,
    hasta que los valores converjan (cambien menos que THETA).
    """
    while True:
        delta = 0
        nuevo_u = utilidades.copy()
        for s in estados:
            a = politica[s]  # Acción que indica la política para este estado
            # Suma de recompensas inmediatas y utilidades futuras esperadas
            nuevo_u[s] = recompensas[s] + GAMMA * sum(
                prob * utilidades[sig] for (sig, prob) in transiciones[s][a]
            )
            delta = max(delta, abs(nuevo_u[s] - utilidades[s]))
        utilidades = nuevo_u
        if delta < THETA:
            break
    return utilidades

def mejorar_politica(utilidades: Dict[str, float], politica: Dict[str, str]) -> Tuple[Dict[str, str], bool]:
    """
    Mejora la política actual: para cada estado, elige la acción que maximiza la utilidad esperada.
    Devuelve la nueva política y un indicador de si hubo cambios (si es estable).
    """
    estable = True
    nueva_politica = politica.copy()
    for s in estados:
        acciones = transiciones[s].keys()
        # Busca la acción que da mayor utilidad esperada
        mejor_accion = max(
            acciones,
            key=lambda a: sum(prob * utilidades[sig] for (sig, prob) in transiciones[s][a])
        )
        if mejor_accion != politica[s]:
            estable = False  # Si cambia alguna acción, la política no es estable
        nueva_politica[s] = mejor_accion
    return nueva_politica, estable

def iteracion_politicas():
    """
    Algoritmo principal de iteración de políticas (Policy Iteration).
    Alterna entre evaluar la política actual y mejorarla hasta que sea óptima.
    """
    # Política inicial (puede ser aleatoria o fija)
    politica = {
        "Casa": "IrCamino",
        "Camino": "IrHospital",
        "Hospital": "Quedarse"
    }
    utilidades = {s: 0 for s in estados}  # Inicializa utilidades en 0

    iteracion = 1
    while True:
        print(f"\n Iteración de política #{iteracion}")
        utilidades = evaluar_politica(politica, utilidades)  # Evalúa la política actual
        politica, estable = mejorar_politica(utilidades, politica)  # Mejora la política

        print("Utilidades:", {s: round(utilidades[s], 3) for s in estados})
        print("Política:", politica)

        if estable:
            print("\n Política estable: se alcanzó la política óptima.")
            break
        iteracion += 1

if __name__ == "__main__":
    iteracion_politicas()
