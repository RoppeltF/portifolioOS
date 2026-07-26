import shlex


class CommandParser:

    @staticmethod
    def parse(line):

        line = line.strip()

        if not line:

            return "", []

        parts = shlex.split(line)

        return parts[0].lower(), parts[1:]