import re
import dns.resolver
from colorama import Fore, Style

def analyze(email):
    """Returns a dict of email validity info."""
    result = {"valid_format": False, "mx_found": False, "disposable": False, "domain": None}
    
    # 1. Format
    regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if re.search(regex, email):
        result['valid_format'] = True
        result['domain'] = email.split('@')[1]
        
        # 2. MX Record
        try:
            records = dns.resolver.resolve(result['domain'], 'MX')
            result['mx_found'] = True
            result['mx_records'] = [str(r.exchange) for r in records]
        except:
             result['mx_found'] = False
             
        # 3. Disposable
        disposables = ["tempmail.com", "guerrillamail.com", "10minutemail.com", "yopmail.com"]
        if result['domain'] in disposables:
            result['disposable'] = True
            
    return result

def run():
    print(f"\n{Fore.CYAN}[*] Email Analysis Module Loaded")
    email = input(f"{Fore.YELLOW}Enter target email address: {Style.RESET_ALL}").strip()
    
    data = analyze(email)
    
    if not data['valid_format']:
         print(f"{Fore.RED}[!] Invalid email format.")
         return

    print(f"{Fore.GREEN}[+] Format is valid.")
    
    if data['mx_found']:
        print(f"{Fore.GREEN}[+] MX Record found: {data['mx_records'][0]}")
        print(f"{Fore.GREEN}[+] Domain {data['domain']} is active.")
    else:
        print(f"{Fore.RED}[!] Could not get MX records.")

    if data['disposable']:
        print(f"{Fore.RED}[!] WARNING: This is a known disposable/temporary email provider.")
    else:
        print(f"{Fore.GREEN}[+] Domain is likely legitimate.")

    input(f"\n{Fore.YELLOW}Press Enter to return to menu...{Style.RESET_ALL}")
