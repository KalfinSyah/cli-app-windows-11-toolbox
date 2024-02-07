import ctypes
import os
import subprocess
import re

class Win11Toolbox:
    def is_admin(self):
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False

    def open_SystemPropertiesPerformanceExe(self):
        os.system("SystemPropertiesPerformance.exe")
    
    def menage_autostart_programs(self):
        os.system("start ms-settings:startupapps")
    
    def perform_cleanmgr(self):
        os.system("cleanmgr")

    def game_mode(self):
        os.system("start ms-settings:gaming-gamemode")

    def install_wsl(self):
        print("")
        os.system("wsl --install")

    def upgrade_my_apps(self):
        print("")
        os.system("winget upgrade")
        print("\nHelp :")
        print("--all = for upgrade all your apps.")
        print("cencel = for cenceling.")
        print("If error occurred try use id instead of name.")
        user_input = str(input(f"\nChoose one (by name/id) : "))

        if user_input == "cencel":
            return

        print("")
        os.system(f'winget upgrade "{user_input}"')
        print("")
        os.system("pause")

win11_toolbox = Win11Toolbox() 
is_admin = win11_toolbox.is_admin()

options = [
    ["System Properties Performance", 
    "Tweak your apperance of your windows, and some functionality"], 

    ["Menage Startup Apps",
    "Manage an apps that automatically start when your computer is on"],

    ["Perform Cleanmgr", 
    "Clear unnecessary files from your computer's hard disk"],

    ["Game Mode",
    "Turning things off in the background"],

    ["Install WSL (Windows Subsystem for Linux)",
    "Run native Linux command-line tools and software directly on Windows, without the need for virtual machines (VMs) or dual-boot setups"],

    ["Upgrade My Apps",
    "Upgrade your apps using winget"],

    ["Exit", 
    "Exit from this app"]
]

if is_admin:
    while True:
        os.system("cls")
        print("\n- - - - - - -  program by Kalfin Syah - - - - - - -")
        for i, j in enumerate(options, start=1):
            print(f"\n{i} = {j[0]}")
            print(f"Description : \n{j[1]}")
        print("\n- - - - - - - - - - - - - - - - - - - - - - - - - -")
        user_option = str(input("\nPick option : "))

        os.system("cls")
        if user_option == "1":
            title = "System Properties Performance"
            run_method = win11_toolbox.open_SystemPropertiesPerformanceExe
        
        elif user_option == "2":
            title = "Manage Stratup Apps"
            run_method =  win11_toolbox.menage_autostart_programs
        
        elif user_option == "3":
            title = "Perform Cleanmgr"
            run_method = win11_toolbox.perform_cleanmgr

        elif user_option == "4":
            title = "Game Mode"
            run_method = win11_toolbox.game_mode

        elif user_option == "5":
            title = "Install WSL (Windows Subsystem for Linux)"
            run_method = win11_toolbox.install_wsl

        elif user_option == "6":
            title = "Upgrade My Apps"
            run_method = win11_toolbox.upgrade_my_apps

        elif user_option == "7":
            os.system("cls")
            exit()
        else:
            print("\nInvalid input!\n")
            os.system("pause")
            continue

        print(f"\n- - - - - - - - {title} - - - - - - -")
        user_sureness = str(input("\nContinue (y/n) ? "))
        if user_sureness == "Y" or user_sureness == "y":
            run_method()
        elif user_sureness == "N" or user_sureness == "n":
            continue
        else:
            print("\nInvalid input!\n")
            os.system("pause")
            continue

else:
    os.system("cls")
    print("\nAdministrative privileges is needed for running this program smoothly......")
    print("\nHints : Right click WindowsPowerShell (recommended) or cmd, then click on 'Run as Administrator'\n")
    quit()