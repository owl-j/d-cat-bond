__contributors__ = ["Oliver Johnson"]


from flask import Blueprint, request

from server import cat_bond_server_apis
from server.handlers.handle_cat_bond_server_api import (
    handle_api_tiles_sensors_observation_GET, handle_api_tiles_validation_GET)

cat_bond_server_api_blueprint = Blueprint("cat-bond-server-api", __name__)


@cat_bond_server_api_blueprint.route(
    cat_bond_server_apis.tiles_validation_GET,
    methods=["GET"],
)
def api_tiles_validation_GET():
    got = request.args
    res = handle_api_tiles_validation_GET(got)
    return {"res": res}


@cat_bond_server_api_blueprint.route(
    cat_bond_server_apis.tiles_sensors_observation_GET,
    methods=["GET"],
)
def api_tiles_sensors_observation_GET():
    got = request.args
    res = handle_api_tiles_sensors_observation_GET(got)
    return {"res": res}
