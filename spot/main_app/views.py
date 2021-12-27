from django.http import request
from django.shortcuts import render
from modules.spotipyFunctions import search_tracks, get_track, get_top_fifthy
from modules.sklearnFunctions import predict_track


# Create your views here.
def home_view(request):
    return render(request, 'main_app/home.html')

def search_view(request):
    content = {'searched_tracks': []}   
    if request.method == 'POST':
        print(request.POST.get("search"))
        #print(search_tracks(request.POST.get("search")))
        content['searched_tracks'] = search_tracks(request.POST.get("search"))
    else:
         content['searched_tracks'] = get_top_fifthy()
    return render(request, 'main_app/search.html',content)

def result_view(requenst):
    content = {'track_details': []}
    print(requenst.GET.get('uri'))
    content['track_details'] = get_track(requenst.GET.get('uri'))
    prediction = predict_track(content['track_details'][1])
    content['track_details'].append(prediction[0])
    ##print(prediction)
    return render(requenst, 'main_app/result.html', content)