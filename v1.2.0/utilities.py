from dependencies import os

def clear_terminal():
    os.system("cls")

def show_error_with_pause(message=""):
    print(f"\033[91m(Error) \033[93m{message}\033[0m\n")
    os.system("pause")
    return