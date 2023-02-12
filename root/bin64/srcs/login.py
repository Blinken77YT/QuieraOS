import os
from lib.libs import echo

cwd = os.getcwd()
user = os.getcwd()
user = user[:-11]
user = f"{user}/user"

l_n = open(f"{user}/user.data").read()
l_p = open(f"{user}/password.data").read()

echo("""
░██████╗░░█████╗░░██████╗
██╔═══██╗██╔══██╗██╔════╝
██║██╗██║██║░░██║╚█████╗░
╚██████╔╝██║░░██║░╚═══██╗
░╚═██╔═╝░╚█████╔╝██████╔╝
░░░╚═╝░░░░╚════╝░╚═════╝░
██╗░░░░░░█████╗░░██████╗░██╗███╗░░██╗
██║░░░░░██╔══██╗██╔════╝░██║████╗░██║
██║░░░░░██║░░██║██║░░██╗░██║██╔██╗██║
██║░░░░░██║░░██║██║░░╚██╗██║██║╚████║
███████╗╚█████╔╝╚██████╔╝██║██║░╚███║
╚══════╝░╚════╝░░╚═════╝░╚═╝╚═╝░░╚══╝
""")

while True:
    p_i = input(f"Enter password to {l_n}: ")
    if p_i == l_p:
        echo("Successful")
        os.startfile(f"{cwd}\\home.pyw")
        break
    else:
        echo("Incorrect")
        continue
