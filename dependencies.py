import ctypes, os
 
try:
    from cryptography.fernet import Fernet
    from PIL import Image
    from tkinter import filedialog
except:
    import importlib.util

    os.system("cls")

    dependencies = ["cryptography", "tkinter", "pillow"]
    missing_dependencies = []

    for dependency in dependencies:
        spec = importlib.util.find_spec(dependency)
        if spec is None:
            missing_dependencies.append(dependency)

    if missing_dependencies:
        print("\033[91mMISSING DEPENDENCIES:\033[0m")

        for dep in missing_dependencies:
            print(f"- {dep}")
        
        print("\n\033[92mYou given two options : \033[0m")
        print("1. Manual install missing dependencies (will exit this program)")
        print("2. Automatic install")
        print("\n\033[93mHint for manual install : after exit this program, type 'pip install dependencies_name' in your terminal\033[0m")
        user_input = str(input("\nInput your option : "))

        if user_input == "1":
            exit()

        elif user_input == "2":
            for i in missing_dependencies:
                print("")
                os.system(f"pip install {i}")

            print("\nPlease RESTART/(RUN AGAIN) this toolbox")
            os.system("pause")
            exit()