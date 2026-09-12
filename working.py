import os 
import requests
import webbrowser
import random
from datetime import datetime
import time
from http.server import HTTPServer, SimpleHTTPRequestHandler
from colorama import init, Fore

init(autoreset=False)

class Types:
    def __init__(self):
        return (
            f"FileNameOrPath ( {Fore.CYAN}str{Fore.RESET} )",
            f"IntegerText    ( {Fore.CYAN}int{Fore.RESET} )",
            f"PrefixText     ( {Fore.CYAN}str{Fore.RESET} )",
            f"StringText     ( {Fore.CYAN}str{Fore.RESET} )",
            f"SiteType       ( {Fore.CYAN}str{Fore.RESET} )",
            f"SiteType_      ( {Fore.CYAN}requests.code{Fore.RESET} )",
            f"HTTPPort       ( {Fore.CYAN}int{Fore.RESET} )",
            f"HTTPHost       ( {Fore.CYAN}str{Fore.RESET} )",
            f"Choices        ( {Fore.CYAN}dict{Fore.RESET} )",
            f"Choice1        ( {Fore.CYAN}str{Fore.RESET} )",
            f"Choice2        ( {Fore.CYAN}str{Fore.RESET} )",
            f'TimeFormat     ( {Fore.CYAN}str: "DD/MM/YYYY HH:MM"{Fore.RESET} )',
            f"FormatTime     ( {Fore.CYAN}str{Fore.RESET} )"
        )
    #NameType      = <type>                             #TODO: <class '{class_where_using_type}'>
    FileNameOrPath = str                                #TODO: <class 'FileWorking'>
    IntegerText    = int                                #TODO: <class 'FileWorking'>
    PrefixText     = str                                #TODO: <class 'Returns'>
    StringText     = str                                #TODO: <class 'FileWorking'>
    SiteType       = str                                #TODO: <class 'WorkingWeb'>
    SiteType_      = requests.codes                     #TODO: <class 'WorkingWeb'>
    HTTPPort       = int                                #TODO: <class 'WorkingWeb'>
    HTTPHost       = str                                #TODO: <class 'WorkingWeb'>
    Choices        = dict                               #TODO: <class 'WorkingRandom'>
    Choice1        = str                                #TODO: <class 'WorkingRandom'>
    Choice2        = str                                #TODO: <class 'WorkingRandom'>
    TimeFormat     = "%d/%m/%Y %H:%M"                   #TODO: <class 'WorkingTime'>
    FormatType     = str                                #TODO: <class 'WorkingTime'>
    Version        = "mp.one.1"                         #TODO: <class 'Console'>

class FileWorking(Types):
    def __init__(self):
            return (
                "ReadFile       ( fuction )",
                "MakeFile       ( fuction )",
                "EditFile       ( function )"
            )
    # TODO: __files__
    def ReadFile(
            self,
            s: Types.FileNameOrPath
        ) -> any:
        if os.path.exists(s):
            with open(s, encoding="utf8") as _:
                f = _.read()
        else:
            print("Error: File is not exists in main path.")
        return f
    def MakeFile(
            self,
            s: Types.FileNameOrPath
    ) -> Types.FileNameOrPath:
        with open(s, "w", encoding="utf8") as _:
            readed = _.read()
    def EditFile(
            self,
            s: Types.FileNameOrPath,
            l: Types.IntegerText,
            t: Types.StringText
    ) -> Types.StringText:
        if os.path.exists(s):
            with open(s, "a", encoding="utf8") as _:
                r = _.read()
                r_ = _.readline(l)
                r_.write(t)
        else:
            return ""

# TODO: __returns__
class Returns(Types):
    def ReturnText(
        *text: Types.StringText,
        prefix: Types.PrefixText = "\x81[32mPREFIX\033[0m",
        end: Types.StringText = None
    ) -> Types.StringText:
        if not end and not prefix:
            return text
        elif end and prefix:
            return f"{Fore.GREEN}{prefix}{Fore.RESET} | {text} {end}"
        elif end:
            return f"{text} {end}"
        elif prefix:
            return F"{Fore.GREEN}{prefix}{Fore.RESET} | {text}"

    def InputText(
        prompt: object = "", /
    ) -> str: 
        ...

class WorkingWeb(Types):
    def __init__(self):
            return (
                f"OpenSite       ( {Fore.CYAN}function{Fore.RESET} )",
                f"Mozilla        ( {Fore.CYAN}function{Fore.RESET} )",
                f"Chrome         ( {Fore.CYAN}function{Fore.RESET} )",
                f"Server         ( {Fore.CYAN}function{Fore.RESET} )"
            )
    def OpenSite(
            self,
            *s: Types.SiteType,
    ) -> Types.StringText:
        if s.startswith("https://"):
            ...
        else:
            s = f"https://{s}"
        webbrowser.open(s)
    def Mozilla(
            self,
            *s
    ):
        if s.startswith("https://"):
            ...
        else:
            s = f"https://{s}"
        webbrowser.Mozilla(s)
    def Chrome(
            self,
            *s
    ):
        if s.startswith("https://"):
            ...
        else:
            s = f"https://{s}"
        webbrowser.Chrome(s)
    def Server(
            self,
            port: Types.HTTPPort,
            host: Types.HTTPHost
    ):
        server = (host, port)
        site = HTTPServer(server, SimpleHTTPRequestHandler)

        print(
            Returns.ReturnText(f"http server started on 'https://{host}:{port}'", prefix="[LocalServer]")
            )

        site.serve_forever()


class WorkingRandom(Types):
    def __init__(self):
            return (
                f"Choice         ( {Fore.CYAN}function{Fore.RESET} )",
                f"Randint        ( {Fore.CYAN}function{Fore.RESET} )"
            )
    def Choice(
            self,
            choices: Types.Choices
    ) -> any:
        return random.choice(choices)

    def Randint(
            self,
            choice1: Types.Choice1,
            choice2: Types.Choice2
    ):
        return random.randint(choice1, choice2)

class WorkingTime(Types, Returns):
    def __init__(self):
                return (
                    f"Now            ( {Fore.CYAN}function{Fore.RESET} )",
                    f"StrfTime       ( {Fore.CYAN}function{Fore.RESET} )",
                    f"Sleep          ( {Fore.CYAN}function{Fore.RESET} )"
                )
    @staticmethod
    def Now(self):
        return datetime.now().strftime(Types.TimeFormat)
    def Sleep(
            self,
            t: Types.IntegerText
    ):
        time.sleep(t)
        print(Returns.ReturnText("All is ok", prefix="[LOG]"))
    def StrfTime(
            self,
            f: Types.FormatType
    ) -> any:
        Types.FormatType = f 
        print(Returns.ReturnText("Format changed", prefix="[LOG]"))

class Console(Types, Returns, WorkingRandom, WorkingTime, WorkingWeb, FileWorking):
    def __init__(self):
        self.table = [".types", ".randomchoice", ".randomrandint", ".timenow", ".timesleep", ".timestrf"]
        self.table_= ["Shows types/functions of classes", "Return random choice. Need to input: choices (dict-type)", "Return random choice. Need to input: choice1, choice2 (str-type, str-type)", "Returns real time", "Program sleeping by a user inputted type", "User changes a format type of time."]
        for Key, Value in zip(self.table, self.table_):
            print(Returns.ReturnText(f"{Value}", prefix=f"[Command '{Key}']"))
        while True:
            try:
                print(    f"_____{Fore.CYAN}{__file__}")
                _ = input(f"Enter Text:{Fore.CYAN} ")
                if _ == "exit":
                    break 
                elif _ == ".types":
                    print(Types())
            except Exception as e:
                print(Returns.ReturnText(e, prefix="[Error]"))
if __name__ == "__main__":
    Console()
else:
    print(Returns.ReturnText(f"file {__file__} imported succefully", prefix="[LOG] [IMPORTED_IN_YOUR_FILE]"))
