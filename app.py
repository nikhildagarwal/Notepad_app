from flask import Flask, render_template, session, request, redirect, url_for
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
    try:
        email = session['email']
        name = session['name']
        return f'hi {name}!'
    except KeyError:
        return redirect(url_for('sign_up'))


@app.route('/sign_up')
def sign_up():
    return render_template(SIGN_UP)


@app.route('/sign_up', methods=['GET', 'POST'])
def sign_up_post():
    n = request.form.get('first_name')
    email = request.form.get('email')
    password = request.form.get('password')
    confirm_password = request.form.get('confirm-password')
    if confirm_password != password:
        return render_template(SIGN_UP, FIRST_NAME=n, EMAIL=email)
    else:
        au = add_user.AddUser(str(n), str(email), str(password))
        print(str(au.done))
        if au.done:
            session['name'] = n
            session['email'] = email
            return redirect(url_for("home"))
        else:
            return render_template(SIGN_UP)


@app.route('/login')
def login():
    return render_template(LOGIN)


if __name__ == "__main__":
    app.run(debug=True)
