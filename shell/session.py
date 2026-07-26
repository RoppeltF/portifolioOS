from flask import session


DEFAULT_SESSION = {
    "cwd": "/home/roberto",
    "history": []
}


def get_shell_session():

    if "shell" not in session:
        session["shell"] = DEFAULT_SESSION.copy()

    return session["shell"]


def save_shell_session(data):

    session["shell"] = data
    session.modified = True