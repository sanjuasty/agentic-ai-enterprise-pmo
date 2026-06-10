class GovernanceAgent:
    def analyze(self, update: str):
        flags = []

        if "compliance" in update.lower():
            flags.append("Regulatory review required")

        return {
            "governance_status": "Checked",
            "flags": flags
        }
