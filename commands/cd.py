from app.shell.command import Command
from app.shell.filesystem import Directory


class CdCommand(Command):

    name = "cd"

    aliases = []

    description = "Change directory"

    usage = "cd <directory>"


    help_text = """
cd

Change the current directory.

Usage:

cd <directory>

Examples:

cd projects
cd ..
cd /home/roberto
"""


    def execute(self, shell, args):

        if not args:

            shell.cwd = "/home/roberto"

            return []


        target = args[0]


        new_path = shell.fs.normalize_path(
            target,
            shell.cwd
        )


        node = shell.fs.get_node(
            new_path
        )


        if node is None:

            return [
                f"cd: no such file or directory: {target}"
            ]


        if not isinstance(
            node,
            Directory
        ):

            return [
                f"cd: not a directory: {target}"
            ]


        shell.cwd = new_path


        return []