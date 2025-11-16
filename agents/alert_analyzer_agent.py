"""
Extract IOCs and provide a short classification from raw alert text.
"""
from tools.extract_iocs import extract_iocs

class AlertAnalyzerAgent:
    def __init__(self):
        pass

    def analyze(self, text: str) -> dict:
        """
        Returns a dict:
        {
            'raw': <original text>,
            'iocs': {'ips': [...], 'urls': [...]},
            'classification': '...'
        }
        """
        iocs = extract_iocs(text)
        summary = {
            'raw': text,
            'iocs': iocs,
            'classification': self.classify(text)
        }
        return summary

    def classify(self, text: str) -> str:
        text_lower = text.lower()
        if 'sql' in text_lower or 'sql injection' in text_lower:
            return 'SQL Injection'
        if 'xss' in text_lower or 'cross-site scripting' in text_lower:
            return 'Cross-Site Scripting'
        if 'failed login' in text_lower or 'bruteforce' in text_lower:
            return 'Brute Force / Authentication'
        return 'Unknown'