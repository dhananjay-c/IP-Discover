#import the necessary module!
import socket as s
from termcolor import colored


def print_colored_ascii_art():
    ascii_art = """                                                                                             
@@@  @@@@@@@         @@@@@@@   @@@   @@@@@@    @@@@@@@   @@@@@@   @@@  @@@  @@@@@@@@  @@@@@@@   
@@@  @@@@@@@@        @@@@@@@@  @@@  @@@@@@@   @@@@@@@@  @@@@@@@@  @@@  @@@  @@@@@@@@  @@@@@@@@  
@@!  @@!  @@@        @@!  @@@  @@!  !@@       !@@       @@!  @@@  @@!  @@@  @@!       @@!  @@@  
!@!  !@!  @!@        !@!  @!@  !@!  !@!       !@!       !@!  @!@  !@!  @!@  !@!       !@!  @!@  
!!@  @!@@!@!         @!@  !@!  !!@  !!@@!!    !@!       @!@  !@!  @!@  !@!  @!!!:!    @!@!!@!   
!!!  !!@!!!          !@!  !!!  !!!   !!@!!!   !!!       !@!  !!!  !@!  !!!  !!!!!:    !!@!@!    
!!:  !!:             !!:  !!!  !!:       !:!  :!!       !!:  !!!  :!:  !!:  !!:       !!: :!!   
:!:  :!:             :!:  !:!  :!:      !:!   :!:       :!:  !:!   ::!!:!   :!:       :!:  !:!  
 ::   ::              :::: ::   ::  :::: ::    ::: :::  ::::: ::    ::::     :: ::::  ::   :::  
:     :              :: :  :   :    :: : :     :: :: :   : :  :      :      : :: ::    :   : :  
"""

    # Print the ASCII art with colored letters
    print(colored(ascii_art, "light_green"))



# Call the function to print the colored ASCII art
print_colored_ascii_art()



print("\n\n")
promptColor = "light_green"	
prompt = colored("Enter Domain Target Name : ", promptColor)
target = input(prompt)

try:
    #fetch the IP
    ip = s.gethostbyname(target)
    #display the IP
    dprompt = colored('[+] - Target Domain Name : ', promptColor)
    iprompt = colored('[+] - Target IP Address  : ', promptColor)
    print(dprompt + target)
    print(iprompt + ip + "\n\n")
except:
    error = colored( "Invalid Domain Name !", "red", attrs=["bold"])
    print(error + "\n\n")
