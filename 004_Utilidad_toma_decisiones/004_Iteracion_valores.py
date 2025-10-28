
from typing import Dict, Tuple

# Lista de estados posibles en el sistema (ejemplo: GPS)
estados = ["Casa", "Camino", "Hospital"]

 # Diccionario de recompensas inmediatas para cada estado
recompensa: Dict[str, float] = {
    "Casa": 0,
    "Camino": -1,
    "Hospital": 10
}

 # Diccionario de transiciones: para cada estado, lista de (siguiente_estado, probabilidad)
transiciones: Dict[str, list] = {
    "Casa": [("Camino", 1.0)],
    "Camino": [("Hospital", 0.8), ("Casa", 0.2)],
    "Hospital": [("Hospital", 1.0)]  # estado terminal
}

# Parámetros de aprendizaje
GAMMA = 0.9      # Factor de descuento: importancia del futuro
ITERACIONES = 10 # Número de iteraciones del algoritmo

def iteracion_valores():
    """Implementación simple del algoritmo de Value Iteration."""
    utilidades = {s: 0 for s in estados}  # Inicializa utilidades en 0

    for i in range(ITERACIONES):
        nuevo_valor = {}  # Diccionario para guardar los nuevos valores de utilidad
        print(f"\n Iteración {i+1}:")
        for s in estados:
            # Si es estado terminal, su utilidad es su recompensa
            if s == "Hospital":
                nuevo_valor[s] = recompensa[s]
                continue

            # Calcular utilidad esperada para el estado actual
            total = 0
            for (sig, prob) in transiciones[s]:
                total += prob * utilidades[sig]  # Suma ponderada de utilidades futuras
            nuevo_valor[s] = recompensa[s] + GAMMA * total  # Actualiza utilidad
            print(f"  U({s}) = {nuevo_valor[s]:.3f}")

        utilidades = nuevo_valor  # Actualiza utilidades para la siguiente iteración

    print("\n Utilidades finales:")
    for s, u in utilidades.items():
        print(f"  {s}: {u:.3f}")  # Muestra la utilidad final de cada estado

if __name__ == "__main__":
    iteracion_valores()
