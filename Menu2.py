import os
import requests
import subprocess
import sys
import time
from Crypto.Cipher import AES
import xxtea
import base64
import json
import tempfile
import webbrowser
from tqdm import tqdm
from datetime import datetime

class TextColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    ITALIC = '\033[3m'
    BLINK = '\033[5m'
    REVERSE = '\033[7m'
    RED = '\033[91m' 
    GREEN = '\033[92m'  
    YELLOW = '\033[93m' 
    BLUE = '\033[94m'  
    MAGENTA = '\033[95m'  
    CYAN = '\033[96m' 
    WHITE = '\033[97m'  
    
def scrolling_text(text, delay=0.1):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write('\n')


#kode decrypt        
def decrypt_string(encrypted_str):
    char_mapping = {
        "ဒ": "f",
        "ᜉ": "e",
        "ဘ": "d",
        "ᜂ": "c",
        "o": "b",
        "ᜄ": "a",
        "ᜑ": "0",
        "ᜐ": "9",
        "ᜋ": "8",
        "ᜃ": "7",
        "က": "6",
        "ဃ": "5",
        "ᜌ": "4",
        "ᜏ": "3",
        "ရ": "2",
        "ᜇ": "1"
    }

    for key, value in char_mapping.items():
        encrypted_str = encrypted_str.replace(key, value)

    decrypted_str = bytes.fromhex(encrypted_str).decode('utf-8')

    return decrypted_str

    
#kode github
def run_script_from_github(github_link, script_name):
    with tempfile.NamedTemporaryFile(mode="w", delete=False) as temp_file:
        temp_file_name = temp_file.name

        response = requests.get(github_link)
        if response.status_code == 200:
            encrypted_content = response.text
            decrypted_content = decrypt_string(encrypted_content)
            
            
            temp_file.write(decrypted_content)
        else:
            print(f"Failed to fetch script from GitHub.")
            return

    try:
        total_fmt = 50  # Set total_fmt to the desired value
        for _ in tqdm(range(total_fmt), desc=f"{TextColors.BOLD}{TextColors.OKGREEN}Progress: {TextColors.ENDC}", bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt}", colour='#00FF00'):
            # Simulate work being done
            time.sleep(0.01)   
            
        subprocess.run(["python", temp_file_name])
        print("")

    except Exception as e:
        print(f"Error executing script: {e}")

    finally:
        os.remove(temp_file_name)

    input(f"\n{TextColors.REVERSE}Press Enter To Return To The Menu{TextColors.ENDC}")    

    
def display_menu():
    os.system('clear')
    print(f'{TextColors.BOLD}{TextColors.OKGREEN}=================================================={TextColors.ENDC}')   
    print(f"[ {TextColors.BOLD}{TextColors.GREEN}1. {TextColors.ENDC}] {TextColors.BOLD}{TextColors.GREEN}JOJO VPN{TextColors.ENDC}")
    print(f"[ {TextColors.BOLD}{TextColors.GREEN}2. {TextColors.ENDC}] {TextColors.BOLD}{TextColors.GREEN}JTUNNEL V5{TextColors.ENDC}")
    print(f"[ {TextColors.BOLD}{TextColors.GREEN}3. {TextColors.ENDC}] {TextColors.BOLD}{TextColors.GREEN}TSS MAX PRO{TextColors.ENDC}")
    print(f"[ {TextColors.BOLD}{TextColors.GREEN}4. {TextColors.ENDC}] {TextColors.BOLD}{TextColors.GREEN}INET VPN{TextColors.ENDC}")
    print(f"[ {TextColors.BOLD}{TextColors.GREEN}5. {TextColors.ENDC}] {TextColors.BOLD}{TextColors.GREEN}NP TUNNEL{TextColors.ENDC}")
    print(f"[ {TextColors.BOLD}{TextColors.GREEN}6. {TextColors.ENDC}] {TextColors.BOLD}{TextColors.GREEN}BS SOCKET{TextColors.ENDC}")
    print(f"[ {TextColors.BOLD}{TextColors.GREEN}7. {TextColors.ENDC}] {TextColors.BOLD}{TextColors.GREEN}HR NETWORK{TextColors.ENDC}")
    print(f"[ {TextColors.BOLD}{TextColors.GREEN}8. {TextColors.ENDC}] {TextColors.BOLD}{TextColors.GREEN}R CODE VPN{TextColors.ENDC}")
    print(f'{TextColors.BOLD}{TextColors.OKGREEN}=================================================={TextColors.ENDC}')    
    print(f"[ {TextColors.BOLD}{TextColors.OKGREEN}9. {TextColors.ENDC}] {TextColors.BOLD}NEXT{TextColors.ENDC}                      [ {TextColors.BOLD}{TextColors.OKGREEN}0. {TextColors.ENDC}] {TextColors.BOLD}EXIT MENU{TextColors.ENDC}")

    print(f'{TextColors.BOLD}{TextColors.OKGREEN}=================================================={TextColors.ENDC}')
    scrolling_text(f'{TextColors.BOLD}{TextColors.OKGREEN}[PAGE - 2]{TextColors.ENDC}', delay=0.00)
    scrolling_text(f'\n{TextColors.BOLD}{TextColors.WHITE}✅ Check Decrypt Results in Folder [EnzoSniffer]{TextColors.ENDC}', delay=0.00)
def get_menu_choice():
    while True:
        choice = input(f"\n{TextColors.BOLD}{TextColors.CYAN}Select Menu = {TextColors.ENDC}")
        if choice.isdigit() and 0 <= int(choice) <= 9:
            return choice
        else:
            print(f"{TextColors.FAIL}Invalid selection. Please enter a valid menu option.{TextColors.ENDC}")
            

def main():
    while True:
        display_menu()
        choice = get_menu_choice()

        if choice == "1":
            enzo_jojo = "https://raw.githubusercontent.com/cc01k/Menu1/main/jojovip_enc.py"
            run_script_from_github(enzo_jojo, "JOJO VPN")
        elif choice == "2":
            enzo_jtunnel = "https://raw.githubusercontent.com/cc01k/Menu1/main/jtunnelv5_enc.py"
            run_script_from_github(enzo_jtunnel, "JTUNNEL V5")
        elif choice == "3":
            enzo_dev = "https://bitbin.it/GmvDfxEg/raw/"
            run_script_from_github(enzo_dev, "TSS MAX PRO")
        elif choice == "4":
            enzo_dev = "https://bitbin.it/GmvDfxEg/raw/"
            run_script_from_github(enzo_dev, "INET VPN")
        elif choice == "5":
            enzo_dev = "https://bitbin.it/GmvDfxEg/raw/"
            run_script_from_github(enzo_dev, "NP TUNNEL")
        elif choice == "6":
            enzo_dev = "https://bitbin.it/GmvDfxEg/raw/"
            run_script_from_github(enzo_dev, "BS SOCKET") 
        elif choice == "7":
            enzo_dev = "https://bitbin.it/GmvDfxEg/raw/"
            run_script_from_github(enzo_dev, "HR NETWORK")
        elif choice == "8":
            enzo_dev = "https://bitbin.it/GmvDfxEg/raw/"
            run_script_from_github(enzo_dev, "R CODE VPN")
        elif choice == "9":
            enzo_dev = "https://bitbin.it/GmvDfxEg/raw/"
            run_script_from_github(enzo_dev, "DECRYPT LINK JSON")                                                        
        elif choice == "0":
            return

if __name__ == "__main__":
    main()
    
    
    