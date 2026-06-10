from core.orchestrator import PMOOrchestrator


def main():

    sample_update = """
    Data center rollout delayed due to vendor issue.
    Budget review in progress.
    Compliance signoff pending.
    """

    orchestrator = PMOOrchestrator()

    result = orchestrator.run(sample_update)

    print(result)


if __name__ == "__main__":
    main()
