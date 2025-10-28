# Enfoque 6: Probabilidad e Incertidumbre

Este enfoque introduce la representación matemática de la incertidumbre.  
El agente ya no asume que conoce todo el entorno, sino que **razona con probabilidades** para estimar lo que no sabe.  
El objetivo es manejar información incompleta y tomar decisiones racionales basadas en evidencia.

---

## Incertidumbre

La incertidumbre aparece cuando el agente **no tiene información completa o confiable** del entorno.  
En lugar de respuestas exactas, se trabaja con **probabilidades**.

**Ejemplo:**  
El GPS no sabe si hay tráfico, pero estima:  
- P(Tráfico) = 0.6  
- P(No Tráfico) = 0.4  

**Ley de la probabilidad total:**
\[
P(A) = \sum_i P(A|B_i)P(B_i)
\]

**Idea:**  
El agente combina probabilidades parciales para formar una visión global del mundo.

---

## Probabilidad a Priori

Representa la **creencia inicial** del agente antes de recibir evidencia.  
Es el conocimiento previo basado en experiencia o datos históricos.

**Ejemplo:**  
Antes de revisar el clima:  
\[
P(\text{Lluvia}) = 0.3, \quad P(\text{No Lluvia}) = 0.7
\]

**Formalismo:**
\[
P(H) = \text{probabilidad a priori de una hipótesis H}
\]

**Uso:**  
Sirve como punto de partida para actualizar creencias con nueva información.

---

## Probabilidad Condicionada y Normalización

Actualiza las creencias cuando se recibe evidencia nueva.  
Permite calcular la probabilidad de un evento **dado que otro ya ocurrió**.

**Definición:**
\[
P(A|B) = \frac{P(A,B)}{P(B)} = \frac{P(B|A)P(A)}{P(B)}
\]

**Normalización:**
Asegura que las probabilidades resultantes sumen 1:
\[
\sum_i P(A_i|B) = 1
\]

**Ejemplo:**  
Si está lloviendo, el GPS ajusta:
\[
P(\text{Tráfico|Lluvia}) = 0.8
\]

---

## Distribución de Probabilidad

Una distribución describe **todas las posibilidades de un evento** junto con sus probabilidades.  
La suma de todas ellas siempre es igual a 1.

**Ejemplo:**
| Estado del tráfico | Probabilidad |
|--------------------|--------------|
|       Ligero       |     0.5      |
|        Medio       |     0.3      |
|       Pesado       |     0.2      |

**Valor esperado:**
\[
E[X] = \sum_i P(x_i) \times x_i
\]
Representa el promedio ponderado de los resultados posibles.

---

## Independencia Condicional

Dos eventos son independientes si el conocimiento de uno **no afecta** la probabilidad del otro.  
La independencia condicional se da cuando esto es cierto **dado un tercer evento**.

**Fórmula:**
\[
P(A,B|C) = P(A|C) \times P(B|C)
\]

**Ejemplo:**  
Si se conoce el clima, el tráfico y los accidentes son independientes:
\[
P(\text{Accidente|Tráfico, Clima}) = P(\text{Accidente|Clima})
\]

**Ventaja:**  
Simplifica los cálculos probabilísticos en modelos grandes.

---

## Regla de Bayes

Permite invertir la relación entre causa y efecto.  
A partir de un efecto observado, calcula la probabilidad de la causa.

**Ecuación:**
\[
P(H|E) = \frac{P(E|H)P(H)}{P(E)}
\]

donde:
- H = hipótesis (causa)  
- E = evidencia (efecto)

**Ejemplo:**  
El GPS observa tráfico y estima:
\[
P(\text{Lluvia|Tráfico}) = \frac{P(\text{Tráfico|Lluvia})P(\text{Lluvia})}{P(\text{Tráfico})}
\]

**Interpretación:**  
Permite razonar al revés: si veo un efecto, ¿qué tan probable es su causa?

---

## Fórmulas clave del enfoque

1. **Probabilidad total:**
   \[
   P(A) = \sum_i P(A|B_i) P(B_i)
   \]

2. **Probabilidad condicionada:**
   \[
   P(A|B) = \frac{P(A,B)}{P(B)}
   \]

3. **Regla de Bayes:**
   \[
   P(H|E) = \frac{P(E|H) P(H)}{P(E)}
   \]

4. **Esperanza matemática:**
   \[
   E[X] = \sum_i x_i P(x_i)
   \]

---
