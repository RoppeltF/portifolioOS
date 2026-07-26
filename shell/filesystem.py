from pathlib import PurePosixPath


class File:

    def __init__(self, name, content=""):

        self.name = name
        self.content = content



class Directory:

    def __init__(self, name):

        self.name = name
        self.children = {}



    def add(self, item):

        self.children[item.name] = item



class VirtualFileSystem:


    def __init__(self):

        self.root = Directory("/")

        self.build()


    def build(self):

        home = Directory("home")

        self.root.add(home)


        roberto = Directory("roberto")

        home.add(roberto)



        roberto.add(
            File(
                "README.md",
                """
# Roberto Oppelt Filho

Python Developer
DevOps Engineer

Welcome to my interactive portfolio.
"""
            )
        )


        # ABOUT

        about = Directory("about")

        roberto.add(about)


        about.add(
            File(
                "profile.txt",
                """
Roberto Oppelt Filho

Python developer focused on:

- Flask
- Automation
- Linux
- Docker
- APIs
"""
            )
        )


        # EXPERIENCE

        experience = Directory("experience")

        roberto.add(experience)


        experience.add(
            File(
                "amazon.txt",
                """
Amazon

Selling Partner Support Associate

Oct 2022 - Present

Supporting Amazon Selling Partners,
solving technical and platform issues.
"""
            )
        )


        experience.add(
            File(
                "hcl.txt",
                """
HCL Technologies

Critical Incident Management

Supported LATAM and North America
incident response processes.
"""
            )
        )


        # PROJECTS

        projects = Directory("projects")

        roberto.add(projects)


        flask_project = Directory(
            "flask-portfolio"
        )

        projects.add(flask_project)


        flask_project.add(
            File(
                "README.md",
                """
Flask Portfolio Website

Python backend
Bootstrap frontend
Minimal JavaScript
"""
            )
        )


        rail = Directory(
            "irish-rail-api"
        )

        projects.add(rail)


        rail.add(
            File(
                "README.md",
                """
Irish Rail API project.

Realtime train information
using Python.
"""
            )
        )


        # SKILLS

        skills = Directory("skills")

        roberto.add(skills)


        skills.add(
            File(
                "stack.txt",
                """
Python
Flask
Docker
Linux
Git
SQL
REST APIs
"""
            )
        )


        # CONTACT

        contact = Directory("contact")

        roberto.add(contact)


        contact.add(
            File(
                "links.txt",
                """
GitHub:
github.com/RoppeltF

LinkedIn:
linkedin.robertooppeltfilho.com
"""
            )
        )


    def normalize_path(self, path, cwd):

        if not path:

            return cwd


        if not path.startswith("/"):

            path = str(
                PurePosixPath(cwd) / path
            )


        parts = []

        for part in PurePosixPath(path).parts:

            if part in ["/", "."]:

                continue


            if part == "..":

                if parts:

                    parts.pop()

            else:

                parts.append(part)


        return "/" + "/".join(parts)


    def get_node(self, path, cwd="/"):

        if not path:

            path = cwd


        # Relative path
        if not path.startswith("/"):

            path = str(
                PurePosixPath(cwd) / path
            )


        # Normalize path
        path = self.normalize_path(
            path,
            cwd
        )


        if path == "/":

            return self.root


        parts = [
            p for p in PurePosixPath(path).parts
            if p != "/"
        ]


        current = self.root


        for part in parts:


            if not isinstance(
                current,
                Directory
            ):

                return None


            current = current.children.get(part)


            if current is None:

                return None


        return current