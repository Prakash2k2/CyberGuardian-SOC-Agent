# CyberGuardian — Automated SOC Incident Analysis Agent  
### Kaggle · Google AI Agents Intensive · Capstone Project  
Track: **Enterprise Agents**

---

## Project Overview - CyberGuardian SOC Agent
CyberGuardian is a **multi-agent SOC assistant** that analyzes raw security alerts, extracts IOCs (IPs, URLs), enriches them using threat intelligence services, and generates **incident reports** automatically in Markdown/PDF.

This project demonstrates:

- Multi-agent architecture (Supervisor + 3 sub-agents)
- Parallel threat intel lookups
- Memory & session state
- Custom tools (IOC extraction, reputation lookup)
- Automated reporting
- Local runnable code (NO API keys needed)

This version is fully executable locally and compatible with Kaggle / GitHub.

---

## Agent Architecture  

### Supervisor Agent 
Coordinates the pipeline:
1. Alert Analysis  
2. Threat Intelligence Enrichment (parallel workers)  
3. Report Generation  
4. Memory Persistence  

### Alert Analyzer Agent 
- Extracts IOCs (IPs, URLs)  
- Classifies attack type  
- Returns structured alert data  

### Threat Intel Agent 
- Parallel IP reputation lookup (ThreadPoolExecutor)  
- Stubbed offline mode (no API keys needed)  
- Supports extension to real TI providers (AbuseIPDB / VirusTotal)  

### Report Agent 
- Generates readable Markdown incident report  
- Saves to `reports/` folder  
- Optional PDF generation (if wkhtmltopdf installed)  

### Memory Service 
- Persists incidents to `memory/memory_bank.json`  
- Useful for history, auditing, and trend analysis  

---

# How to Run and Execute Code ?

## Run Locally (No API Keys Required)

### Create and activate virtual environment 
#### Windows :-
Powershell
python -m venv venv >> 
.\venv\Scripts\Activate.ps1

#### macOS/Linux :-
Terminal
python3 -m venv venv >> 
source venv/bin/activate

### Install dependencies :-
pip install -r requirements.txt

### Run the demo :-
python run.py --demo sample_data/alert_sample.txt


### You will see output like :-

--- Generated Incident Report ---
#### Incident Report
...
Report saved to reports/report_1.md

### Sample Input (alert text) :-

High priority alert: multiple failed login attempts from 203.0.113.12.
Suspicious GET to https://malicious.example.com/login.php with SQL errors.
Possible SQL Injection attempts.

### Sample Output (summary) :-

Extracted IP: 203.0.113.12
Extracted URL: https://malicious.example.com/login.php
Attack Classification: SQL Injection
Threat Intel: Stubbed offline result (can be replaced with real TI)
Auto-generated Markdown report.s
