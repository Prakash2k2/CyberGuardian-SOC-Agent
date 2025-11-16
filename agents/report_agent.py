"""
Generate a human readable incident report (markdown), save to disk, optionally convert to PDF.
"""
from tools.save_report import save_report_markdown
from datetime import datetime
import os

class ReportAgent:
    def __init__(self):
        pass

    def generate(self, alert_data: dict, intel: dict) -> str:
        md_lines = []
        md_lines.append(f"# Incident Report")
        md_lines.append(f"**Generated:** {datetime.utcnow().isoformat()} UTC\n")
        md_lines.append("## Summary")
        md_lines.append(alert_data.get('raw', ''))
        md_lines.append("\n## Classification")
        md_lines.append(alert_data.get('classification', 'Unknown'))
        md_lines.append("\n## IOCs")
        iocs = alert_data.get('iocs', {})
        ips = iocs.get('ips', [])
        urls = iocs.get('urls', [])
        if ips:
            for ip in ips:
                md_lines.append(f"- IP: `{ip}`")
        else:
            md_lines.append("- IPs: None detected")
        if urls:
            for url in urls:
                md_lines.append(f"- URL: {url}")
        else:
            md_lines.append("- URLs: None detected")

        md_lines.append("\n## Threat Intelligence Results")
        ip_checks = intel.get('ip_checks', {})
        if ip_checks:
            for ip, res in ip_checks.items():
                md_lines.append(f"- {ip}: {res}")
        else:
            md_lines.append("- No IP reputation results")

        md_lines.append("\n## Notes / Recommended Actions")
        md_lines.append("- Triage the source IPs and block if confirmed malicious.")
        md_lines.append("- Investigate affected endpoints for SQLi evidence.")
        md_lines.append("- Preserve logs for forensic analysis.")

        report_md = '\n'.join(md_lines)

        # Save report to disk (reports/)
        return save_report_markdown(report_md)