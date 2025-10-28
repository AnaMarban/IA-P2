
from typing import Dict, List, Tuple

# Lista de estados posibles
estados = ["Casa", "Camino", "Hospital"]

# Lista de acciones disponibles
acciones = ["Avanzar", "Esperar"]

 # Diccionario de recompensas inmediatas para cada estado
recompensa = {
    "Casa": 0,
    "Camino": -1,
    "Hospital": 10
}

 # Diccionario de transiciones: para cada (estado, acción), lista de (siguiente_estado, probabilidad)
transiciones: Dict[Tuple[str, str], List[Tuple[str, float]]] = {
    ("Casa", "Avanzar"): [("Camino", 1.0)],
    ("Camino", "Avanzar"): [("Hospital", 0.8), ("Casa", 0.2)],
    ("Camino", "Esperar"): [("Camino", 1.0)],
    ("Hospital", "Esperar"): [("Hospital", 1.0)]
}

 # Diccionario de probabilidades de observación: para cada estado, probabilidad de cada observación
observaciones: Dict[str, Dict[str, float]] = {
    "Casa": {"Silencio": 0.8, "Ambulancia": 0.1, "Motor": 0.1},
    "Camino": {"Silencio": 0.3, "Ambulancia": 0.3, "Motor": 0.4},
    "Hospital": {"Silencio": 0.1, "Ambulancia": 0.8, "Motor": 0.1}
}

# Creencia inicial: distribución de probabilidad sobre los estados
creencia = {"Casa": 1.0, "Camino": 0.0, "Hospital": 0.0}

def actualizar_creencia(creencia: Dict[str, float], accion: str, observacion: str) -> Dict[str, float]:
    """
    Actualiza la creencia del GPS (distribución de probabilidad sobre los estados)
    según la acción tomada y la observación recibida.
    """
    nueva_creencia = {}
    for s_prime in estados:
        total = 0
        for s in estados:
            # Probabilidad de llegar a s_prime desde s con la acción dada
            trans = [prob for (dest, prob) in transiciones.get((s, accion), []) if dest == s_prime]
            prob_trans = trans[0] if trans else 0
            total += creencia[s] * prob_trans
        # Multiplica por la probabilidad de observar lo que se observó en s_prime
        nueva_creencia[s_prime] = observaciones[s_prime][observacion] * total

    # Normaliza la creencia para que sume 1
    normalizador = sum(nueva_creencia.values())
    for s in estados:
        nueva_creencia[s] /= normalizador if normalizador > 0 else 1
    return nueva_creencia

def demo_pomdp():
    print("== POMDP: Decisiones bajo incertidumbre ==")
    print(f"Creencia inicial: {creencia}\n")

    # Secuencia de acciones y observaciones simuladas
    secuencia = [("Avanzar", "Motor"), ("Avanzar", "Ambulancia")]

    belief = creencia.copy()  # Copia de la creencia inicial
    for (accion, obs) in secuencia:
        belief = actualizar_creencia(belief, accion, obs)  # Actualiza la creencia
        print(f"Acción: {accion}, Observación: {obs}")
        print(f" Nueva creencia: {belief}\n")  # Muestra la creencia actualizada

if __name__ == "__main__":
    demo_pomdp()
