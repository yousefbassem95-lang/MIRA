# MIRA - Advanced OSINT Chatbot

![MIRA](mira_icon.png)

> **Made by Yousef.bassem**

## Overview
Mira is a powerful, modular OSINT (Open Source Intelligence) chatbot and toolset designed to assist researchers and security professionals in gathering information. It features a dual interface: a hacker-styled CLI and a modern Web UI (Gradio) suitable for Hugging Face Spaces.

**⚠️ DISCLAIMER: This tool is for educational and ethical testing purposes only. The authors are not responsible for any misuse.**

## Features
- **Mobile Number Intelligence**: Carrier, location, and format validation.
- **Username Recon**: Check availability across multiple social platforms.
- **Email Analysis**: Domain checks and format validation.
- **Deep/Darkweb Checks**: Connectivity and availability checks for .onion sites (Requires Tor).
- **Social Media Analysis**: Targeted platform checks.
- **Google Dorking**: Automated dork generation.
- **Web Scraping**: Extract info from targets.
- **Hunting**: Fact aggregation and analysis.
- **Privacy First**: Optional Tor/Proxy tunneling support.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/MIRA.git
   cd MIRA
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. (Optional) For Darkweb features, ensure Tor is installed and running on your system (default port 9050).

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
