# 24_Funcion_Utilidad.
# Tema 24 - Teoría de la Utilidad: Función de Utilidad

from typing import Dict

# Cada ruta tiene factores que influyen en la satisfacción del GPS
rutas: Dict[str, Dict[str, float]] = {
    "A": {"tiempo": 10, "gasolina": 2, "riesgo": 0.1},
    "B": {"tiempo": 8, "gasolina": 3, "riesgo": 0.5},
    "C": {"tiempo": 15, "gasolina": 1, "riesgo": 0.05}
}

# Coeficientes de preferencia (qué tanto le importa cada cosa)
# Estos pueden variar según el “carácter” del GPS 😆
PESO_TIEMPO = -0.5      # le disgusta tardar
PESO_GASOLINA = -1.0    # le duele gastar
PESO_RIESGO = -10.0     # odia el tráfico o el peligro

def utilidad(ruta: Dict[str, float]) -> float:
    """Calcula la utilidad total de una ruta."""
    return (
        (PESO_TIEMPO * ruta["tiempo"]) +
        (PESO_GASOLINA * ruta["gasolina"]) +
        (PESO_RIESGO * ruta["riesgo"]) + 50  # constante base de felicidad 😄
    )

def demo_utilidad():
    print("== Teoría de la Utilidad – Función de Utilidad ==")
    utilidades = {}
    for nombre, datos in rutas.items():
        u = utilidad(datos)
        utilidades[nombre] = u
        print(f"Ruta {nombre}: utilidad = {u:.2f}")

    mejor_ruta = max(utilidades, key=utilidades.get)
    print(f"\n🚗 Mejor decisión: tomar la ruta {mejor_ruta} con utilidad {utilidades[mejor_ruta]:.2f}")

if __name__ == "__main__":
    demo_utilidad()
