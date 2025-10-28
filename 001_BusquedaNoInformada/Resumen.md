# Enfoque 1: Búsqueda en Grafos – Búsqueda No Informada

Este enfoque representa las estrategias de exploración que no usan conocimiento previo del entorno.  
El agente busca soluciones probando caminos hasta encontrar el objetivo.  
Los algoritmos se basan en estructuras como colas, pilas y listas de nodos visitados.

---

## Búsqueda en Anchura (BFS)

Explora el grafo por niveles.  
Visita primero los nodos más cercanos al punto inicial.  
Usa una **cola (FIFO)** para almacenar los caminos pendientes.


**Características:**  
- Garantiza la ruta más corta.  
- Usa mucha memoria.  
- Se detiene cuando encuentra el objetivo.  

---

## Búsqueda en Anchura de Costo Uniforme

Busca el camino con el **menor costo acumulado**.  
Usa una **cola de prioridad** ordenada por el costo total g(n).  

**Función de costo:**  
f(n) = g(n)

**Notas:**  
- Explora caminos más cortos antes que los largos.  
- Equivalente a BFS si todos los costos son iguales.  


---

## Búsqueda en Profundidad (DFS)

Explora lo más profundo posible antes de retroceder.  
Utiliza una **pila (LIFO)** para almacenar los caminos.  

**Ventajas:**  
- Usa poca memoria.  
- Encuentra soluciones rápido en espacios pequeños.  

**Desventajas:**  
- Puede quedar atrapada en bucles.  
- No garantiza la solución más corta.

---

## Búsqueda en Profundidad Limitada

Variante de DFS con un límite de profundidad definido.  
Evita bucles y explora hasta un nivel máximo.

**Condición:**  
Si profundidad > límite → detener expansión.

**Fórmula general:**  
DepthLimitedSearch(n, límite)

**Observaciones:**  
- Puede fallar si la solución está más profunda que el límite.  
- Útil para espacios infinitos o mal definidos.

---

## Búsqueda en Profundidad Iterativa

Combina BFS y DFS.  
Realiza varias búsquedas en profundidad aumentando el límite cada vez.  

**Ciclo:**  
Límite = 1 → 2 → 3 → … hasta encontrar la meta.  

**Ventajas:**  
- Garantiza la solución óptima.  
- Usa menos memoria que BFS.  
- Repite nodos, pero mantiene bajo el consumo.

---

## Búsqueda Bidireccional

Ejecuta dos búsquedas simultáneas: una desde el inicio y otra desde el objetivo.  
Se detiene cuando ambas se encuentran.  

**Fórmula:**  
Costo ≈ O(b^(d/2))  

**Características:**  
- Reduce significativamente el tiempo de búsqueda.  
- Requiere conocer el estado final con precisión.  

---

## Búsqueda en Grafos

Versión general que controla nodos repetidos mediante una lista de visitados.  
Permite aplicar cualquier algoritmo anterior en entornos con ciclos.  

**Estructura base:**
- Lista de visitados.  
- Expansión de nodos no explorados.  
- Control de duplicados.

**Ventajas:**  
- Evita bucles infinitos.  
- Asegura que cada nodo se procese una sola vez.

---

