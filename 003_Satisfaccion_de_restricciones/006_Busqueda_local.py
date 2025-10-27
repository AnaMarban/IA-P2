# 22_Minimos_Conflictos.
# Búsqueda Local con Mínimos Conflictos: ajusta las variables problemáticas hasta resolver.

from typing import Dict, List, Tuple
import random

# Variables y dominios
variables = ["Av1", "Av2", "Parque"]
dominios: Dict[str, List[str]] = {
    "Av1": ["8:00", "8:15", "8:30"],
    "Av2": ["8:00", "8:15", "8:30"],
    "Parque": ["8:00", "8:15", "8:30"]
}

# Restricciones: no pueden compartir el mismo horario
restricciones: List[Tuple[str, str]] = [("Av1", "Av2"), ("Av2", "Parque")]

def conflictos(asignacion: Dict[str, str]) -> List[Tuple[str, str]]:
    """Devuelve las variables que están en conflicto."""
    conflictos_encontrados = []
    for (a, b) in restricciones:
        if a in asignacion and b in asignacion:
            if asignacion[a] == asignacion[b]:
                conflictos_encontrados.append((a, b))
    return conflictos_encontrados

def contar_conflictos(var: str, valor: str, asignacion: Dict[str, str]) -> int:
    """Cuenta cuántos conflictos genera asignar cierto valor a una variable."""
    temp = asignacion.copy()
    temp[var] = valor
    return len(conflictos(temp))

def minimos_conflictos(
    max_iteraciones: int = 20
) -> Dict[str, str]:
    """Implementa el algoritmo de Mínimos Conflictos."""
    # 1️⃣ Asignación inicial aleatoria
    asignacion = {v: random.choice(dominios[v]) for v in variables}
    print(f"Inicio aleatorio: {asignacion}\n")

    for paso in range(max_iteraciones):
        conflictos_act = conflictos(asignacion)
        if not conflictos_act:
            print(f"✅ Solución encontrada en {paso} pasos.")
            return asignacion

        # 2️⃣ Elegir una variable en conflicto
        var_conflictiva = random.choice(random.choice(conflictos_act))

        # 3️⃣ Buscar el valor con menos conflictos
        mejor_valor = min(dominios[var_conflictiva],
                          key=lambda val: contar_conflictos(var_conflictiva, val, asignacion))

        print(f"Paso {paso+1}: {var_conflictiva} cambia a {mejor_valor}")
        asignacion[var_conflictiva] = mejor_valor

    print("⚠️ No se encontró solución completa.")
    return asignacion

def demo_min_conflicts():
    print("== Búsqueda Local: Mínimos Conflictos ==")
    solucion = minimos_conflictos()
    print("\nResultado final:")
    for v, val in solucion.items():
        print(f"  {v}: {val}")

if __name__ == "__main__":
    demo_min_conflicts()
