from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from mysite.keyword import extract_keywords
from rest_framework.decorators import api_view
from rest_framework import status

# Create your views here.
def index(request):
    return HttpResponse("응답 입니다")

# @api_view(['GET'])
@api_view(['POST'])
def analyze_text(request):
    # 요청에서 텍스트 추출
    text = request.data.get('text', '')

    # if not text:
    #     return JsonResponse({'error': 'No text provided'}, status=status.HTTP_400_BAD_REQUEST)


    # text = """소나기를 읽은후 소년, 소녀의 사랑의 순수함을 느꼈다.
    #         소년과 소녀는 사랑이라고 말할 수 있을만큼 순수하고 아름다웠다.
    #        
    #         어쩌면 사랑이란 꿈처럼 달콤하지만 결국엔 마무리짓고 깨게 되는 것이 아닌가 싶은 생각도 들었다.
    #         꿈 또한 결국 잠에서 깰 때 깨게 되는 것처럼 말이다."""

    # 텍스트로부터 키워드 추출
    top_keywords = extract_keywords(text)

    return JsonResponse(top_keywords, safe=False, status=status.HTTP_200_OK, json_dumps_params={'ensure_ascii': False})