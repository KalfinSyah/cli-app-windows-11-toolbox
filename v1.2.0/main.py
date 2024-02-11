from utilities import clear_terminal, show_error_with_pause
from win11_toolbox import run_win11_toolbox_method, toolbox_options_lists

while True:
    ###################################################################
    clear_terminal()
    print("============= Windows 11 Toolbox v1.1.0 by kalfin syah ==============")
    print("=====================================================================")
    for i, j in enumerate(toolbox_options_lists, start=1):
        print(f"{i} = {j[0]}")
        print(f"{j[1]}\n")
    print("\033[93mwrite 'exit' for exit\033[0m")
    print("=====================================================================")
    user_option = str(input("Pick option : "))
    print("=====================================================================")
    user_sureness = str(input(f"Are you sure (y/n) ? "))
    print("=====================================================================")
    ###################################################################

    ###################################################################
    if str.lower(user_sureness) == 'n':
        continue
    elif str.lower(user_sureness) not in ['y', 'n']:
        show_error_with_pause("Invalid input!")
        continue
    ###################################################################
    
    ###################################################################
    if str.lower(user_option) == "exit":
        exit()
    ###################################################################
    
    ###################################################################
    try:
        run_win11_toolbox_method(user_option)
    except:
        show_error_with_pause("Options is not available")
    ###################################################################
