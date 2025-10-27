# 20_Propagacion_Restricciones
# Propagación de Restricciones: los cambios se comunican entre variables relacionadas.

from typing import Dict, List, Tuple, Optional
import copy

# Variables y dominios
variables = ["Av1", "Av2", "Parque"]
dominios_iniciales: Dict[str, List[str]] = {
    "Av1": ["8:00", "8:15", "8:30"],
    "Av2": ["8:00", "8:15", "8:30"],
    "Parque": ["8:00", "8:15", "8:30"]
}

# Restricciones: calles que no pueden compartir el mismo horario
restricciones: List[Tuple[str, str]] = [("Av1", "Av2"), ("Av2", "Parque")]

def propagar_restricciones(dominios: Dict[str, List[str]], restricciones: List[Tuple[str, str]]):
    """
    Propaga restricciones: elimina valores incompatibles de los dominios relacionados.
    Usa el algoritmo AC-3 (simplificado).
    """
    cola = restricciones.copy()

    while cola:
        (a, b) = cola.pop(0)
        if revisar(dominios, a, b):
            # Si se eliminan valores, volver a revisar vecinos de 'a'
            for (x, y) in restricciones:
                if y == a:
                    cola.append((x, y))

def revisar(dominios: Dict[str, List[str]], a: str, b: str) -> bool:
    """
    Revisa la consistencia entre los dominios de a y b.
    Si un valor de 'a' no tiene soporte en 'b', se elimina.
    """
    eliminado = False
    valores_a = dominios[a].copy()

    for valor_a in valores_a:
        # Un valor de 'a' es válido si existe al menos un valor diferente en 'b'
        if not any(valor_b != valor_a for valor_b in dominios[b]):
            dominios[a].remove(valor_a)
            eliminado = True
            print(f"⛔ Eliminado {valor_a} de {a} porque no es compatible con {b}")

    return eliminado

def ac3():
    """Ejemplo de ejecución del algoritmo AC-3 para propagación de restricciones."""
    dominios = copy.deepcopy(dominios_iniciales)
    print("== Propagación de Restricciones (AC-3) ==")
    print("Dominios iniciales:")
    for v, d in dominios.items():
        print(f"  {v}: {d}")
    print()

    propagar_restricciones(dominios, restricciones)

    print("\nDominios finales después de la propagación:")
    for v, d in dominios.items():
        print(f"  {v}: {d}")

if __name__ == "__main__":
    ac3()
