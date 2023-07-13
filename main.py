from flask import Flask, redirect, render_template, request
import string
import random

app = Flask(__name__)
urls = {}

def generate_short_url():
    characters = string.ascii_letters + string.digits
    short_url = ''.join(random.choice(characters) for _ in range(6))
    return short_url

@app.route('/', methods=['GET', 'POST'])
def shorten_url():
    if request.method == 'POST':
        long_url = request.form['url']
        short_url = generate_short_url()
        urls[short_url] = long_url
        return render_template('index.html', short_url=request.host_url + short_url)

    return render_template('index.html')

@app.route('/<short_url>')
def redirect_to_url(short_url):
    if short_url in urls:
        long_url = urls[short_url]
        return redirect(long_url)
    else:
        return 'Invalid URL'

if __name__ == '__main__':
    app.run(debug=True)
