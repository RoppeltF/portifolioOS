from app.shell.command import Command
from app.shell.filesystem import Directory


class LsCommand(Command):

    name = "ls"

    aliases = []

    description = "List directory contents"

    usage = "ls [path]"


    help_text = """
ls

Lists files and directories.

Usage:

ls [path]
"""


    def execute(self, shell, args):

        path = (
            args[0]
            if args
            else shell.cwd
        )


        node = shell.fs.get_node( path, shell.cwd )


        if node is None:

            return [
                f"ls: cannot access {path}"
            ]


        if not isinstance(
            node,
            Directory
        ):

            return [
                node.name
            ]


        return sorted(
            node.children.keys()
        )