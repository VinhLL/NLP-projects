import json
from django.shortcuts import render
from django.http import JsonResponse
from googletrans import Translator
from nltk.sentiment import SentimentIntensityAnalyzer

def analyze_sentiment(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            input_text = data.get('text', '')
            if input_text:
                sia = SentimentIntensityAnalyzer()
                sentiment_score = sia.polarity_scores(input_text)
                compound_score = sentiment_score['compound']
                if compound_score > 0:
                    sentiment = 'This text is positive'
                elif compound_score < 0:
                    sentiment = 'This text is negative'
                else:
                    sentiment = 'This text is neutral'
                return JsonResponse({'sentiment': sentiment})
            return JsonResponse({'error': 'No text provided'}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=405)

def translate_text(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            input_text = data.get('text', '')
            if input_text:
                translator = Translator()
                translated = translator.translate(input_text, src='en', dest='vi')
                return JsonResponse({'translated_text': translated.text})
            return JsonResponse({'error': 'No text provided'}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=405)

import spacy
import pytextrank

def summarize_long_text(text, num_sentences=2, num_phrases=2):
    nlp = spacy.load("en_core_web_lg")
    nlp.add_pipe("textrank")
    doc = nlp(text)

    summary_sentences = []
    for sent in doc._.textrank.summary(limit_phrases=num_phrases, limit_sentences=num_sentences):
        summary_sentences.append(sent.text)

    summary_text = ' '.join(summary_sentences)
    return summary_text
def summarize_text(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            input_text = data.get('text', '')
            if input_text:
                summarized_text = summarize_long_text(input_text)
                return JsonResponse({'summarized_text': summarized_text})
            return JsonResponse({'error': 'No text provided'}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=405)

# Create your views here.
def index(request):
    return render(request, "Homepage.html")

def introduction(request):
    return render(request, "Introduction.html")

def summarize(request):
    return render(request, 'Text-Summarization.html')

def qa(request):
    return render(request, 'Q&A.html')

def sentimental(request):
    return render(request, 'Sentimental-Analysis.html')

def translate(request):
    return render(request, 'Machine-Translation.html')