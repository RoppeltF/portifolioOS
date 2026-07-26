from app.shell.command import Command

class WhoamiCommand(Command):

    name = "whoami"

    aliases = []

    description = "Display current user"

    usage = "whoami"

    category = "General"


    def execute(self, shell, args):

        return [

                "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@",
                "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@",
                "@@@@__░█▀▄░█▀█░█▀▄░█▀▀░█▀▄░▀█▀░█▀█░░░█▀█░█▀█░█▀█░█▀▀░█░░░▀█▀░░░█▀▀░▀█▀░█░░░█░█░█▀█____@@@",
                "@@@@__░█▀▄░█░█░█▀▄░█▀▀░█▀▄░░█░░█░█░░░█░█░█▀▀░█▀▀░█▀▀░█░░░░█░░░░█▀▀░░█░░█░░░█▀█░█░█____@@@",
                "@@@@__░▀░▀░▀▀▀░▀▀░░▀▀▀░▀░▀░░▀░░▀▀▀░░░▀▀▀░▀░░░▀░░░▀▀▀░▀▀▀░░▀░░░░▀░░░▀▀▀░▀▀▀░▀░▀░▀▀▀____@@@",
                "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@",
                "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@",
                "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@",
                "@@xxxxxxx;+xx+++++x++$xXXxxxxXX$X$X;X$X$$$$$$$X$XXXXXxxxxx;xxxXXXXX$X$XXXXXXXX$X$XXXXXX@@ Hi there, ",
                "@@xxxxxxxx+xxxx$$$XXXXXxxxXxX$xX$Xxx$xX$xx:::::::::;::::;;::::::::::::::::;;;;;;;;;;:::@@",
                "@@xxxxxxxx+xx$XxXXX$xxxxxxx$xx$$$$$$X$$$X$x::::::::::::::::::::::::;:.::;xx;;;;;xxxxxxx@@ I'm an IT professional with over 10 years of",
                "@@xxxxxxxx+X$xxxXXxxXxxx$$$XX$$$$$$$$$$$$$x;;;;;;;;;+++++++;;;;;;;x::+;;;;;;;;;;;;;;;;;@@ experience supporting enterprise environments",
                "@@xxxxxxxxXXxxXXxxX$$$$$$$$$$$Xxxxxxxx+::x$$;;;;;;;;;;;;;;;;;;;;;x:.:.x;;;;;;;;;;++x+;;@@ Throughout my career I've worked in technical",
                "@@xxxxxxxx$xxXX$$$$$$$$$$$X+;::::::::::::::$;;;;;;;;;;;;;;;;;;;x:.:.::;;;;;;+;:::;:+:;:@@ support, incident management, and customer",
                "@@xxxxxxx$X$$$XX$xX$$$$$x;::::::::::::::::::x;;;;;;;;;;;;;;;;;;;+:.:.:.;x;:::::;:::::;;@@ service. My technical background includes",
                "@@xxxxxx$$$$X$$$X$Xx$XX$+::::::::::::::::::::x;;;;;;;;;;;;;;;;;;;:;;:xx;::xxxx;;;;:.;::@@ Windows and Linux administration,",
                "@@xxxxxx$&$$$$$$$$$$X$$$x:::::::::::::::::::X$$+++;;;;;;;;;;;;;x::.::;::+;::::x;:;x+;:;@@ Active Directory, SCCM, PoweShell,",
                "@@xxxxxxx&$$$$$$$$$$$$$$$;::::::::xxX$x:::;xxx;;::x+;;;;;;;;;;;+.:.:;;x++;x$;:+;:+x::x;@@ Python, along with troubleshooting hardware",
                "@@xxxxxxxX&$$$$$$$$$$$$$X;:::::x$$xxxxxX;:+xXxxxxxx$x;;;;;;;;;++:.:;::x;xxXx;x+xXXx:;xx@@ software and networking issues.",
                "@@xxxxxxxX&$$$$$$$$$$$$X;::::;x;;;++xxx+xx;xXxX;;;;x+;+++++;+++x::x:;x::xx+:::::::;X$;:@@",
                "@@xxxxxxxx$&$$$$$$$$$$$;:::::;:;;x;x$+;;:x:::X:xx+xXxxxxxxxxxxxxx+X:x:::x;::::::::::;Xx@@ Today I'm expanding my focus toward ",
                "@@xxxxxxxxX$$$$$$$&&&&&xxxxxxxxxx$::;;::;x;:::;;+xXxxxxxxxxxxxxx;:x;x::::::::::::::::;;@@ software development, building projects ",
                "@@xxxxxxxxx$&$&x;;xx$$$X;;;;:::::x+:;:::+x::::::xxxxxxxxxxxxxxxx:::++x::::::::::::::::x@@ with Python, Flask, Linux, web technologies.",
                "@@xxxxxxxxxx&&x;xx;:;X$X;::;;;:::::x::;$+;:;x+xx:$xxxxxxxxxxxxxx:;:x;x:::::::::::::::;;@@",
                "@@xxxxxxxxxxX&xx;:+x;;xXx;:::::::::::::::+xXxx$x;$xxxxxxxxxxxxxx:;:;xx;:::::::::::::;x:@@",
                "@@xxXxxxxxxxx$X:;;x;+:;xxx:::::::::::::::xxX$$xxxxx+++;;;:::;;;+;::;:xxx::::::::::::xx:@@",
                "@@xxXxxxxxxxxX$$;::::;:;XXx;;::::::::::xxxx+xxxxx$x+++++++++++++;::;::Xxx::::::::::xx:.@@",
                "@@xxXxxxxxxxxxX&$x;::::;X$xxxxx;;;:::;xXXxx;:::;:$$xxxxxxxxxxxxxxxxxxx++x;::::::::;$$Xx@@",
                "@@xxXXxxxxxx;X$&&Xxx$$$xxXxXxxxxxx+;::xx::::xXXX;x$$$$$$$$$$$$$$$$$$$$++x+::::::::;&$$$@@",
                "@@xxXxxxxxxx$x$$XXX+;;;:;$$$X$xxxxxxx;+xx::::;xxx;x$XXXXXXXXXXxxxxxxxx;xx+::::::::;$xxx@@",
                "@@xxxXxxxxx$xxxxX$XXX;;:;+X$$X$$XXxxxxx$Xxxx;x+xxxX$xxxxxxxxxxxxxxxxX;xxx+::::::::;$$$$@@",
                "@@xxxXxxxXX$xxxx+;;xxXx;::;xX$$$$$$X$$$$XXxxxXXXX$$xxxxxxxxxxxxxxxxXx;xxx+::::::::;$$$$@@",
                "@@xxxxx$xx;xx;+xxxxx+xx$$+:;;xxxX$$$$$$$$$$$$$$&$xxxxxxxxxxxxxxxxxxx;+xxx+:::::::::x$$$@@",
                "@@;;;x;+++xx;;;;;;+xXXxXXX$X+:;xxxxxxxXxX$$xXxx++x++xXxxxxxxxxxxxxX;;xxxX;:::::::::x$$$@@",
                "@@;xx;;;;+x;;;;+++xxx+;xX$X$$$$xxxxxxxxx$&$+xxxxxXxxxxxxxxxxxxxxxX::+xxxx::::::::::;$$+@@",
                "@@$Xx;;;;;x;;;;;;;;;;;;;;;;;;xxX$$$$$xx$&$&$xxxxxxXXx++;+x$$xxxxx::+xxxxx:::::::::::x::@@",
                "@@xxx;;;;x+;;;;;;;;++xXX$$$$$$$$xxx+x$$$$$$$xxXxxxXxxxxx+x++x+xXx:;xxxxxx:::::::::::x;;@@",
                "@@xxxx;;xx;;;;;;+xxxxx+;;;;;;;;;;;;xxxx$$$X$XxxXXX$Xxxxxxxxxx+xxx$xxxxxx;:::::::::::;x:@@",
                "@@xxxx++x;;;;;+xxx+;;;xxxxxx+;;;;;;xxxxxxxX$$XxX$$$XxxxxxxxXxxxXxx$xxxxx::::::::::::;x:@@",
                "@@xxxxxx;+++xxxxx;+xxxxxx+;;;;+xxxxx+xxxxxXx$XXx$$$XxxXxxxXXxxxxX$XX$Xxx::::::::::::;xx@@",
                "@@xxxxxxxxxxxxxxxxxxxxxx+;+xxx++;;;xxxxxxxxx$$Xx$&&$$$XX$XXXXxXxXX$$XXX:::::::::::::;xx@@",
                "@@xxx+xxxxxxxxxxxxxxxxxxxxxxxxx+xxxxxx+;;;;;+xx$$&&$$$$$X$$xXX$xx$X$$$+:::::::::::::;xx@@",
                "@@xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx+;;;+xxxxxxxxxxX&&$&&$$$$X$$$$XX$$$$x::::::::::::::;+X@@",
                "@@xxxXxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx+$$&&&&&&$&$$$XXX$$X$;:::::::::::::::;X@@",
                "@@xxxXxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx;;xxx$&&&&$$XXXXX$$x:::::::::::::::;;$@@",
                "@@xxx$xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx+;;xx;;xxxxxx&Xx$$$$xx::::::::::::::::;X@@",
                "@@xxXX$xXxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx;;xXXx;+x;+xxX+xxxxxxXxx;::::::::::::;:;X@@",
                "@@XXXX$xXxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx+;+xxXxx;;xx;xxxxxxXxxxXxXxxx::::::::::::;;X@@",
                "@@XXXX$XxXXXXXxxxxxxxxxxxxxxxxxxxxxxxxxx+xxxXXXxx+;+xx;xXxxxxxxxxxxxxxxxx;:::::::::;:+X@@",
                "@@XXXXX$xXXXXXXXXXXxxxxxxxxxxxxxxxxxxxXXXXXXXxx+;xxXx;xXxxxxxxxxxxxXxXxxxxx;:::::;::;x$@@",
                "@@XXXXXX$xXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXxxxxxxxXXx+;xXxxxxxxxxxXxxXXx$$Xxxxxxxxxxxxx$$@@",
                "@@XXXXXXX$XXXXXXXXXXXXXXXXXXXXXXXXXXXXxxxxxxxXXxx;;xXXxxxxxxxxxx$xxXXxx$$X$XX$XXX$$$$$$@@",
                "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@",
                "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@",
                "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@",


            
        ]
