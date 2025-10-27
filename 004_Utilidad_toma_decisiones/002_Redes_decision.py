# 25_Redes_Decision.
# Tema 25 - Redes de Decisión: combinación de decisiones, azar y utilidad

from typing import Dict, Tuple

# Probabilidades del tráfico
P_trafico = {"Si": 0.3, "No": 0.7}

# Utilidades en puntos de felicidad del GPS
# (mientras más alto, mejor)
# Formato: (Ruta, Trafico) : Utilidad
utilidades: Dict[Tuple[str, str], int] = {
    ("Autopista", "Si"): 35,   # rápido pero con peaje + tráfico
    ("Autopista", "No"): 45,   # mejor escenario
    ("Calle", "Si"): 20,       # lento con tráfico
    ("Calle", "No"): 30        # normal y sin costo
}

def utilidad_esperada(ruta: str) -> float:
    """Calcula la utilidad esperada para una ruta dada."""
    u = 0
    for trafico, prob in P_trafico.items():
        u += prob * utilidades[(ruta, trafico)]
    return u

def demo_red_decision():
    print("== Redes de Decisión ==")
    rutas = ["Autopista", "Calle"]

    for r in rutas:
        ue = utilidad_esperada(r)
        print(f"Ruta {r}: utilidad esperada = {ue:.2f}")

    mejor = max(rutas, key=lambda r: utilidad_esperada(r))
    print(f"\n🚗 Decisión óptima: tomar la {mejor}")

if __name__ == "__main__":
    demo_red_decision()
