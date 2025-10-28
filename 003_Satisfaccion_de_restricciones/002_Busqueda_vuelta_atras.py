# GPS Inteligente - Enfoque 3: Satisfacción de Restricciones (CSP)
# Búsqueda de Vuelta Atrás: retrocede (backtrack) si una decisión viola una restricción.

from typing import Dict, List, Tuple, Optional

# Variables del problema: calles/intersecciones que requieren un horario
variables = ["Av1", "Av2", "Parque"]

# Dominios: valores posibles para cada variable (horarios disponibles)
dominios: Dict[str, List[str]] = {
    "Av1": ["8:00", "8:15", "8:30"],
    "Av2": ["8:00", "8:15", "8:30"],
    "Parque": ["8:00", "8:15", "8:30"]
}

# Restricciones binarias: pares que no pueden compartir el mismo horario
restricciones: List[Tuple[str, str]] = [("Av1", "Av2"), ("Av2", "Parque")]


def es_valido(asignacion: Dict[str, str]) -> bool:
    """Comprueba que una asignación parcial/no parcial respete las restricciones.

    Recorre cada restricción y, si ambas variables están asignadas, verifica
    que sus valores no coincidan (condición de exclusión para este ejemplo).
    """
    for (a, b) in restricciones:
        if a in asignacion and b in asignacion:
            if asignacion[a] == asignacion[b]:
                # Violación encontrada
                return False
    return True


def backtracking(asignacion: Dict[str, str]) -> Optional[Dict[str, str]]:
    """Resolver el CSP mediante búsqueda por vuelta atrás (backtracking).

    Algoritmo básico:
    - Si todas las variables están asignadas, devolvemos la asignación completa.
    - Seleccionamos una variable sin asignar y probamos cada valor de su dominio.
    - Tras probar un valor, comprobamos si la asignación parcial es válida. Si lo es,
      recursivamente continuamos; si la recursión encuentra solución la devolvemos.
    - Si ningún valor del dominio sirve, devolvemos None para provocar backtrack.
    """

    # Caso base: todas las variables asignadas
    if len(asignacion) == len(variables):
        return asignacion

    # Seleccionamos la siguiente variable sin asignar (sin heurística aquí)
    var = [v for v in variables if v not in asignacion][0]

    # Probamos cada valor del dominio de 'var'
    for valor in dominios[var]:
        nueva_asig = asignacion.copy()
        nueva_asig[var] = valor

        # Mostrar intención para depuración/visualización
        print(f"Probando {var} = {valor} → {nueva_asig}")

        # Si la asignación parcial es válida, intentamos continuar recursivamente
        if es_valido(nueva_asig):
            resultado = backtracking(nueva_asig)
            if resultado:
                # Si la recursión devuelve una solución, la propagamos hacia arriba
                return resultado

        # Si llegamos aquí, el valor no funcionó: retrocedemos y probamos otro
        print(f"❌ {var} = {valor} no funciona, volviendo atrás...")

    # Ningún valor del dominio condujo a solución -> backtrack
    return None


def demo_backtracking():
    print("== Búsqueda de Vuelta Atrás ==")
    solucion = backtracking({})  # empezamos sin asignaciones
    if solucion:
        print("\n✅ Solución encontrada:")
        for k, v in solucion.items():
            print(f"  {k}: {v}")
    else:
        print("\n🚫 No se encontró solución válida.")


if __name__ == "__main__":
    demo_backtracking()
