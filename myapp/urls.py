from django.urls import path, include
from .views import GreetUserView, ProcessFormView, FetchJokesView

urlpatterns = [
    path('greet/', GreetUserView.as_view(), name = 'greet_user'),
    path('', include('myapps.urls')),
]
urlpatterns += [
    path('process_form/', ProcessFormView.as_view(), name = 'process_form'),
    path('fetch_jokes/', FetchJokesView.as_view(), name = 'fetch_jokes'),
] 