import google.generativeai as genai
from backend.config import API_KEY

genai.configure(api_key=API_KEY)

models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
print('Available models:', models)

successful_models = []
for m in models:
    try:
        model = genai.GenerativeModel(m)
        response = model.generate_content('Say hello')
        print(f'SUCCESS for {m}')
        successful_models.append(m)
    except Exception as e:
        print(f'FAILED for {m}: {e}')

print('\nWORKING MODELS:', successful_models)
