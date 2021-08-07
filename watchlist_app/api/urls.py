from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from watchlist_app.api.views import movie_list, movie_details
# from watchlist_app.api.views import MovieListAV, MovieDetailAV
from watchlist_app.api.views import (StreamPlatformVS, StreamPlatformAV, WatchListAV, WatchDetailAV, 
                                    StreamPlatformDetailAV, ReviewList, 
                                    ReviewDetail, ReviewLCreate)

router = DefaultRouter()
router.register('stream', StreamPlatformVS, 'streamplatform')

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>', WatchDetailAV.as_view(), name='movie-detail'),

    path('', include(router.urls)),

    # path('stream/', StreamPlatformAV.as_view(), name='stream'),
    # path('stream/<int:pk>', StreamPlatformDetailAV.as_view(), name='stream-detail'),
    # path('review/', ReviewList.as_view(), name='review-list'),
    # path('review/<int:pk>', ReviewDetail.as_view(), name='review-detail'),

    path('stream/<int:pk>/review-create/', ReviewLCreate.as_view(), name='review-create'),
    path('stream/<int:pk>/review/', ReviewList.as_view(), name='review-list'),
    path('stream/review/<int:pk>', ReviewDetail.as_view(), name='review-detail'),
]
