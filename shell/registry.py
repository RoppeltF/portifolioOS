from app.commands.education import EducationCommand
from app.commands.help import HelpCommand
from app.commands.about import AboutCommand
from app.commands.clear import ClearCommand
#from app.commands.history import HistoryCommand
from app.commands.projects import ProjectsCommand
from app.commands.pwd import PwdCommand
from app.commands.whoami import WhoamiCommand
from app.commands.man import ManCommand
from app.commands.ls import LsCommand
from app.commands.tree import TreeCommand
from app.commands.cd import CdCommand
from app.commands.cat import CatCommand
from app.commands.exp import ExperienceCommand
from app.commands.education import EducationCommand
from app.commands.projects import ProjectsCommand
from app.commands.contacts import ContactCommand



class CommandRegistry:

    def __init__(self):

        self.commands = {}

        self.register(HelpCommand())
        self.register(AboutCommand())
        self.register(ClearCommand())
        # self.register(HistoryCommand())
        self.register(PwdCommand())
        self.register(WhoamiCommand())
        self.register(ManCommand())
        self.register(CatCommand())
        self.register(LsCommand())
        self.register(TreeCommand())
        self.register(CdCommand())
        self.register(ExperienceCommand())
        self.register(EducationCommand())
        self.register(ProjectsCommand())
        self.register(ContactCommand())



    def register(self, command):

        self.commands[command.name] = command

        for alias in command.aliases:

            self.commands[alias] = command


    def get(self, name):

        return self.commands.get(name)


    def names(self):

        return sorted(self.commands.keys())
    
    def all_commands(self):

        seen = set()

        commands = []


        for command in self.commands.values():

            if command.name not in seen:

                commands.append(command)

                seen.add(command.name)


        return commands