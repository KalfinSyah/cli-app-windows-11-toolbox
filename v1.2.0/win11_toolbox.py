from dependencies import ctypes, Fernet, filedialog, Image, os

class Win11Toolbox:
    def open_system_properties_performance(self):
        os.system("SystemPropertiesPerformance.exe")
    
    def menage_autostart_programs(self):
        os.system("start ms-settings:startupapps")
    
    def perform_cleanmgr(self):
        os.system("cleanmgr")

    def open_game_mode(self):
        os.system("start ms-settings:gaming-gamemode")

    def install_wsl(self):
        if ctypes.windll.shell32.IsUserAnAdmin() != 1:
            print("\033[91mError : \033[0mYou are not in administrator mode\n")
            os.system('pause')
            return
        else:
            os.system("wsl --install -n")
            user_input = str(input("\nWant to run it (y/n)? "))
            if str.lower(user_input) == "y":
                os.system("cls")
                print("Please wait......\n")
                os.system("wsl -d Ubuntu")
            else:
                return

    def upgrade_my_apps(self):
        ################################################################################
        if ctypes.windll.shell32.IsUserAnAdmin() != 1:
            print("\033[91mError : \033[0mYou are not in administrator mode\n")
            os.system('pause')
            return
        ################################################################################
        
        ################################################################################
        os.system("winget upgrade")

        print("\n\033[93mHelp :")
        print("\twrite '--all' for upgrade all your apps.")
        print("\twrite 'cencel' for cencel.")
        print("\tif error occurred try use id instead of name.\033[0m")

        user_input = str(input("\nChoose one (by name/id) : "))

        if str.lower(user_input) == "cencel":
            return
        else:
            os.system(f'winget upgrade "{user_input}"')
        os.system("pause")
        ################################################################################


    def encrypt_a_file(self):        
        ################################################################################
        enter = input("Press enter to select a file (that you want to encrypt) from your computer......")
        target_file = filedialog.askopenfilename()
        print(f"\033[32m{os.path.basename(target_file)} is selected as a file\033[0m")
        ################################################################################

        ################################################################################
        try:
            key = Fernet.generate_key()
            fernet = Fernet(key)
            with open(target_file, "rb") as file:
                user_file = file.read()
            encrypted_user_file = fernet.encrypt(user_file)
        except:
            print("\n\033[91mError!\033[0m\n")
            os.system("pause")
            return
        ################################################################################

        ################################################################################
        target_file_name, target_file_extension = os.path.splitext(target_file)
        target_file_directory = os.path.dirname(target_file)
        target_file_path = os.path.join(target_file_directory, target_file_name)
        ################################################################################

        ################################################################################
        print("\nGenerating key........")

        try:
            with open(f"{target_file_path}.key", "wb") as file:
                file.write(key)
        except:
            print("\n\033[91mError!\033[0m :\n")
            os.system("pause")
            return
        
        print("\033[32mGenerating key success ✓\033[0m")
        ################################################################################

        ################################################################################
        print(f"\nEncrypting {os.path.basename(target_file)} in progress......")
        try:
            with open(f"{target_file_path}_encrypted{target_file_extension}", "wb") as file:
                file.write(encrypted_user_file)
        except:
            print("\n\033[91mError!\033[0m\n")
            os.system("pause")
            return
        print("\033[32mEncrtypting success ✓\033[0m")
        ################################################################################

        print("\nSaving both  files......")
        print(f"\033[32mBoth file is saved on {target_file_directory}/\033[0m\n")
        os.system("pause")

    def decrypt_a_file(self):        
        #################################################################################
        enter = input("Select an encrypted file from your computer please......")
        encrypted_file = filedialog.askopenfilename()
        print(f"\033[32m{encrypted_file} selected\033[0m")
        
        enter = input(f"\nSelect the key file from your computer please......")
        key_file = filedialog.askopenfilename()
        print(f"\033[32m{key_file} selected\033[0m")
        #################################################################################

        #################################################################################
        try:
            with open(key_file, 'rb') as file:
                key = file.read()

            fernet = Fernet(key)

            with open(encrypted_file, "rb") as file:
                encrypted_file_buffer = file.read()
        except:
            print("\n\033[91mError!\033[0m\n")
            os.system("pause")
            return
        #################################################################################

        #################################################################################  
        encrypted_file_name, encrypted_file_extension = os.path.splitext(encrypted_file)
        encrypted_file_directory = os.path.dirname(encrypted_file)
        encrypted_file_path = os.path.join(encrypted_file_directory, encrypted_file_name)

        decrypted_file = fernet.decrypt(encrypted_file_buffer)
        #################################################################################                            
        
        #################################################################################                            
        try:
            print("\nSaving decrypted file......")

            with open(f"{encrypted_file_path}_get_decrypted{encrypted_file_extension}", "wb") as file:
                file.write(decrypted_file)

            print(f"\033[32mDecrypted file saved at {encrypted_file_directory}/\033[0m\n")
            os.system("pause")
        except:
            print("\n\033[91mError!\033[0m\n")
            os.system("pause")
            return            
        #################################################################################
    
    def convert_image(self):
        enter = input("Press enter to select your image......")
        target_image = filedialog.askopenfilename()
        print(f"\033[32m{os.path.basename(target_image)} is selected as a file\033[0m")

        target_image_name, target_image_extension = os.path.splitext(target_image)
        target_image_directory = os.path.dirname(target_image)
        target_image_path = os.path.join(target_image_directory, target_image_name)

        print("\nSupported format : JPEG, PNG, BMP, GIF, TIFF, WebP, ICO")
        print("Hint : just write format you want ")

        new_extension = input(f"\nConvert to : ")

        try:
            with Image.open(target_image) as img:
                if img.mode == "RGBA":
                    img = img.convert("RGB")
                img.save(f"{target_image_path}_new.{str.lower(new_extension)}", format=new_extension)

            print("\n\033[32mConverting Success\033[0m\n")
            print(f"\033[32mSaved at {os.path.dirname(target_image)}/ \033[0m\n")
            os.system("pause")    
        except:
            print("\n\033[91mError!\033[0m\n")
            os.system("pause")

#################################################################################
win11_toolbox = Win11Toolbox() 
win11_toolbox_methods = {
    '1' : win11_toolbox.open_system_properties_performance,
    '2' : win11_toolbox.menage_autostart_programs,
    '3' : win11_toolbox.perform_cleanmgr,
    '4' : win11_toolbox.open_game_mode,
    '5' : win11_toolbox.install_wsl,
    '6' : win11_toolbox.upgrade_my_apps,
    '7' : win11_toolbox.encrypt_a_file,
    '8' : win11_toolbox.decrypt_a_file,
    '9' : win11_toolbox.convert_image
}
run_win11_toolbox_method = lambda i: win11_toolbox_methods[i]()
#################################################################################

#################################################################################
toolbox_options_lists = [
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

    ["Encrypt a File.", 
    "Encrypt your file, and also genereting the key using cryptography. Supported format file : .txt, .doc, .docx, .pdf, .xls, .xlsx, .ppt, .pptx, .jpg, .png, .gif, .bmp, .mp3, .wav, .flac, .mp4, .avi, .mov, .log, .zip"],

    ["Decrypted a File.",
    "Decrypt your file using cryptography (but please make sure you have the key first!)"],

    ["Convert Image.",
    "Convert your image to : JPG, PNG, BMP, GIF, TIFF, WebP, ICO"]
]
#################################################################################
