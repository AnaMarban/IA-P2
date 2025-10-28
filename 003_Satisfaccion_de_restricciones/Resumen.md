# Enfoque 3: Satisfacción de Restricciones (CSP)

Este enfoque se usa cuando el problema se define por un conjunto de **variables**, **dominios de valores posibles** y **restricciones** que deben cumplirse simultáneamente.  
El objetivo es encontrar una asignación de valores que cumpla todas las condiciones.  
Estos métodos permiten resolver problemas lógicos, combinatorios o de planificación.

---

## Estructura general de un CSP

- Variables: X₁, X₂, …, Xₙ  
- Dominios: posibles valores para cada variable (D₁, D₂, …, Dₙ)  
- Restricciones: relaciones que limitan las combinaciones válidas de valores.

**Ejemplo:**
X = {Color1, Color2, Color3}
D = {Rojo, Verde, Azul}
Restricciones = Color1 ≠ Color2, Color2 ≠ Color3

**Solución:** conjunto de valores que satisface todas las restricciones.

---

## Problemas de Satisfacción de Restricciones

Definen el modelo base del enfoque.  
El agente busca una asignación que cumpla todas las restricciones sin violar ninguna.

**Representación formal:**
\[
\text{CSP} = (X, D, C)
\]
donde:
- X: variables  
- D: dominios  
- C: restricciones

**Métodos comunes:**
- Búsqueda sistemática (backtracking).  
- Reducción del dominio.  
- Propagación de restricciones.

**Ejemplo clásico:** colorear un mapa sin repetir colores adyacentes.

---

## Búsqueda de Vuelta Atrás (Backtracking)

Expande asignaciones parciales e intenta completarlas.  
Si una restricción se viola, retrocede (backtrack) al paso anterior.  

**Idea general:**
1. Asignar un valor a la primera variable.  
2. Comprobar si cumple las restricciones.  
3. Si no, volver atrás y probar otro valor.

**Pseudocódigo:**
def backtracking(asignación):
si completa(asignación): return asignación
variable = seleccionar_no_asignada()
para cada valor en dominio:
si es_consistente(variable, valor):
asignar(variable, valor)
resultado = backtracking(asignación)
si resultado: return resultado
desasignar(variable)
return None



---

## Comprobación Hacia Delante (Forward Checking)

Anticipa conflictos reduciendo los dominios de las variables futuras.  
Cada vez que una variable se asigna, se eliminan los valores incompatibles en las siguientes.

**Ejemplo:**
Si A = Rojo, entonces B ≠ Rojo.  
Se borra “Rojo” del dominio de B.

**Ventajas:**
- Detecta conflictos temprano.  
- Reduce la profundidad de la búsqueda.

**Fórmula conceptual:**
\[
D_j = D_j - \{v_j | (v_i,v_j) \notin C_{ij}\}
\]

---

## Propagación de Restricciones

Propaga los efectos de una restricción a lo largo del grafo de variables.  
Si un dominio se reduce, se actualizan los demás que dependen de él.

**Técnica común: AC-3 (Arc Consistency 3)**

**Condición de consistencia de arco:**
Para cada restricción (Xi, Xj):
\[
\forall x \in D_i, \exists y \in D_j : (x, y) \text{ satisface } C_{ij}
\]

Si no existe tal y, se elimina x del dominio de Xi.

**Resultado:** dominios reducidos antes de iniciar la búsqueda, mejorando la eficiencia.

---

## Salto Atrás Dirigido por Conflictos (Conflict-Directed Backjumping)

Mejora el backtracking estándar analizando la causa del conflicto.  
En lugar de retroceder solo un nivel, salta directamente al nodo responsable del error.

**Funcionamiento:**
- Registra las variables que causan conflictos.  
- Cuando ocurre una falla, vuelve al conflicto más cercano en la cadena de dependencias.

**Ventajas:**
- Menor cantidad de retrocesos.  
- Eficiencia en problemas con muchas restricciones interdependientes.

---

## Búsqueda Local: Mínimos-Conflictos

Algoritmo basado en la heurística de **minimizar los conflictos**.  
Se inicia con una asignación completa (posiblemente inválida)  
y se modifica para reducir el número de restricciones violadas.

**Idea:**
Cambiar el valor de la variable que más conflictos genera.

**Pseudocódigo:**
asignación = aleatoria()
mientras no solución:
variable = variable_con_conflictos()
valor = valor_que_minimiza_conflictos(variable)
asignar(variable, valor)


**Ventajas:**
- Rápido en problemas grandes (como n-reinas).  
- No requiere retroceso.

**Fórmula heurística:**
\[
h(x) = \text{número de conflictos}
\]

---

## Acondicionamiento del Corte (Cutset Conditioning)

Divide el problema en subgrupos más pequeños eliminando ciertas variables.  
Al fijar valores a esas variables, el resto del problema se simplifica.

**Proceso:**
1. Identificar un conjunto de corte (cutset).  
2. Asignar valores a ese conjunto.  
3. Resolver los subproblemas independientes.  

**Ventajas:**
- Permite paralelizar el proceso.  
- Reduce la complejidad del grafo de restricciones.

**Costo estimado:**
\[
O(d^{|S|}) \text{ donde } S = \text{conjunto de corte.}
\]

---
