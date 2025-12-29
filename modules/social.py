import requests
from bs4 import BeautifulSoup
from colorama import Fore, Style
from utils.network import create_tor_session

def scrape(url, use_tor=False):
    """Returns dict of metadata (title, desc, image)."""
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    try:
        if use_tor:
            session = create_tor_session()
            response = session.get(url, headers=headers, timeout=15)
        else:
            response = requests.get(url, headers=headers, timeout=10)
            
        if response.status_code != 200:
            return None
            
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.title.string if soup.title else "No Title"
        
        # Meta description
        desc = "Not found"
        for m in soup.find_all('meta'):
            if m.get('name') == 'description' or m.get('property') == 'og:description':
                desc = m.get('content')
                break
                
        # Image
        img = "Not found"
        for m in soup.find_all('meta'):
            if m.get('property') == 'og:image':
                img = m.get('content')
                break
                
        return {"title": title, "description": desc, "image": img, "url": url}
        
    except Exception:
        return None

def run():
    print(f"\n{Fore.CYAN}[*] Social Media Analysis Module Loaded")
    print(f"{Fore.WHITE}Extracts metadata (Title, Description) from a profile URL.")
    
    url = input(f"{Fore.YELLOW}Enter profile URL (e.g., https://twitter.com/user): {Style.RESET_ALL}").strip()
    
    if not url.startswith("http"):
        print(f"{Fore.RED}[!] URL must start with http/https")
        return

    use_tor = input(f"{Fore.YELLOW}Use Tor for requests? (y/n): {Style.RESET_ALL}").lower() == 'y'

    print(f"{Fore.BLUE}[*] Fetching page...")
    data = scrape(url, use_tor)
    
    if data:
        print(f"\n{Fore.GREEN}[+] Page Fetched Successfully")
        print(f"{Fore.WHITE}[*] Title: {data['title'].strip()}")
        print(f"{Fore.WHITE}[*] Description: {data['description']}")
        print(f"{Fore.WHITE}[*] Profile/OG Image: {data['image']}")
    else:
        print(f"{Fore.RED}[!] Failed to fetch or invalid status code.")

    input(f"\n{Fore.YELLOW}Press Enter to return to menu...{Style.RESET_ALL}")
