import requests
from bs4 import BeautifulSoup
from colorama import Fore, Style
from utils.network import create_tor_session

def run():
    print(f"\n{Fore.CYAN}[*] Social Media Analysis Module Loaded")
    print(f"{Fore.WHITE}Extracts metadata (Title, Description) from a profile URL.")
    
    url = input(f"{Fore.YELLOW}Enter profile URL (e.g., https://twitter.com/user): {Style.RESET_ALL}").strip()
    
    if not url.startswith("http"):
        print(f"{Fore.RED}[!] URL must start with http/https")
        return

    use_tor = input(f"{Fore.YELLOW}Use Tor for requests? (y/n): {Style.RESET_ALL}").lower() == 'y'

    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        
        print(f"{Fore.BLUE}[*] Fetching page...")
        if use_tor:
            session = create_tor_session()
            response = session.get(url, headers=headers, timeout=15)
        else:
            response = requests.get(url, headers=headers, timeout=10)
            
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            title = soup.title.string if soup.title else "No Title"
            
            print(f"\n{Fore.GREEN}[+] Page Fetched Successfully")
            print(f"{Fore.WHITE}[*] Title: {title.strip()}")
            
            # Try to find meta description
            metas = soup.find_all('meta')
            desc = "Not found"
            for m in metas:
                if m.get('name') == 'description' or m.get('property') == 'og:description':
                    desc = m.get('content')
                    break
            
            print(f"{Fore.WHITE}[*] Description: {desc}")
            
            # Try to find image
            img = "Not found"
            for m in metas:
                if m.get('property') == 'og:image':
                    img = m.get('content')
                    break
            print(f"{Fore.WHITE}[*] Profile/OG Image: {img}")

        else:
             print(f"{Fore.RED}[!] Status Code: {response.status_code}")

    except Exception as e:
        print(f"{Fore.RED}[!] Error: {e}")

    input(f"\n{Fore.YELLOW}Press Enter to return to menu...{Style.RESET_ALL}")
