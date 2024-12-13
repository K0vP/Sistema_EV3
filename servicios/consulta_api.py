import http.client
import json

# Definir la clave de API como una variable fija
API_KEY = "a6c0eae16270843eefb2313e17a7a7199489f815"

def buscar_en_serper(query):
    conn = http.client.HTTPSConnection("google.serper.dev")  # Conexión a la API de Serper
    payload = json.dumps({
        "q": query  # El string de búsqueda
    })
    headers = {
        'X-API-KEY': API_KEY,  # Autenticación con la clave de API
        'Content-Type': 'application/json'
    }

    try:
        conn.request("POST", "/search", payload, headers)  # Realiza la solicitud POST
        res = conn.getresponse()  # Obtiene la respuesta
        data = res.read()  # Lee los datos de la respuesta
        if res.status == 200:
            return json.loads(data.decode("utf-8"))  # Retorna los resultados en formato JSON
        else:
            print(f"Error: {res.status} - {res.reason}")
            return None
    except Exception as e:
        print(f"Error en la solicitud: {e}")
        return None
    finally:
        conn.close()  # Cierra la conexión
