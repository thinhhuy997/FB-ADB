import google.generativeai as genai
from pathlib import Path
import time

genai.configure(api_key="AIzaSyDgVnGKqKpWI_aGA5XIbtoVYrPjuFLDh7A")
model = genai.GenerativeModel('gemini-pro-vision')


for i in range(1, 6):
    start_time = time.time()
    cookie_picture = {
        'mime_type': 'image/png',
        'data': Path(f'./gen-imgs/{i}.png').read_bytes()
    }
    prompt = "Solve this captcha for me (only the top side of the dice is counted, both the number and the dots of the dice are counted), If the value of the image on the right matches the condition of the image on the left, then say correct, otherwise say wrong."

    response = model.generate_content(
        contents=[prompt, cookie_picture]
    )
    spent_time = time.time() - start_time
    print(f'The image {i} was{response.text} - spent time: ({spent_time})')
    