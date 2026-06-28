import asyncio
import random

class RetrieverAgent:

    async def run(self, task):

        print("Retriever Agent Started")

        await asyncio.sleep(2)

        if random.random() < 0.3:
            raise Exception("Data Source Failed")

        return {
            "tools": [
                "ChatGPT",
                "Gemini",
                "Claude",
                "Perplexity",
                "Copilot"
            ]
        }

