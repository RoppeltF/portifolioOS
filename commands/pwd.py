from app.shell.command import Command


class PwdCommand(Command):

    name = "pwd"

    aliases = []

    description = "Print current directory"

    usage = "pwd"

    help_text = """
pwd

Prints the current working directory.

Usage:

pwd
"""


    def execute(self, shell, args):

        return [
            shell.cwd
        ]