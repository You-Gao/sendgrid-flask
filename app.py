from flask import Flask
from flask_smorest import Api

from blueprints.forward_blueprint import bp as forward_blueprint


app = Flask(__name__)

app.config["API_TITLE"] = "My API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.2"
app.config["OPENAPI_URL_PREFIX"] = "/api/docs"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdnjs.cloudflare.com/ajax/libs/swagger-ui/3.23.11/"
app.config["OPENAPI_REDOC_PATH"] = "/redoc"
app.config["OPENAPI_REDOC_URL"] = "https://cdn.jsdelivr.net/npm/redoc@next/bundles/redoc.standalone.js"

api = Api(app)
api.register_blueprint(forward_blueprint)

if __name__ == '__main__':
    app.run(debug=True)