from orchestrator import PMOOrchestrator

if __name__ == "__main__":
    system = PMOOrchestrator()

    sample_update = """
    Data center rollout is progressing but there is a delay in procurement.
    Budget impact under review. Compliance sign-off pending.
    """

    result = system.run(sample_update)

    print(result["executive_summary"])
