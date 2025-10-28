# Incertidumbre.
# GPS Inteligente - Enfoque 6: Probabilidad
# Tema - Incertidumbre

# El GPS razona con probabilidades cuando no sabe todo con certeza

# Datos conocidos
P_clima = {"Soleado": 0.6, "Lluvioso": 0.4}
P_trafico_dado_clima = {"Soleado": 0.3, "Lluvioso": 0.9}

# Calcular probabilidad total de tráfico (Ley de la probabilidad total)
P_trafico = (
    P_clima["Soleado"] * P_trafico_dado_clima["Soleado"]
    + P_clima["Lluvioso"] * P_trafico_dado_clima["Lluvioso"]
)

print("== INCERTIDUMBRE DEL GPS ==")
print(f"Probabilidad de tráfico total (sin saber el clima): {P_trafico:.2f}")
print("➡️ El GPS no sabe el clima exacto, pero estima la posibilidad de tráfico.")
