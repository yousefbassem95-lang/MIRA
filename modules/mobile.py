import phonenumbers
from phonenumbers import geocoder, carrier, timezone
from colorama import Fore, Style

def run():
    print(f"\n{Fore.CYAN}[*] Mobile Number Intelligence Module Loaded")
    number = input(f"{Fore.YELLOW}Enter target phone number (with country code, e.g., +14445556666): {Style.RESET_ALL}")
    
    try:
        parsed_number = phonenumbers.parse(number)
        if not phonenumbers.is_valid_number(parsed_number):
            print(f"{Fore.RED}[!] Invalid phone number format.")
            return

        print(f"\n{Fore.GREEN}[+] Number Validated: {number}")
        
        # Geolocation
        region = geocoder.description_for_number(parsed_number, "en")
        print(f"{Fore.WHITE}[*] Region: {region}")
        
        # Carrier
        service_provider = carrier.name_for_number(parsed_number, "en")
        print(f"{Fore.WHITE}[*] Carrier: {service_provider}")
        
        # Timezone
        time_zones = timezone.time_zones_for_number(parsed_number)
        print(f"{Fore.WHITE}[*] Timezone(s): {', '.join(time_zones)}")
        
        # Formatting
        national_fmt = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.NATIONAL)
        intl_fmt = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
        print(f"{Fore.WHITE}[*] National Format: {national_fmt}")
        print(f"{Fore.WHITE}[*] International Format: {intl_fmt}")

        input(f"\n{Fore.YELLOW}Press Enter to return to menu...{Style.RESET_ALL}")

    except phonenumbers.NumberParseException as e:
        print(f"{Fore.RED}[!] Error parsing number: {e}")
    except Exception as e:
         print(f"{Fore.RED}[!] Unexpected error: {e}")
