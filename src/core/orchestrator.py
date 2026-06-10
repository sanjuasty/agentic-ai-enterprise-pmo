from agents.execution_agent import ExecutionAgent
from agents.risk_agent import RiskAgent
from agents.governance_agent import GovernanceAgent
from agents.reporting_agent import ReportingAgent

class PMOOrchestrator:
    def __init__(self):
        self.execution = ExecutionAgent()
        self.risk = RiskAgent()
        self.governance = GovernanceAgent()
        self.reporting = ReportingAgent()

    def run(self, update: str):

        execution_result = self.execution.analyze(update)
        risk_result = self.risk.analyze(update)
        governance_result = self.governance.analyze(update)

        report = self.reporting.generate(
            execution_result,
            risk_result,
            governance_result
        )

        return report
