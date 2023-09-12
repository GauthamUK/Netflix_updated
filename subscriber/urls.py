from django.urls import path
from.views import *
from . import views

urlpatterns = [
    path('subhome',SubscriberHomeView.as_view(),name='subhome'),
    path('cinema',CinemaView.as_view(),name='cinema'),
    path('tvshow',TvshowView.as_view(),name='tvshow'),

    path('mdet/<int:id>',MoviedetailView.as_view(),name='mdet'),
    path('play_video/<int:video_id>/', views.play_video, name='play_video'),
    # path('play_bvideo/<int:video_id>/', views.backplay_video, name='play_bvideo'),
    path('alist/<int:id>',addmylist,name='alist'),
    path('mlist',MylistView.as_view(),name='mlist'),
    path('rlist/<int:id>',removemylist,name='rlist'),
    path('watch_history/', WatchHistoryView.as_view(), name='watch_history'),



]