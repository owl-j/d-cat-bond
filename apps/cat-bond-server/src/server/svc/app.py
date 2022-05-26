from flask import Flask, jsonify, make_response
from flask_cors import CORS

from server.svc.cat_bond_server_api import cat_bond_server_api_blueprint

app = Flask(__name__)

cors = CORS(app, resources={r"/*": {"origins": "*"}})


@app.route("/")
def app_root():
    data = {"status": "OK"}
    return make_response(jsonify(data), 200)


@app.route("/healthz")
def app_healthz():
    data = {"status": "OK"}
    return make_response(jsonify(data), 200)


@app.route("/livez")
def app_livez():
    data = {"status": "OK"}
    return make_response(jsonify(data), 200)


@app.route("/readyz")
def app_readyz():
    data = {"status": "OK"}
    return make_response(jsonify(data), 200)


def app_register_blueprints(app_, *blueprints):
    for blueprint in blueprints:
        app_.register_blueprint(blueprint, url_prefix="/" + blueprint.name)


app_register_blueprints(app, cat_bond_server_api_blueprint)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7000, threaded=True)
