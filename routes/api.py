from flask import Blueprint, jsonify, request

from app.shell.engine import Shell

api_bp = Blueprint("api", __name__)

shell = Shell()


@api_bp.post("/command")
def command():

    data = request.get_json()

    cmd = data.get("command", "")

    output = shell.execute(cmd)

    return jsonify(output)
