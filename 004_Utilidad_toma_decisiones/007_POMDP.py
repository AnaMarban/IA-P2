# 30_POMDP.
# GPS Inteligente - Enfoque 4: Utilidad y Toma de Decisiones
# Tema 30 - POMDP (Proceso de Decisión de Markov Parcialmente Observable)

from typing import Dict, List, Tuple

# Estados posibles
estados = ["Casa", "Camino", "Hospital"]

# Acciones disponibles
acciones = ["Avanzar", "Esperar"]

# Recompensas
recompensa = {
    "Casa": 0,
    "Camino": -1,
    "Hospital": 10
}

# Transiciones: P(s'|s,a)
transiciones: Dict[Tuple[str, str], List[Tuple[str, float]]] = {
    ("Casa", "Avanzar"): [("Camino", 1.0)],
    ("Camino", "Avanzar"): [("Hospital", 0.8), ("Casa", 0.2)],
    ("Camino", "Esperar"): [("Camino", 1.0)],
    ("Hospital", "Esperar"): [("Hospital", 1.0)]
}

# Probabilidades de observación P(o|s)
observaciones: Dict[str, Dict[str, float]] = {
    "Casa": {"Silencio": 0.8, "Ambulancia": 0.1, "Motor": 0.1},
    "Camino": {"Silencio": 0.3, "Ambulancia": 0.3, "Motor": 0.4},
    "Hospital": {"Silencio": 0.1, "Ambulancia": 0.8, "Motor": 0.1}
}

# Creencia inicial (lo que el GPS cree)
creencia = {"Casa": 1.0, "Camino": 0.0, "Hospital": 0.0}

def actualizar_creencia(creencia: Dict[str, float], accion: str, observacion: str) -> Dict[str, float]:
    """Actualiza la creencia del GPS según la acción tomada y lo que observa."""
    nueva_creencia = {}
    for s_prime in estados:
        total = 0
        for s in estados:
            trans = [prob for (dest, prob) in transiciones.get((s, accion), []) if dest == s_prime]
            prob_trans = trans[0] if trans else 0
            total += creencia[s] * prob_trans
        # Multiplicar por probabilidad de observación
        nueva_creencia[s_prime] = observaciones[s_prime][observacion] * total

    # Normalizar
    normalizador = sum(nueva_creencia.values())
    for s in estados:
        nueva_creencia[s] /= normalizador if normalizador > 0 else 1
    return nueva_creencia

def demo_pomdp():
    print("== POMDP: Decisiones bajo incertidumbre ==")
    print(f"Creencia inicial: {creencia}\n")

    # Simular observaciones
    secuencia = [("Avanzar", "Motor"), ("Avanzar", "Ambulancia")]

    belief = creencia.copy()
    for (accion, obs) in secuencia:
        belief = actualizar_creencia(belief, accion, obs)
        print(f"Acción: {accion}, Observación: {obs}")
        print(f"➡️ Nueva creencia: {belief}\n")

if __name__ == "__main__":
    demo_pomdp()
