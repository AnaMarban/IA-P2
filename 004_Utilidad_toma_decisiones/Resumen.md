# Enfoque 4: Utilidad y Toma de Decisiones

Este enfoque introduce la capacidad de la IA para **elegir entre alternativas** en situaciones de incertidumbre.  
A diferencia de los algoritmos de búsqueda, aquí no se busca un camino fijo, sino la **mejor decisión posible** según las probabilidades y la utilidad esperada.  

El razonamiento se basa en **valores numéricos** que representan el beneficio o costo de cada acción.

---

## Teoría de la Utilidad

La utilidad representa el valor de satisfacción o beneficio que un agente obtiene de un resultado.  
El objetivo del agente racional es **maximizar la utilidad esperada**.

**Ecuación general:**
\[
EU(a) = \sum_{s} P(s|a) \times U(s)
\]

donde:
- EU(a): utilidad esperada de la acción a.  
- P(s|a): probabilidad de llegar al estado s dado a.  
- U(s): utilidad del estado s.  

**Conceptos clave:**
- Utilidad normalizada: valores entre 0 (peor caso) y 1 (mejor caso).  
- Preferencia racional: un agente siempre elige la acción con mayor utilidad esperada.

**Ejemplo:**  
Si el GPS puede elegir entre dos rutas, evalúa tiempo, tráfico y riesgo:
\[
EU(\text{Ruta}_i) = (P_{\text{rápida}} \times U_{\text{tiempo}}) + (P_{\text{segura}} \times U_{\text{seguridad}})
\]

---

## Redes de Decisión

Estructura gráfica que combina **redes bayesianas** con **nodos de decisión y utilidad**.  
Permite representar problemas donde las decisiones afectan las probabilidades y los resultados.

**Componentes:**
- Nodos aleatorios: variables con incertidumbre.  
- Nodos de decisión: acciones posibles.  
- Nodos de utilidad: valor asociado al resultado.

**Ejemplo:**
Clima → (Decisión: Llevar paraguas) → Utilidad


**Cálculo general:**
\[
EU(\text{decisión}) = \sum_{variables} P(\text{variables} | \text{decisión}) \times U(\text{resultado})
\]

**Criterio óptimo:**
Elegir la decisión con máxima utilidad esperada.

---

## Valor de la Información

Mide cuánto mejora la utilidad esperada del agente al obtener información adicional antes de tomar una decisión.

**Ecuación:**
\[
VPI(E) = EU(\text{con evidencia } E) - EU(\text{sin evidencia})
\]

**Interpretación:**
Si conocer algo cambia las probabilidades o mejora la elección, la información tiene valor.  
El agente racional solo paga por información si su valor esperado es positivo.

**Ejemplo:**  
Un GPS evalúa si vale la pena esperar una actualización del tráfico antes de elegir ruta.

---

## Iteración de Valores

Método para calcular la política óptima en problemas secuenciales donde las decisiones se repiten con el tiempo.  
Actualiza las utilidades de cada estado hasta converger.

**Ecuación de Bellman:**
\[
U_{t+1}(s) = R(s) + \gamma \max_a \sum_{s'} P(s'|s,a) U_t(s')
\]

donde:
- R(s): recompensa inmediata del estado s.  
- γ: factor de descuento (0 < γ ≤ 1).  
- P(s'|s,a): probabilidad de transición.  
- U_t(s): utilidad actual.

**Propiedades:**
- Converge a una política óptima.  
- Se aplica en entornos Markovianos (donde el futuro depende solo del estado actual).

---

## Iteración de Políticas

Algoritmo que alterna entre evaluar una política y mejorarla hasta que deja de cambiar.  
Evalúa la utilidad bajo una política fija y luego la ajusta.

**Pasos principales:**
1. Inicializar una política aleatoria π(s).  
2. Evaluar U(s) bajo esa política.  
3. Mejorar π(s) eligiendo la acción con mayor utilidad esperada.  
4. Repetir hasta la convergencia.

**Fórmula de mejora:**
\[
\pi'(s) = \arg\max_a \sum_{s'} P(s'|s,a)[R(s) + \gamma U(s')]
\]

**Diferencia con iteración de valores:**
Iteración de políticas trabaja directamente con las decisiones,  
mientras que iteración de valores calcula las utilidades de los estados.

---

## Proceso de Decisión de Markov (MDP)

Modelo matemático para decisiones secuenciales bajo incertidumbre.  
Cada acción lleva a un nuevo estado con cierta probabilidad y recompensa.

**Elementos:**
- S: conjunto de estados.  
- A: conjunto de acciones.  
- P(s'|s,a): función de transición.  
- R(s): recompensa.  
- γ: factor de descuento.  

**Ecuación de utilidad óptima:**
\[
U^*(s) = \max_a [R(s) + \gamma \sum_{s'} P(s'|s,a) U^*(s')]
\]

**Objetivo:** encontrar una **política óptima π*(s)** que maximice la utilidad total esperada.

**Propiedades:**
- El entorno es estocástico (probabilístico).  
- El agente aprende mediante interacción continua.

---

## MDP Parcialmente Observable (POMDP)

Extensión de MDP cuando el agente **no puede observar completamente** el estado del entorno.  
En lugar de conocer s directamente, mantiene una **creencia b(s)** sobre los posibles estados.

**Representación:**
\[
b'(s') = \alpha P(o|s') \sum_s P(s'|s,a) b(s)
\]

donde:
- b(s): creencia actual.  
- o: observación.  
- α: factor de normalización.

**Objetivo:**  
Maximizar la utilidad esperada sobre la distribución de creencias.

**Aplicación:**  
Robots o sistemas que deben decidir sin conocer el estado exacto del entorno (ej. conducción autónoma en niebla).

---

## Red Bayesiana Dinámica

Extiende las redes bayesianas al tiempo, modelando cómo las variables cambian de un paso a otro.  
Se representan dependencias entre estados consecutivos.

**Fórmula general:**
\[
P(X_1, ..., X_t) = P(X_1) \prod_{i=2}^{t} P(X_i | X_{i-1})
\]

**Uso:**  
Modelar procesos temporales, predicciones, y aprendizaje por secuencias.

---

## Teoría de Juegos: Equilibrios y Mecanismos

Modela situaciones donde varios agentes toman decisiones simultáneamente y los resultados dependen de todos.  
Cada agente busca maximizar su utilidad.

**Conceptos clave:**
- Estrategia: conjunto de acciones posibles.  
- Equilibrio de Nash: punto donde ningún jugador mejora cambiando solo su estrategia.  

**Ejemplo simple:**
En una intersección, dos GPS eligen ruta:
- Si ambos eligen la misma → tráfico (baja utilidad).  
- Si se reparten → flujo equilibrado.

**Condición de equilibrio:**
\[
U_i(\pi_i^*, \pi_{-i}^*) \geq U_i(\pi_i, \pi_{-i}^*) \quad \forall i
\]

---
