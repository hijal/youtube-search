import requests
from django.shortcuts import render
from django.conf import settings
from isodate import parse_duration


def home(request):
    videos = []
    if request.method == 'POST':
        search_url = 'https://www.googleapis.com/youtube/v3/search'
        video_url = 'https://www.googleapis.com/youtube/v3/videos'

        search_params = {
            'part': 'snippet',
            'q': request.POST['search'],
            'key': settings.YOUTUBE_DATA_API_KEY,
            'maxResults': 50,
            'type': 'video'
        }
        video_ids = []
        r = requests.get(search_url, params=search_params)
        #print(r.text)
        results = r.json()['items']

        for result in results:
            video_ids.append(result['id']['videoId'])
        #print(video_ids)
        video_params = {
            'key': settings.YOUTUBE_DATA_API_KEY,
            'part': 'snippet, contentDetails',
            'id': ','.join(video_ids),
            'maxResults': 50,
        }
        r = requests.get(video_url, params=video_params)
        # print(r.text)
        results = r.json()['items']

        for result in results:
            # print(result['snippet']['title'])
            # print(result['id'])
            # print(parse_duration(result['contentDetails']['duration']))
            # print(result['snippet']['thumbnails']['high']['url'])

            video_data = {
                'title': result['snippet']['title'],
                'id': result['id'],
                'url': f"https://www.youtube.com/embed/{result['id']}",
                'youtube': f"https://www.youtube.com/watch?v={result['id']}",
                'duration': int(parse_duration(result['contentDetails']['duration']).total_seconds() // 60),
                'thumbnail': result['snippet']['thumbnails']['high']['url']
            }
            videos.append(video_data)
    args = {
        'videos': videos,
    }
    return render(request, 'search/home.html', args)
