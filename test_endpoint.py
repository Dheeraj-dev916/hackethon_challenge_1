import requests
import time

print("Testing local API...")
start = time.time()
try:
    res = requests.post("http://127.0.0.1:8000/analyze", json={"content": "Test scenario: system crashed."})
    end = time.time()
    print(f"Time taken: {end-start}s")
    print("Status:", res.status_code)
    print("Response:", res.json())
except Exception as e:
    print("Failed:", e)
