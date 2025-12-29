import requests
from colorama import Fore, Style
from utils.network import create_tor_session

# Simple list of sites to check
# In a real rigorous tool this would be much larger or load from a JSON execution list
SITES = {
    "Instagram": "https://www.instagram.com/{}",
    "Twitter": "https://twitter.com/{}",
    "Facebook": "https://www.facebook.com/{}",
    "GitHub": "https://github.com/{}",
    "TikTok": "https://www.tiktok.com/@{}",
    "Pinterest": "https://www.pinterest.com/{}",
    "Telegram": "https://t.me/{}",
    "GitLab": "https://gitlab.com/{}"
}

def search(username, use_tor=False):
    """Returns a list of found URLs."""
    found_urls = []
    session = create_tor_session() if use_tor else requests.Session()
    
    for site, url_template in SITES.items():
        url = url_template.format(username)
        try:
            # We print progress here because username checks are slow, but logic is separated
            # Ideally callback or yield, but simple print is fine for now
            response = session.get(url, timeout=10)
            if response.status_code == 200:
                found_urls.append({"site": site, "url": url})
        except Exception:
            pass # Silent fail for API logic
            
    return found_urls

def run():
    print(f"\n{Fore.CYAN}[*] Username Recon Module Loaded")
    username = input(f"{Fore.YELLOW}Enter target username: {Style.RESET_ALL}").strip()
    
    if not username:
        return

    use_tor = input(f"{Fore.YELLOW}Use Tor for requests? (y/n): {Style.RESET_ALL}").lower() == 'y'
    
    print(f"{Fore.BLUE}[*] Scanning {len(SITES)} sites for '{username}'...")
    
    # We re-implement the visual loop here to keep the "Hacker UI" feel
    # The search() function is for the Overload coordinator
    
    session = create_tor_session() if use_tor else requests.Session()

    for site, url_template in SITES.items():
        url = url_template.format(username)
        try:
            print(f"{Fore.BLUE}[*] Checking {site}...", end="\r")
            response = session.get(url, timeout=5) # Shorter timeout for UI responsiveness
            
            if response.status_code == 200:
                print(f"{Fore.GREEN}[+] FOUND: {site} -> {url}        ")
            elif response.status_code == 404:
                print(f"{Fore.RED}[-] Not Found: {site}        ")
            else:
                print(f"{Fore.YELLOW}[?] Status {response.status_code}: {site}        ")
                
        except Exception as e:
            print(f"{Fore.RED}[!] Error checking {site}: {str(e)[:30]}...        ")

    input(f"\n{Fore.YELLOW}Press Enter to return to menu...{Style.RESET_ALL}")
