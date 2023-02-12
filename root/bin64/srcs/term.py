from lib.libs import echo
import os, subprocess, whois

cwd = os.getcwd()
cwd = cwd[:-11]
print(cwd)
l_n = open(f"{cwd}\\user\\user.data").read()

echo("""
░██████╗░░█████╗░░██████╗
██╔═══██╗██╔══██╗██╔════╝
██║██╗██║██║░░██║╚█████╗░
╚██████╔╝██║░░██║░╚═══██╗
░╚═██╔═╝░╚█████╔╝██████╔╝
░░░╚═╝░░░░╚════╝░╚═════╝░
████████╗███████╗██████╗░███╗░░░███╗██╗███╗░░██╗░█████╗░██╗░░░░░
╚══██╔══╝██╔════╝██╔══██╗████╗░████║██║████╗░██║██╔══██╗██║░░░░░
░░░██║░░░█████╗░░██████╔╝██╔████╔██║██║██╔██╗██║███████║██║░░░░░
░░░██║░░░██╔══╝░░██╔══██╗██║╚██╔╝██║██║██║╚████║██╔══██║██║░░░░░
░░░██║░░░███████╗██║░░██║██║░╚═╝░██║██║██║░╚███║██║░░██║███████╗
░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝╚═╝░░╚══╝╚═╝░░╚═╝╚══════╝
""")

def whois_command(domain):
    w = whois.whois(domain)
    echo(f"Registrar: {w.registrar}")
    echo(f"Creation date: {w.creation_date}")
    echo(f"Expiration date: {w.expiration_date}")
    echo(f"Name servers: {w.name_servers}")
    echo(f"Status: {w.status}")

while True:
    cmd = input(f"{l_n} => ")
    if cmd.startswith("ping "):
        ip = cmd.split(" ")[1]
        result = subprocess.run(["ping", "-n", "5", ip], capture_output=True)
        echo(result.stdout.decode())
    elif cmd.startswith("whois "):
        domain = cmd.split(" ")[1]
        whois_command(domain)
    