from flask import Flask
from flask_restful import Api

from apispec import APISpec
from flask_apispec.extension import FlaskApiSpec
from apispec.ext.marshmallow import MarshmallowPlugin
from flask_jwt_extended import JWTManager

from resource.user import Users, User
from resource.login import Login, Register

app = Flask(__name__)
api = Api(app)
jwt = JWTManager(app)

# Swagger

## JWT swagger setting
### JWT Secret Key 的設定
app.config["JWT_SECRET_KEY"] = "secret_key"
### 為了讓 swagger 能長出鎖頭 （如附件1）
security_definitions = {
    "bearer": {
        "type": "apiKey",
        "in": "header",
        "name": "Authorization",
    }
}

app.config.update(
    {
        "APISPEC_SPEC": APISpec(
            title="Awesome Projectdfdfssdd",
            version="v1",
            ### 實際上帶入 swagger 的位置
            securityDefinitions=security_definitions,
            plugins=[MarshmallowPlugin()],
            openapi_version="2.0.0",
        ),
        "APISPEC_SWAGGER_URL": "/swagger/",  # URI to access API Doc JSON
        "APISPEC_SWAGGER_UI_URL": "/swagger-ui/",  # URI to access UI of API Doc
    }
)

docs = FlaskApiSpec(app)

# 註冊
api.add_resource(Users, "/users")
docs.register(Users)
api.add_resource(User, "/user/<int:id>")
docs.register(User)
api.add_resource(Login, "/login")
docs.register(Login)
api.add_resource(Register, "/Register")
docs.register(Register)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="10009", debug=True, use_reloader=True)

