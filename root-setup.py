#!/Users/lucamarchetti/anaconda3/bin/python3

"""
ROOT-SETUP.Py
by Luca Marchetti

This small python script allows to automatically create a 
ROOT project using CMake, with the correct tree structure.
"""

import os
import sys
import shutil
import pathlib


class Text:
    @staticmethod
    def make_visible(text: str) -> str:
        return f"\033[1m\033[38;5;10m{text}\033[0m"

    @staticmethod
    def make_error(text: str) -> str:
        return f"\033[1m\033[38;5;160m{text}\033[0m"


class Tree:
    @staticmethod
    def make_dirs() -> None:
        os.mkdir(dir_path)
        os.mkdir(dir_path.joinpath("src"))
        os.mkdir(dir_path.joinpath("include"))
        os.mkdir(dir_path.joinpath("build"))
        os.mkdir(dir_path.joinpath(".vscode"))

    @staticmethod
    def make_necessary() -> None:
        # files in main dir
        names = ["CMakeLists.txt", "compile.sh", ".clang-format", "main.cpp"]
        for i, val in enumerate(["cmake", "compile", "format", "main"]):
            shutil.copyfile(
                pathlib.Path(
                    f"/Users/lucamarchetti/Python/useful/root-setup/data/{val}.txt"
                ),
                dir_path.joinpath(names[i]),
            )

        # constants.hh
        shutil.copyfile(
            pathlib.Path(
                f"/Users/lucamarchetti/Python/useful/root-setup/data/include.txt"
            ),
            dir_path.joinpath("include/constants.hh"),
        )

        # vscode settings
        shutil.copyfile(
            pathlib.Path(
                f"/Users/lucamarchetti/Python/useful/root-setup/data/vscode.txt"
            ),
            dir_path.joinpath(".vscode/c_cpp_properties.json"),
        )

    @staticmethod
    def make_optional(flag: str = None) -> None:
        if flag == "-s":
            return

        # make readme
        with open(dir_path.joinpath("README.MD"), "w") as _:
            pass

        # make license
        shutil.copyfile(
            pathlib.Path("/Users/lucamarchetti/Python/useful/package/data/mit.txt"),
            dir_path.joinpath("LICENSE"),
        )

        if flag == "-g":
            # make gitignore
            shutil.copyfile(
                pathlib.Path(
                    "/Users/lucamarchetti/Python/useful/package/data/ignore.txt"
                ),
                dir_path.joinpath(".gitignore"),
            )


# no project name
if len(sys.argv) < 2:
    print(
        "[root-setup.py]: " + Text.make_error("ERROR") + " - Project name not inserted"
    )
    print(f"[root-setup.py]: Use 'root-setup.py -h' for help.")
    sys.exit()

# help
if sys.argv[1] == "-h":
    print("usage: root-setup.py [project name] [option] \n")
    print(
        "root-setup is a small python script that makes it possible to setup a ROOT project using CMake \n"
    )
    print("options:")
    print("-s   Simple project: only necessary files")
    print("-g   Git project: complete project with .gitignore")
    sys.exit()

# start
print(f"You are about to create a project named {Text.make_visible(sys.argv[1])}.")
proceed = input("Are you sure you want to proceed? (Y/n) ")
if proceed:
    print("Process terminated")
    sys.exit()

if pathlib.Path.exists((dir_path := pathlib.Path(f"./{sys.argv[1]}"))):
    print("A package with the same name already exists!")
    sys.exit()

# make directories
try:
    Tree.make_dirs()
    Tree.make_necessary()
    flag = sys.argv[2] if len(sys.argv) > 2 else None
    Tree.make_optional(flag)

    print("Package structure completed!")
except Exception as exc:
    print(exc)
    shutil.rmtree(dir_path)
    sys.exit()
