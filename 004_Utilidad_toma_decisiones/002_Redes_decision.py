
from typing import Dict, Tuple

# Diccionario con las probabilidades de que haya o no tráfico
P_trafico = {"Si": 0.3, "No": 0.7}

 # Diccionario de utilidades: para cada combinación de ruta y tráfico, indica la utilidad (felicidad)
utilidades: Dict[Tuple[str, str], int] = {
    ("Autopista", "Si"): 35,   # rápido pero con peaje + tráfico
    ("Autopista", "No"): 45,   # mejor escenario
    ("Calle", "Si"): 20,       # lento con tráfico
    ("Calle", "No"): 30        # normal y sin costo
}

def utilidad_esperada(ruta: str) -> float:
    """
    Calcula la utilidad esperada para una ruta dada, considerando las probabilidades
    de tráfico y la utilidad de cada escenario.
    """
    u = 0
    for trafico, prob in P_trafico.items():
        u += prob * utilidades[(ruta, trafico)]  # Suma ponderada de utilidades
    return u

def demo_red_decision():
    print("== Redes de Decisión ==")
    rutas = ["Autopista", "Calle"]  # Opciones de ruta

    for r in rutas:
        ue = utilidad_esperada(r)  # Calcula la utilidad esperada para cada ruta
        print(f"Ruta {r}: utilidad esperada = {ue:.2f}")

    # Selecciona la ruta con mayor utilidad esperada
    mejor = max(rutas, key=lambda r: utilidad_esperada(r))
    print(f"\n🚗 Decisión óptima: tomar la {mejor}")

if __name__ == "__main__":
    demo_red_decision()
