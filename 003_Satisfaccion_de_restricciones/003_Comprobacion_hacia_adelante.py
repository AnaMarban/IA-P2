# 19_Comprobacion_Hacia_Delante
# Comprobación hacia adelante: predice conflictos antes de cometer errores.

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

def es_valido(asignacion: Dict[str, str]) -> bool:
    """Verifica que no haya conflicto con las restricciones."""
    for (a, b) in restricciones:
        if a in asignacion and b in asignacion:
            if asignacion[a] == asignacion[b]:
                return False
    return True

def forward_check(asignacion: Dict[str, str], dominios: Dict[str, List[str]]) -> Optional[Dict[str, str]]:
    """Búsqueda con comprobación hacia adelante."""
    if len(asignacion) == len(variables):
        return asignacion  # solución completa

    # Elegir una variable no asignada
    var = [v for v in variables if v not in asignacion][0]

    for valor in dominios[var]:
        nueva_asig = asignacion.copy()
        nueva_asig[var] = valor

        if not es_valido(nueva_asig):
            continue

        # Clonar dominios para no modificar el original
        nuevos_dominios = copy.deepcopy(dominios)

        # Eliminar el valor elegido de los dominios de las variables relacionadas
        for (a, b) in restricciones:
            if a == var and b not in nueva_asig:
                if valor in nuevos_dominios[b]:
                    nuevos_dominios[b].remove(valor)
                    print(f"⛔ Eliminando {valor} del dominio de {b}")
            elif b == var and a not in nueva_asig:
                if valor in nuevos_dominios[a]:
                    nuevos_dominios[a].remove(valor)
                    print(f"⛔ Eliminando {valor} del dominio de {a}")

        print(f"✅ Asignando {var} = {valor}")
        print(f"   Dominios actualizados: {nuevos_dominios}\n")

        # Comprobar si aún hay dominios posibles
        if all(len(vals) > 0 for vals in nuevos_dominios.values()):
            resultado = forward_check(nueva_asig, nuevos_dominios)
            if resultado:
                return resultado

        print(f"❌ {var} = {valor} conduce a calle sin opciones, retrocediendo...\n")

    return None

def demo_forward():
    print("== Comprobación Hacia Delante ==")
    solucion = forward_check({}, copy.deepcopy(dominios_iniciales))
    if solucion:
        print("\n✅ Solución encontrada:")
        for k, v in solucion.items():
            print(f"  {k}: {v}")
    else:
        print("\n🚫 No se encontró solución válida.")

if __name__ == "__main__":
    demo_forward()
