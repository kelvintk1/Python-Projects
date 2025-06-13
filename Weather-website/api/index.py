from flask import Flask, render_template, request
import sys
import os

# Add the parent directory to the path so we can import weather module
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from weather import get_current_weather

app = Flask(__name__, 
           template_folder='../templates',
           static_folder='../static')

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/weather')
def get_weather():
    city = request.args.get('city')
    if not city:
        return render_template('error.html', message="Please enter a city name")

    weather_data = get_current_weather(city)
    if weather_data.get('cod') != 200:
        return render_template('error.html', message=weather_data.get('message', 'Unknown error'))
    
    return render_template(
        "weather.html",
        title=weather_data["name"],
        status=weather_data["weather"][0]["description"].capitalize(),
        temp=f"{weather_data['main']['temp']:.1f}°C"
    )

# For Vercel, we need to export the app
if __name__ == "__main__":
    app.run(debug=True)