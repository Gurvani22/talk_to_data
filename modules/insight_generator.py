from groq import Groq
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

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