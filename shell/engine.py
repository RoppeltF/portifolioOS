from .registry import CommandRegistry
from .parser import CommandParser
from .filesystem import VirtualFileSystem
from difflib import get_close_matches

class Shell:

    def __init__(self):

        self.registry = CommandRegistry()

        self.fs = VirtualFileSystem()

        self.cwd = "/home/roberto"


    def execute(self, line):

        command_name, args = CommandParser.parse(line)


        if not command_name:

            return []


        command = self.registry.get(command_name)


        if command is None:

            return self.command_not_found(
                command_name
            )


        return command.execute(
            self,
            args
        )



    def command_not_found(self, command_name):

        output = [

            f"{command_name}: command not found"

        ]


        suggestions = get_close_matches(
            command_name,
            self.registry.names(),
            n=3,
            cutoff=0.5
        )


        if suggestions:
            output.extend(
                [
                    "",
                    "Did you mean:"
                ]
            )
            for suggestion in suggestions:

                output.append(
                    f"  {suggestion}"
                )
    
        return output