from openai import OpenAI
from config import constants
import json
import re

def process_description(description:str):
    client = OpenAI(api_key=constants.OPENAI_API_KEY)

    prompt = f"""
        You are an AI assistant that evaluates descriptions of client requests.
        
        A valid description must contain:
        - Information about the IDEA (what the project is about, how it works, or its purpose).
        - Information about the CLIENT (who is the client that has the proposed project idea).
        
        Given the following description, assess whether both criteria are met. 
        If the idea is present, return 'idea_info': True; otherwise, False.
        If the client info is present, return 'client_info': True; otherwise, False.
        Also, return 'valid': True if both are present; otherwise, False.

        Here is the description: {description}

        Provide the result in valid JSON format with keys: 'idea_info', 'client_info', 'valid'. Make sure to use proper line breaks and no extra spaces.
    """
    chat_completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful AI assistant that processes and evaluates project description from user"},
            {"role": "user", "content": prompt}
        ]
    )
    result_text = chat_completion.choices[0].message.content

    # Regex pattern to extract the JSON object from the response
    pattern = r"\{[^{}]*\}"

    match = re.search(pattern, result_text, re.DOTALL)  # DOTALL allows matching across multiple lines
    result_json = match.group(0)
    return json.loads(result_json)