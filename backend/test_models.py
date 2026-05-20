import os
import time
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
API_KEY = os.getenv("AIzaSyCc96V07m-JRvEpsgHGM842azFgmgq5Esk")
genai.configure(api_key=API_KEY)

models_to_test = [
    "gemini-flash-latest",
    "gemini-2.0-flash",
    "gemini-3.5-flash",
    "gemini-2.5-flash"
]

for m in models_to_test:
    print(f"Testing {m}...")
    try:
        model = genai.GenerativeModel(m)
        resp = model.generate_content("Say YES")
        print(f"✅ {m} WORKS! (Quota available)")
    except Exception as e:
        print(f"❌ {m} FAILED: {e}")
    time.sleep(2)
