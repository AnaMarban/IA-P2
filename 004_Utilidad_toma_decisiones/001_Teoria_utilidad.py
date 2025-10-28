
from typing import Dict

 # Diccionario de rutas, cada una con sus factores: tiempo, gasolina y riesgo
rutas: Dict[str, Dict[str, float]] = {
    "A": {"tiempo": 10, "gasolina": 2, "riesgo": 0.1},
    "B": {"tiempo": 8, "gasolina": 3, "riesgo": 0.5},
    "C": {"tiempo": 15, "gasolina": 1, "riesgo": 0.05}
}

# Coeficientes de preferencia: indican cuánto pesa cada factor en la utilidad
# (pueden variar según el usuario o el "carácter" del GPS)
PESO_TIEMPO = -0.5      # Penaliza el tiempo (negativo porque menos es mejor)
PESO_GASOLINA = -1.0    # Penaliza el gasto de gasolina
PESO_RIESGO = -10.0     # Penaliza el riesgo (tráfico/peligro)

def utilidad(ruta: Dict[str, float]) -> float:
    """
    Calcula la utilidad total de una ruta sumando los factores ponderados.
    Un valor más alto indica una ruta más conveniente según las preferencias.
    """
    return (
        (PESO_TIEMPO * ruta["tiempo"]) +
        (PESO_GASOLINA * ruta["gasolina"]) +
        (PESO_RIESGO * ruta["riesgo"]) + 50  # constante base de felicidad
    )

def demo_utilidad():
    print("== Teoría de la Utilidad – Función de Utilidad ==")
    utilidades = {}  # Diccionario para guardar la utilidad de cada ruta
    for nombre, datos in rutas.items():
        u = utilidad(datos)  # Calcula la utilidad de la ruta
        utilidades[nombre] = u
        print(f"Ruta {nombre}: utilidad = {u:.2f}")  # Muestra la utilidad calculada

    # Selecciona la ruta con mayor utilidad
    mejor_ruta = max(utilidades, key=utilidades.get)
    print(f"\n Mejor decisión: tomar la ruta {mejor_ruta} con utilidad {utilidades[mejor_ruta]:.2f}")

if __name__ == "__main__":
    demo_utilidad()
