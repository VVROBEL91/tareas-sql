DIARIO DE APRENDIZAJE SQL
Alumna: Paulina Wroblewska

PARTE 1. Registro de las Misiones

Misión 1. Consigue tus primeras pistas

Consulta 1 (Seleccionar y filtrar): SELECT * FROM peliculas WHERE anio > 2000;
Explicación Consulta 1: Selecciona todas las columnas de la tabla peliculas y filtra los resultados con WHERE para mostrar solo las películas estrenadas después del año 2000.

Consulta 2 (Ordenar resultados): SELECT titulo, anio FROM peliculas ORDER BY anio DESC;
Explicación Consulta 2: Muestra únicamente el título y el año de las películas, ordenándolas de la más reciente a la más antigua con ORDER BY.

Misión 2. Sube de nivel

Consulta difícil (JOIN): SELECT peliculas.titulo, directores.nombre FROM peliculas JOIN directores ON peliculas.director_id = directores.id;
Cómo lo conseguí: Me costó juntar dos tablas distintas, pero revisando la teoría y las pistas entendí que debía unirlas usando la columna que tienen en común (director_id e id).

Misión 4. Mi registro de aprendizaje

Una consulta SQL sirve para pedir, filtrar y obtener información específica guardada en una base de datos.
La instrucción que mejor entiendo es SELECT junto con WHERE y ORDER BY para buscar y ordenar datos.
La instrucción que todavía me cuesta es JOIN, porque requiere identificar qué columnas conectan dos tablas diferentes.
El error más interesante que he encontrado es intentar combinar tablas sin especificar bien la condición de unión o equivocarme en el orden de las instrucciones.
Una cosa que ahora puedo hacer y antes no sabía hacer es escribir consultas desde cero, filtrar por condiciones y completar el 100% de los 10 módulos de SQL Cinema.

ENTREGABLE FINAL

1. Registro de consultas SQL

A) Consulta básica comprendida: SELECT * FROM peliculas; — Muestra la tabla completa con las 25 películas de la base de datos cine_db, ya que SELECT * selecciona todas las columnas y FROM peliculas indica la tabla.

B) Consulta con filtro u ordenación: SELECT titulo, puntuacion FROM peliculas WHERE puntuacion >= 8 ORDER BY puntuacion DESC; — Muestra las películas con puntuación igual o superior a 8 ordenadas de mayor a menor usando WHERE y ORDER BY.

C) Consulta difícil o reto: SELECT peliculas.titulo, directores.nombre FROM peliculas JOIN directores ON peliculas.director_id = directores.id; — Muestra el título de cada película junto al nombre de su director conectando ambas tablas con JOIN.

2. Reto de SQL Agent

¿Qué pedía el reto?: Observar los eventos de acceso en la tabla eventos_login para investigar quién intentó entrar, cuándo y desde dónde.
¿Qué consulta he escrito?: SELECT * FROM eventos_login;
¿He conseguido resolverlo?: He ejecutado la consulta inicial de exploración y el primer ejercicio de listar usuarios, tras haber dedicado la sesión a completar el 100% de SQL Cinema.
¿Qué he aprendido al resolverlo?: Que las mismas consultas SQL aprendidas con películas permiten analizar registros de seguridad en el mundo real.

3. Reflexión final y Autoevaluación

¿Qué concepto de SQL entiendo mejor ahora?: El uso de SELECT, FROM, WHERE y ORDER BY para extraer y ordenar información.
¿Qué ejercicio me ha resultado más difícil?: El módulo 7 (JOIN — Combinar tablas), porque juntar tablas diferentes ha sido lo más complejo.
¿Qué puedo hacer ahora que al principio no sabía hacer?: Consultar una base de datos real, filtrar datos y usar funciones de agregación.
¿Qué necesito seguir practicando?: Las uniones de tablas con JOIN y completar el resto de casos de SQL Agent.

Autoevaluación completada: Sé consultar datos de una tabla, sé filtrar y ordenar resultados, comprendo para qué sirven las funciones de agregación, he intentado al menos un reto de SQL Agent, he guardado ejemplos de consultas y mis aprendizajes, puedo explicar al menos una consulta que he escrito y he identificado qué necesito seguir practicando.
