import re
import dns.resolver
from colorama import Fore, Style

def run():
    print(f"\n{Fore.CYAN}[*] Email Analysis Module Loaded")
    email = input(f"{Fore.YELLOW}Enter target email address: {Style.RESET_ALL}").strip()
    
    # 1. Format Validation
    regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if not re.search(regex, email):
         print(f"{Fore.RED}[!] Invalid email format.")
         return

    print(f"{Fore.GREEN}[+] Format is valid.")
    
    domain = email.split('@')[1]
    
    # 2. DNS MX Record Check
    try:
        print(f"{Fore.BLUE}[*] Checking MX records for domain: {domain}...")
        records = dns.resolver.resolve(domain, 'MX')
        mx_record = records[0].exchange
        mx_record = str(mx_record)
        print(f"{Fore.GREEN}[+] MX Record found: {mx_record}")
        print(f"{Fore.GREEN}[+] Domain {domain} is active and can receive emails.")
    except Exception as e:
        print(f"{Fore.RED}[!] Could not get MX records: {e}")
        print(f"{Fore.RED}[!] Domain might be invalid or inactive.")

    # 3. Disposable Email Check (Basic List)
    disposables = ["tempmail.com", "guerrillamail.com", "10minutemail.com", "yopmail.com"]
    if domain in disposables:
        print(f"{Fore.RED}[!] WARNING: This is a known disposable/temporary email provider.")
    else:
        print(f"{Fore.GREEN}[+] Domain is likely legitimate (not in internal disposable list).")

    input(f"\n{Fore.YELLOW}Press Enter to return to menu...{Style.RESET_ALL}")
