# 29_MDP.
# GPS Inteligente - Enfoque 4: Utilidad y Toma de Decisiones
# Tema 29 - Proceso de Decisión de Markov (MDP)

from typing import Dict, List, Tuple

# Estados y acciones
estados = ["Casa", "Camino", "Hospital"]
acciones: Dict[str, List[str]] = {
    "Casa": ["IrCamino"],
    "Camino": ["IrHospital", "VolverCasa"],
    "Hospital": ["Quedarse"]
}

# Recompensas inmediatas
recompensas: Dict[str, float] = {
    "Casa": 0,
    "Camino": -1,
    "Hospital": 10
}

# Probabilidades de transición P(s'|s,a)
# Ejemplo: desde Camino, con IrHospital hay 0.8 de llegar al Hospital y 0.2 de volver a Casa
transiciones: Dict[Tuple[str, str], List[Tuple[str, float]]] = {
    ("Casa", "IrCamino"): [("Camino", 1.0)],
    ("Camino", "IrHospital"): [("Hospital", 0.8), ("Casa", 0.2)],
    ("Camino", "VolverCasa"): [("Casa", 1.0)],
    ("Hospital", "Quedarse"): [("Hospital", 1.0)]
}

# Parámetros
GAMMA = 0.9
ITERACIONES = 10

def mdp_iteracion_valores():
    """Ejemplo de MDP usando iteración de valores."""
    utilidades = {s: 0 for s in estados}

    for i in range(ITERACIONES):
        nuevo_valor = {}
        print(f"\n📘 Iteración {i+1}:")
        for s in estados:
            # Para cada acción, calculamos su valor esperado
            valores_acciones = []
            for a in acciones[s]:
                total = sum(prob * utilidades[sig] for sig, prob in transiciones[(s, a)])
                valor_a = recompensas[s] + GAMMA * total
                valores_acciones.append(valor_a)
            nuevo_valor[s] = max(valores_acciones)
            print(f"  U({s}) = {nuevo_valor[s]:.3f}")
        utilidades = nuevo_valor

    print("\n🔹 Utilidades finales:")
    for s, u in utilidades.items():
        print(f"  {s}: {u:.3f}")

if __name__ == "__main__":
    mdp_iteracion_valores()
