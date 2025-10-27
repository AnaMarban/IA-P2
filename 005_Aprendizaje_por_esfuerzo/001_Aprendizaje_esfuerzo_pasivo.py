# 33_RL_Pasivo.
# GPS Inteligente - Enfoque 5: Aprendizaje por Refuerzo
# Aprendizaje por Refuerzo Pasivo

from typing import Dict, List, Tuple

# Estados y transiciones
estados = ["Casa", "Camino", "Hospital"]
transiciones: Dict[str, List[Tuple[str, float]]] = {
    "Casa": [("Camino", 1.0)],
    "Camino": [("Hospital", 0.8), ("Casa", 0.2)],
    "Hospital": [("Hospital", 1.0)]
}

# Recompensas inmediatas
recompensas = {"Casa": 0, "Camino": -1, "Hospital": 10}

# Política fija (el GPS observa esta estrategia)
politica = {"Casa": "Camino", "Camino": "Hospital", "Hospital": "Hospital"}

# Parámetros
GAMMA = 0.9   # factor de descuento
ALFA = 0.1    # tasa de aprendizaje
ITERACIONES = 20

def aprendizaje_pasivo():
    """Simula el aprendizaje pasivo observando una política fija."""
    utilidades = {s: 0 for s in estados}

    for i in range(ITERACIONES):
        print(f"\n📘 Episodio {i+1}:")
        estado = "Casa"
        secuencia = [estado]
        total_recompensa = 0

        # Simular un trayecto siguiendo la política
        while estado != "Hospital":
            siguiente = politica[estado]
            # Escoger transición según probabilidad
            if estado == "Camino":
                # 80% chance de llegar al Hospital, 20% de volver a Casa
                estado = "Hospital" if i % 5 != 0 else "Casa"
            else:
                estado = siguiente
            secuencia.append(estado)
            total_recompensa += recompensas[estado]

        # Actualizar utilidad de cada estado en la secuencia
        for s in secuencia:
            utilidades[s] += ALFA * (total_recompensa - utilidades[s])
        print(f"  Trayecto: {secuencia}")
        print(f"  Recompensa total: {total_recompensa}")
        print(f"  Utilidades actuales: {utilidades}")

    print("\n🔹 Utilidades finales estimadas:")
    for s, u in utilidades.items():
        print(f"  {s}: {u:.2f}")

if __name__ == "__main__":
    aprendizaje_pasivo()
