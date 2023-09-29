from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic import TemplateView,ListView,DetailView,View
from account.models import Movie,Video,Watchlist,BackVideo,Cinema,Tvshow,WatchHistory
from django.contrib import messages


from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache

# decorator
def signin_required(fn):
    def inner(request,*args,**kwargs):
        if request.user.is_authenticated:
            return fn(request,*args,**kwargs)
        else:
            return redirect('h')
    return inner
decs=[never_cache,signin_required]
# Create your views here.

@method_decorator(decs,name='dispatch')
class SubscriberHomeView(ListView):
    template_name='sub_home.html'
    queryset=Movie.objects.all()
    context_object_name = 'movie'

@method_decorator(decs,name='dispatch')
class CinemaView(ListView):
    template_name='cinema.html'
    queryset=Cinema.objects.all()
    context_object_name = 'cinema'

@method_decorator(decs,name='dispatch')
class TvshowView(ListView):
    template_name='tvshow.html'
    queryset = Tvshow.objects.all()
    context_object_name = 'tvshow'

@method_decorator(decs,name='dispatch')
class MoviedetailView(DetailView):
    template_name='moviedetails.html'
    pk_url_kwarg='id'
    queryset=Movie.objects.all()
    context_object_name='data'


from django.utils import timezone
decs
def play_video(request, video_id):
    video = get_object_or_404(Video, pk=video_id)
    user = request.user

    # Check if the movie is already in the user's watch history
    existing_watch_history_entry = WatchHistory.objects.filter(user=user, movie=video.movie).first()

    if not existing_watch_history_entry:
        # If the movie is not in the watch history, create a new entry
        WatchHistory.objects.create(user=user, movie=video.movie, timestamp=timezone.now())

    return render(request, 'play_video.html', {'video': video})


# def backplay_video(request, video_id):
#     bvideo = get_object_or_404(BackVideo, pk=video_id)
#     return render(request, 'sub_home.html', {'bvideo': bvideo})

decs
def addmylist(request, *args, **kwargs):
    id = kwargs.get('id')
    mov = Movie.objects.get(id=id)
    user = request.user

    # Check if the movie is already in the user's watchlist
    existing_watchlist_entry = Watchlist.objects.filter(movie=mov, user=user).first()

    if not existing_watchlist_entry:
        # If the movie is not in the watchlist, add it
        Watchlist.objects.create(movie=mov, user=user)
    else:
        # If the movie is already in the watchlist, show a message
        messages.info(request, f'{mov.name} is already in your list.')

    return redirect('subhome')

@method_decorator(decs,name='dispatch')
class MylistView(ListView):
    template_name='mylist.html'
    queryset=Watchlist.objects.all()
    context_object_name='myl'

decs
def removemylist(request,**kwargs):
    mid=kwargs.get("id")
    m=Watchlist.objects.get(id=mid)
    m.delete()
    return redirect('mlist')

@method_decorator(decs, name='dispatch')
class WatchHistoryView(ListView):
    template_name = 'watchhistory.html'
    context_object_name = 'watch_history'
    

    def get_queryset(self):
        return WatchHistory.objects.filter(user=self.request.user)

decs
def removewatchlist(request,**kwargs):
    wid=kwargs.get("id")
    w=WatchHistory.objects.get(id=wid)
    w.delete()
    return redirect('watch_history')
