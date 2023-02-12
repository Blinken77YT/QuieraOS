import os
from lib.libs import echo

cwd = os.getcwd()
user = f"{cwd}\\root\\user"

echo("""
░██████╗░░█████╗░░██████╗
██╔═══██╗██╔══██╗██╔════╝
██║██╗██║██║░░██║╚█████╗░
╚██████╔╝██║░░██║░╚═══██╗
░╚═██╔═╝░╚█████╔╝██████╔╝
░░░╚═╝░░░░╚════╝░╚═════╝░
░██████╗███████╗████████╗██╗░░░██╗██████╗░
██╔════╝██╔════╝╚══██╔══╝██║░░░██║██╔══██╗
╚█████╗░█████╗░░░░░██║░░░██║░░░██║██████╔╝
░╚═══██╗██╔══╝░░░░░██║░░░██║░░░██║██╔═══╝░
██████╔╝███████╗░░░██║░░░╚██████╔╝██║░░░░░
╚═════╝░╚══════╝░░░╚═╝░░░░╚═════╝░╚═╝░░░░░
""")

username = input("Enter your desired username: ")
pas = input("Enter your desired password: ")

with open(f"{user}\\user.data", "w") as f:
    f.writelines(username)

with open(f"{user}\\password.data", "w") as f:
    f.writelines(pas)

with open(f"{user}\\isLogged.data", "w") as f:
    f.writelines("1")

os.startfile(f"{cwd}\\root\\bin64\\srcs\\login.py")