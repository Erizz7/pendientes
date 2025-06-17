import mysql.connector

def conectar(consulta_sql):
    configuracion = {
        'user': 'uuncs1uwrazade6d',
        'password': 'qxINV1wXerGuuorgfY8Y',
        'host': 'bzi6cvcgslprvvbbghzr-mysql.services.clever-cloud.com',
        'database': 'bzi6cvcgslprvvbbghzr',
        'raise_on_warnings': True
    }

    try:
        conexion = mysql.connector.connect(**configuracion)
        print('Conexion Realizada')

        consulta = conexion.cursor()
        print("Consulta ejecutada:", consulta_sql)
        consulta.execute(consulta_sql)
        resultado = consulta.fetchall()

        consulta.close()
        conexion.close()
        return resultado
    
    except mysql.connector.Error as err:
        print(f"No fue posible conectarse a la base de datos: {err}")
        return []