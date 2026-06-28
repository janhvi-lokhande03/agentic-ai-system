import asyncio

class AnalyzerAgent:

    async def run(self, data):

        print("Analyzer Agent Started")

        await asyncio.sleep(2)

        return {
            "best_tool": "ChatGPT",
            "reason": "Most versatile AI assistant"
        }