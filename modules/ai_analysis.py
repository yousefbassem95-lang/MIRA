import os
from colorama import Fore, Style
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

class AIAnalyst:
    def __init__(self):
        self.provider = None
        self.model = None
        
        # Determine provider
        if GEMINI_API_KEY:
            self.provider = "gemini"
            import google.generativeai as genai
            genai.configure(api_key=GEMINI_API_KEY)
            self.model = genai.GenerativeModel('gemini-pro')
        elif OPENAI_API_KEY:
            self.provider = "openai"
            from openai import OpenAI
            self.client = OpenAI(api_key=OPENAI_API_KEY)
            self.model = "gpt-4" # or gpt-3.5-turbo
        
    def is_configured(self):
        return self.provider is not None

    def analyze_report(self, report_text):
        if not self.provider:
            return "AI Analysis Unavailable: No API Key found in .env file."

        prompt = f"""
        You are a Senior Cyber Intelligence Analyst. 
        Analyze the following OSINT report gathered from a target investigation.
        
        REPORT DATA:
        {report_text}
        
        YOUR TASK:
        1. Summarize the key findings.
        2. Identify any potential security risks, leaks, or vulnerabilities found.
        3. Correlate the data to suggest the target's likely location, identity, or digital footprint.
        4. Recommend next steps for further investigation.
        
        Keep the tone professional, objective, and analytical.
        """

        print(f"{Fore.CYAN}[*] Sending report to {self.provider.upper()} for analysis... (This may take a moment){Style.RESET_ALL}")

        try:
            if self.provider == "gemini":
                response = self.model.generate_content(prompt)
                return response.text
            elif self.provider == "openai":
                response = self.client.chat.completions.create(
                    model=self.model,
                    messages=[{"role": "user", "content": prompt}]
                )
                return response.choices[0].message.content
        except Exception as e:
            return f"Error during AI analysis: {str(e)}"

def analyze(report_data_list):
    analyst = AIAnalyst()
    if not analyst.is_configured():
        return None
    
    # Convert list to string
    report_text = "\n".join(report_data_list)
    return analyst.analyze_report(report_text)
