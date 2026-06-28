import asyncio

class WriterAgent:

    async def run(self, analysis):

        print("Writer Agent Started")

        await asyncio.sleep(1)

        report = f"""
BEST TOOL REPORT

Best Tool:
{analysis['best_tool']}

Reason:
{analysis['reason']}
"""

        return report