import requests
from bs4 import BeautifulSoup
import re
from colorama import Fore, Style
from utils.network import create_tor_session

def extract(url, use_tor=False):
    """Returns dict of found emails, phones, and link count."""
    try:
        if use_tor:
            session = create_tor_session()
            response = session.get(url, timeout=15)
        else:
            response = requests.get(url, timeout=10)
            
        text = response.text
        
        # Emails
        emails = list(set(re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', text)))
        
        # Phones (Simple regex)
        raw_phones = set(re.findall(r'\+?\d{1,4}[-.\s]?\(?\d{1,3}\)?[-.\s]?\d{1,4}[-.\s]?\d{1,4}[-.\s]?\d{1,9}', text))
        phones = [p for p in raw_phones if len(p) >= 10]
        
        # Links
        soup = BeautifulSoup(text, 'html.parser')
        links = [a.get('href') for a in soup.find_all('a', href=True)]
        
        return {"emails": emails, "phones": phones, "links": links, "content_len": len(text)}
        
    except Exception:
        return None

def run():
    print(f"\n{Fore.CYAN}[*] Web Scraper Module Loaded")
    url = input(f"{Fore.YELLOW}Enter URL to scrape: {Style.RESET_ALL}").strip()
    
    if not url.startswith("http"):
        print(f"{Fore.RED}[!] URL must start with http/https")
        return

    use_tor = input(f"{Fore.YELLOW}Use Tor for requests? (y/n): {Style.RESET_ALL}").lower() == 'y'
    
    print(f"{Fore.BLUE}[*] Scraping {url}...")
    data = extract(url, use_tor)
    
    if data:
        print(f"{Fore.BLUE}[*] Content Length: {data['content_len']} bytes")
        
        if data['emails']:
            print(f"\n{Fore.GREEN}[+] Emails Found:")
            for email in data['emails']:
                print(f"  {email}")
        else:
             print(f"\n{Fore.YELLOW}[-] No emails found.")

        if data['phones']:
            print(f"\n{Fore.GREEN}[+] Potential Phone Numbers Found:")
            for p in data['phones'][:10]:
                 print(f"  {p}")
        else:
            print(f"\n{Fore.YELLOW}[-] No phone numbers found.")
            
        print(f"\n{Fore.GREEN}[+] Found {len(data['links'])} links on page.")
    else:
        print(f"{Fore.RED}[!] Failed to scrape URL.")

    input(f"\n{Fore.YELLOW}Press Enter to return to menu...{Style.RESET_ALL}")
