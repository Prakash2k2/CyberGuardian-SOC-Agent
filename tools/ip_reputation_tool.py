"""
Example IP reputation tool wrapper. This is a placeholder that can call AbuseIPDB, VirusTotal etc.
Keys should be provided via environment variables if you enable those services.

For demo, if no API key is present, return a stubbed response.
"""
import os
import requests

ABUSEIPDB_API_KEY = os.getenv('ABUSEIPDB_API_KEY', None)
VIRUSTOTAL_API_KEY = os.getenv('VIRUSTOTAL_API_KEY', None)

def check_ip_reputation(ip: str) -> dict:
    # If no keys, return a stubbed response so demo runs offline
    if not ABUSEIPDB_API_KEY and not VIRUSTOTAL_API_KEY:
        return {'score': 'unknown', 'note': 'no API keys provided; demo stub'}
    # Example: integrate with AbuseIPDB (commented out)
    if ABUSEIPDB_API_KEY:
        try:
            url = 'https://api.abuseipdb.com/api/v2/check'
            headers = {'Key': ABUSEIPDB_API_KEY, 'Accept': 'application/json'}
            params = {'ipAddress': ip, 'maxAgeInDays': 90}
            r = requests.get(url, headers=headers, params=params, timeout=10)
            if r.status_code == 200:
                return r.json()
            else:
                return {'error': f'abuseipdb_status_{r.status_code}'}
        except Exception as e:
            return {'error': str(e)}
    # Add VirusTotal flow similarly if VIRUSTOTAL_API_KEY provided
    return {'score': 'unknown', 'note': 'no configured provider returned data'}