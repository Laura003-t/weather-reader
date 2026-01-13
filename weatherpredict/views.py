from django.shortcuts import render, redirect
import requests
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from .models import WeatherSearch
import os

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration Successful!')
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'weatherpredict/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
        return render(request, 'weatherpredict/login.html', {'form': form})

@login_required
def home(request):
    weather_data = None
    error_message = None

    if request.method == 'POST':
        #Get location from automatic geolocation
        lat = request.POST.get('latitude')
        lon = request.POST.get('longitude')

        api_key = os.environ.get('WEATHER_API_KEY')

        if not api_key:
            error_message = "Server API key missing"


        if lat and lon:
            url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric'

            try:
                response = requests.get(url)
                data = response.json()

                if response.status_code == 200:
                    weather_data = {
                        'city': data['name'],
                        'temperature': round(data['main']['temp'], 1),
                        'humidity': data['main']['humidity'],
                        'description': data['weather'][0]['description'],
                        'icon': data['weather'][0]['icon'],
                        'latitude': data['coord']['lat'],
                        'longitude': data['coord']['lon'],
                    }

                    #Save to the database
                    WeatherSearch.objects.create(
                        user=request.user,
                        city=weather_data['city'],
                        temperature=weather_data['temperature'],
                        humidity=weather_data['humidity'],
                        description=weather_data['description'],
                        latitude=weather_data['latitude'],
                        longitude=weather_data['longitude'],
                    )
                else:
                    # Get more specific error message from API response
                    error_detail = data.get('message', 'Unknown error')
                    error_message = f"Weather API Error: {error_detail} (Status: {response.status_code})"
            except Exception as e:
                error_message = f"Error fetching weather information: {str(e)}"
        else:
            error_message = "We cannot detect your loaction. Please enable location services."

    return render(request, 'weatherpredict/home.html', {
        'weather_data': weather_data,
        'error': error_message,
    })
