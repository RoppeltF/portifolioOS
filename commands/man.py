from app.shell.command import Command


class ManCommand(Command):

    name = "man"

    aliases = []

    description = "Display command manual"

    usage = "man <command>"

    help_text = """
man

Displays the manual page of a command.

Usage:

man <command>

Example:

man ls
"""


    def execute(self, shell, args):

        if not args:

            return [

                "Usage: man <command>"

            ]


        command_name = args[0]


        command = shell.registry.get(
            command_name
        )


        if command is None:

            return [

                f"man: no manual entry for {command_name}"

            ]


        return [

            f"{command.name.upper()}(1)",

            "",

            command.help_text

        ]