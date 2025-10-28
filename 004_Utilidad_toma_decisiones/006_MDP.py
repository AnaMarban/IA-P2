
from typing import Dict, List, Tuple

# Lista de estados posibles
estados = ["Casa", "Camino", "Hospital"]
# Diccionario de acciones posibles para cada estado
acciones: Dict[str, List[str]] = {
    "Casa": ["IrCamino"],
    "Camino": ["IrHospital", "VolverCasa"],
    "Hospital": ["Quedarse"]
}

 # Diccionario de recompensas inmediatas para cada estado
recompensas: Dict[str, float] = {
    "Casa": 0,
    "Camino": -1,
    "Hospital": 10
}

 # Diccionario de transiciones: para cada (estado, acción), lista de (siguiente_estado, probabilidad)
transiciones: Dict[Tuple[str, str], List[Tuple[str, float]]] = {
    ("Casa", "IrCamino"): [("Camino", 1.0)],
    ("Camino", "IrHospital"): [("Hospital", 0.8), ("Casa", 0.2)],
    ("Camino", "VolverCasa"): [("Casa", 1.0)],
    ("Hospital", "Quedarse"): [("Hospital", 1.0)]
}

# Parámetros del algoritmo
GAMMA = 0.9        # Factor de descuento: importancia del futuro
ITERACIONES = 10   # Número de iteraciones

def mdp_iteracion_valores():
    """Ejemplo de MDP usando iteración de valores."""
    utilidades = {s: 0 for s in estados}  # Inicializa utilidades en 0

    for i in range(ITERACIONES):
        nuevo_valor = {}  # Diccionario para guardar los nuevos valores de utilidad
        print(f"\n Iteración {i+1}:")
        for s in estados:
            # Para cada acción posible en el estado, calcula su valor esperado
            valores_acciones = []
            for a in acciones[s]:
                # Suma ponderada de utilidades futuras según las probabilidades de transición
                total = sum(prob * utilidades[sig] for sig, prob in transiciones[(s, a)])
                valor_a = recompensas[s] + GAMMA * total  # Valor esperado de la acción
                valores_acciones.append(valor_a)
            # Selecciona la acción con mayor valor esperado
            nuevo_valor[s] = max(valores_acciones)
            print(f"  U({s}) = {nuevo_valor[s]:.3f}")
        utilidades = nuevo_valor  # Actualiza utilidades para la siguiente iteración

    print("\n Utilidades finales:")
    for s, u in utilidades.items():
        print(f"  {s}: {u:.3f}")  # Muestra la utilidad final de cada estado

if __name__ == "__main__":
    mdp_iteracion_valores()
