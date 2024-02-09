import importlib.util
import ctypes
import os

def check_dependencies():
    dependencies = [
        "cryptography",
        "tkinter"
    ]
    missing_dependencies = []
    for dependency in dependencies:
        spec = importlib.util.find_spec(dependency)
        if spec is None:
            missing_dependencies.append(dependency)
    return missing_dependencies

def show_input_error():
    print(f"\033[91m(Error) \033[93mPlease check your input!\033[0m")
    os.system("pause")

class Win11Toolbox:
    def open_SystemPropertiesPerformanceExe(self):
        os.system("SystemPropertiesPerformance.exe")
    
    def menage_autostart_programs(self):
        os.system("start ms-settings:startupapps")
    
    def perform_cleanmgr(self):
        os.system("cleanmgr")

    def open_game_mode(self):
        os.system("start ms-settings:gaming-gamemode")

    def install_wsl(self):
        if ctypes.windll.shell32.IsUserAnAdmin() != 1:
            print("\033[91mError : \033[0mYou are not in administrator mode")
            os.system('pause')
            return

        os.system("wsl --install")

    def upgrade_my_apps(self):
        if ctypes.windll.shell32.IsUserAnAdmin() != 1:
            print("\033[91mError : \033[0mYou are not in administrator mode")
            os.system('pause')
            return
        
        os.system("winget upgrade")
        print("\nHelp :")
        print("\twrite --all for upgrade all your apps.")
        print("\twrite <back for back.")
        print("\t\033[93mif error occurred try use id instead of name.\033[0m")
        print("=====================================================================")
        user_input = str(input(f"\nChoose one (by name/id) : "))
        print("=====================================================================")
        if str.lower(user_input) == "<back":
            return
        print("=====================================================================")
        os.system(f'winget upgrade "{user_input}"')
        print("=====================================================================")
        os.system("pause")

    def encrypt_a_file(self):
        if ctypes.windll.shell32.IsUserAnAdmin() != 1:
            print("\033[91mError : \033[0mYou are not in administrator mode")
            os.system('pause')
            return
        
        try:
            print("Select a file from your computer please!")
            os.system("pause")
            target_file = filedialog.askopenfilename()
            print(target_file)

            ################################################################################
            key = Fernet.generate_key()
            with open(f"{os.path.basename(target_file)}.key", "wb") as key_file:
                key_file.write(key)
            print("Generating key........")
            print(f"\033[93m{os.path.basename(target_file)}.key is saved on {os.getcwd()}\\\033[0m")
            ################################################################################

            ################################################################################
            print(f"Encrypting \033[93m{os.path.basename(target_file)}\033[0m in progress......")
            fernet = Fernet(key)
            with open(target_file, "rb") as file:
                user_file = file.read()
            encrypted_user_file = fernet.encrypt(user_file)
            with open(f"{os.getcwd()}\\{os.path.basename(target_file)}.encrypted", "wb") as file:
                file.write(encrypted_user_file)
            print(f"\033[93m{os.path.basename(target_file)}.encrypted is saved on {os.getcwd()}\\\033[0m")
            os.system("pause")
            ################################################################################
        except:
            print("\033[91mError! Failed to encrypt your file.\033[0m")
            os.system('pause')

    def decrypt_a_file(self):
        if ctypes.windll.shell32.IsUserAnAdmin() != 1:
            print("\033[91mError : \033[0mYou are not in administrator mode")
            os.system('pause')
            return
        
        #################################################################################
        print("Select an encrypted file from your computer please!")
        os.system("pause")
        encrypted_file = filedialog.askopenfilename()
        encrypted_file_extension = os.path.splitext(encrypted_file)[1].lower()
        if encrypted_file and encrypted_file_extension != ".encrypted":
            print("\033[91mError : \033[0mYour file is not an encrypted file")
            os.system("pause")
            return
        print(f"{encrypted_file} selected")
        
        print("Select the key file for that file from your computer please!")
        os.system("pause")
        key_file = filedialog.askopenfilename()
        key_file_extension = os.path.splitext(key_file)[1].lower()
        if key_file and key_file_extension != ".key":
            print("\033[91mError : \033[0mYour file is not a key file")
            os.system("pause")
            return
        print(f"{key_file} selected")
        #################################################################################

        #################################################################################
        print("decrypting........")
        with open(key_file, 'rb') as f:
            key = f.read()
        fernet = Fernet(key)
        with open(encrypted_file, "rb") as file:
            encrypted_file_buffer = file.read()
        
        encrypted_file_extension_length = len(encrypted_file_extension)
        decrypted_file_path = encrypted_file[:-encrypted_file_extension_length]
        
        decrypted_file = fernet.decrypt(encrypted_file_buffer)
        
        with open(decrypted_file_path, "wb") as file:
            file.write(decrypted_file)
        print(f"Decrypted file saved at : {decrypted_file_path}")
        os.system("pause")
        #################################################################################


missing_dependencies = check_dependencies()
if missing_dependencies:
    os.system("cls")
    print("MISSING DEPENDENCIES:")
    for dep in missing_dependencies:
        print(f"- {dep}")
    print("\nYou given two options : ")
    print("1. Manual install the missing dependencies (use pip install missing_dependencies_name) (it will exit this program).")
    print("2. Automatic install")
    is_user_want_install_manual_or_automatic = input("Choose : ")

    if is_user_want_install_manual_or_automatic == "2":
        print("")
        for i in missing_dependencies:
            os.system(f"pip install {i}")

        print("")
        os.system("pause")
    else:
        exit()

from cryptography.fernet import Fernet
from tkinter import filedialog

win11_toolbox = Win11Toolbox() 

options = [
    ["Open System Properties Performance.", 
    "Tweak your apperance of your windows, and some functionality"], 

    ["Menage Startup Apps.",
    "Manage an apps that automatically start when your computer is on"],

    ["Perform Cleanmgr.", 
    "Clear unnecessary files from your computer's hard disk"],

    ["Game Mode.",
    "Turning things off in the background"],

    ["(administrator mode only) Install WSL/Windows Subsystem for Linux.",
    "Run native Linux command-line tools and software directly on Windows, without the need for virtual machines (VMs) or dual-boot setups"],

    ["(administrator mode only) Upgrade My Apps.",
    "Upgrade your apps using winget"],

    ["(administrator mode only) Encrypt a File.", 
    "Encrypt your file, and also genereting the key using cryptography. Supported format file : .txt, .doc, .docx, .pdf, .xls, .xlsx, .ppt, .pptx, .jpg, .png, .gif, .bmp, .mp3, .wav, .flac, .mp4, .avi, .mov, .log, .zip"],

    ["(administrator mode only) Decrypted a File.",
    "Decrypt your file using cryptography (but please make sure you have the key first!)"]
]

methods = {
    '1' : win11_toolbox.open_SystemPropertiesPerformanceExe,
    '2' : win11_toolbox.menage_autostart_programs,
    '3' : win11_toolbox.perform_cleanmgr,
    '4' : win11_toolbox.open_game_mode,
    '5' : win11_toolbox.install_wsl,
    '6' : win11_toolbox.upgrade_my_apps,
    '7' : win11_toolbox.encrypt_a_file,
    '8' : win11_toolbox.decrypt_a_file
}

while True:
    ###################################################################
    os.system("cls")
    print("============= Windows 11 Toolbox v1.1.0 by kalfin syah ==============")
    print("=====================================================================")
    for i, j in enumerate(options, start=1):
        print(f"{i} = {j[0]}")
        print(f"{j[1]}")
        print("=====================================================================")
    print("\033[93mwrite 'exit' for exit\033[0m")
    print("=====================================================================")
    user_option = str(input("Pick option : "))
    user_sureness = str(input(f"Are you sure (y/n) ? "))
    print("=====================================================================")
    ###################################################################

    ###################################################################
    if str.lower(user_sureness) == "y":
        if str.lower(user_option) == "exit":
            exit()
        else:
            try:
                os.system("cls")
                methods[user_option]()
            except:
                show_input_error()
    elif str.lower(user_sureness) == "n":
        continue
    else:
        show_input_error()
    ###################################################################