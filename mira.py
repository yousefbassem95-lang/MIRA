import argparse
import sys
import time
from colorama import init, Fore, Style
from utils.network import check_tor_connection

# Initialize Colorama
init(autoreset=True)

BANNER = f"""
{Fore.CYAN}
              #####                    ****                     #####   
              #######                 ******                   ######             
          ####   ##########           ******             ##########  ###          
         #####           #######       ****        ########         #####        
         #####                #####             #####               #####        
           #####################  #   #####     # ######################         
                              ###   #########   ###                            
                       #######    ############      ######                       
                     ##########   #############    #########                     
                   ###########    #############    ###########                   
                 ######       ##  ############# ##         ######                 
               #####        #####  ###########  ####         #####               
             ****#        *******#  #########   #******         #****             
           ****         **+++***     ######      ***+++***        ****           
         ***          *++++*+  ***  *+++++++*  *** ++++++**          ***         
       **           *+++++    *+++  ++++++++   +++*    ++++++*          **       
                  +++++       +=+    +=====+    +=+      +++++*                  
                ++++         +=+     +=====+     +=+        ++++*                
              ++==          +=+      +=====+      +=+          ==++              
            ++=            ===       =----=        ===            ==+            
                           ==        =----=         ==              =++         
                          ==         =----=          ==                          
                         ==          =-::-=           ==                         
                         =            =::=             =                         
                        =             =::=              =                        
                       -              =..=               -                       
                      :               :.:                 :                       
                                      :::                                       
                                      :::                                        
                                      ---                                        
                                      |||                                           

███╗   ███╗██╗██████╗  █████╗ 
████╗ ████║██║██╔══██╗██╔══██╗
██╔████╔██║██║██████╔╝███████║
██║╚██╔╝██║██║██╔══██╗██╔══██║
██║ ╚═╝ ██║██║██║  ██║██║  ██║
╚═╝     ╚═╝╚═╝╚═╝  ╚═╝╚═╝  ╚═╝
{Style.RESET_ALL}
{Fore.MAGENTA}>> Advanced OSINT Chatbot & Toolset{Style.RESET_ALL}
{Fore.YELLOW}>> Made by Yousef.bassem{Style.RESET_ALL}
"""

def print_banner():
    print(BANNER)
    print(f"{Fore.GREEN}[*] System: {sys.platform}")
    print(f"{Fore.GREEN}[*] Time: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 50)

def check_security():
    print(f"{Fore.BLUE}[*] Checking Network Security...{Style.RESET_ALL}")
    is_tor, msg = check_tor_connection()
    if is_tor:
        print(f"{Fore.GREEN}[+] {msg}")
    else:
        print(f"{Fore.RED}[!] {msg}")
        print(f"{Fore.RED}[!] WARNING: You are NOT using Tor. Your IP is visible.")
        
def main_menu():
    while True:
        print(f"\n{Fore.WHITE}Select an Module:{Style.RESET_ALL}")
        print(f"{Fore.RED}0. OVERLOAD MODE (Auto-Recon){Style.RESET_ALL}")
        print(f"{Fore.CYAN}1. Mobile Number Intelligence")
        print(f"{Fore.CYAN}2. Username Recon")
        print(f"{Fore.CYAN}3. Email Analysis")
        print(f"{Fore.CYAN}4. Social Media Analysis")
        print(f"{Fore.CYAN}5. Deep/Darkweb History (Tor Required)")
        print(f"{Fore.CYAN}6. Hunting Context (Facts & Clues)")
        print(f"{Fore.CYAN}7. Web Scraper")
        print(f"{Fore.CYAN}8. Google Dorking")
        print(f"{Fore.CYAN}99. Exit")
        
        choice = input(f"\n{Fore.YELLOW}Mira > {Style.RESET_ALL}").strip()
        
        if choice == '0':
            from modules import overload
            overload.run()
        elif choice == '1':
            from modules import mobile
            mobile.run()
        elif choice == '2':
            from modules import username
            username.run()
        elif choice == '3':
            from modules import email
            email.run()
        elif choice == '4':
             from modules import social
             social.run()
        elif choice == '5':
            from modules import darkweb
            darkweb.run()
        elif choice == '6':
            from modules import hunting
            hunting.run()
        elif choice == '7':
            from modules import scraper
            scraper.run()
        elif choice == '8':
            from modules import dorking
            dorking.run()
        elif choice == '99':
            print("Exiting...")
            sys.exit()
        else:
            print(f"{Fore.RED}Invalid selection: '{choice}'")

def main():
    print_banner()
    check_security()
    try:
        main_menu()
    except KeyboardInterrupt:
        print("\nExiting...")
        sys.exit()

if __name__ == "__main__":
    main()
