from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from lara_sdk import Translator, Credentials, TranslatePriority
import os

# Securely load credentials from environment variables
credentials = Credentials(
    access_key_id=os.getenv('O40OKB4EGU1DRG0PRI867N1J43'),
    access_key_secret=os.getenv('xSTFpT-KP2gw2TM60MSj0OGYpbtQFG_Eqvvp_oVvnPI')
)
lara = Translator(credentials)

@api_view(['POST'])
def translate(request):
    text = request.data.get("text")
    target = request.data.get("target_lang")
    
    if not text or not target:
        return Response({'error': 'Text and target language are required'}, status=400)
    
    try:
        res = lara.translate(
            text,
            source='en-US',
            target=target,
            content_type='text/plain',
            timeout_ms=2000,
            priority=TranslatePriority.NORMAL
        )
        return Response({'translated_text': res.translation})
    except Exception as e:
        return Response({'error': str(e)}, status=500)

@api_view(['POST'])
def translate_bulk(request):
    texts = request.data.get("texts", [])
    target = request.data.get("target_lang")
    
    if not texts or not target:
        return Response({'error': 'Texts and target language are required'}, status=400)
    
    results = []
    try:
        for t in texts:
            res = lara.translate(
                t,
                source='en-US',
                target=target,
                content_type='text/plain',
                timeout_ms=2000,
                priority=TranslatePriority.NORMAL
            )
            results.append(res.translation)
        return Response({'translations': results})
    except Exception as e:
        return Response({'error': str(e)}, status=500)
