from app.shell.command import Command


class HelpCommand(Command):

    name = "help"

    aliases = []

    description = "Show available commands"

    usage = "help"


    help_text = """
help

Displays all available terminal commands.

Usage:

help
"""


    def execute(self, shell, args):

        output = [

            "PortfolioOS Terminal",

            "",

            "Available commands:",

            ""

        ]


        commands = sorted(
            shell.registry.all_commands(),
            key=lambda cmd: cmd.name
        )


        for command in commands:


            # Main command + description
            line = (
                f"{command.name:<15}"
                f" - {command.description}"
            )


            # Display aliases if they exist
            if command.aliases:

                line += (
                    f" "
                    f"(alias: {', '.join(command.aliases)})"
                )


            output.append(line)



        output.extend(
            [

                "",

                "Type 'man <command>' for detailed information.",

                "Type 'help <command>' to see command usage."

            ]
        )


        return output