import os

cwd = os.getcwd()
isLogged = f"{cwd}\\root\\user\\isLogged.data"
setup = f"{cwd}\\root\\bin64\\srcs\\setup.py"
login = f"{cwd}\\root\\bin64\\srcs\\login.py"
isLogged = open(isLogged).read()

if isLogged == "0":
    os.startfile(setup)

if isLogged == "1":
    os.startfile(login)