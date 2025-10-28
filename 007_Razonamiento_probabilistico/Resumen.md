# Enfoque 7: Razonamiento Probabilístico

Este enfoque amplía el uso de la probabilidad para realizar **inferencia lógica** en entornos inciertos.  
El objetivo es calcular la probabilidad de ciertos eventos o causas dadas observaciones parciales.  
Para lograrlo, se utilizan estructuras como **redes bayesianas** y métodos de inferencia.

---

## Red Bayesiana

Una Red Bayesiana es un **grafo dirigido acíclico** que representa dependencias probabilísticas entre variables.  
Cada nodo es una variable y las aristas indican relaciones de causa y efecto.

**Componentes:**
- Nodos: variables aleatorias.  
- Arcos: dependencias condicionales.  
- Tablas de probabilidad condicional (CPT).

**Fórmula general:**
\[
P(X_1, X_2, ..., X_n) = \prod_{i=1}^{n} P(X_i | Padres(X_i))
\]

**Ejemplo:**
Lluvia → Tráfico → Accidente


\[
P(L, T, A) = P(L) \times P(T|L) \times P(A|T)
\]

Las redes bayesianas permiten calcular probabilidades conjuntas y condicionales de forma eficiente.

---

## Regla de la Cadena

Permite descomponer una probabilidad conjunta en una serie de probabilidades condicionales.  
Es la base matemática que respalda las redes bayesianas.

**Fórmula:**
\[
P(X_1, X_2, ..., X_n) = P(X_1) P(X_2|X_1) P(X_3|X_1,X_2) ... P(X_n|X_1,...,X_{n-1})
\]

**Uso:**  
Divide problemas grandes en fragmentos manejables.  
Permite calcular la probabilidad de varios eventos simultáneos.

**Ejemplo:**
\[
P(L, T, A) = P(A|T,L) \times P(T|L) \times P(L)
\]

---

## Manto de Markov

Define el conjunto mínimo de variables que **vuelven independiente** a una variable del resto del sistema.  
Es decir, si se conoce su manto, no se necesita información adicional del resto del grafo.

**Componentes del Manto de Markov de un nodo X:**
1. Sus padres (causas directas).  
2. Sus hijos (efectos).  
3. Los otros padres de sus hijos (causas compartidas).

**Propiedad:**
\[
P(X | Todo) = P(X | Manto(X))
\]

**Ejemplo:**
Para el nodo *Tráfico*, su manto puede ser {Lluvia, Accidente, Hora_Pico}.

---

## Inferencia por Enumeración

Método exacto que calcula probabilidades marginales recorriendo **todas las combinaciones posibles** de variables.  
Se usa para obtener P(X|E), donde E es la evidencia conocida.

**Ecuación general:**
\[
P(X|E) = \alpha \sum_Y P(X,E,Y)
\]

donde:
- Y: variables ocultas.  
- α: factor de normalización.

**Ventajas:**
- Preciso.  
- Conceptualmente simple.

**Desventajas:**
- Exponencialmente costoso para muchas variables.

---

## Eliminación de Variables

Optimiza la inferencia evitando enumerar todo el espacio posible.  
Suma las variables irrelevantes y conserva solo las necesarias para el cálculo.

**Ecuación:**
\[
P(X|E) = \alpha \sum_Y \prod_i P(X_i | Padres(X_i))
\]

**Ventajas:**
- Misma precisión que la enumeración.  
- Requiere menos cálculos.  
- Base de los algoritmos modernos de inferencia.

---

## Muestreo Directo y por Rechazo

Aproxima las probabilidades mediante **simulación aleatoria**.  
Genera muestras según las probabilidades de la red y cuenta la frecuencia de los resultados.

- **Muestreo directo:** genera muestras completas y calcula frecuencias.  
- **Muestreo por rechazo:** descarta las muestras que no cumplen la evidencia.

**Fórmulas:**
\[
P(X) \approx \frac{\text{# de veces que X ocurre}}{\text{# de muestras totales}}
\]
\[
P(X|E) \approx \frac{\text{# de veces que X ocurre con E}}{\text{# de veces que E ocurre}}
\]

**Ventajas:**
- No necesita cálculo exacto.  
- Escalable a redes grandes.

---

## Ponderación de Verosimilitud

Mejora el muestreo por rechazo al **asignar pesos** a las muestras en lugar de descartarlas.  
Cada muestra recibe un peso según qué tan consistente sea con la evidencia.

**Ecuación:**
\[
P(X|E) \approx \frac{\sum_i w_i \cdot I(X_i)}{\sum_i w_i}
\]

donde:
- \( w_i = P(E|X_i) \): peso de la muestra.  
- \( I(X_i) \): 1 si X ocurre, 0 si no.

**Ventaja:**  
Evita desperdiciar muestras y mejora la eficiencia de la estimación.

---

## Monte Carlo para Cadenas de Markov (MCMC)

Método de inferencia basado en muestreo encadenado.  
Cada muestra depende de la anterior y forma una **cadena de Markov** que converge a la distribución real.

**Procedimiento:**
1. Elegir una variable.  
2. Asignar valores condicionales según sus vecinos.  
3. Repetir hasta alcanzar el equilibrio (convergencia).

**Ecuación general:**
\[
P(X_t) = P(X_{t-1}) T(X_{t-1} \rightarrow X_t)
\]

**Ventajas:**
- Muy eficiente para redes grandes.  
- Utiliza menos memoria.  
- Base de los métodos de inferencia modernos (como Gibbs Sampling).

---
