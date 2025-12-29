from colorama import Fore, Style
from utils.network import check_tor_connection, create_tor_session

# Common search engines on Tor
ONION_SITES = {
    "Ahmia": "http://juhanurmihxlp77nkq76byazcldy2hlmovfu2epvl5ankdibsot4csyd.onion/",
    "Torch": "http://xmh57jrknzkhv6y3ls3ubitz6847wceher7q5wz3a54tycnz8plttnyd.onion/",
    "DuckDuckGo": "https://duckduckgogg42xjoc72x3sjasowoarfbgcmvfimaftt6twagswzczad.onion/"
}

def run():
    print(f"\n{Fore.CYAN}[*] Darkweb Module Loaded")
    
    # Check Tor First
    is_tor_active, msg = check_tor_connection()
    if not is_tor_active:
        print(f"{Fore.RED}[!] Tor is NOT active or not configured correctly.")
        print(f"{Fore.RED}[!] Please start Tor (e.g., 'sudo systemctl start tor') and set proxy to 127.0.0.1:9050")
        return

    print(f"{Fore.GREEN}[+] {msg}")
    print(f"{Fore.YELLOW}[*] WARNING: Accessing .onion sites can be slow. Please wait.")
    
    choice = input(f"{Fore.WHITE}Check connection to common darkweb engines? (y/n): {Style.RESET_ALL}").lower()
    
    if choice == 'y':
        session = create_tor_session()
        for name, url in ONION_SITES.items():
            try:
                print(f"{Fore.BLUE}[*] Checking {name}...", end="\r")
                r = session.get(url, timeout=20)
                if r.status_code == 200:
                    print(f"{Fore.GREEN}[+] {name} is UP ({url})      ")
                else:
                    print(f"{Fore.YELLOW}[?] {name} is reachable but returned {r.status_code}      ")
            except Exception as e:
                print(f"{Fore.RED}[-] {name} is DOWN or Unreachable      ")

    input(f"\n{Fore.YELLOW}Press Enter to return to menu...{Style.RESET_ALL}")
