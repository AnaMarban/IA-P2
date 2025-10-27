# GPS Inteligente - Enfoque 3: Satisfacción de Restricciones (CSP)

from typing import Dict, List, Tuple, Optional

# Variables: calles principales que necesitan horario de paso
variables = ["Av1", "Av2", "Parque"]

# Posibles horarios (valores)
dominios: Dict[str, List[str]] = {
    "Av1": ["8:00", "8:15", "8:30"],
    "Av2": ["8:00", "8:15", "8:30"],
    "Parque": ["8:00", "8:15", "8:30"]
}

# Restricciones: pares que no pueden tener el mismo horario
restricciones: List[Tuple[str, str]] = [("Av1", "Av2"), ("Av2", "Parque")]

def es_valido(asignacion: Dict[str, str]) -> bool:
    """Verifica que la asignación no viole las restricciones."""
    for (a, b) in restricciones:
        if a in asignacion and b in asignacion:
            if asignacion[a] == asignacion[b]:
                return False
    return True

def csp_busqueda(asignacion: Dict[str, str]) -> Optional[Dict[str, str]]:
    """Búsqueda básica para resolver CSP (sin heurísticas todavía)."""
    if len(asignacion) == len(variables):
        return asignacion  # todas las variables asignadas

    var = [v for v in variables if v not in asignacion][0]
    for valor in dominios[var]:
        nueva_asig = asignacion.copy()
        nueva_asig[var] = valor
        if es_valido(nueva_asig):
            resultado = csp_busqueda(nueva_asig)
            if resultado:
                return resultado
    return None

def demo_csp():
    print("== Problema de Satisfacción de Restricciones ==")
    solucion = csp_busqueda({})
    if solucion:
        print("Solución encontrada:")
        for k, v in solucion.items():
            print(f"  {k}: {v}")
    else:
        print("No se encontró solución válida.")

if __name__ == "__main__":
    demo_csp()
