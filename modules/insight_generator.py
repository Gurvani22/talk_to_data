from groq import Groq
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize client
api_key = os.getenv("GROQ_API_KEY") or os.getenv("OPENAI_API_KEY")
if not api_key:
    raise RuntimeError(
        "Missing API key. Set GROQ_API_KEY (preferred) or OPENAI_API_KEY in your .env file."
    )

client = Groq(api_key=api_key)

def generate_insight(query, data_preview):
    prompt = f"""
    You are a data analyst.

    User Question: {query}

    Data:
    {data_preview}

    Tasks:
    - Explain key trends
    - Highlight increases/decreases
    - Give reasons ONLY based on data
    - Keep it simple and clear
    - Use bullet points

    Avoid assumptions not supported by data.
    """

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content