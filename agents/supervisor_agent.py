"""
Supervisor agent coordinates sub-agents.
"""
from agents.alert_analyzer_agent import AlertAnalyzerAgent
from agents.threat_intel_agent import ThreatIntelAgent
from agents.report_agent import ReportAgent
from memory.session_service import SessionService

class Supervisor:
    def __init__(self):
        self.alert_agent = AlertAnalyzerAgent()
        self.intel_agent = ThreatIntelAgent()
        self.report_agent = ReportAgent()
        self.session = SessionService()

    def run_pipeline(self, alert_text: str) -> str:
        """
        Full pipeline:
          1) Analyze alert
          2) Enrich IOCs with threat intel (parallel)
          3) Generate a markdown report and save
          4) Persist into memory
        """
        # 1) Analyze alert
        alert_data = self.alert_agent.analyze(alert_text)

        # 2) Threat intelligence enrichment
        intel = self.intel_agent.query(alert_data)

        # 3) Create report
        report = self.report_agent.generate(alert_data, intel)

        # 4) Save report to memory bank
        self.session.save_incident(report, alert_data, intel)

        return report