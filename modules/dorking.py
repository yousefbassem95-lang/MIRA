from colorama import Fore, Style
import urllib.parse

def run():
    print(f"\n{Fore.CYAN}[*] Google Dorking Module Loaded")
    print(f"{Fore.WHITE}Generate Google Dorks to find specific information.")
    
    target = input(f"{Fore.YELLOW}Enter target domain or keyword: {Style.RESET_ALL}").strip()
    
    dorks = {
        "Public Directories": f"site:{target} intitle:index.of",
        "Config Files": f"site:{target} ext:xml | ext:conf | ext:cnf | ext:reg | ext:inf | ext:rdp | ext:cfg | ext:txt | ext:ini",
        "Database Files": f"site:{target} ext:sql | ext:dbf | ext:mdb",
        "Log Files": f"site:{target} ext:log",
        "Backup Files": f"site:{target} ext:bkf | ext:bkp | ext:bak | ext:old | ext:backup",
        "Login Pages": f"site:{target} inurl:login | inurl:signin | intitle:Login | intitle:\"sign in\" | inurl:auth",
        "SQL Errors": f"site:{target} intext:\"sql syntax near\" | intext:\"syntax error has occurred\" | intext:\"incorrect syntax near\" | intext:\"unexpected end of SQL command\" | intext:\"Warning: mysql_connect()\" | intext:\"Warning: mysql_query()\" | intext:\"Warning: pg_connect()\"",
        "Publicly Exposed Documents": f"site:{target} ext:doc | ext:docx | ext:odt | ext:pdf | ext:rtf | ext:sxw | ext:psw | ext:ppt | ext:pptx | ext:pps | ext:csv",
        "PHP Info": f"site:{target} ext:php intitle:phpinfo \"published by the PHP Group\""
    }

    print(f"\n{Fore.GREEN}[*] Generated Dorks for: {target}\n")
    
    for name, query in dorks.items():
        print(f"{Fore.CYAN}--- {name} ---")
        print(f"{query}")
        # Create a clickable link for terminals that support it
        encoded = urllib.parse.quote(query)
        link = f"https://www.google.com/search?q={encoded}"
        print(f"{Fore.WHITE}{link}\n")

    input(f"\n{Fore.YELLOW}Press Enter to return to menu...{Style.RESET_ALL}")
