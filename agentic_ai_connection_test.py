#pip install litellm

# <---- For Google Colab, Set your 'OPENAI_API_KEY' as a secret over there with the "key" icon
# <---- For local, set your 'OPENAI_API_KEY' as an environment variable

import os
import base64
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

def generate_response_base64_encoded(messages: List[Dict]) -> str:
    """Call LLM to get response and encode it in Base64"""
    response = completion(
        model="openai/gpt-4o",
        messages=messages,
        max_tokens=1024
    )
    # Encode the response in Base64
    response_text = response.choices[0].message.content
    encoded_response = base64.b64encode(response_text.encode('utf-8')).decode('utf-8')
    return encoded_response

# Option 1: Ask the model to respond in Base64 format
messages_model_base64 = [
    {"role": "system", "content": "You are an expert software engineer that prefers functional programming. Always encode your entire response in Base64 format."},
    {"role": "user", "content": "Write a function to swap the keys and values in a dictionary."}
]

# Option 2: Get normal response and encode it in Base64 ourselves
messages_normal = [
    {"role": "system", "content": "You are an expert software engineer that prefers functional programming."},
    {"role": "user", "content": "Write a function to swap the keys and values in a dictionary."}
]

print("=== Option 1: Model responds in Base64 ===")
response1 = generate_response(messages_model_base64)
print("Model's Base64 response:")
print(response1)
print("\nDecoded response:")
try:
    decoded = base64.b64decode(response1).decode('utf-8')
    print(decoded)
except:
    print("Response was not valid Base64")

print("\n=== Option 2: We encode the response in Base64 ===")
response2 = generate_response_base64_encoded(messages_normal)
print("Base64 encoded response:")
print(response2)
print("\nDecoded response:")
decoded2 = base64.b64decode(response2).decode('utf-8')
print(decoded2) 