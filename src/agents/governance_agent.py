class GovernanceAgent:
    def analyze(self, update: str):

        escalation_needed = False

        if "delay" in update.lower():
            escalation_needed = True

        return {
            "governance_status": "Reviewed",
            "executive_escalation": escalation_needed
        }
