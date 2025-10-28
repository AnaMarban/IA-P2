# _RL_Activo.
# GPS Inteligente - Enfoque 5: Aprendizaje por Refuerzo
# Tema - Aprendizaje por Refuerzo Activo

import random
from typing import Dict, Tuple

# Estados y acciones posibles
estados = ["Casa", "Camino", "Hospital"]
acciones = {"Casa": ["Avanzar"], "Camino": ["Avanzar", "Volver"], "Hospital": []}

# Recompensas inmediatas
recompensas = {
    ("Casa", "Avanzar"): 0,
    ("Camino", "Avanzar"): -1,
    ("Camino", "Volver"): -2,
    ("Hospital", None): 10
}

# Transiciones
transiciones: Dict[Tuple[str, str], Tuple[str, float]] = {
    ("Casa", "Avanzar"): ("Camino", 1.0),
    ("Camino", "Avanzar"): ("Hospital", 0.8),  # 80% de llegar
    ("Camino", "Volver"): ("Casa", 1.0)
}

# Parámetros del aprendizaje
GAMMA = 0.9   # factor de descuento
ALFA = 0.1    # tasa de aprendizaje
ITERACIONES = 30

def aprendizaje_activo():
    """El GPS aprende tomando decisiones y actualizando sus utilidades."""
    utilidades = {s: 0 for s in estados}
    politica = {"Casa": "Avanzar", "Camino": "Avanzar"}

    for episodio in range(ITERACIONES):
        estado = "Casa"
        print(f"\n📘 Episodio {episodio + 1}:")
        while estado != "Hospital":
            accion = politica.get(estado)
            if accion is None:
                break

            # Ejecutar acción
            siguiente, prob = transiciones[(estado, accion)]
            recompensa = recompensas[(estado, accion)]

            # Actualizar utilidad (regla de Bellman)
            utilidades[estado] += ALFA * (
                recompensa + GAMMA * utilidades[siguiente] - utilidades[estado]
            )

            # Elegir mejor acción futura
            if estado in politica:
                mejor_accion = max(
                    acciones[estado],
                    key=lambda a: recompensas.get((estado, a), 0)
                    + GAMMA * utilidades.get(transiciones.get((estado, a), (estado, 0))[0], 0)
                )
                politica[estado] = mejor_accion

            print(f"  {estado} → {accion} → {siguiente} | Recompensa: {recompensa} | U({estado})={utilidades[estado]:.2f}")
            estado = siguiente

        print(f"🧭 Política actual: {politica}")

    print("\n🔹 Utilidades finales:")
    for s, u in utilidades.items():
        print(f"  {s}: {u:.2f}")

    print("\n🚗 Política final aprendida:")
    for s, a in politica.items():
        print(f"  En {s}, elige: {a}")

if __name__ == "__main__":
    aprendizaje_activo()
