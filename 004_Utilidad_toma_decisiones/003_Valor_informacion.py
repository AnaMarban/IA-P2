
from typing import Dict, Tuple

# Diccionario con las probabilidades de que haya o no tráfico
P_trafico = {"Si": 0.3, "No": 0.7}

 # Diccionario de utilidades: para cada combinación de ruta y tráfico, indica la utilidad
utilidades: Dict[Tuple[str, str], int] = {
    ("Autopista", "Si"): 20,   # Autopista con tráfico: mala opción
    ("Autopista", "No"): 50,   # Autopista sin tráfico: excelente
    ("Calle", "Si"): 30,       # Calle con tráfico: estable
    ("Calle", "No"): 35        # Calle sin tráfico: aceptable
}

def utilidad_esperada(ruta: str) -> float:
    """
    Calcula la utilidad esperada de una ruta, sin información adicional sobre el tráfico.
    Suma ponderada de utilidades según la probabilidad de cada escenario.
    """
    return sum(P_trafico[t] * utilidades[(ruta, t)] for t in P_trafico)

def utilidad_con_informacion() -> float:
    """
    Calcula la utilidad esperada si tuviéramos información perfecta sobre el tráfico.
    En cada escenario (con o sin tráfico), se elige la mejor ruta posible.
    """
    # Si hay tráfico, elegimos la mejor ruta para ese caso
    mejor_con_trafico = max(["Autopista", "Calle"], key=lambda r: utilidades[(r, "Si")])
    # Si no hay tráfico, elegimos la mejor ruta para ese caso
    mejor_sin_trafico = max(["Autopista", "Calle"], key=lambda r: utilidades[(r, "No")])

    return (
        P_trafico["Si"] * utilidades[(mejor_con_trafico, "Si")] +
        P_trafico["No"] * utilidades[(mejor_sin_trafico, "No")]
    )

def demo_voi():
    print("== Valor de la Información ==")
    # Calcula la mejor decisión sin información adicional
    sin_info = max(["Autopista", "Calle"], key=lambda r: utilidad_esperada(r))
    ue_sin_info = utilidad_esperada(sin_info)
    # Calcula la utilidad esperada si tuviéramos información perfecta
    ue_con_info = utilidad_con_informacion()
    valor_info = ue_con_info - ue_sin_info

    print(f"Decisión sin información: {sin_info} (utilidad esperada = {ue_sin_info:.2f})")
    print(f"Decisión con información perfecta: utilidad = {ue_con_info:.2f}")
    print(f" Valor de la información = {valor_info:.2f}")

    # Indica si vale la pena obtener la información
    if valor_info > 0:
        print(" Vale la pena obtener la información")
    else:
        print(" No cambia mucho la decisión, no vale la pena pagar por ella.")

if __name__ == "__main__":
    demo_voi()
