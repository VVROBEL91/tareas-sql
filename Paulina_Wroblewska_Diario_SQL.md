DIARIO DE APRENDIZAJE SQL
Alumna: Paulina Wroblewska

1. Registro de consultas SQL

A) Consulta básica comprendida:
- Código SQL: SELECT * FROM peliculas;
- Resultado que obtiene: Muestra la tabla completa con las 25 películas de la base de datos cine_db y todas sus columnas.
- Explicación breve: SELECT * selecciona todas las columnas de la tabla y FROM peliculas indica de qué tabla se deben extraer los datos.

B) Consulta con filtro u ordenación:
- Código SQL: SELECT titulo, puntuacion FROM peliculas WHERE puntuacion >= 8 ORDER BY puntuacion DESC;
- Resultado que obtiene: Devuelve una lista con los títulos y puntuaciones de las películas mejor valoradas (nota igual o mayor a 8), ordenadas de mayor a menor puntuación.
- Explicación breve: WHERE aplica un filtro para mostrar únicamente las filas que cumplen la condición numérica, y ORDER BY ... DESC ordena esos resultados de forma descendente.

C) Consulta difícil o que ha supuesto un reto:
- Código SQL: SELECT peliculas.titulo, directores.nombre FROM peliculas JOIN directores ON peliculas.director_id = directores.id;
- Resultado que obtiene: Muestra el título de cada película junto al nombre de su director combinando la información de dos tablas distintas.
- Explicación breve: Utiliza la instrucción JOIN para unir la tabla de películas con la de directores a través de la columna en común que comparten (director_id e id).

2. Reto de SQL Agent

- Qué pedía el reto?: Observar los eventos de acceso en la tabla eventos_login para iniciar una investigación de seguridad (ver quién intentó entrar, cuándo y desde dónde).
- Qué consulta he escrito?: SELECT * FROM eventos_login;
- Ha conseguido resolverlo?: Sí, he ejecutado la consulta inicial de exploración y el primer ejercicio de listar usuarios tras haber completado los módulos de SQL Cinema.
- Qué ha aprendido al resolverlo o al revisar el resultado?: He aprendido que las mismas instrucciones básicas de SQL que se practican con bases de datos de películas se aplican exactamente igual para analizar registros de eventos y ciberseguridad en casos reales.

3. Reflexión final

- Qué concepto de SQL entiendo mejor ahora?: El uso de la estructura principal (SELECT, FROM, WHERE y ORDER BY) para extraer, filtrar y ordenar datos de una tabla.
- Qué ejercicio me ha resultado más difícil?: Las uniones de tablas mediante JOIN en el módulo correspondiente, ya que conectar distintas tablas requiere identificar con precisión sus relaciones.
- Qué puedo hacer ahora que al principio no sabía hacer?: Consultar bases de datos desde cero, aplicar filtros avanzados, ordenar resultados y comprender cómo se estructuran las consultas de información.
- Qué necesito seguir practicando?: Seguir practicando las combinaciones complejas de tablas con JOIN y profundizar en los retos de análisis e investigación de SQL Agent.
