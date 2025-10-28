
from typing import Dict, List, Tuple
import random

variables = ["Av1", "Av2", "Parque"]  # Lugares a asignar horario
dominios: Dict[str, List[str]] = {
    "Av1": ["8:00", "8:15", "8:30"],  # Horarios posibles para Av1
    "Av2": ["8:00", "8:15", "8:30"],  # Horarios posibles para Av2
    "Parque": ["8:00", "8:15", "8:30"]  # Horarios posibles para Parque
}

# Restricciones: pares de variables que no pueden compartir el mismo horario
restricciones: List[Tuple[str, str]] = [("Av1", "Av2"), ("Av2", "Parque")]  # Restricciones de incompatibilidad

def conflictos(asignacion: Dict[str, str]) -> List[Tuple[str, str]]:
    """
    Dada una asignación, devuelve una lista de pares de variables que están en conflicto
    (es decir, que tienen el mismo horario y están restringidas).
    """
    conflictos_encontrados = []
    for (a, b) in restricciones:
        if a in asignacion and b in asignacion:
            if asignacion[a] == asignacion[b]:
                conflictos_encontrados.append((a, b))  # Se detecta conflicto
    return conflictos_encontrados

def contar_conflictos(var: str, valor: str, asignacion: Dict[str, str]) -> int:
    """
    Cuenta cuántos conflictos se generarían si se asigna 'valor' a 'var',
    manteniendo el resto de la asignación igual.
    """
    temp = asignacion.copy()
    temp[var] = valor  # Asigna temporalmente el valor
    return len(conflictos(temp))  # Devuelve el número de conflictos resultantes

def minimos_conflictos(
    max_iteraciones: int = 20
) -> Dict[str, str]:
    """Implementa el algoritmo de Mínimos Conflictos."""
    # Asignación inicial aleatoria: se elige un horario al azar para cada variable
    asignacion = {v: random.choice(dominios[v]) for v in variables}
    print(f"Inicio aleatorio: {asignacion}\n")

    for paso in range(max_iteraciones):
        conflictos_act = conflictos(asignacion)  # Busca los conflictos actuales
        if not conflictos_act:
            print(f"✅ Solución encontrada en {paso} pasos.")
            return asignacion  # Si no hay conflictos, retorna la solución

        # Elegir una variable que esté en conflicto (al azar entre los pares conflictivos)
        var_conflictiva = random.choice(random.choice(conflictos_act))

        # Buscar el valor del dominio de esa variable que minimiza los conflictos
        mejor_valor = min(
            dominios[var_conflictiva],
            key=lambda val: contar_conflictos(var_conflictiva, val, asignacion)
        )

        print(f"Paso {paso+1}: {var_conflictiva} cambia a {mejor_valor}")
        asignacion[var_conflictiva] = mejor_valor  # Realiza el cambio

    # Si se llega aquí, no se encontró solución en el número de pasos dado
    print(" No se encontró solución completa.")
    return asignacion

def demo_min_conflicts():
    print("== Búsqueda Local: Mínimos Conflictos ==")
    # Ejecuta el algoritmo de mínimos conflictos y muestra el resultado
    solucion = minimos_conflictos()
    print("\nResultado final:")
    for v, val in solucion.items():
        print(f"  {v}: {val}")  # Muestra la asignación final

if __name__ == "__main__":
    demo_min_conflicts()
