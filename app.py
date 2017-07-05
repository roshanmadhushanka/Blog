from flask import Flask, render_template, redirect, session, request
from flask_cors import CORS
from system import boot

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    news_list = boot.load_news()
    return render_template('home.html', newsList=news_list)

if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.jinja_env.cache = {}
    app.run(debug=True, host="127.0.0.1", port=12345)



