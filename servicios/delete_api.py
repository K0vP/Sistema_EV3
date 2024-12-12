def crear_sentencia_delete(nombre_tabla, condiciones):
    if not condiciones:
        raise ValueError("Se requieren condiciones para la sentencia DELETE.")
    condiciones_sql = " AND ".join([f"{columna} = ?" for columna in condiciones.keys()])
    valores = tuple(condiciones.values())
    sentencia = f"DELETE FROM {nombre_tabla} WHERE {condiciones_sql}"
    return sentencia, valores
