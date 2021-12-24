from django.http import request
from django.shortcuts import render
from modules.spotipyFunctions import search_tracks, get_track


# Create your views here.
def home_view(request):
    return render(request, 'main_app/home.html')

def search_view(request):
    content = {'searched_tracks': []}   
    if request.method == 'POST':
        print(request.POST.get("search"))
        #print(search_tracks(request.POST.get("search")))
        content['searched_tracks'] = search_tracks(request.POST.get("search"))
        
    return render(request, 'main_app/search.html',content)

def result_view(requenst):
    content = {'track_details': []}
    print(requenst.GET.get('uri'))
    content['track_details'] = get_track(requenst.GET.get('uri'))
    return render(requenst, 'main_app/result.html', content)