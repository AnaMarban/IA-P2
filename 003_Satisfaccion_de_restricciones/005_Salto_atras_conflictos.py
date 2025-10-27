# 21_Salto_Atras_Conflictos.
# Salto Atrás Dirigido por Conflictos: retrocede directamente al origen del problema.

from typing import Dict, List, Tuple, Optional

# Variables y dominios
variables = ["Av1", "Av2", "Parque"]
dominios: Dict[str, List[str]] = {
    "Av1": ["8:00", "8:15", "8:30"],
    "Av2": ["8:00", "8:15", "8:30"],
    "Parque": ["8:00", "8:15", "8:30"]
}

# Restricciones: calles que no pueden tener el mismo horario
restricciones: List[Tuple[str, str]] = [("Av1", "Av2"), ("Av2", "Parque")]

def conflicto(var: str, valor: str, asignacion: Dict[str, str]) -> Optional[str]:
    """Devuelve la variable que causa conflicto, si existe."""
    for (a, b) in restricciones:
        if a == var and b in asignacion and asignacion[b] == valor:
            return b
        if b == var and a in asignacion and asignacion[a] == valor:
            return a
    return None

def salto_atras_conflictos(asignacion: Dict[str, str], orden: List[str], indice: int = 0) -> Optional[Dict[str, str]]:
    """Búsqueda con salto atrás dirigido por conflictos."""
    if indice == len(orden):
        return asignacion  # solución completa

    var = orden[indice]

    for valor in dominios[var]:
        nueva_asig = asignacion.copy()
        nueva_asig[var] = valor
        print(f"Probando {var} = {valor} → {nueva_asig}")

        # Revisar si hay conflicto
        causa = conflicto(var, valor, nueva_asig)
        if not causa:
            resultado = salto_atras_conflictos(nueva_asig, orden, indice + 1)
            if resultado:
                return resultado
        else:
            # Detecta la variable causante y salta directo hacia ella
            print(f"⚠️ Conflicto detectado: {var} choca con {causa}. Saltando atrás...\n")
            if causa in orden:
                nuevo_indice = orden.index(causa)
                return salto_atras_conflictos(asignacion, orden, nuevo_indice)

    print(f"❌ Ningún valor válido para {var}, regresando...")
    return None

def demo_salto_conflictos():
    print("== Salto Atrás Dirigido por Conflictos ==")
    solucion = salto_atras_conflictos({}, variables)
    if solucion:
        print("\n✅ Solución encontrada:")
        for k, v in solucion.items():
            print(f"  {k}: {v}")
    else:
        print("\n🚫 No se encontró solución válida.")

if __name__ == "__main__":
    demo_salto_conflictos()
