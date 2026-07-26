from app.shell.command import Command


class EducationCommand(Command):

    name = "education"

    aliases = [
        "edu"
    ]

    description = "Show education history"

    usage = "education"


    category = "Portfolio"


    help_text = """
education

Displays education and academic background.

Usage:

education
"""


    def execute(self, shell, args):

        return [

            "Education",

            "",

            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━",

            "",

            "Academic Background",

            "",

            "Information Technology",

            "",

            "Focused on:",

            "• Systems administration",

            "• Networking",

            "• Software and hardware troubleshooting",

            "• IT infrastructure",

            "",

            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━",

        ]