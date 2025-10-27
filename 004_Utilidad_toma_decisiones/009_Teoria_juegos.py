# 32_Teoria_Juegos.
# GPS Inteligente - Enfoque 4: Utilidad y Toma de Decisiones
# Tema 32 - Teoría de Juegos: Equilibrios y Mecanismos

import itertools

# Jugadores
jugadores = ["GPS_A", "GPS_B"]

# Estrategias posibles
estrategias = ["Autopista", "Calle"]

# Tabla de pagos (utilidades)
# (Elección A, Elección B): (Utilidad A, Utilidad B)
pagos = {
    ("Autopista", "Autopista"): (2, 2),   # Congestión
    ("Autopista", "Calle"): (8, 3),       # A gana, B va lento
    ("Calle", "Autopista"): (3, 8),       # B gana
    ("Calle", "Calle"): (5, 5)            # Ambos tranquilos
}

def encontrar_equilibrios():
    """Encuentra Equilibrios de Nash simples por inspección."""
    equilibrios = []
    for (a, b) in itertools.product(estrategias, estrategias):
        # Mejor respuesta de A dado B
        mejor_a = max(estrategias, key=lambda x: pagos[(x, b)][0])
        # Mejor respuesta de B dado A
        mejor_b = max(estrategias, key=lambda y: pagos[(a, y)][1])

        if a == mejor_a and b == mejor_b:
            equilibrios.append((a, b))
    return equilibrios

def demo_teoria_juegos():
    print("== Teoría de Juegos – Equilibrios y Mecanismos ==")
    for (a, b), (ua, ub) in pagos.items():
        print(f"{a} / {b} → GPS_A={ua}, GPS_B={ub}")
    print()

    eq = encontrar_equilibrios()
    print("🎯 Equilibrios de Nash encontrados:")
    for e in eq:
        print(f"  {e[0]} / {e[1]}")

if __name__ == "__main__":
    demo_teoria_juegos()
