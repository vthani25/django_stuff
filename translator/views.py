from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from lara_sdk import Translator, Credentials, TranslatePriority

credentials = Credentials(
    access_key_id="O40OKB4EGU1DRG0PRI867N1J43",
    access_key_secret="xSTFpT-KP2gw2TM60MSj0OGYpbtQFG_Eqvvp_oVvnPI"
)
lara = Translator(credentials)

@api_view(['POST'])
def translate(request):
    text = request.data.get("text")
    target = request.data.get("target_lang")
    res = lara.translate(
        text,
        source='en-US',
        target=target,
        content_type='text/plain',
        timeout_ms=2000,
        priority=TranslatePriority.NORMAL
    )
    return Response({'translation': res.translation})


@api_view(['POST'])
def translate_bulk(request):
    texts = request.data.get("texts", [])
    target = request.data.get("target_lang")
    results = []
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

