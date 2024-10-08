# myapp/views.py
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import time  # 임시로 분석 시간을 시뮬레이션하기 위해 사용

def home(request):
    return render(request, 'myapp/home.html')

@csrf_exempt
def loading(request):
    if request.method == 'POST':
        # 여기서 실제 음성 파일 처리 및 분석을 수행합니다.
        # 현재는 임시로 파일을 저장하고 3초 대기 후 분석 페이지로 리다이렉트합니다.
        audio_file = request.FILES.get('audio_data')
        if audio_file:
            # 파일 저장 로직 (실제 구현 시 적절한 저장 경로와 파일명을 사용해야 합니다)
            with open('recorded_audio.webm', 'wb+') as destination:
                for chunk in audio_file.chunks():
                    destination.write(chunk)
        
        time.sleep(3)
        return JsonResponse({'status': 'success'})
    return render(request, 'myapp/loading.html')

def analyze(request):
    # 임시 분석 결과 데이터
    analysis_result = {
        'vocal_range': 'A2 - C5',
        'voice_character': '맑고 부드러운 음색',
        'recommended_songs': [
            '노래 제목 1 - 가수 1',
            '노래 제목 2 - 가수 2',
            '노래 제목 3 - 가수 3',
        ]
    }
    return render(request, 'myapp/analyze.html', {'result': analysis_result})

def recommend(request):
    if request.method == 'POST':
        song_title = request.POST.get('song_title')
        # 실제로는 여기서 노래 정보를 검색하고 키 추천을 수행합니다.
        song_info = {
            'title': song_title,
            'artist': '가수 이름',
            'original_key': 'C',
            'recommended_key': 'A'
        }
        return render(request, 'myapp/recommend.html', {'song_info': song_info})
    return render(request, 'myapp/recommend.html')


def mypage(request):
    # 임시 데이터 (실제로는 데이터베이스에서 가져와야 함)
    voice_analyses = [
        {'date': '2024-03-15', 'vocal_range': 'A2 - C5', 'voice_character': '맑고 부드러운 음색'},
        {'date': '2024-03-10', 'vocal_range': 'G2 - B4', 'voice_character': '파워풀한 음색'},
    ]
    song_searches = [
        {'title': '노래 제목 1', 'artist': '가수 1', 'date': '2024-03-14'},
        {'title': '노래 제목 2', 'artist': '가수 2', 'date': '2024-03-13'},
    ]
    return render(request, 'myapp/mypage.html', {
        'voice_analyses': voice_analyses,
        'song_searches': song_searches
    })