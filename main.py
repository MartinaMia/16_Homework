from flask import Flask, render_template

app = Flask(__name__)

import datetime

@app.route("/")
def index():
    some_text = "Welcome to my homepage"
    current_year = datetime.datetime.now().year

    return render_template("index.html", some_text=some_text, current_year=current_year)

@app.route("/about-me")
def about():
    return render_template("about.html")

@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")

if __name__ == '__main__':
    app.run(debug=False)