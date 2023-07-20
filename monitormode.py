import subprocess
import argparse


def arguments():
    parser = argparse.ArgumentParser(
        prog="Monitor mode changer",
        description="Change your network adapter from managed to monitor mode",
        epilog=f"\033[1m\033[95mWireless mode changer WMD \033[0m1.1.2 by Roberto Fernandino, a cybersecurity enthusiast",
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
        backManaged(options.interface)
    else:
        print(options.b)
        changeMode(options.interface)


main()
