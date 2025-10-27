# GPS Inteligente - Enfoque 3: Satisfacción de Restricciones (CSP)
# Búsqueda de Vuelta Atrás: retrocede si una decisión viola una regla.

from typing import Dict, List, Tuple, Optional

# Variables: calles que necesitan horario
variables = ["Av1", "Av2", "Parque"]

# Dominios: posibles horarios
dominios: Dict[str, List[str]] = {
    "Av1": ["8:00", "8:15", "8:30"],
    "Av2": ["8:00", "8:15", "8:30"],
    "Parque": ["8:00", "8:15", "8:30"]
}

# Restricciones: calles que no pueden compartir el mismo horario
restricciones: List[Tuple[str, str]] = [("Av1", "Av2"), ("Av2", "Parque")]

def es_valido(asignacion: Dict[str, str]) -> bool:
    """Verifica que no se violen restricciones."""
    for (a, b) in restricciones:
        if a in asignacion and b in asignacion:
            if asignacion[a] == asignacion[b]:
                return False
    return True

def backtracking(asignacion: Dict[str, str]) -> Optional[Dict[str, str]]:
    """Búsqueda de Vuelta Atrás."""
    # Si todas las variables están asignadas → solución completa
    if len(asignacion) == len(variables):
        return asignacion

    # Elegir la siguiente variable sin asignar
    var = [v for v in variables if v not in asignacion][0]

    for valor in dominios[var]:
        nueva_asig = asignacion.copy()
        nueva_asig[var] = valor

        print(f"Probando {var} = {valor} → {nueva_asig}")

        # Si es válida, seguimos
        if es_valido(nueva_asig):
            resultado = backtracking(nueva_asig)
            if resultado:
                return resultado  # Solución encontrada

        # Si no es válida, retrocedemos
        print(f"❌ {var} = {valor} no funciona, volviendo atrás...")

    return None  # Ningún valor válido → retrocede más

def demo_backtracking():
    print("== Búsqueda de Vuelta Atrás ==")
    solucion = backtracking({})
    if solucion:
        print("\n✅ Solución encontrada:")
        for k, v in solucion.items():
            print(f"  {k}: {v}")
    else:
        print("\n🚫 No se encontró solución válida.")

if __name__ == "__main__":
    demo_backtracking()
