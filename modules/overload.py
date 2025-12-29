import time
from colorama import Fore, Style
from modules import mobile, username, email, social, scraper, darkweb, dorking
import datetime

class OverloadSession:
    def __init__(self):
        self.found_phones = set()
        self.found_emails = set()
        self.found_usernames = set()
        self.found_urls = set()
        self.found_onions = set()
        self.intelligence = []

    def add_intel(self, source, info):
        entry = f"[{source}] {info}"
        if entry not in self.intelligence:
            self.intelligence.append(entry)
            print(f"{Fore.GREEN}[+] NEW INTEL: {entry}")

    def collect_input(self, prompt_name, storage_set):
        print(f"\n{Fore.CYAN}>> Add {prompt_name}s (Press Enter empty to finish):{Style.RESET_ALL}")
        while True:
            val = input(f"{Fore.YELLOW}   + Add {prompt_name}: {Style.RESET_ALL}").strip()
            if not val:
                break
            storage_set.add(val)

    def save_report(self):
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"mira_report_{timestamp}.txt"
        with open(filename, "w") as f:
            f.write("=== MIRA INTELLIGENCE REPORT ===\n")
            f.write(f"Generated: {timestamp}\n\n")
            for line in self.intelligence:
                f.write(f"{line}\n")
        print(f"\n{Fore.GREEN}[+] Report saved to {filename}")

    def run(self):
        print(f"\n{Fore.MAGENTA}=== OVERLOAD MODE ENHANCED ==={Style.RESET_ALL}")
        
        # Multi-Input Collection
        self.collect_input("Phone Number", self.found_phones)
        self.collect_input("Username", self.found_usernames)
        self.collect_input("Email", self.found_emails)
        self.collect_input("Target URL (Social/Web)", self.found_urls)
        self.collect_input("Onion Link (.onion)", self.found_onions)
        
        use_tor = input(f"\n{Fore.WHITE}Enable Tor/Darkweb features? (y/n): {Style.RESET_ALL}").strip().lower() == 'y'
        auto_dork = input(f"{Fore.WHITE}Enable Deep Search (Auto-Dorking)? (y/n): {Style.RESET_ALL}").strip().lower() == 'y'
        
        print(f"\n{Fore.MAGENTA}=== STARTING AUTOMATED RECON CYCLE ==={Style.RESET_ALL}")
        
        # Cycle 1: Phones
        for p in list(self.found_phones):
            print(f"{Fore.BLUE}[*] Analyzing Phone: {p}...")
            res = mobile.analyze(p)
            if res['valid']:
                self.add_intel("Mobile", f"{res['number']} - {res['carrier']} ({res['region']})")

        # Cycle 2: Emails
        for e in list(self.found_emails):
            print(f"{Fore.BLUE}[*] Analyzing Email: {e}...")
            res = email.analyze(e)
            if res['valid_format']:
                status = "Active" if res['mx_found'] else "Inactive/Invalid"
                self.add_intel("Email", f"{e} - {status}")

            # Auto-Dork Email
            if auto_dork:
                print(f"{Fore.CYAN}    -> Dorking Email: {e}...")
                queries = dorking.generate_queries(e)
                # Just use "Publicly Exposed Documents" or refined queries for emails to avoid noise
                # Or just general search
                leaks = dorking.perform_search(f"\"{e}\"", num_results=3)
                for l in leaks:
                    self.found_urls.add(l)
                    self.add_intel("Dorking", f"Found Leak/Ref for {e}: {l}")

        # Cycle 3: Usernames -> URLs & Dorking
        for u in list(self.found_usernames):
            print(f"{Fore.BLUE}[*] Searching Username: {u}...")
            urls = username.search(u, use_tor)
            for item in urls:
                self.found_urls.add(item['url'])
                self.add_intel("Username", f"Found Profile: {item['url']} ({item['site']})")
            
            # Auto-Dork Username
            if auto_dork:
                print(f"{Fore.CYAN}    -> Deep Searching (Dorking) Username: {u}...")
                # Search for username in text bodies or titles
                results = dorking.perform_search(f"intext:\"{u}\" | inurl:\"{u}\"", num_results=5)
                for r in results:
                    if r not in self.found_urls:
                        self.found_urls.add(r)
                        self.add_intel("Dorking", f"Deep Search Result for {u}: {r}")

        # Cycle 4: Onion Links (if enabled)
        if use_tor and self.found_onions:
            print(f"{Fore.MAGENTA}[*] Verifying Darkweb Links...{Style.RESET_ALL}")
            for onion in list(self.found_onions):
                res = darkweb.check(onion)
                if res['reachable']:
                    self.add_intel("Darkweb", f"ACTIVE ONION: {onion}")
                else:
                    self.add_intel("Darkweb", f"INACTIVE: {onion} (Status: {res['status']})")

        # Cycle 5: Deep Dive (URLs -> Scrape)
        if self.found_urls:
            print(f"{Fore.BLUE}[*] Deep Diving into found URLs (Max 7 checks)...")
            count = 0
            for url in list(self.found_urls):
                if count >= 7: break
                
                print(f"{Fore.CYAN}    -> Scraping {url}...")
                
                # Metadata
                meta = social.scrape(url, use_tor)
                if meta and meta['image'] != "Not found":
                    self.add_intel("Social", f"Image found at {url}: {meta['image']}")
                
                # Content
                scraped = scraper.extract(url, use_tor)
                if scraped:
                    count += 1
                    for new_e in scraped['emails']:
                        if new_e not in self.found_emails:
                            self.found_emails.add(new_e)
                            self.add_intel("Scraper", f"Found new email in {url}: {new_e}")
                    
                    for new_p in scraped['phones']:
                        if new_p not in self.found_phones:
                            self.found_phones.add(new_p)
                            self.add_intel("Scraper", f"Found new phone in {url}: {new_p}")
                            
        print(f"\n{Fore.MAGENTA}=== OVERLOAD REPORT ==={Style.RESET_ALL}")
        for line in self.intelligence:
            print(line)
        
        self.save_report()

        # AI Analysis Integration
        from modules import ai_analysis
        analyst = ai_analysis.AIAnalyst()
        if analyst.is_configured():
            ai_choice = input(f"\n{Fore.WHITE}Run AI Detective Analysis on this report? (y/n): {Style.RESET_ALL}").strip().lower()
            if ai_choice == 'y':
                print(f"\n{Fore.MAGENTA}=== AI DETECTIVE REPORT ==={Style.RESET_ALL}")
                analysis_result = ai_analysis.analyze(self.intelligence)
                print(analysis_result)
                
                # Append analysis to report
                self.intelligence.append("\n--- AI ANALYSIS ---")
                self.intelligence.append(analysis_result)
                self.save_report() # Save again with AI data
        else:
            print(f"\n{Fore.YELLOW}[!] AI features available. Add GEMINI_API_KEY or OPENAI_API_KEY to .env to enable.{Style.RESET_ALL}")

        input(f"\n{Fore.YELLOW}Press Enter to return to menu...{Style.RESET_ALL}")

def run():
    session = OverloadSession()
    session.run()
