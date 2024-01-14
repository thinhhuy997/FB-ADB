import google.generativeai as genai
from pathlib import Path

genai.configure(api_key="AIzaSyDgVnGKqKpWI_aGA5XIbtoVYrPjuFLDh7A")
model = genai.GenerativeModel('gemini-pro-vision')

cookie_picture = {
    'mime_type': 'image/png',
    'data': Path('./gen-imgs/captcha.png').read_bytes()
}
prompt = "Solve me this captcha - How many pixels do I need to drag the slider?"

response = model.generate_content(
    contents=[prompt, cookie_picture]
)
print(response.text)