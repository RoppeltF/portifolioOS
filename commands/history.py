from app.shell.command import Command


class HistoryCommand(Command):

    name = "history"

    aliases = []

    description = "Show command history"

    usage = "history"


    def execute(self, shell, args):

        return [

            "History is managed by the frontend."

        ]