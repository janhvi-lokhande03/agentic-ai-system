class PlannerAgent:

    async def run(self, task):

        print("Planner Agent Started")

        steps = [
            "retrieve",
            "analyze",
            "write"
        ]

        return steps