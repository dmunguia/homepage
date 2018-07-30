# 99 Problemas en Racket

## Trabajando con listas

### P01 (*)  Encuentre el último de la lista

```lisp
=> (último '(a b c d))
(d)
```

### P02 (*) Encuentre los últimos dos de la lista

```lisp
=> (últimos-dos '(a b c d))
(c d)
```

### P03 (*) Encuentre el k-ésimo de la lista

```lisp
=> (elemento-en '(a b c d e) 3)
c
```

### P04 (*) Encuentre el número de elementos en la lista

### P05 (*) Invierta la lista

### P06 (*) Determine si la lista es un palíndrome

Un palíndrome se lee igual de izquierda a derecha que de derecha a izquierda. Ejemplo `(x a m a x)`.

### P07 (**) Aplane una estructura anidada de listas

Transforme una lista, que posible contenga otras listas, en una lista "plana" al reemplazar cada sublista por sus elementos (recursivamente).

```lisp
=> (aplanar '(a (b (c d) e)))
(a b c d e)
```

*Pista*: Puede utilizar las funciones predefinidas `list` y `append`.

### P08 (**) Elimine elementos consecutivos duplicados de la lista

Si una lista contiene elementos que se repiten consecutivamente, estos deben ser reemplazados por una única copia del elemento. El orden de los elementos no debe variar.

```lisp
=> (comprimir '(a a a a b c c a a d e e e e))
(a b c a d e)
```

### P09 (**) Empacar elementos consecutivos duplicados de una lista en sublistas.

Si una lista contiene elementos consecutivos duplicados, estos deben ser colocados en sublistas.

```lisp
=> (empacar '(a a a a b c c a a d e e e e))
((a a a a) (b) (c c) (a a) (d) (e e e e))
```

### P10 (*) Codificación de longitud de repetición de una lista.

Utilice el resultado del problema P09 para implementar el método de compresión llamado *longitud de repetición* (run-length encoding en inglés). Los duplicados consecutivos de un elemento se codifican como listas `(n e)` donde `n` es el número de duplicados del elemento `e`.

```lisp
=> (codificar '(a a a a b c c a a d e e e e))
((4 a) (1 b) (2 c) (2 a) (1 d) (4 e))
```

### P11 (*) Codificación de longitud de repetición modificado.

Modifique el resultado del problema P10 tal que si un elemento no tiene duplicados simplemente se copia en la lista resultante. Sólo los elementos duplicados se transfieren como listas `(n e)`.

```lisp
=> (codificar-mod '(a a a a b c c a a d e e e e))
((4 a) b (2 c) (2 a) d (4 e))
```

### P12 (**) Decodificación de una lista codificada con longitud de repetición.

Dada una lista codificada con el algoritmo de longitud de repetición como la especificada en el problema P11, construya su versión decodificada.

```lisp
=> (decodificar '((4 a) b (2 c) (2 a) d (4 e)))
(a a a a b c c a a d e e e e)
```

### P13 (**) Solución directa para la codificación de longitud de ejecución.

Implemente la codificación de longitud de ejecución directamente, es decir no utilice el resultado de P09, sino más bien cuente las repeticiones conforme vaya creando las listas `(n e)`. Al igual que en P11, simplifique el resultado reemplazando las listas de la forma `(1 x)` por `x`.

```lisp
=> (codificar-directo '(a a a a b c c a a d e e e e))
((4 a) b (2 c) (2 a) d (4 e))
```

### P14 (*) Duplicar los elementos de una lista.

```lisp
=> (dup '(a b c c d))
(a a b b c c c c d d)
```

### P15 (**) Replicar los elementos de una lista un número dado de veces.

```lisp
=> (replicar '(a b c) 3)
(a a a b b b c c c)
```

### P16 (**) Elimine cada k-ésimo elemento de una lista.

El índice inicia en `1`, no en `0`.

```lisp
=> (eliminar '(a b c d e f g h i k) 3)
(a b d e g h k)
```

### P17 (*) Parta una lista en dos partes, la longitud de la primera parte es dada.

No utilice ninguna función predefinida.

```lisp
=> (partir '(a b c d e f g h i k) 3)
((a b c) (d e f g h i k))
```

### P18 (**) Extraiga una porción de una lista.

Dados dos índices `i` y `k`, la porción es la lista que contiene los elementos entre el i-ésimo y el k-ésimo elemento de la lista original (incluyendo ambos límites). Empiece a contar los elementos de `1`.

```lisp
=> (porción '(a b c d e f g h i k) 3 7)
(c d e f g)
```

### P19 (**) Rote la lista `n` lugares a la izquierda.

```lisp
=> (rotar '(a b c d e f g h) 3)
(d e f g h a b c)
```

```lisp
=> (rotar '(a b c d e f g h) -2)
(g h a b c d e f)
```

*Pista*: Utilice las funciones predefinidas `length` y `append`, así como el resultado del problema P17.

### P20 (*) Elimine el k-ésimo elemento de la lista.

```lisp
=> (eliminar-el '(a b c d) 2)
(a c d)
```

### P21 (*) Inserte un elemento en una posición dada en una lista.

```lisp
=> (insertar-en 'alfa '(a b c d) 2)
(a alfa b c d)
```

### P22 (*) Crear una lista que contiene todos los enteros en un rango dado.

Si el primer argumento es mayor que el segundo, produzca una lista en orden descendente.

```lisp
=> (rango 4 9)
(4 5 6 7 8 9)
```

```lisp
=> (rango 6 2)
(6 5 4 3 2)
```

### P23 (**) Extraiga un número dado de elementos seleccionados al azar de una lista.

Los elementos seleccionados deben ser retornados en una lista.

```lisp
=> (seleccionar-al-azar '(a b c d e f g h) 3)
(e d a)
```

*Pista*: Utilice el generador de números pseudo-aleatorios de racket y el resultado del problema P20.

### P24 (*) Lotería: elija `n` números diferentes aleatoriamente del conjunto `1..M`.

Los números elegidos deben ser retornados en una lista.

Si `n` es `6` y `m` es `49`:

```lisp
=> (lotería 6 49)
(23 1 17 33 21 37)
```

*Pista*: combine las soluciones a los problemas P22 y P23.

### P25 (*) Generar una permutación aleatoria de elementos de una lista.

```lisp
=> (permutación-azar '(a b c d e f))
(b a d c e f)
```

*Pista*: Utilice la solución al problema P23.

### P26 (**) Genere las combinaciones de `k` objetos distintos elegidos de `n` elementos de una lista.

¿De cuántas maneras diferentes puede elegirse un comité de 3 personas de un grupo de 12? Sabemos que hay `C(12, 3) = 220` posibilidades (`C(n, k)` denota el conocido coeficiente binomial). Para los matemáticos puros este resultado podría ser suficiente. Pero nosotros queremos generar realmente todas las posibilidades en una lista.

```lisp
=> (combinaciones 3 '(a b c d e f))
((a b c) (a b d) (a b e) ...)
```

### P27  (**) Agrupar los elementos de un conjunto en subconjuntos disjuntos.

* ¿De cuántas maneras diferentes puede un grupo de 9 personas trabajar en 3 subgrupos disjuntos de 2, 3 y 4 personas? Escriba una función que genere todas las posibilidades y las retorne en una lista.

```lisp
=> (agrupar3 '(abel beatriz carla david eva felipe gabriela hugo ignacio))
(((abel beatriz) (carla david eva) (felipe gabriela hugo ignacio)) ...)
```

* Generalice el predicado anterior tal que podamos especificar en una lista los tamaños de los grupos, y el predicado retornará las listas correspondientes.

```lisp
=> (agrupar '(abel beatriz carla david eva felipe gabriela hugo ignacio) '(2 2 5))
(((abel beatriz) (carla david) (eva felipe gabriela hugo ignacio)) ...)
```

Note que no queremos las permutaciones de los miembros de los grupos; por ejemplo `'((abel beatriz) ...)` es la misma solución que `((beatriz abel) ...)`

Ud podría encontrar más información acerca de este problema combinatorio en algún buen libro de matemática discreta bajo el término "coeficientes multinomiales".

### P28 (**) Ordenar una lista de listas de acuerdo con la longitud de las sublistas.

* Supongamos que una lista contiene elementos que son a su vez listas. El objetivo es ordenar los elementos de esta lista de acuerdo con sus longitudes. Es decir, las listas más cortas de primero, las más largas después.

```lisp
=> (ordenar-long '((a b c) (d e) (f g h) (d e) (i j k l) (m n) (o))
((o) (d e) (d e) (m n) (a b c) (f g h) (i j k l))
```

* Nuevamente, supongamos que una lista contiene elementos que son a su vez listas. Esta vez, el objetivo es ordenar los elementos de acuerdo con su frecuencia de longitud. Es decir, las listas con longitudes poco frecuentes aparecerán de primero, las listas con longitudes más frecuentes aparecerán después.

```lisp
=> (ordenar-frec-long '((a b c) (d e) (f g h) (d e) (i j k l) (m n) (o))
((i j k l) (o) (a b c) (f g h) (d e) (d e) (m n))
```

Note que en el ejemplo anterior, las primeras dos listas en el resultado tienen longitud 4 y 1, ambas longitudes aparecen sólo una vez. El tercer y cuarto elementos tienen largo 3 el cual aparece dos veces (hay dos listas con esta longitud). Y finalmente, las últimas tres listas tienen largo 2, esta es la longitud más frecuente.
