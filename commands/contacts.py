from app.shell.command import Command


class ContactCommand(Command):

    name = "contact"

    aliases = [
        "reach"
    ]

    description = "Show contact information"

    usage = "contact"


    category = "Resources"


    help_text = """
contact

Displays contact information.

Usage:

contact
"""


    def execute(self, shell, args):

        return [

            "Contact Information",

            "",

            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━",

            "",

            "Roberto Oppelt Filho",

            "",

            "Email:",

            "your.email@example.com",

            "",

            "GitHub:",

            "github.com/RoppeltF",

            "",

            "LinkedIn:",

            "linkedin.robertooppeltfilho.com",

            "",

            "Location:",

            "Ireland",

            "",

            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━",

            "",

            "Available for:",

            "• Python Development",

            "• IT Support",

            "• Technical Support",

            "• Incident Management",

        ]