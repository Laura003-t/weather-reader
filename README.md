# 🌦️ Weather Prediction & Geolocation App

A robust Django-based weather application that leverages the OpenWeatherMap API to provide real-time weather updates based on the user's precise geolocation.

## 🚀 Features

- **📍 Automatic Geolocation**: Detects user location via browser-based coordinates (latitude & longitude).
- **📊 Real-time Weather Data**: Fetches current temperature, humidity, and weather conditions.
- **🔐 User Authentication**: Secure registration and login system.
- **📜 Search History**: Automatically logs weather searches to a database for authenticated users.
- **📱 Responsive Design**: Clean and intuitive interface for both desktop and mobile.

## 🛠️ Tech Stack

- **Backend**: Python, [Django](https://www.djangoproject.com/)
- **Frontend**: HTML5, CSS3, JavaScript (Geolocation API)
- **Database**: SQLite3 (Development)
- **API**: [OpenWeatherMap API](https://openweathermap.org/api)
- **Tools**: `requests`, `django-environ`, `python-dotenv`

## ⚙️ Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone <your-repo-url>
   cd "Personally Built Weather Prediction App Using Django"
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r weatherapp/requirements.txt
   ```

4. **Environment Variables**:
   Create a `.env` file in the `weatherapp` directory and add your OpenWeatherMap API key:
   ```env
   WEATHER_API_KEY=your_api_key_here
   DEBUG=True
   SECRET_KEY=your_django_secret_key
   ```

5. **Run Migrations**:
   ```bash
   cd weatherapp
   python manage.py migrate
   ```

6. **Start the server**:
   ```bash
   python manage.py runserver
   ```

## 📝 Usage

1. Register a new account or log in.
2. Allow the browser to access your location.
3. Click the search button to fetch the current weather for your area.
4. Your searches will be saved to your profile for future reference.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](<your-repo-url>/issues).

## 📄 License

This project is open-source and available under the MIT License.
