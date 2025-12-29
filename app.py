import gradio as gr
import phonenumbers
from phonenumbers import geocoder, carrier
import requests
import dns.resolver

def mobile_check(number):
    try:
        parsed_number = phonenumbers.parse(number)
        if not phonenumbers.is_valid_number(parsed_number):
            return "Invalid Number"
        region = geocoder.description_for_number(parsed_number, "en")
        service = carrier.name_for_number(parsed_number, "en")
        return f"Valid: Yes\nRegion: {region}\nCarrier: {service}"
    except Exception as e:
        return f"Error: {e}"

def username_check(username):
    sites = {
        "Instagram": f"https://www.instagram.com/{username}",
        "GitHub": f"https://github.com/{username}",
        "Twitter": f"https://twitter.com/{username}"
    }
    results = []
    for site, url in sites.items():
        try:
            r = requests.get(url, timeout=5)
            status = "FOUND" if r.status_code == 200 else "Not Found"
            results.append(f"{site}: {status} ({url})")
        except:
             results.append(f"{site}: Error")
    return "\n".join(results)

def email_check(email):
    try:
        domain = email.split('@')[1]
        records = dns.resolver.resolve(domain, 'MX')
        return f"Valid Format: Yes\nMX Records: {[str(r.exchange) for r in records]}"
    except Exception as e:
        return f"Error: {e}"

with gr.Blocks(title="Mira OSINT") as demo:
    gr.Markdown("# Mira - Advanced OSINT Tool\n### Made by Yousef.bassem")
    
    with gr.Tab("Mobile"):
        phone_input = gr.Textbox(label="Phone Number (+1...)")
        phone_output = gr.Textbox(label="Result")
        phone_btn = gr.Button("Check")
        phone_btn.click(mobile_check, inputs=phone_input, outputs=phone_output)

    with gr.Tab("Username"):
        user_input = gr.Textbox(label="Username")
        user_output = gr.Textbox(label="Result")
        user_btn = gr.Button("Check")
        user_btn.click(username_check, inputs=user_input, outputs=user_output)

    with gr.Tab("Email"):
        email_input = gr.Textbox(label="Email")
        email_output = gr.Textbox(label="Result")
        email_btn = gr.Button("Check")
        email_btn.click(email_check, inputs=email_input, outputs=email_output)

demo.launch()
