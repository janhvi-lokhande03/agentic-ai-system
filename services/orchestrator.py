from agents.planner import PlannerAgent
from agents.retriever import RetrieverAgent
from agents.analyzer import AnalyzerAgent
from agents.writer import WriterAgent


class Orchestrator:

    def __init__(self):

        self.planner = PlannerAgent()
        self.retriever = RetrieverAgent()
        self.analyzer = AnalyzerAgent()
        self.writer = WriterAgent()

    async def execute(self, task):

        plan = await self.planner.run(task)

        yield "Plan Generated\n"

        try:

            data = await self.retriever.run(task)

            yield "Data Retrieved\n"

        except Exception as e:

            yield f"Retriever Failed: {str(e)}\n"

            data = {
                "tools": ["Fallback Tool"]
            }

        analysis = await self.analyzer.run(data)

        yield "Analysis Complete\n"

        report = await self.writer.run(analysis)

        yield report