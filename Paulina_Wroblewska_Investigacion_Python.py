
FICHA DE INVESTIGACIÓN: SQL + Python + IA
Alumna: Paulina Wroblewska


# ==========================================
# RETO 1. Comprende los conceptos básicos
# ==========================================
# 1. Qué es SQL?: Un lenguaje para consultar, filtrar y extraer información de bases de datos.
# 2. Qué es Python?: Un lenguaje de programación claro y versátil para automatizar y analizar datos.
# 3. Diferencia?: La base de datos es el archivo donde se guardan las tablas ordenadas, y Python es el lenguaje que procesa y calcula con esos datos.
# 4. Para qué sirve SQLite?: Un motor de base de datos ligero que guarda todo en un único archivo local, ideal para aprender.
# 5. Por qué juntos?: SQL extrae exactamente los datos necesarios de tablas grandes, y Python los analiza o procesa.


# ==========================================
# RETO 2. Investiga cómo se conectan
# ==========================================
# - import sqlite3: Carga el módulo nativo de Python para manejar bases de datos SQLite.
# - sqlite3.connect(): Abre o crea el archivo de la base de datos.
# - execute(): Envía y ejecuta una instrucción SQL desde el código de Python.
# - fetchall(): Recupera en una lista todos los registros que devolvió la consulta.
# - close(): Cierra la conexión con la base de datos de forma segura.


# RETO 3. Detective de código (Ejemplo práctico)

import sqlite3

def ejecutar_ejemplo_sql_python():
    print("--- INICIANDO PRUEBA DE SQL Y PYTHON ---")
    
    # 1. Conectar a una base de datos local llamada 'practica.db'
    conexion = sqlite3.connect("practica.db")
    cursor = conexion.cursor()

    # 2. Crear una tabla de prueba si no existe e insertar un registro
    cursor.execute("CREATE TABLE IF NOT EXISTS usuarios (nombre TEXT, edad INTEGER)")
    
    # Insertamos un dato de ejemplo de forma segura
    cursor.execute("INSERT INTO usuarios VALUES ('Ana', 25)")
    conexion.commit()

    # 3. Dónde está escrita la consulta y qué recupera:
    # La consulta SQL está dentro del método execute() y busca todos los registros de 'usuarios'.
    cursor.execute("SELECT * FROM usuarios")

    # 4. Cómo se reciben los resultados:
    # fetchall() convierte las filas obtenidas en una lista de Python que podemos recorrer o imprimir.
    resultados = cursor.fetchall()
    print("Resultados recuperados de la base de datos:", resultados)

    # 5. Cerrar la conexión correctamente
    conexion.close()
    print("--- CONEXIÓN CERRADA CON ÉXITO ---")

# Si ejecutas este archivo, se pondrá en marcha la función de prueba:
if __name__ == "__main__":
    ejecutar_ejemplo_sql_python()


# RETO 4. Comprueba lo que has aprendido

# 1. Qué instrucción conecta la BD? -> sqlite3.connect()
# 2. Qué método recupera todos los resultados? -> fetchall()
# 3. Por qué es útil SQLite para empezar? -> Porque no requiere servidores externos, todo vive en un archivo local.


# RETO 5. Reflexión final

Reflexión:
Ahora entiendo que SQL y Python pueden trabajar juntos porque SQL se encarga 
de buscar,filtrar y extraer de forma eficiente los datos que necesitamos de las tablas, mientras que Python procesa esa información, realiza cálculos y automatiza  los análisis de manera muy sencilla
