# Enfoque 5: Aprendizaje por Refuerzo (Reinforcement Learning)

En este enfoque, el agente aprende a actuar mediante **interacción con el entorno**.  
No se le dan las respuestas correctas, sino **recompensas o castigos** según sus decisiones.  
El objetivo es aprender una **política óptima** que maximice la recompensa total a largo plazo.

---

## Conceptos básicos del Aprendizaje por Refuerzo

- **Agente:** quien toma las decisiones.  
- **Entorno:** donde actúa el agente.  
- **Acción (a):** decisión tomada.  
- **Estado (s):** situación actual.  
- **Recompensa (r):** valor obtenido tras una acción.  
- **Política (π):** estrategia que define qué acción tomar en cada estado.  
- **Valor (V):** utilidad esperada de un estado.  
- **Q-valor (Q):** utilidad esperada de una acción en un estado.

**Objetivo general:**
\[
\pi^*(s) = \arg\max_a Q^*(s, a)
\]

El agente aprende por **ensayo y error**, reforzando acciones que llevan a mayores recompensas.

---

## Aprendizaje por Refuerzo Pasivo

El agente **no actúa libremente**: sigue una política fija y evalúa su desempeño.  
Aprende los valores esperados de los estados siguiendo esa política.

**Ecuación de actualización:**
\[
V(s) = V(s) + \alpha [r + \gamma V(s') - V(s)]
\]
donde:
- α: tasa de aprendizaje.  
- γ: factor de descuento.  
- r: recompensa inmediata.  

**Idea:** aprender cuánto vale cada estado sin modificar la política.

---

## Aprendizaje por Refuerzo Activo

El agente **explora** y **mejora su política** al mismo tiempo.  
Debe balancear **exploración** (probar cosas nuevas) y **explotación** (usar lo que ya sabe).

**Regla general:**
\[
Q(s,a) = Q(s,a) + \alpha [r + \gamma \max_{a'} Q(s',a') - Q(s,a)]
\]

Este aprendizaje produce una política adaptativa que cambia según la experiencia.

**Ejemplo:** un GPS que prueba rutas nuevas y actualiza su mapa interno según los tiempos obtenidos.

---

## Q-Learning

Algoritmo fundamental de RL.  
Aprende el valor Q(s,a) sin conocer las probabilidades de transición del entorno.  
Es un método **fuera de política (off-policy)**.

**Ecuación de Bellman para Q-Learning:**
\[
Q(s,a) \leftarrow Q(s,a) + \alpha [r + \gamma \max_{a'} Q(s',a') - Q(s,a)]
\]

**Propiedades:**
- Converge a Q* si explora lo suficiente.  
- Aprende sin modelo del entorno.  
- Permite obtener π*(s) = argmax Q(s,a).

**Ejemplo:** el GPS ajusta su confianza en cada ruta según la experiencia previa.

---

## Exploración vs Explotación

Dilema entre probar nuevas acciones (explorar) o usar la mejor conocida (explotar).  
El equilibrio se maneja con la estrategia **ε-greedy**.

**Regla:**
\[
\text{Con probabilidad } \epsilon \rightarrow \text{acción aleatoria (explorar)}
\]
\[
\text{Con probabilidad } 1 - \epsilon \rightarrow \text{acción óptima (explotar)}
\]

**Ejemplo:** el GPS a veces prueba un nuevo camino aunque conozca uno más rápido, para descubrir rutas alternativas.

**Técnicas:**
- ε decreciente: explorar mucho al inicio, menos con el tiempo.  
- Softmax: elige acciones proporcionalmente a su valor Q.

---

## Búsqueda de la Política

Método que optimiza directamente la política sin calcular valores intermedios.  
Usa gradientes para ajustar las probabilidades de elegir cada acción.

**Regla general:**
\[
\pi(a|s) = \pi(a|s) + \alpha \, R(s,a) \, (1 - \pi(a|s))
\]

**Pasos:**
1. Ejecutar la política actual.  
2. Medir las recompensas obtenidas.  
3. Ajustar la política favoreciendo acciones más exitosas.

**Ejemplo:** el GPS ajusta sus preferencias de ruta según los resultados obtenidos en viajes previos.

---

## Aprendizaje por Refuerzo Pasivo vs Activo

|    Característica   |   Pasivo   |    Activo    |
|---------------------|------------|--------------|
|  Controla acciones  |     No     |      Sí      |
|    Política fija    |     Sí     |      No      |
|   Aprende valores   |     Sí     |      Sí      |
|       Explora       |     No     |      Sí      |
| Tipo de aprendizaje | Evaluativo | Exploratorio |

---

## Fórmulas generales del RL

1. **Valor de estado:**
   \[
   V^\pi(s) = \sum_a \pi(a|s) \sum_{s'} P(s'|s,a) [R(s,a,s') + \gamma V^\pi(s')]
   \]

2. **Ecuación de Bellman óptima:**
   \[
   V^*(s) = \max_a \sum_{s'} P(s'|s,a)[R(s,a,s') + \gamma V^*(s')]
   \]

3. **Q-función óptima:**
   \[
   Q^*(s,a) = \sum_{s'} P(s'|s,a)[R(s,a,s') + \gamma \max_{a'} Q^*(s',a')]
   \]

---
