from flask import Flask, render_template
from webapp.python_org_news import get_python_news
from webapp.weather import weather_by_city


app = Flask(__name__)

@app.route('/')
def index():
    weather = weather_by_city("Moscow,Russia")
    if weather:
        weather_text = f"Сейчас {weather['temp_C']}, ощущается как {weather['FeelsLikeC']}"
    else:
        weather_text = "Прогноз сейчас недоступен"

    return render_template('index.html', weather_text=weather_text)


@app.route('/python')    
def get_html(url):
    try:
        result = requests.get(url)
        result.raise_for_status()
        return result.text
    except(requests.RequestException, ValueError):
        print('Сетевая ошибка')
        return False
        
@app.route('/hello')
def hello():
    return 'Hello, World'

if __name__=="__main__":
    html = get_html("https://www.python.org/blogs/")
        if html:
            with open("python-org-news.html", "w", encoding="utf8") as f:
                f.write(html)
    app.run(debug=True)