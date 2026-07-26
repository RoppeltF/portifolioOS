from app.shell.command import Command


class ClearCommand(Command):

    name = "clear"

    aliases = ["cls"]

    description = "Clear terminal"

    usage = "clear"

    help_text = """
clear

Clears the terminal screen.

Usage:

clear
"""

    def execute(self, shell, args):

        return [

            "__CLEAR__"

        ]