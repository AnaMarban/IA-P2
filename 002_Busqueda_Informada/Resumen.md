# Enfoque 2: Búsqueda Informada – Heurísticas

Este enfoque utiliza **conocimiento adicional** (heurísticas) para orientar la búsqueda hacia el objetivo más rápido.  
A diferencia de la búsqueda no informada, el agente ahora “sabe hacia dónde ir” mediante una estimación del costo restante.  
Las heurísticas permiten reducir el número de nodos explorados y mejorar la eficiencia.

---

## Heurísticas

Una heurística es una **función de estimación** que aproxima el costo desde un nodo actual hasta la meta.  
Se representa como h(n).  

**Tipos comunes:**
- Admisible: nunca sobreestima el costo real.  
- Consistente: cumple h(n) ≤ c(n, n') + h(n').


**Fórmula general:**
\[
f(n) = g(n) + h(n)
\]
donde:
- g(n): costo desde el inicio hasta n.  
- h(n): costo estimado desde n hasta la meta.

---

## Búsqueda Voraz Primero el Mejor

Selecciona siempre el nodo con la **menor heurística h(n)**.  
Se centra en acercarse rápidamente al objetivo, sin considerar el costo recorrido.

**Función de evaluación:**
\[
f(n) = h(n)
\]

**Ventajas:**
- Muy rápida en espacios simples.  
- Ideal cuando se busca una solución aproximada.  

**Desventajas:**
- No garantiza la ruta más corta.  
- Puede atascarse en mínimos locales.  

**Implementación:**  
Usa una cola de prioridad basada en h(n).  
Expande el nodo con menor valor heurístico.

---

## Búsqueda A* y AO*

A* combina costo recorrido y heurística.  
El algoritmo elige el nodo con el menor valor de f(n) = g(n) + h(n).  
Es uno de los métodos más usados en IA y navegación.

**Propiedades:**
- Óptimo si h(n) es admisible.  
- Completo si el costo es positivo.  

# Enfoque 2: Búsqueda Informada – Heurísticas

Este enfoque utiliza **conocimiento adicional** (heurísticas) para orientar la búsqueda hacia el objetivo más rápido.  
A diferencia de la búsqueda no informada, el agente ahora “sabe hacia dónde ir” mediante una estimación del costo restante.  
Las heurísticas permiten reducir el número de nodos explorados y mejorar la eficiencia.

---

## Heurísticas

Una heurística es una **función de estimación** que aproxima el costo desde un nodo actual hasta la meta.  
Se representa como h(n).  

**Tipos comunes:**
- Admisible: nunca sobreestima el costo real.  
- Consistente: cumple h(n) ≤ c(n, n') + h(n').

**Ejemplo:**  
Distancia euclidiana entre dos puntos.  

**Fórmula general:**
\[
f(n) = g(n) + h(n)
\]
donde:
- g(n): costo desde el inicio hasta n.  
- h(n): costo estimado desde n hasta la meta.

---

## Búsqueda Voraz Primero el Mejor

Selecciona siempre el nodo con la **menor heurística h(n)**.  
Se centra en acercarse rápidamente al objetivo, sin considerar el costo recorrido.

**Función de evaluación:**
\[
f(n) = h(n)
\]

**Ventajas:**
- Muy rápida en espacios simples.  
- Ideal cuando se busca una solución aproximada.  

**Desventajas:**
- No garantiza la ruta más corta.  
- Puede atascarse en mínimos locales.  

**Implementación:**  
Usa una cola de prioridad basada en h(n).  
Expande el nodo con menor valor heurístico.

---

## Búsqueda A* y AO*

A* combina costo recorrido y heurística.  
El algoritmo elige el nodo con el menor valor de f(n) = g(n) + h(n).  
Es uno de los métodos más usados en IA y navegación.

**Propiedades:**
- Óptimo si h(n) es admisible.  
- Completo si el costo es positivo.  

# Enfoque 2: Búsqueda Informada – Heurísticas

Este enfoque utiliza **conocimiento adicional** (heurísticas) para orientar la búsqueda hacia el objetivo más rápido.  
A diferencia de la búsqueda no informada, el agente ahora “sabe hacia dónde ir” mediante una estimación del costo restante.  
Las heurísticas permiten reducir el número de nodos explorados y mejorar la eficiencia.

---

## Heurísticas

Una heurística es una **función de estimación** que aproxima el costo desde un nodo actual hasta la meta.  
Se representa como h(n).  

**Tipos comunes:**
- Admisible: nunca sobreestima el costo real.  
- Consistente: cumple h(n) ≤ c(n, n') + h(n').

**Ejemplo:**  
Distancia euclidiana entre dos puntos.  

**Fórmula general:**
\[
f(n) = g(n) + h(n)
\]
donde:
- g(n): costo desde el inicio hasta n.  
- h(n): costo estimado desde n hasta la meta.

---

## Búsqueda Voraz Primero el Mejor

Selecciona siempre el nodo con la **menor heurística h(n)**.  
Se centra en acercarse rápidamente al objetivo, sin considerar el costo recorrido.

**Función de evaluación:**
\[
f(n) = h(n)
\]

**Ventajas:**
- Muy rápida en espacios simples.  
- Ideal cuando se busca una solución aproximada.  

**Desventajas:**
- No garantiza la ruta más corta.  
- Puede atascarse en mínimos locales.  

**Implementación:**  
Usa una cola de prioridad basada en h(n).  
Expande el nodo con menor valor heurístico.

---

## Búsqueda A* y AO*

A* combina costo recorrido y heurística.  
El algoritmo elige el nodo con el menor valor de f(n) = g(n) + h(n).  
Es uno de los métodos más usados en IA y navegación.

**Propiedades:**
- Óptimo si h(n) es admisible.  
- Completo si el costo es positivo.  


**AO*** es una variante para **problemas AND-OR**, donde algunas acciones dependen de resolver varios subproblemas simultáneamente.

**Fórmula AO***:
\[
f(n) = g(n) + \sum_{i} p_i \cdot h_i(n)
\]

---

## Búsqueda de Ascensión de Colinas

Método local que avanza siempre hacia el **vecino con mejor heurística**.  
No mantiene una lista de caminos, solo el estado actual y sus vecinos inmediatos.

**Idea principal:**  
Elige la dirección que mejore h(n).

**Problemas comunes:**
- Se puede quedar atrapado en un mínimo local.  
- No garantiza solución global.  

**Variantes:**  
- Ascenso simple.  
- Reinicio aleatorio.  
- Templado simulado (se mejora más adelante).

---

## Búsqueda Tabú

Estrategia que evita volver a estados ya visitados mediante una lista “tabú”.  
Permite moverse a soluciones peores de forma temporal, escapando de mínimos locales.

**Componentes:**
- Lista tabú: memoria de estados recientes.  
- Función de aspiración: permite excepciones si la nueva solución mejora la mejor global.  

**Fórmula conceptual:**
\[
S_{nuevo} = \arg\min_{S' \notin Tabú} f(S')
\]

---

## Búsqueda de Temple Simulado (Simulated Annealing)

Usa un parámetro de temperatura (T) que va disminuyendo con el tiempo.  
Permite aceptar soluciones peores al inicio para escapar de mínimos locales.

**Regla de aceptación:**
\[
P(\text{aceptar peor}) = e^{-\Delta E / T}
\]

**Funcionamiento:**
- Alta T → movimiento aleatorio.  
- Baja T → movimiento determinista (como ascensión de colinas).  

**Ventaja:**  
Encuentra soluciones casi óptimas en entornos complejos.

---

## Búsqueda de Haz Local

Evalúa **varios estados simultáneamente** y conserva solo los mejores k en cada iteración.  
El parámetro k define el ancho del haz (beam width).

**Proceso:**
1. Generar k estados iniciales.  
2. Expandir todos sus vecinos.  
3. Mantener los k mejores.  

**Ventajas:**  
- Paraleliza la búsqueda.  
- Reduce la posibilidad de quedar atrapado en mínimos locales.

---

## Algoritmos Genéticos

Inspirados en la evolución biológica.  
Cada solución se representa como un cromosoma.  
Usan operadores de selección, cruza y mutación para mejorar las soluciones generación tras generación.

**Etapas principales:**
1. Población inicial aleatoria.  
2. Evaluación con una función de aptitud f(x).  
3. Selección y reproducción.  
4. Cruce y mutación.  
5. Reemplazo de la población.

**Fórmulas:**
- Selección proporcional:
\[
P_i = \frac{f_i}{\sum f_j}
\]
- Cruce:
\[
C = A[0:k] + B[k:]
\]
- Mutación: cambio aleatorio de bits o valores.

---

## Búsqueda Online

Realiza la búsqueda en tiempo real, tomando decisiones mientras explora.  
Usada cuando el entorno es **dinámico** o **desconocido**.

**Características:**
- Aprende del entorno sobre la marcha.  
- No necesita conocer el grafo completo.  
- Puede reajustar su ruta según nueva información.

**Ejemplo práctico:**  
Robots que navegan mientras detectan obstáculos.
