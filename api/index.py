from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    #return 'Hello, World!'
     with open('link.txt', 'r', encoding='utf-8') as file:
        links = file.readlines()
    return render_template('display_links.html', links=links)

@app.route('/about')
def about():
    return 'About'
