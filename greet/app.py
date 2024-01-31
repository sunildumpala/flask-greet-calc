from flask import Flask

app = Flask(__name__)

@app.route('/welcome')
def just_welcome():
    return "welcome"

@app.route('/welcome/<verb>')
def show_welcome(verb):
    return f"welcome {verb}"