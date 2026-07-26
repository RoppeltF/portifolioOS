from flask import (
    Blueprint,
    request,
    jsonify
)

from app.shell.engine import Shell
from ..static.boot.boot import get_boot_sequence


terminal_bp = Blueprint(
    "terminal",
    __name__
)


shell = Shell()


@terminal_bp.post("/command")
def command():

    data = request.json

    output = shell.execute(
        data.get(
            "command",
            ""
        )
    )

    return jsonify(
        {
            "output": output,
            "cwd": shell.cwd
        }
    )


@terminal_bp.get("/boot")
def boot():

    return jsonify(
        get_boot_sequence()
    )