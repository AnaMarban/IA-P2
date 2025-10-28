
from typing import Dict, List, Tuple, Optional
import itertools

# Variables divididas por zonas
zona_norte = ["Av1", "Av2", "Av3"]  # Zona norte de la ciudad
zona_sur = ["Parque", "Mercado", "Hospital"]  # Zona sur de la ciudad

dominios: Dict[str, List[str]] = {
    "Av1": ["8:00", "8:15", "8:30"],  # Horarios posibles para Av1
    "Av2": ["8:00", "8:15", "8:30"],  # Horarios posibles para Av2
    "Av3": ["8:00", "8:15", "8:30"],  # Horarios posibles para Av3
    "Parque": ["8:00", "8:15", "8:30"],  # Horarios posibles para Parque
    "Mercado": ["8:00", "8:15", "8:30"],  # Horarios posibles para Mercado
    "Hospital": ["8:00", "8:15", "8:30"]  # Horarios posibles para Hospital
}

# Restricciones internas (dentro de cada zona)
restricciones_norte: List[Tuple[str, str]] = [("Av1", "Av2"), ("Av2", "Av3")]  # Restricciones en la zona norte
restricciones_sur: List[Tuple[str, str]] = [("Parque", "Mercado"), ("Mercado", "Hospital")]  # Restricciones en la zona sur

# Restricción de corte (entre zonas): conecta la zona norte con la sur
restriccion_corte = ("Av3", "Parque")

def es_valida(asignacion: Dict[str, str], restricciones: List[Tuple[str, str]]) -> bool:
    """
    Verifica que una asignación cumpla las restricciones dadas.
    Devuelve True si no hay conflictos, False si alguna restricción se viola.
    """
    for (a, b) in restricciones:
        if a in asignacion and b in asignacion:
            if asignacion[a] == asignacion[b]:
                return False  # Hay conflicto
    return True

def resolver_zona(variables: List[str], restricciones: List[Tuple[str, str]]) -> List[Dict[str, str]]:
    """
    Genera todas las combinaciones posibles de horarios para las variables de una zona
    y devuelve solo aquellas que cumplen las restricciones internas de la zona.
    """
    soluciones = []
    for valores in itertools.product(*[dominios[v] for v in variables]):
        asignacion = dict(zip(variables, valores))  # Asigna un horario a cada variable
        if es_valida(asignacion, restricciones):
            soluciones.append(asignacion)  # Solo guarda las asignaciones válidas
    return soluciones

def acondicionamiento_corte():
    print("== Acondicionamiento del Corte ==")
    print("Dividiendo la ciudad en dos zonas...\n")

    # Paso 1: Resolver cada zona por separado, generando todas las combinaciones válidas
    soluciones_norte = resolver_zona(zona_norte, restricciones_norte)
    soluciones_sur = resolver_zona(zona_sur, restricciones_sur)

    print(f"Zona Norte: {len(soluciones_norte)} combinaciones válidas")
    print(f"Zona Sur:   {len(soluciones_sur)} combinaciones válidas\n")

    # Paso 2: Combinar soluciones de ambas zonas y aplicar la restricción de corte
    for sol_norte in soluciones_norte:
        for sol_sur in soluciones_sur:
            # Solo se combinan si cumplen la restricción de corte (Av3 ≠ Parque)
            if sol_norte["Av3"] != sol_sur["Parque"]:
                solucion_total = {**sol_norte, **sol_sur}  # Unimos ambas asignaciones
                print(" Solución combinada válida:")
                for k, v in solucion_total.items():
                    print(f"  {k}: {v}")
                return  # Detener en la primera solución válida encontrada

    # Si no se encuentra ninguna combinación válida, se informa
    print("🚫 No se encontró solución que conecte ambas zonas sin conflicto.")

if __name__ == "__main__":
    acondicionamiento_corte()
