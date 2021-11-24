import connexion
from flask_cors import CORS

# Create the application instance
app = connexion.App(__name__, specification_dir="./")
CORS(app.app)

# Read the swagger.yaml file to configure the endpoints
app.add_api('ecommerce.yaml')


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)
