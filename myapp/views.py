from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from .forms import UserForm
import requests
from django.conf import Settings

class GreetUserView(View):
    def get(self, request):
        name = request.GET.get('name', 'guest')
        return JsonResponse({'message': f'Hello {name}'})

class ProcessFormView:
    def get(self, request):
        form = UserForm()
        return request(request, 'user_form.html', {'form': form})
    
    def post(self, request):
        form = UserForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            age = form.cleaned_data['age']
            salary = form.cleaned_data['salary']
            return render(request, 'result.html', {'result': f'{name} is {age} years old and earns {salary} every month'})
        return render(request, 'user_form.html', {'form': form})

class FetchJokesView(View):
    def get(self, request):
        form = JokesForm()
        return render(request, 'jokes_form.html', {'form': form})
    def post(self, request):
        form = JokesForm(request.POST)
        if form.is_valid():
            count = form.cleaned_data['count']
            response = requests.get(f'https://api.api-ninjas.com/v1/jokes?limit={count}', headers = {'X-Api-Key': settings.API_KEY})
            jokes = response.json()
            return render(request, 'jokes_result.html', {'jokes': jokes})
        return render(request, 'jokes_form.html', {'form': form})