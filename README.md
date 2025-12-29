# MIRA - Advanced OSINT Chatbot

![MIRA]<img width="833" height="929" alt="Screenshot from 2025-12-30 00-18-18" src="https://github.com/user-attachments/assets/982ff941-2a4f-4ed8-8f6f-08a1f57cb534" />

> **Made by Yousef.bassem**

## Overview
Mira is a powerful, modular OSINT (Open Source Intelligence) chatbot and toolset designed to assist researchers and security professionals in gathering information. It features a dual interface: a hacker-styled CLI and a modern Web UI (Gradio) suitable for Hugging Face Spaces.

**⚠️ DISCLAIMER: This tool is for educational and ethical testing purposes only. The authors are not responsible for any misuse.**

## Features
*   **🧠 AI Detective Mode**: Integrates **Gemini** or **OpenAI** to analyze your findings and generate a summary, threat assessment, and investigation leads.
*   **🚀 Overload Mode (Auto-Recon)**: Automated intelligence gathering. Inputs multiple seeds (phones, usernames, emails), correlates data, performs deep searches (Auto-Dorking), and generates reports.
*   **📱 Mobile Number Intelligence**: Validation, Carrier, Region, Timezone lookup.
*   **👤 Username Recon**: Check username presence across social media.
*   **📧 Email Analysis**: Format validation, MX record check, Disposable email detection.
*   **🌐 web Scraper**: Extract emails and phone numbers from websites.
*   **🧅 Darkweb Tools**: Tor connection check, .onion site availability check.
*   **🕸️ Social Media Analysis**: Extract metadata (Title, Description, Image) from profile URLs.
*   **🔍 Google Dorking**: Automated and manual generation of dorks for deep searching.
*   **📄 Reporting**: specific findings are saved to local text files in Overload Mode.
- **Privacy First**: Optional Tor/Proxy tunneling support.

## Installation
1.  **Clone the repository**:
    ```bash
    git clone https://github.com/Yousef-bassem/Mira.git
    cd MIRA
    ```
2.  **Set up Python Environment** (Recommended):
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # Linux/Mac
    # .\venv\Scripts\activate  # Windows
    ```
3.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
4.  **Configuration (New!)**:
    To enable AI features, create a `.env` file in the project root:
    ```bash
    cp .env.example .env
    ```
    Open `.env` and paste your API key (Gemini or OpenAI).

5.  **Install Tor** (Optional, for Darkweb features):
    *   **Linux**: `sudo apt install tor` then `sudo systemctl start tor`
ed and running on your system (default port 9050).

## Usage

### CLI Mode (Hacker Style)
```bash
python mira.py
```

### Web UI (Hugging Face / Gradio)
```bash
python app.py
```

## Attribution
Concept and Core Design by **Yousef.bassem**.
# MIRA
# MIRA
# MIRA
