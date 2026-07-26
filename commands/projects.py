from app.shell.command import Command


class ProjectsCommand(Command):

    name = "projects"

    aliases = [
        "proj"
    ]

    description = "Show personal projects"

    usage = "projects"


    category = "Portfolio"


    help_text = """
projects

Displays personal and professional projects.

Usage:

projects
"""


    def execute(self, shell, args):

        return [

            "Projects",

            "",

            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━",

            "",

            "PortfolioOS",

            "",

            "Terminal-style portfolio website",

            "",

            "Technologies:",

            "• Python",

            "• Flask",

            "• HTML/CSS",

            "• JavaScript",

            "",

            "Features:",

            "• Interactive terminal",

            "• Command system",

            "• Virtual filesystem",

            "• GitHub integration",

            "",

            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━",

            "",

            "Irish Rail API Integration",

            "",

            "Python application using Irish Rail realtime services.",

            "",

            "Technologies:",

            "• Python",

            "• XML parsing",

            "• REST APIs",

            "",

            "Features:",

            "• Station lookup",

            "• Realtime train information",

            "• Data processing",

            "",

            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━",

            "",

            "Automation Tools",

            "",

            "Collection of scripts and utilities.",

            "",

            "Technologies:",

            "• Python",

            "• Bash",

            "• Linux",

        ]