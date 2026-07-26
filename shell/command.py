from abc import ABC, abstractmethod


class Command(ABC):

    name = ""

    aliases = []

    description = ""

    category = "General"

    usage = ""

    help_text = ""



    @abstractmethod
    def execute(self, shell, args):
        pass


    def help(self):

        return [
            self.help_text
        ]