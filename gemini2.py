import os
import google.generativeai as genai
from dotenv import load_dotenv
import pandas as pd

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-1.5-flash-latest')

df = pd.read_csv("data/ulasan.csv")

def generate_tags(review_text):
    """
    Generate tags for a given review text using the Gemini model.
    """
    prompt = f"""
    Berikan tags dari ulasan: {review_text}.
    Jawab berupa daftar tag yang relevan dengan ulasan tersebut.
    Berikan 3 tag yang relevan dengan ulasan tersebut.
    Tag dalam format: tag1, tag2, tag3.
    Tambahkan tanda pagar (#) di depan setiap tag tanpa spasi.
    Contoh: #tag1, #tag2, #tag3.
    """

    response = model.generate_content(prompt)
    return response.text

df['tags'] = df['review_text'].apply(generate_tags)
df.to_csv("data/ulasan_with_tags.csv", index=False)
print(df.head())