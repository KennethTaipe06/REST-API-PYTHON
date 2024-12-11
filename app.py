from flask import Flask
from flasgger import Swagger

# Crea una instancia de la aplicación Flask
app = Flask(__name__)

# Inicializa Swagger para la documentación automática de la API
swagger = Swagger(app)

# Define una ruta para el endpoint /api/hello con el método GET
@app.route('/api/hello', methods=['GET'])
def hello_world():
    """
    Un endpoint simple de hola mundo.
    ---
    responses:
      200:
        description: Un mensaje simple de hola mundo
        content:
          text/html:
            schema:
              type: string
              example: "<h1>Hola Mundo</h1>"
    """
    # Responde con un mensaje de hola mundo en HTML
    return "<h1>Hola Mundo</h1>"

# Punto de entrada de la aplicación
if __name__ == '__main__':
    # Ejecuta la aplicación en el host 0.0.0.0 y el puerto 5000 en modo debug
    app.run(host='0.0.0.0', port=5000, debug=True)