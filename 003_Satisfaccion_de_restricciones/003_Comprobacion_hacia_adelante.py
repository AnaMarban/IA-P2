

from typing import Dict, List, Tuple, Optional
import copy

# --- Definición de variables y dominios ---
# Lista de variables (lugares a asignar)
variables = ["Av1", "Av2", "Parque"]  # Nombres de los lugares a asignar horario

# Dominios iniciales: horarios posibles para cada variable
dominios_iniciales: Dict[str, List[str]] = {
    "Av1": ["8:00", "8:15", "8:30"],  # Horarios posibles para Av1
    "Av2": ["8:00", "8:15", "8:30"],  # Horarios posibles para Av2
    "Parque": ["8:00", "8:15", "8:30"]  # Horarios posibles para Parque
}

# Restricciones binarias: pares de variables que no pueden tener el mismo valor
# aquí: Av1 no puede coincidir con Av2; Av2 no puede coincidir con Parque
restricciones: List[Tuple[str, str]] = [("Av1", "Av2"), ("Av2", "Parque")]  # Restricciones de incompatibilidad


def es_valido(asignacion: Dict[str, str]) -> bool:
    """Comprueba si una asignación parcial respeta las restricciones.

    Parámetros:
    - asignacion: diccionario variable->valor con las asignaciones actuales.

    Devuelve True si no hay pares en conflicto, False en caso contrario.
    """
    # Recorremos todas las restricciones y verificamos si ambas variables
    # están asignadas y si tienen el mismo valor (lo cual sería conflicto).
    for (a, b) in restricciones:
        if a in asignacion and b in asignacion:
            # Si ambas variables ya tienen horario asignado y es el mismo, hay conflicto
            if asignacion[a] == asignacion[b]:
                return False  # No es válido
    # Si no encontramos conflictos, la asignación es válida
    return True


def forward_check(asignacion: Dict[str, str], dominios: Dict[str, List[str]]) -> Optional[Dict[str, str]]:
    """Algoritmo de búsqueda con comprobación hacia delante (forward checking).

    - asignacion: asignaciones parciales actuales (variable->valor).
    - dominios: dominios actuales por variable (se modifican en la recursión).

    Retorna una asignación completa válida si se encuentra, o None si no hay solución.
    """
    # Caso base: si ya asignamos todas las variables, devolvemos la solución
    if len(asignacion) == len(variables):
        return asignacion  # Si ya están todas asignadas, retornamos la solución


    # Elegimos la primera variable que aún no ha sido asignada
    var = [v for v in variables if v not in asignacion][0]

    # Probamos cada valor posible para la variable seleccionada
    for valor in dominios[var]:
        # Copiamos la asignación actual y agregamos la nueva variable
        nueva_asig = asignacion.copy()
        nueva_asig[var] = valor  # Asignamos el valor a la variable

        # Verificamos si la asignación parcial es válida
        if not es_valido(nueva_asig):
            # Si no es válida, probamos el siguiente valor
            continue

        # Clonamos los dominios para no modificar los originales en otras ramas
        nuevos_dominios = copy.deepcopy(dominios)

        # Aplicamos comprobación hacia delante: eliminamos el valor asignado
        # de los dominios de las variables relacionadas por restricción
        for (a, b) in restricciones:
            if a == var and b not in nueva_asig:
                # Si 'var' es la primera variable de la restricción y la otra no está asignada
                if valor in nuevos_dominios[b]:
                    nuevos_dominios[b].remove(valor)  # Quitamos el valor del dominio
                    print(f"⛔ Eliminando {valor} del dominio de {b}")
            elif b == var and a not in nueva_asig:
                # Si 'var' es la segunda variable de la restricción y la otra no está asignada
                if valor in nuevos_dominios[a]:
                    nuevos_dominios[a].remove(valor)
                    print(f"⛔ Eliminando {valor} del dominio de {a}")

        # Mostramos la asignación tentativa y los dominios resultantes
        print(f" Asignando {var} = {valor}")
        print(f"   Dominios actualizados: {nuevos_dominios}\n")

        # Si algún dominio queda vacío, no hay solución por este camino
        if all(len(vals) > 0 for vals in nuevos_dominios.values()):
            # Llamada recursiva con la nueva asignación y dominios
            resultado = forward_check(nueva_asig, nuevos_dominios)
            if resultado:
                # Si encontramos solución, la devolvemos
                return resultado

        # Si llegamos aquí, el valor probado no lleva a solución
        print(f"❌ {var} = {valor} conduce a calle sin opciones, retrocediendo...\n")

    # Si ningún valor funcionó, devolvemos None para indicar fracaso en esta rama
    return None


def demo_forward():
    """Función demo que ejecuta el algoritmo desde el estado inicial."""
    print("== Comprobación Hacia Delante ==")
    # Ejecutamos el algoritmo con una copia de los dominios iniciales
    solucion = forward_check({}, copy.deepcopy(dominios_iniciales))
    if solucion:
        print("\n Solución encontrada:")
        for k, v in solucion.items():
            print(f"  {k}: {v}")  # Mostramos la solución final
    else:
        print("\n No se encontró solución válida.")


if __name__ == "__main__":
    demo_forward()
