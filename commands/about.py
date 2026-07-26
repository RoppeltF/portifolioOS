from app.shell.command import Command


class AboutCommand(Command):

    name = "about"

    aliases = []

    description = "About Roberto"

    usage = "about"


    def execute(self, shell, args):

        return [ 
             "Hi there,"
                "",
                "I'm an IT professional with over 10 years of experience supporting enterprise environments, solving technical problems, and helping customers across global companies including Amazon, Dell Technologies, and HCL Technologies.",
                "",
                "",
                "Throughout my career I've worked in technical support, incident management, and customer service, always focusing on practical solutions that improve both user experience and business processes.",
                "",
                "",
                "My technical background includes Windows and Linux administration, Active Directory, SCCM, Workspace ONE, PowerShell and Python, along with troubleshooting hardware, software and networking issues.",
                "",
                "",
                "Today I'm expanding my focus toward software development, building projects with Python, Flask, Linux, and modern web technologies."
                
                ]                                                        



