from flask import Flask, render_template

app = Flask(__name__)

# For writing out the AI
# pen = '[ "nerdy", "pretty", "fun" ]'

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/portfolio')
def index():
    return render_template('index.html')
