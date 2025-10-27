# 26_Valor_Informacion.
# Tema 26 - Valor de la Información (VOI)

from typing import Dict, Tuple

# Probabilidades del tráfico
P_trafico = {"Si": 0.3, "No": 0.7}

# Utilidades según ruta y condición
utilidades: Dict[Tuple[str, str], int] = {
    ("Autopista", "Si"): 20,   # mala si hay tráfico
    ("Autopista", "No"): 50,   # excelente si no hay tráfico
    ("Calle", "Si"): 30,       # estable aunque haya tráfico
    ("Calle", "No"): 35
}

def utilidad_esperada(ruta: str) -> float:
    """Calcula la utilidad esperada sin información adicional."""
    return sum(P_trafico[t] * utilidades[(ruta, t)] for t in P_trafico)

def utilidad_con_informacion() -> float:
    """
    Calcula la utilidad esperada si supiéramos
    de antemano si hay tráfico (decisión informada).
    """
    # Si hay tráfico → elegimos la mejor ruta en ese escenario
    mejor_con_trafico = max(["Autopista", "Calle"], key=lambda r: utilidades[(r, "Si")])
    mejor_sin_trafico = max(["Autopista", "Calle"], key=lambda r: utilidades[(r, "No")])

    return (
        P_trafico["Si"] * utilidades[(mejor_con_trafico, "Si")] +
        P_trafico["No"] * utilidades[(mejor_sin_trafico, "No")]
    )

def demo_voi():
    print("== Valor de la Información ==")
    sin_info = max(["Autopista", "Calle"], key=lambda r: utilidad_esperada(r))
    ue_sin_info = utilidad_esperada(sin_info)
    ue_con_info = utilidad_con_informacion()
    valor_info = ue_con_info - ue_sin_info

    print(f"Decisión sin información: {sin_info} (utilidad esperada = {ue_sin_info:.2f})")
    print(f"Decisión con información perfecta: utilidad = {ue_con_info:.2f}")
    print(f"💡 Valor de la información = {valor_info:.2f}")

    if valor_info > 0:
        print("✅ Vale la pena obtener la información (por ejemplo, revisar el tráfico).")
    else:
        print("⚠️ No cambia mucho la decisión, no vale la pena pagar por ella.")

if __name__ == "__main__":
    demo_voi()
