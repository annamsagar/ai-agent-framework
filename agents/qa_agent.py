import os
from dotenv import load_dotenv
from groq import Groq
from core.agent import Agent

# Force load .env from project root
load_dotenv(dotenv_path=".env")

class QAAgent(Agent):
    def run(self, state: dict) -> dict:
        api_key = os.getenv("GROQ_API_KEY")

        # If key is missing, return readable error (no crash)
        if not api_key:
            return {
                "error": "GROQ_API_KEY not found. Check .env file location and content."
            }

        try:
            client = Groq(api_key=api_key)

            response = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[
                    {
                        "role": "system",
                        "content": "You are a helpful AI assistant. Answer clearly."
                    },
                    {
                        "role": "user",
                        "content": state["input"]
                    }
                ],
                temperature=0.3
            )

            return {
                "answer": response.choices[0].message.content.strip()
            }

        except Exception as e:
            # Return Groq error as JSON instead of 500 crash
            return {
                "error": str(e)
            }
