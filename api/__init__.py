from flask import Flask


def create_app():

    app = Flask(__name__)
    from api.views.controllers import parcel_blueprint as parcel_blueprint

    app.register_blueprint(parcel_blueprint)

    return app

