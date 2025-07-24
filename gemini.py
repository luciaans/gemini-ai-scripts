import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-1.5-flash-latest')

teks_panjang = """
Indonesia adalah negara kepulauan terbesar di dunia yang terdiri dari 17.504 pulau.
Dengan populasi lebih dari 270 juta jiwa, Indonesia adalah negara berpenduduk
terpadat keempat di dunia.
Negara ini memiliki keanekaragaman suku, budaya, dan bahasa yang luar biasa.
Ibu kotanya adalah Jakarta, yang merupakan pusat bisnis dan pemerintahan.
Ekonomi Indonesia terus berkembang pesat, didorong oleh sektor jasa,
industri, dan pertanian.
"""

#prompt = input("Enter your prompt: ")
prompt = f"Ringkas artikel:{teks_panjang}"

response = model.generate_content(prompt)

print(f"Response from Gemini: {response.text}")