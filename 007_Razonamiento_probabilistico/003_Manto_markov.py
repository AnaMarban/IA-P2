# Manto_de_Markov.
# GPS Inteligente - Enfoque 7: Razonamiento Probabilístico
# Tema - Manto de Markov

# Simulación simple de una red Bayesiana:
# Lluvia → Tráfico → Accidente
#            ↑
#         Hora_Pico

# Definición de las conexiones
red_bayesiana = {
    "Lluvia": ["Tráfico"],
    "Hora_Pico": ["Tráfico"],
    "Tráfico": ["Accidente"],
    "Accidente": []
}

# Función para encontrar el Manto de Markov de un nodo
def manto_de_markov(nodo, red):
    padres = [n for n, hijos in red.items() if nodo in hijos]
    hijos = red[nodo]
    otros_padres = []
    for h in hijos:
        for n, hs in red.items():
            if h in hs and n != nodo and n not in otros_padres:
                otros_padres.append(n)
    return set(padres + hijos + otros_padres)

# Calcular el manto de Markov para "Tráfico"
manto_trafico = manto_de_markov("Tráfico", red_bayesiana)

print("== MANTO DE MARKOV ==")
print("Nodo analizado: Tráfico")
print(f"Manto de Markov: {manto_trafico}")
print("\n El GPS solo necesita mirar a estas variables para razonar sobre 'Tráfico'.")
