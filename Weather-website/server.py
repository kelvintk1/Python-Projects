from flask import Flask, render_template, request
from weather import get_current_weather
from waitress import serve

app = Flask(__name__)

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

if __name__ == "__main__":
    print(" * Running on http://localhost:8080 (Press CTRL+C to quit)")
    serve(app, host="0.0.0.0", port=8080)
