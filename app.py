from flask import Flask
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

@app.route('/api/hello', methods=['GET'])
def hello_world():
    """
    A simple hello world endpoint.
    ---
    responses:
      200:
        description: A simple hello world message
        content:
          text/html:
            schema:
              type: string
              example: "<h1>Hola Mundo</h1>"
    """
    return "<h1>Hola Mundo</h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)