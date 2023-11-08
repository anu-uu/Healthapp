from flask import Flask, render_template, url_for, flash, redirect
import joblib
from flask import request
import numpy as np

app = Flask(__name__, template_folder='templates')


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/home")
def home():
    return render_template("index.html")


@app.route('/homes')
def homes():
    # Redirect to the Kidney API's home page by generating the URL
    return redirect(url_for('home', _external=True))


@app.route('/diabetess')
def diabetess():
    # Redirect to the Kidney API's home page by generating the URL
    return redirect(url_for('diabetes', _external=True))


@app.route("/diabetes")
def diabetes():
    return render_template("diabetes.html")


def ValuePredictor(to_predict_list, size):
    to_predict = np.array(to_predict_list).reshape(1, size)
    if (size == 6):
        loaded_model = joblib.load(
            'C:/Users/anupa/Downloads/Health-App-main/Health-App-main/Diabetes_API/diabetes_model.pkl')
        result = loaded_model.predict(to_predict)
    return result[0]


def ValuePredictor2(to_predict_list, size):
    to_predict = np.array(to_predict_list).reshape(1, size)
    if (size == 7):
        loaded_model = joblib.load(
            'C:/Users/anupa/Downloads/Health-App-main/Health-App-main/Kidney_API/kidney_model.pkl')
        result = loaded_model.predict(to_predict)
    return result[0]


def ValuePredictor3(to_predict_list, size):
    to_predict = np.array(to_predict_list).reshape(1, size)
    if (size == 7):
        loaded_model = joblib.load(
            'C:/Users/anupa/Downloads/Health-App-main/Health-App-main/Kidney_API/liver_model1.pkl')
        result = loaded_model.predict(to_predict)
    return result[0]


@app.route('/predict', methods=["POST"])
def predict():
    if request.method == "POST":
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(float, to_predict_list))
        result = 0
        # diabetes
        if (len(to_predict_list) == 6):
            result = ValuePredictor(to_predict_list, 6)

    if (int(result) == 1):
        prediction = "Sorry you chances of getting the disease. Please consult the doctor immediately"
    else:
        prediction = "No need to fear. You have no dangerous symptoms of the disease"
    return (render_template("result.html", prediction_text=prediction))


@app.route('/predict2', methods=["POST"])
def predict2():
    if request.method == "POST":
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(float, to_predict_list))
        result = 0
        # diabetes
        if (len(to_predict_list) == 6):
            result = ValuePredictor2(to_predict_list, 6)

    if (int(result) == 1):
        prediction = "Sorry you chances of getting the disease. Please consult the doctor immediately"
    else:
        prediction = "No need to fear. You have no dangerous symptoms of the disease"
    return (render_template("result.html", prediction_text=prediction))


@app.route('/predict3', methods=["POST"])
def predict3():
    if request.method == "POST":
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(float, to_predict_list))
        result = 0
        # diabetes
        if (len(to_predict_list) == 6):
            result = ValuePredictor3(to_predict_list, 6)

    if (int(result) == 1):
        prediction = "Sorry you chances of getting the disease. Please consult the doctor immediately"
    else:
        prediction = "No need to fear. You have no dangerous symptoms of the disease"
    return (render_template("result.html", prediction_text=prediction))


@app.route('/kidneys')
def kidneys():
    # Redirect to the Kidney API's home page by generating the URL
    return redirect(url_for('kidney', _external=True))


@app.route("/kidney")
def kidney():
    return render_template("kidney.html")


@app.route('/liverss')
def liverss():
    # Redirect to the Kidney API's home page by generating the URL
    return redirect(url_for('liver', _external=True))


@app.route("/liver")
def liver():
    return render_template("liver.html")


if __name__ == "__main__":
    app.run(debug=True)
