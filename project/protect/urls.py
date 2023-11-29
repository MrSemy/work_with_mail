from django.urls import path, include
from .views import IndexView


urlpatterns = [
    path('', IndexView.as_view()),
    path('pages/', include('django.contrib.flatpages.urls')),
    #path('', include('simpleapp.urls')),
]