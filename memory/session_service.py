"""
Simple session and memory bank for storing incidents.
"""
import json
from pathlib import Path

MEM_FILE = Path('memory/memory_bank.json')
MEM_FILE.parent.mkdir(parents=True, exist_ok=True)

class SessionService:
    def __init__(self):
        if MEM_FILE.exists():
            try:
                self.store = json.loads(MEM_FILE.read_text(encoding='utf-8'))
            except Exception:
                self.store = {'incidents': []}
        else:
            self.store = {'incidents': []}

    def save_incident(self, report_md: str, alert_data: dict, intel: dict):
        rec = {
            'report': report_md,
            'alert': alert_data,
            'intel': intel
        }
        self.store['incidents'].append(rec)
        MEM_FILE.write_text(json.dumps(self.store, indent=2), encoding='utf-8')