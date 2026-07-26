from app.shell.command import Command
from app.shell.filesystem import Directory


class TreeCommand(Command):

    name = "tree"

    aliases = []

    description = "Display directory tree"

    usage = "tree [path]"


    help_text = """
tree

Display directory structure.

Usage:

tree [path]
"""


    def execute(self, shell, args):


        path = (
            args[0]
            if args
            else shell.cwd
        )


        node = shell.fs.get_node(
            path,
            shell.cwd
        )


        if node is None:

            return [
                "tree: path not found"
            ]


        output = [
            "."
        ]


        self.walk(
            node,
            "",
            output
        )


        return output



    def walk(
        self,
        node,
        prefix,
        output
    ):


        if not isinstance(
            node,
            Directory
        ):

            return


        items = list(
            node.children.values()
        )


        for index, item in enumerate(items):


            last = index == len(items)-1


            connector = (
                "└── "
                if last
                else "├── "
            )


            output.append(
                prefix +
                connector +
                item.name
            )


            if isinstance(
                item,
                Directory
            ):


                extension = (
                    "    "
                    if last
                    else "│   "
                )


                self.walk(
                    item,
                    prefix + extension,
                    output
                )