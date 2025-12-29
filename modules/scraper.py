import requests
from bs4 import BeautifulSoup
import re
from colorama import Fore, Style
from utils.network import create_tor_session

def run():
    print(f"\n{Fore.CYAN}[*] Web Scraper Module Loaded")
    url = input(f"{Fore.YELLOW}Enter URL to scrape: {Style.RESET_ALL}").strip()
    
    if not url.startswith("http"):
        print(f"{Fore.RED}[!] URL must start with http/https")
        return

    use_tor = input(f"{Fore.YELLOW}Use Tor for requests? (y/n): {Style.RESET_ALL}").lower() == 'y'

    try:
        if use_tor:
            session = create_tor_session()
            response = session.get(url, timeout=15)
        else:
            response = requests.get(url, timeout=10)
            
        print(f"{Fore.BLUE}[*] Content Length: {len(response.text)} bytes")
        
        # Extract Emails
        emails = set(re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', response.text))
        if emails:
            print(f"\n{Fore.GREEN}[+] Emails Found:")
            for email in emails:
                print(f"  {email}")
        else:
             print(f"\n{Fore.YELLOW}[-] No emails found.")

        # Extract Phone Numbers (Simple Regex, can be improved)
        # Matches typical international formats roughly
        phones = set(re.findall(r'\+?\d{1,4}[-.\s]?\(?\d{1,3}\)?[-.\s]?\d{1,4}[-.\s]?\d{1,4}[-.\s]?\d{1,9}', response.text))
        # Filter out short matches which are likely dates or other numbers
        phones = [p for p in phones if len(p) >= 10]
        
        if phones:
            print(f"\n{Fore.GREEN}[+] Potential Phone Numbers Found (May include false positives):")
            for p in phones[:10]: # Limit to 10
                 print(f"  {p}")
            if len(phones) > 10: print(f"  ... and {len(phones)-10} more.")
        else:
            print(f"\n{Fore.YELLOW}[-] No phone numbers found.")
            
        # Extract Links
        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.find_all('a')
        print(f"\n{Fore.GREEN}[+] Found {len(links)} links on page.")

    except Exception as e:
        print(f"{Fore.RED}[!] Error: {e}")

    input(f"\n{Fore.YELLOW}Press Enter to return to menu...{Style.RESET_ALL}")
