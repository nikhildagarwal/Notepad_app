from flask import Flask, render_template, session, request, redirect, url_for
from scripts import add_user, fetch_user, send_mail, check_user

app = Flask(__name__, template_folder='html')
app.secret_key = 'fga738sfl8w9jJk824ISFafh0980h4tsg093ASFoiughasdg'

EMAIL = fetch_user.EMAIL
PASSWORD = fetch_user.PASSWORD

SIGN_UP = './sign_up.html'
LOGIN = './login.html'
LOGOUT = './logout.html'
HOME = './home.html'
VERIFICATION = './verification.html'


@app.route('/')
def no_url():
    return redirect(url_for('home'))


@app.route('/home')
def home():
    try:
        email = session['email']
        name = session['name']
        return render_template(HOME, name=name)
    except KeyError:
        return redirect(url_for('login'))


@app.route('/sign_up')
def sign_up():
    return render_template(SIGN_UP)


@app.route('/verification')
def verification():
    return render_template(VERIFICATION)


@app.route('/verification', methods=['POST'])
def verification_check():
    verification_code = request.form.get('vc')
    if str(verification_code) == session['verification_code']:
        email = session['sensitive_data'][1]
        name = session['sensitive_data'][0]
        password = session['sensitive_data'][2]
        session.clear()
        au = add_user.AddUser(str(name), str(email), str(password), "")
        if au.done:
            session['name'] = name
            session['email'] = email
            return redirect(url_for("home"))
        else:
            return render_template(SIGN_UP, message="email provided is already linked to an existing account")
    else:
        return render_template(VERIFICATION,message="invalid code")


@app.route('/sign_up', methods=['GET', 'POST'])
def sign_up_post():
    n = request.form.get('first_name')
    email = request.form.get('email')
    password = request.form.get('password')
    confirm_password = request.form.get('confirm-password')
    if confirm_password != password:
        return render_template(SIGN_UP, FIRST_NAME=n, EMAIL=email, message="passwords provided do not match")
    else:
        cu = check_user.CheckUser(email)
        if cu.exists:
            return render_template(SIGN_UP, message="email provided is already linked to an existing account",
                                   FIRST_NAME=n, PASSWORD=password, C_PASSWORD=confirm_password)
        else:
            mailer = send_mail.Mailer(app)
            mailer.send_verification_code('Infinote Sign-Up Verification', 'infinote.app.adteam@gmail.com',
                                          [email])
            string_code = ""
            for num in mailer.code:
                string_code += str(num)
            session['verification_code'] = string_code
            session['sensitive_data'] = [str(n),str(email),str(password)]
            return redirect(url_for('verification'))


@app.route('/login')
def login():
    return render_template(LOGIN)


@app.route('/login', methods=['GET', 'POST'])
def login_get():
    email = request.form.get('email')
    password = request.form.get('password')
    fu = fetch_user.FetchUser(email, password)
    if fu.error is None:
        session['name'] = fu.name
        session['email'] = fu.email
        return redirect(url_for('home'))
    else:
        if fu.error == EMAIL:
            return render_template(LOGIN, e_message="email provided is not associated with any account",
                                   pre_pass=password)
        else:
            return render_template(LOGIN, p_message="password is incorrect", pre_email=email)


@app.route('/logout')
def logout():
    session.clear()
    return render_template(LOGOUT)


@app.route('/vex')
def v():
    return ""


if __name__ == "__main__":
    app.run(debug=True)
