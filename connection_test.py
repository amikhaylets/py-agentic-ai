#pip install litellm

# <---- For Google Colab, Set your 'OPENAI_API_KEY' as a secret over there with the "key" icon
# <---- For local, set your 'OPENAI_API_KEY' as an environment variable

import os
try:
    from google.colab import userdata
    api_key = userdata.get('OPENAI_API_KEY')
except ImportError:
    # Running locally, use environment variable
    api_key = os.getenv('OPENAI_API_KEY')

os.environ['OPENAI_API_KEY'] = api_key

# use of the llm model
from litellm import completion
from typing import List, Dict

def generate_response(messages: List[Dict]) -> str:
    """Call LLM to get response"""
    response = completion(
        model="openai/gpt-4o",
        messages=messages,
        max_tokens=1024
    )
    return response.choices[0].message.content

messages = [
    {"role": "system", "content": "You are an expert software engineer that prefers functional programming."},
    {"role": "user", "content": "Write a function to swap the keys and values in a dictionary."}
]

response = generate_response(messages)
print(response)