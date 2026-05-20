import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

API_KEY = "AIzaSyCc96V07m-JRvEpsgHGM842azFgmgq5Esk"

genai.configure(api_key=API_KEY)

def generate_with_retry(prompt):
    fallback_models = [
        "gemini-2.5-flash-lite",
        "gemini-flash-lite-latest",
        "gemini-3.1-flash-lite",
        "gemini-flash-latest",
        "gemini-3.1-flash-lite-preview"
    ]
    for m in fallback_models:
        try:
            model = genai.GenerativeModel(m)
            response = model.generate_content(prompt)
            print(f"SUCCESSfully generated using model: {m}")
            return response
        except Exception as e:
            print(f"Quota exhausted or error for {m}, switching to next model...")
            continue
    raise ValueError("All backup models have completely exhausted their free tier quotas!")

def get_model():
    return None

import json
import re

def parse_json_response(response):
    try:
        text = response.text
    except Exception as e:
        raise ValueError(f"Failed to get response text: {str(e)}")
        
    # Extract everything between the first { and last }
    match = re.search(r'\{.*\}', text, re.DOTALL)
    if match:
        json_str = match.group(0)
        return json.loads(json_str)
    
    raise ValueError(f"No JSON found in response: {text}")