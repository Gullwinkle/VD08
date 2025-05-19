from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    quote = None
    if request.method == 'GET':
        quote = get_quote()
    return render_template('index.html', quote=quote)

def get_quote():
    url = f'https://zenquotes.io/api/random'
    response = requests.get(url)
    return response.json()[0]


if __name__ == '__main__':
    app.run(debug=True)