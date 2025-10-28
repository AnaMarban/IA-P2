# GPS Inteligente - Enfoque 3: Satisfacción de Restricciones (CSP)

from typing import Dict, List, Tuple, Optional

# Variables del CSP: representan calles o intersecciones que necesitan
# un horario asignado (por ejemplo, para paso de tráfico o semáforos)
variables = ["Av1", "Av2", "Parque"]

# Dominios: valores posibles para cada variable (horarios disponibles)
dominios: Dict[str, List[str]] = {
    "Av1": ["8:00", "8:15", "8:30"],
    "Av2": ["8:00", "8:15", "8:30"],
    "Parque": ["8:00", "8:15", "8:30"]
}

# Restricciones binarias: pares de variables que NO pueden tener el mismo valor
# (por ejemplo, no permitir que Av1 y Av2 estén sincronizadas al mismo horario)
restricciones: List[Tuple[str, str]] = [("Av1", "Av2"), ("Av2", "Parque")]


def es_valido(asignacion: Dict[str, str]) -> bool:
    """Comprueba si la asignación parcial/no parcial cumple las restricciones.

    - asignacion: diccionario variable->valor con las asignaciones ya fijadas.
    - Recorre las restricciones definidas y devuelve False si alguna se viola.
    """
    for (a, b) in restricciones:
        # Sólo comprobamos la restricción si ambas variables ya están asignadas
        if a in asignacion and b in asignacion:
            if asignacion[a] == asignacion[b]:
                # Violación: ambas tienen el mismo horario prohibido
                return False
    return True


def csp_busqueda(asignacion: Dict[str, str]) -> Optional[Dict[str, str]]:
    """Resolver el CSP mediante búsqueda por backtracking simple.

    Estrategia:
    - Si todas las variables están asignadas, devolvemos la solución.
    - Seleccionamos la siguiente variable sin asignar (sin heurística aquí).
    - Probamos cada valor del dominio; si la asignación parcial es válida,
      hacemos una llamada recursiva (backtracking).
    - Si alguna rama devuelve solución, la propagamos hacia arriba.
    """
    # Caso base: todas las variables ya tienen un valor
    if len(asignacion) == len(variables):
        return asignacion

    # Elegimos la siguiente variable sin asignar (podríamos mejorar con heurísticas)
    var = [v for v in variables if v not in asignacion][0]

    # Probamos cada valor posible del dominio de 'var'
    for valor in dominios[var]:
        nueva_asig = asignacion.copy()
        nueva_asig[var] = valor

        # Si la asignación parcial es válida, continuamos recursivamente
        if es_valido(nueva_asig):
            resultado = csp_busqueda(nueva_asig)
            if resultado:
                return resultado

    # Si ningún valor conduce a solución, devolvemos None (backtrack)
    return None


def demo_csp():
    print("== Problema de Satisfacción de Restricciones ==")
    solucion = csp_busqueda({})  # empezamos sin asignaciones
    if solucion:
        print("Solución encontrada:")
        for k, v in solucion.items():
            print(f"  {k}: {v}")
    else:
        print("No se encontró solución válida.")


if __name__ == "__main__":
    demo_csp()
