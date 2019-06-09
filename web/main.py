#! /usr/bin/env python

from flask import Flask, render_template, request
from wtflask.generate import Randomizer, Predictor
from wtflask.validate import random_check, predict_check, string_to_digit


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/random-number", methods=['GET', 'POST'])
def random_int():
    if request.method == 'POST':
        random_start = int(request.form['randomStart'])
        random_end = int(request.form['randomEnd'])
        if random_check(random_start, random_end):
            random_outcome = Randomizer(random_start, random_end).make_random_number()
            return render_template("random_number.html", random_number=random_outcome)
    return render_template("random_number.html")


@app.route("/predict", methods=['GET', 'POST'])
def predict_int():
    if request.method == 'POST':
        # whole validation part can be much more efficient!
        input_numbers = [n.strip() for n in request.form['numberSequence'].split(',')]
        input_numbers = string_to_digit(input_numbers)
        if predict_check(input_numbers):
            prediction = int(Predictor(input_numbers).make_prediction())
            return render_template("predict_number.html", predicted_number=prediction)
    return render_template("predict_number.html")


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(port=8080, debug=True)
