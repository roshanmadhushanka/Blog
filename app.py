from flask import Flask, render_template, redirect, session, request
from flask_cors import CORS
from system import boot

app = Flask(__name__)
CORS(app)

# Begin routing


@app.route('/')
def route_home():
    news_list = boot.load_news()
    return render_template('home.html', newsList=news_list)


@app.route('/projects')
def route_projects():
    return render_template('projects.html')


@app.route('/publications')
def route_publications():
    return render_template('publications.html')


@app.route('/about')
def route_about():
    return render_template('about.html')


# End routing


if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.jinja_env.cache = {}
    app.run(debug=True, host="127.0.0.1", port=12345)



