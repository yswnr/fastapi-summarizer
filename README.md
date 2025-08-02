# FastAPI Summarizer

This is a simple web app built using **FastAPI** that takes long text as input and returns a short summary using a pre-trained transformer model (`facebook/bart-large-cnn`). The app uses HuggingFace's `transformers` pipeline for summarization and is served using **Uvicorn**. It also includes a minimal HTML form for interaction.

---

## Features

- Summarizes large input text in a few sentences
- Clean, minimal HTML interface using Jinja2 templates
- GPU support if available (via PyTorch)
- Dockerized for easy deployment

---

## Model Used

- `facebook/bart-large-cnn` from Hugging Face Transformers
- Summarization pipeline with `max_length=60` and `min_length=20`


---

## Setup Instructions (Local)

1. **Clone the repo**
   ```bash
   git clone https://github.com/<your-username>/fastapi-summarizer.git
   cd fastapi-summarizer
2. **Create a virtual env**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
3. **Run the app**
   ```bash
   uvicorn app.main:app --reload
4. **open website**
   http://127.0.0.1:8000
