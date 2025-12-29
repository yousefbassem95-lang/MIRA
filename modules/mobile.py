import phonenumbers
from phonenumbers import geocoder, carrier, timezone
from colorama import Fore, Style

def analyze(number):
    """Returns a dict of intelligence or None if invalid."""
    try:
        parsed_number = phonenumbers.parse(number)
        if not phonenumbers.is_valid_number(parsed_number):
            return {"valid": False, "error": "Invalid format"}

        return {
            "valid": True,
            "number": number,
            "region": geocoder.description_for_number(parsed_number, "en"),
            "carrier": carrier.name_for_number(parsed_number, "en"),
            "timezones": list(timezone.time_zones_for_number(parsed_number)),
            "national_fmt": phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.NATIONAL),
            "international_fmt": phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
        }
    except Exception as e:
        return {"valid": False, "error": str(e)}

def run():
    print(f"\n{Fore.CYAN}[*] Mobile Number Intelligence Module Loaded")
    number = input(f"{Fore.YELLOW}Enter target phone number (with country code, e.g., +14445556666): {Style.RESET_ALL}").strip()
    
    result = analyze(number)
    
    if not result['valid']:
        print(f"{Fore.RED}[!] {result.get('error')}")
        return

    print(f"\n{Fore.GREEN}[+] Number Validated: {result['number']}")
    print(f"{Fore.WHITE}[*] Region: {result['region']}")
    print(f"{Fore.WHITE}[*] Carrier: {result['carrier']}")
    print(f"{Fore.WHITE}[*] Timezone(s): {', '.join(result['timezones'])}")
    print(f"{Fore.WHITE}[*] National Format: {result['national_fmt']}")
    print(f"{Fore.WHITE}[*] International Format: {result['international_fmt']}")

    input(f"\n{Fore.YELLOW}Press Enter to return to menu...{Style.RESET_ALL}")
