class ReportingAgent:
    def generate(self, execution, risk, governance):
        return {
            "executive_summary": f"""
EXECUTIVE SUMMARY:
- Execution: {execution['status_summary']}
- Risk Level: {risk['risk_level']}
- Governance: {governance['governance_status']}

KEY RISKS:
{risk['risks']}

RECOMMENDATION:
Continue monitoring with weekly governance review.
"""
        }
