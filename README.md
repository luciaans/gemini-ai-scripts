# Gemini AI Scripts - Text Summarization & Review Tagging

Kumpulan script Python yang menggunakan Google Gemini AI untuk pemrosesan teks, meliputi ringkasan artikel dan otomatis tagging ulasan.

## 📁 Struktur Project

```
├── data/
│   ├── masuk/
│   ├── original/
│   ├── ulasan_with_tags.csv
│   └── ulasan.csv
├── venv/
├── .env
├── gemini1.py          # Script ringkasan teks
├── gemini2.py          # Script tagging ulasan
├── Handout-api.pdf
└── README.md
```

## 🌟 Fitur Utama

### 1. **gemini1.py** - Text Summarization
- Meringkas artikel atau teks panjang
- Menggunakan Gemini 1.5 Flash model
- Input manual atau dari variabel

### 2. **gemini2.py** - Review Tagging  
- Otomatis generate tags untuk ulasan produk
- Batch processing dari file CSV
- Output dengan format hashtag (#tag1, #tag2, #tag3)
- Menghasilkan 3 tag relevan per ulasan

## 🔧 Requirements

```txt
google-generativeai
python-dotenv
pandas
os (built-in)
```

## 📦 Instalasi

1. **Clone atau download project**

2. **Install dependencies:**
```bash
pip install google-generativeai python-dotenv pandas
```

3. **Setup Google AI API Key:**
   - Dapatkan API key dari [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Buat file `.env` di root directory:
   ```env
   GOOGLE_API_KEY=your_api_key_here
   ```

4. **Siapkan data (untuk gemini2.py):**
   - Letakkan file `ulasan.csv` di folder `data/`
   - Format CSV harus memiliki kolom `review_text`

## 🚀 Cara Penggunaan

### Script 1: Text Summarization (gemini1.py)

```python
# Jalankan script
python gemini1.py
```

**Fitur:**
- Meringkas teks panjang tentang Indonesia (contoh default)
- Dapat dimodifikasi untuk input manual dengan mengubah baris komentar
- Output: ringkasan artikel yang informatif

**Customization:**
```python
# Untuk input manual, uncomment baris ini:
# prompt = input("Enter your prompt: ")

# Untuk teks custom, ganti variabel teks_panjang
teks_panjang = """
Masukkan teks Anda di sini...
"""
```

### Script 2: Review Tagging (gemini2.py)

```python
# Jalankan script
python gemini2.py
```

**Input Requirements:**
- File CSV: `data/ulasan.csv`
- Kolom yang diperlukan: `review_text`

**Output:**
- File baru: `data/ulasan_with_tags.csv`
- Kolom tambahan: `tags` (format: #tag1, #tag2, #tag3)

## 📊 Format Data

### Input CSV (ulasan.csv):
```csv
review_text
"Produk bagus, pengiriman cepat, recommended"
"Kualitas jelek, tidak sesuai gambar"
"Pelayanan ramah, barang ori, puas banget"
```

### Output CSV (ulasan_with_tags.csv):
```csv
review_text,tags
"Produk bagus, pengiriman cepat, recommended","#bagus, #cepat, #recommended"
"Kualitas jelek, tidak sesuai gambar","#jelek, #kualitas, #tidak_sesuai"
"Pelayanan ramah, barang ori, puas banget","#ramah, #original, #puas"
```

## ⚙️ Konfigurasi

### Model Settings:
- **Model**: `gemini-1.5-flash-latest`
- **Provider**: Google Generative AI
- **Response Type**: Text generation

### Environment Variables:
```env
GOOGLE_API_KEY=your_google_ai_api_key
```

## 🎯 Use Cases

### Text Summarization:
- **Content Curation**: Ringkas artikel berita panjang
- **Research**: Summarize paper atau dokumen akademik  
- **Business**: Executive summary dari laporan
- **Education**: Ringkasan materi pembelajaran

### Review Tagging:
- **E-commerce**: Kategorisasi ulasan produk otomatis
- **Sentiment Analysis**: Pre-processing untuk analisis sentimen
- **Content Management**: Organisasi feedback pelanggan
- **Market Research**: Analisis trending topics dari review

## 🔧 Customization

### Modifikasi Prompt Tagging:
```python
def generate_tags(review_text):
    prompt = f"""
    Berikan tags dari ulasan: {review_text}.
    
    CUSTOM INSTRUCTIONS:
    - Fokus pada aspek [sesuaikan: kualitas/service/delivery]
    - Gunakan bahasa [Indonesia/English]
    - Format: [#tag atau tag biasa]
    - Jumlah tag: [1-5 tag]
    
    Contoh output: #tag1, #tag2, #tag3
    """
    # ... rest of function
```

### Batch Processing Optimization:
```python
# Untuk dataset besar, tambahkan progress tracking
from tqdm import tqdm
tqdm.pandas()

df['tags'] = df['review_text'].progress_apply(generate_tags)
```

## 🛠️ Error Handling

### Common Issues:

1. **API Key Error:**
```python
# Tambahkan validation
if not GOOGLE_API_KEY:
    raise ValueError("GOOGLE_API_KEY not found in environment variables")
```

2. **Rate Limiting:**
```python
import time

def generate_tags_with_retry(review_text, max_retries=3):
    for attempt in range(max_retries):
        try:
            return generate_tags(review_text)
        except Exception as e:
            if attempt < max_retries - 1:
                time.sleep(2 ** attempt)  # Exponential backoff
                continue
            raise e
```

3. **CSV Format Issues:**
```python
# Validasi kolom yang diperlukan
required_columns = ['review_text']
if not all(col in df.columns for col in required_columns):
    raise ValueError(f"CSV must contain columns: {required_columns}")
```

## 📈 Performance Tips

1. **Batch Processing**: Process dalam chunks untuk dataset besar
2. **Caching**: Simpan hasil untuk avoid re-processing
3. **Async Processing**: Gunakan asyncio untuk multiple requests
4. **Error Recovery**: Implementasi retry mechanism
5. **Resource Management**: Monitor API quota usage

## 🔍 Monitoring & Logging

```python
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def generate_tags(review_text):
    try:
        logger.info(f"Processing review: {review_text[:50]}...")
        # ... processing logic
        logger.info("Tags generated successfully")
        return response.text
    except Exception as e:
        logger.error(f"Error generating tags: {e}")
        return "Error generating tags"
```

## 💡 Advanced Features

### 1. Multi-language Support:
```python
def generate_tags_multilang(review_text, language='id'):
    prompts = {
        'id': f"Berikan tags bahasa Indonesia untuk ulasan: {review_text}",
        'en': f"Generate English tags for review: {review_text}"
    }
    # ... implementation
```

### 2. Custom Tag Categories:
```python
def generate_categorized_tags(review_text):
    prompt = f"""
    Analisis ulasan dan berikan tags dalam kategori:
    - Sentiment: [positif/negatif/netral]
    - Aspect: [produk/layanan/pengiriman]
    - Quality: [bagus/jelek/biasa]
    
    Ulasan: {review_text}
    """
```

## 🚨 Rate Limits & Costs

- **Gemini 1.5 Flash**: Check current limits di Google AI Studio
- **Best Practice**: Implement request throttling
- **Cost Optimization**: Use batch processing untuk efisiensi

## 📝 Example Results

### Summarization Output:
```
Input: "Indonesia adalah negara kepulauan terbesar di dunia..."
Output: "Indonesia merupakan negara kepulauan terbesar dengan 17.504 pulau dan populasi 270+ juta jiwa. Memiliki keanekaragaman budaya, ibu kota Jakarta, dan ekonomi berkembang pesat."
```

### Tagging Output:
```
Review: "Barang bagus banget, pengiriman super cepat, seller responsif"
Tags: "#bagus, #cepat, #responsif"
```

## 🔮 Future Enhancements

- [ ] GUI interface menggunakan Streamlit/Gradio
- [ ] Support untuk multiple file formats (JSON, XML)
- [ ] Real-time processing dengan WebSocket
- [ ] Integration dengan database (MySQL, PostgreSQL)
- [ ] Analytics dashboard untuk hasil tagging
- [ ] Export ke berbagai format (Excel, PDF)
- [ ] API wrapper untuk integration mudah

## 🆘 Troubleshooting

### Script tidak berjalan:
1. Periksa API key di file `.env`
2. Pastikan semua dependencies terinstall
3. Check internet connection untuk API calls

### CSV processing error:
1. Pastikan format CSV sesuai (UTF-8 encoding)
2. Check kolom `review_text` ada dan tidak kosong
3. Validate data types

### API errors:
1. Check quota limit di Google AI Studio
2. Verify API key masih aktif
3. Monitor rate limiting

---

**Made by Lucians**
