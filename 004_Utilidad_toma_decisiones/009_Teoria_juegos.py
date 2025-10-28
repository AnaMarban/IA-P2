# 32_Teoria_Juegos.
# GPS Inteligente - Enfoque 4: Utilidad y Toma de Decisiones
# Tema 32 - Teoría de Juegos: Equilibrios y Mecanismos


import itertools

# Lista de jugadores en el juego
jugadores = ["GPS_A", "GPS_B"]

# Lista de estrategias posibles para cada jugador
estrategias = ["Autopista", "Calle"]

 # Diccionario de pagos: para cada combinación de estrategias, la utilidad de cada jugador
pagos = {
    ("Autopista", "Autopista"): (2, 2),   # Ambos eligen autopista: congestión
    ("Autopista", "Calle"): (8, 3),       # A elige autopista, B calle
    ("Calle", "Autopista"): (3, 8),       # A calle, B autopista
    ("Calle", "Calle"): (5, 5)            # Ambos eligen calle: tranquilos
}

def encontrar_equilibrios():
    """
    Encuentra los Equilibrios de Nash simples por inspección.
    Un equilibrio ocurre cuando cada jugador está jugando su mejor respuesta
    a la estrategia del otro.
    """
    equilibrios = []
    for (a, b) in itertools.product(estrategias, estrategias):
        # Mejor respuesta de A dado lo que juega B
        mejor_a = max(estrategias, key=lambda x: pagos[(x, b)][0])
        # Mejor respuesta de B dado lo que juega A
        mejor_b = max(estrategias, key=lambda y: pagos[(a, y)][1])

        # Si ambos están jugando su mejor respuesta, es equilibrio de Nash
        if a == mejor_a and b == mejor_b:
            equilibrios.append((a, b))
    return equilibrios

def demo_teoria_juegos():
    print("== Teoría de Juegos – Equilibrios y Mecanismos ==")
    # Muestra la tabla de pagos para todas las combinaciones de estrategias
    for (a, b), (ua, ub) in pagos.items():
        print(f"{a} / {b} → GPS_A={ua}, GPS_B={ub}")
    print()

    eq = encontrar_equilibrios()  # Busca los equilibrios de Nash
    print(" Equilibrios de Nash encontrados:")
    for e in eq:
        print(f"  {e[0]} / {e[1]}")  # Muestra cada equilibrio encontrado

if __name__ == "__main__":
    demo_teoria_juegos()
