# Acondicionamiento_Corte.
# Acondicionamiento del Corte: divide el problema en subredes y las resuelve por separado.

from typing import Dict, List, Tuple, Optional
import itertools

# Variables divididas por zonas
zona_norte = ["Av1", "Av2", "Av3"]
zona_sur = ["Parque", "Mercado", "Hospital"]

# Dominios (horarios posibles)
dominios: Dict[str, List[str]] = {
    "Av1": ["8:00", "8:15", "8:30"],
    "Av2": ["8:00", "8:15", "8:30"],
    "Av3": ["8:00", "8:15", "8:30"],
    "Parque": ["8:00", "8:15", "8:30"],
    "Mercado": ["8:00", "8:15", "8:30"],
    "Hospital": ["8:00", "8:15", "8:30"]
}

# Restricciones internas (dentro de cada zona)
restricciones_norte: List[Tuple[str, str]] = [("Av1", "Av2"), ("Av2", "Av3")]
restricciones_sur: List[Tuple[str, str]] = [("Parque", "Mercado"), ("Mercado", "Hospital")]

# Restricción de corte (entre zonas)
restriccion_corte = ("Av3", "Parque")

def es_valida(asignacion: Dict[str, str], restricciones: List[Tuple[str, str]]) -> bool:
    """Verifica que una asignación cumpla las restricciones dadas."""
    for (a, b) in restricciones:
        if a in asignacion and b in asignacion:
            if asignacion[a] == asignacion[b]:
                return False
    return True

def resolver_zona(variables: List[str], restricciones: List[Tuple[str, str]]) -> List[Dict[str, str]]:
    """Genera todas las combinaciones válidas para una zona."""
    soluciones = []
    for valores in itertools.product(*[dominios[v] for v in variables]):
        asignacion = dict(zip(variables, valores))
        if es_valida(asignacion, restricciones):
            soluciones.append(asignacion)
    return soluciones

def acondicionamiento_corte():
    print("== Acondicionamiento del Corte ==")
    print("Dividiendo la ciudad en dos zonas...\n")

    # 1️⃣ Resolver cada zona por separado
    soluciones_norte = resolver_zona(zona_norte, restricciones_norte)
    soluciones_sur = resolver_zona(zona_sur, restricciones_sur)

    print(f"Zona Norte: {len(soluciones_norte)} combinaciones válidas")
    print(f"Zona Sur:   {len(soluciones_sur)} combinaciones válidas\n")

    # 2️⃣ Combinar soluciones entre zonas y aplicar restricción de corte
    for sol_norte in soluciones_norte:
        for sol_sur in soluciones_sur:
            if sol_norte["Av3"] != sol_sur["Parque"]:  # cumple el corte
                solucion_total = {**sol_norte, **sol_sur}
                print("✅ Solución combinada válida:")
                for k, v in solucion_total.items():
                    print(f"  {k}: {v}")
                return  # detener en la primera solución válida

    print("🚫 No se encontró solución que conecte ambas zonas sin conflicto.")

if __name__ == "__main__":
    acondicionamiento_corte()
