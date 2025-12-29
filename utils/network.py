import requests
import socket
import socks  # Part of PySocks, usually installed with requests[socks] or stem if needed, but let's stick to simple request proxies first
from colorama import Fore, Style

DEFAULT_TOR_PROXY = "socks5://127.0.0.1:9050"

def get_current_ip(session=None):
    """Returns the current public IP address."""
    try:
        if session:
            response = session.get("https://api.ipify.org?format=json", timeout=10)
        else:
            response = requests.get("https://api.ipify.org?format=json", timeout=10)
        return response.json().get("ip")
    except Exception as e:
        return f"Error: {str(e)}"

def create_tor_session(proxy_url=DEFAULT_TOR_PROXY):
    """Creates a requests session routed through Tor."""
    session = requests.session()
    session.proxies = {
        'http': proxy_url,
        'https': proxy_url
    }
    return session

def check_tor_connection(proxy_url=DEFAULT_TOR_PROXY):
    """Checks if Tor is accessible and returns the IP difference."""
    try:
        # Direct IP
        direct_ip = get_current_ip()
        
        # Tor IP
        session = create_tor_session(proxy_url)
        tor_ip = get_current_ip(session)
        
        if direct_ip == tor_ip:
            return False, f"Tor Not Active. IP is still {direct_ip}"
        
        if "Error" in tor_ip:
             return False, f"Could not connect via Tor: {tor_ip}"

        return True, f"Tor Active. Real IP: {direct_ip} -> Tor IP: {tor_ip}"
    except Exception as e:
        return False, f"Tor Connection Failed: {str(e)}"
