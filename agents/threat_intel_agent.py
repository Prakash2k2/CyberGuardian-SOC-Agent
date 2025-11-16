"""
Query threat intelligence sources for IOCs.

This demo uses a stubbed reputation function; replace or extend check_ip_reputation
to integrate real services (VirusTotal, AbuseIPDB) using API keys.
"""
from tools.ip_reputation_tool import check_ip_reputation
from concurrent.futures import ThreadPoolExecutor, as_completed

class ThreatIntelAgent:
    def __init__(self, max_workers: int = 4):
        self.max_workers = max_workers

    def query(self, alert_data: dict) -> dict:
        iocs = alert_data.get('iocs', {})
        ips = iocs.get('ips', [])
        results = {}

        # Parallelize IP reputation checks
        with ThreadPoolExecutor(max_workers=self.max_workers) as ex:
            futures = {ex.submit(check_ip_reputation, ip): ip for ip in ips}
            for fut in as_completed(futures):
                ip = futures[fut]
                try:
                    res = fut.result()
                except Exception as e:
                    res = {'error': str(e)}
                results[ip] = res

        # If no IPs, optionally include URL checks — omitted here for brevity
        return {'ip_checks': results}