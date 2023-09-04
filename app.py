from flask import Flask, render_template

app = Flask(__name__, template_folder='html')

SIGN_UP = './sign_up.html'


@app.route('/')
def yo():
    return render_template(SIGN_UP, name='NIKHIL')


if __name__ == "__main__":
    app.run(debug=True)
