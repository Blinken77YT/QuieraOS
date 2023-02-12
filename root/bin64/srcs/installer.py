import argparse
import urllib.request
import os, shutil

# define a list of packages
packages = ["discord", "package2", "package3"]
cwd = os.getcwd()
cwd0 = cwd[:-6]

import subprocess

def install_package(package):
    if package in packages:
        url = "https://github.com/Blinken77YT/QuieraOS/raw/master/packages/" + package + ".exe"
        filename = package + ".exe"
        urllib.request.urlretrieve(url=url, filename=filename)
        print(f"Downloading {package}")
        print(f"Installing {package}")
        subprocess.run([filename, "--install"])
    else:
        print(f"{package} not found")

# create a function to list all packages
def list_packages():
    for package in packages:
        print(package)

# create a function to remove a package
def remove_package(package):
    if package in packages:
        packages.remove(package)
        print(f"{package} removed")
    else:
        print(f"{package} not found")

# create the command line interface using argparse
parser = argparse.ArgumentParser(description="QuieraOS Package Installer")
parser.add_argument("command", help="install, remove, or list")
parser.add_argument("package", help="name of the package", nargs='?')

# parse the command line arguments
args = parser.parse_args()

# execute the command based on the arguments
if args.command == "install":
    install_package(args.package)
elif args.command == "remove":
    remove_package(args.package)
elif args.command == "list":
    list_packages()
else:
    print("Invalid command")
