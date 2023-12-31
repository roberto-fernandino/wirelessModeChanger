import subprocess
import argparse


def arguments():
    parser = argparse.ArgumentParser(
        prog="Monitor mode changer",
        description="Change your network adapter from managed to monitor mode",
        epilog=f"\033[1m\033[95mWireless mode changer WMD \033[0m1.1.3 by Roberto Fernandino, a cybersecurity enthusiast",
    )
    parser.add_argument(
        "-i",
        "--interface",
        dest="interface",
        help="USAGE: -i <interfaceyouwant> wlan0/wmon0/...",
    )
    parser.add_argument(
        "--back",
        action="store_true",
        dest="backto",
        help="if specified go back to Managed mode",
    )
    options = parser.parse_args()
    return options


def changeMode(iface: str):
    subprocess.run(f"ifconfig {iface} down", shell=True)
    subprocess.run("sudo airmon-ng check kill", shell=True)
    subprocess.run(f"iwconfig {iface} mode monitor", shell=True)
    subprocess.run(f"ifconfig {iface} up", shell=True)


def backManaged(iface: str):
    subprocess.run(f"ifconfig {iface} down", shell=True)
    subprocess.run("sudo airmon-ng check kill", shell=True)
    subprocess.run(f"iwconfig {iface} mode Managed", shell=True)
    subprocess.run(f"ifconfig {iface} up", shell=True)


options = arguments()


def main():
    if options.backto:
        print("[+] Going back to Managed mode")
        try:
            backManaged(options.interface)
            print("[+] Sucessifuly Changed back to Managed mode")
        except PermissionError:
            print("[-] Error! could not change Monitor mode run the script as a sudo")
    else:
        print("[+]Changing to Monitor mode")
        try:
            changeMode(options.interface)
            print("[+] Sucessifuly Changed to monitor mode")
        except PermissionError:
            print(
                "[-] Error! could not change Monitor mode try run the script as a sudo"
            )


main()
