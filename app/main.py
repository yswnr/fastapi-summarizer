from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from transformers import pipeline
import torch

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")

# Load summarization pipeline
device = 0 if torch.cuda.is_available() else -1
summarizer = pipeline("summarization", model="facebook/bart-large-cnn", device=device)

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "summary": ""})

@app.post("/", response_class=HTMLResponse)
async def summarize(request: Request, text: str = Form(...)):
    summary = summarizer(text, max_length=60, min_length=20, do_sample=False)[0]["summary_text"]
    return templates.TemplateResponse("index.html", {"request": request, "summary": summary, "input_text": text})
