from flask import Flask, render_template, session
from scripts import add_user

app = Flask(__name__, template_folder='html')
app.secret_key = 'fga738sfl8w9jJk824ISFafh0980h4tsg093ASFoiughasdg'

SIGN_UP = './sign_up.html'
LOGIN = './login.html'


@app.route('/')
def no_url():
    return "hello hopey!"


@app.route('/home')
def home():
    return "home"


@app.route('/sign_up')
def sign_up():
    return render_template(SIGN_UP)


@app.route('/login')
def login():
    return render_template(LOGIN)


if __name__ == "__main__":
    app.run(debug=True)
