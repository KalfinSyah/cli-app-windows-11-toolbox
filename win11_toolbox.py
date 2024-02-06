import ctypes
import os

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
        print("\nNB : --all for upgrade all your apps, and if error occurred try use id instead of name")
        user_input = str(input(f"\nChoose one (by name/id) : "))
        print("")
        os.system(f'winget upgrade "{user_input}"')
        print("")
        os.system("pause")



win11_toolbox = Win11Toolbox() 
is_admin = win11_toolbox.is_admin()

if is_admin:
    while True:
        os.system("cls")
        print(f"\n- - - - - - - - - by kalfin syah - - - - - - - - - -")
        print(f"\nAdmin privileges Status : {is_admin}")
        print(f"\n- - - - - - - - - - - - - - - - - - - - - - - - - - -")
        
        print(f"\n- - - - - - - - - - - - - - - - - - - - - - - - - - -")
        print("\nOptions : ")
        print("\n1 = Tweak performance.")
        print("\n2 = Menage startup apps (an apps that automatically start when your computer is on).")
        print("\n3 = Perform cleanmgr (clear unnecessary files from your computer's hard disk).")
        print("\n4 = Enable or Disable game mode.")
        print("\n5 = Install WSL/Windows Subsystem for Linux (run native Linux command-line tools and software directly on Windows, without the need for virtual machines (VMs) or dual-boot setups).")
        print("\n6 = Upgrade my apps (this is using winget, you can also do it on your own if you want).")
        print("\n99 = exit")
        print(f"\n- - - - - - - - - - - - - - - - - - - - - - - - - - -")
        options = str(input("\nYour options : "))
        print(f"\n- - - - - - - - - - - - - - - - - - - - - - - - - - -")

        print(f"\n- - - - - - - - - - - - - - - - - - - - - - - - - - -")
        if options == "1":
            print("\nBefore tweaking, here is recommended advice :")
            print("\n(this is the best tweak for me, but for you it might be diffrent)") 
            print("1. Pick 'custom'")
            print("2. Un-checklist all, except the 'smooth edges of screen fonts'\n")
            os.system("pause")
            win11_toolbox.open_SystemPropertiesPerformanceExe()
        elif options == "2":
            print("\nNB : Before you do something to your PC, make sure you know what you're doing!")
            print("Hint : If you want 'best performance', turning off all startup apps might help.\n")
            os.system("pause")
            win11_toolbox.menage_autostart_programs()
        elif options == "3":
            print("\nCAUTIONS! When cleaning temporary files, as it might affect certain applications or functionalities.\n")
            os.system("pause")
            win11_toolbox.perform_cleanmgr()
        elif options == "4":
            print("\nOptimize your PC for gaming by turning on game mode!\n")
            os.system("pause")
            win11_toolbox.game_mode()
        elif options == "5":
            win11_toolbox.install_wsl()
        elif options == "6":
            win11_toolbox.upgrade_my_apps()
        elif options == "7":
            pass
        elif options == "99":
            os.system("cls")
            exit()
        print(f"\n- - - - - - - - - - - - - - - - - - - - - - - - - - -")



else:
    os.system("cls")
    print("\nAdministrative privileges is needed for running this program smoothly......")
    print("\nHints : Right click WindowsPowerShell (recommended) or cmd, then click on 'Run as Administrator'\n")
    quit()
