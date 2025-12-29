import json
import os
from colorama import Fore, Style

FACTS_FILE = "hunting_facts.json"

def load_facts():
    if os.path.exists(FACTS_FILE):
        with open(FACTS_FILE, 'r') as f:
            return json.load(f)
    return []

def save_facts(facts):
    with open(FACTS_FILE, 'w') as f:
        json.dump(facts, f, indent=4)

def run():
    print(f"\n{Fore.CYAN}[*] Hunting Facts Module Loaded")
    
    facts = load_facts()
    
    while True:
        print(f"\n{Fore.WHITE}Current Facts: {len(facts)}")
        print("1. View/Analyze Facts")
        print("2. Add New Fact")
        print("3. Clear All Facts")
        print("99. Return to Main Menu")
        
        choice = input(f"\n{Fore.YELLOW}Hunting > {Style.RESET_ALL}")
        
        if choice == '1':
            if not facts:
                print(f"{Fore.YELLOW}No facts collected yet.")
            else:
                print(f"\n{Fore.GREEN}=== Collected Intelligence ===")
                for i, fact in enumerate(facts):
                    print(f"{i+1}. [{fact['type']}] {fact['value']} (Note: {fact['note']})")
                print(f"{Fore.GREEN}==============================")
                
        elif choice == '2':
            ftype = input("Fact Type (e.g., Email, IP, Username): ")
            val = input("Value: ")
            note = input("Notes: ")
            facts.append({"type": ftype, "value": val, "note": note})
            save_facts(facts)
            print(f"{Fore.GREEN}[+] Fact saved.")
            
        elif choice == '3':
            confirm = input(f"{Fore.RED}Are you sure? (y/n): ")
            if confirm.lower() == 'y':
                facts = []
                save_facts(facts)
                print("Facts cleared.")
                
        elif choice == '99':
            break
