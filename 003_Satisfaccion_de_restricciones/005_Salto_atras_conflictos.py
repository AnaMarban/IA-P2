
from typing import Dict, List, Tuple, Optional

# Lista de variables (lugares) a los que se les asignará un horario
variables = ["Av1", "Av2", "Parque"]

# Diccionario con los horarios posibles para cada variable
dominios: Dict[str, List[str]] = {
    "Av1": ["8:00", "8:15", "8:30"],
    "Av2": ["8:00", "8:15", "8:30"],
    "Parque": ["8:00", "8:15", "8:30"]
}

# Restricciones binarias: pares de variables que no pueden tener el mismo horario
restricciones: List[Tuple[str, str]] = [("Av1", "Av2"), ("Av2", "Parque")]  # Cada tupla indica que esas dos variables no pueden coincidir

def conflicto(var: str, valor: str, asignacion: Dict[str, str]) -> Optional[str]:
    """
    Dada una variable y un valor, revisa si al asignarla se produce un conflicto
    con alguna restricción. Si hay conflicto, devuelve el nombre de la variable
    que causa el problema; si no, devuelve None.
    """
    for (a, b) in restricciones:
        # Si 'var' es la primera variable de la restricción y la otra ya está asignada con el mismo valor
        if a == var and b in asignacion and asignacion[b] == valor:
            return b  # Devuelve la variable que genera el conflicto
        # Si 'var' es la segunda variable de la restricción y la otra ya está asignada con el mismo valor
        if b == var and a in asignacion and asignacion[a] == valor:
            return a
    return None  # No hay conflicto

def salto_atras_conflictos(asignacion: Dict[str, str], orden: List[str], indice: int = 0) -> Optional[Dict[str, str]]:
    """
    Algoritmo de búsqueda con salto atrás dirigido por conflictos.
    Intenta asignar valores a las variables siguiendo el orden dado.
    Si encuentra un conflicto, retrocede directamente a la variable que lo causa.
    """
    if indice == len(orden):
        # Si ya se asignaron todas las variables, se encontró una solución
        return asignacion

    var = orden[indice]  # Selecciona la variable actual a asignar

    for valor in dominios[var]:
        nueva_asig = asignacion.copy()  # Copia la asignación actual
        nueva_asig[var] = valor  # Asigna el valor a la variable
        print(f"Probando {var} = {valor} → {nueva_asig}")

        # Revisar si la asignación genera conflicto con alguna restricción
        causa = conflicto(var, valor, nueva_asig)
        if not causa:
            # Si no hay conflicto, continúa con la siguiente variable
            resultado = salto_atras_conflictos(nueva_asig, orden, indice + 1)
            if resultado:
                return resultado  # Si se encontró solución, la retorna
        else:
            # Si hay conflicto, identifica la variable causante y retrocede directamente a ella
            print(f"⚠️ Conflicto detectado: {var} choca con {causa}. Saltando atrás...\n")
            if causa in orden:
                nuevo_indice = orden.index(causa)
                # Llama recursivamente saltando al índice de la variable conflictiva
                return salto_atras_conflictos(asignacion, orden, nuevo_indice)

    # Si ningún valor es válido para la variable actual, informa y retorna None
    print(f"❌ Ningún valor válido para {var}, regresando...")
    return None

def demo_salto_conflictos():
    print("== Salto Atrás Dirigido por Conflictos ==")
    # Ejecuta el algoritmo desde una asignación vacía y usando la lista de variables
    solucion = salto_atras_conflictos({}, variables)
    if solucion:
        print("\n✅ Solución encontrada:")
        for k, v in solucion.items():
            print(f"  {k}: {v}")  # Muestra la solución final
    else:
        print("\n🚫 No se encontró solución válida.")

if __name__ == "__main__":
    demo_salto_conflictos()
