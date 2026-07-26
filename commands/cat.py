from app.shell.command import Command
from app.shell.filesystem import File


class CatCommand(Command):

    name = "cat"

    aliases = []

    description = "Display file contents"

    usage = "cat <file>"


    help_text = """
cat

Display the contents of a file.

Usage:

cat <file>
"""


    def execute(self, shell, args):

        if not args:

            return [
                "Usage: cat <file>"
            ]


        path = args[0]


        node = shell.fs.get_node(
            path,
            shell.cwd
        )


        if node is None:

            return [
                f"cat: {path}: No such file"
            ]


        if not isinstance(
            node,
            File
        ):

            return [
                f"cat: {path}: Is a directory"
            ]


        return node.content.splitlines()