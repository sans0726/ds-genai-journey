from flask import Flask, render_template, request, flash, jsonify
import pandas as pd
import joblib

app = Flask(__name__)
app.secret_key = "solar_flare_project"

model = joblib.load("solar_flare_model.pkl")
feature_names = joblib.load("feature_names.pkl")


@app.route("/")
def home():
    return render_template("home.html")
@app.route("/search")
def search():

    city = request.args.get("city")
    risk = request.args.get("risk")

    return f"City: {city}, Risk Level: {risk}"


@app.route("/predict", methods=["POST"])
def predict():

    # -------------------------------
    # Read values from the form
    # -------------------------------

    modified_zurich = request.form["modified_zurich_class"]
    largest_spot = request.form["largest_spot_size"]
    spot_distribution = request.form["spot_distribution"]

    activity = int(request.form["activity"])
    evolution = int(request.form["evolution"])
    previous_flare = int(request.form["previous_flare_activity"])
    historically_complex = int(request.form["historically_complex"])
    became_complex = int(request.form["became_complex"])
    area = int(request.form["area"])
    largest_spot_area = int(request.form["largest_spot_area"])
    common_flares = int(request.form["common_flares"])
    moderate_flares = int(request.form["moderate_flares"])

    # -------------------------------
    # Create input dataframe
    # -------------------------------

    input_df = pd.DataFrame(columns=feature_names)
    input_df.loc[0] = 0

    # Numerical Features
    input_df["activity"] = activity
    input_df["evolution"] = evolution
    input_df["previous 24 hour flare activity"] = previous_flare
    input_df["historically-complex"] = historically_complex
    input_df["became complex on this pass"] = became_complex
    input_df["area"] = area
    input_df["area of largest spot"] = largest_spot_area
    input_df["common flares"] = common_flares
    input_df["moderate flares"] = moderate_flares

    # -------------------------------
    # Encode categorical features
    # -------------------------------

    zurich_col = f"modified Zurich class_{modified_zurich}"
    if zurich_col in input_df.columns:
        input_df.loc[0, zurich_col] = 1

    spot_col = f"largest spot size_{largest_spot}"
    if spot_col in input_df.columns:
        input_df.loc[0, spot_col] = 1

    distribution_col = f"spot distribution_{spot_distribution}"
    if distribution_col in input_df.columns:
        input_df.loc[0, distribution_col] = 1

    # -------------------------------
    # Prediction
    # -------------------------------

    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0][1]

    if prediction == 1:
        risk = "HIGH RISK OF SEVERE SOLAR FLARE"
        color ="#ff4444"
    else:
        risk = "LOW RISK OF SEVERE SOLAR FLARE"
        color = "#00ff99"

    probability = round(probability * 100, 2)
    flash("Prediction completed successfully!", "success")
    return render_template(
        "result.html",
        risk=risk,
        probability=probability,
        color=color
    )
@app.route("/api")
def api():

    return jsonify({

        "message": "Welcome to Solar Flare Prediction API",

        "status": "Running",

        "version": "1.0"

    })
@app.route("/predict_api", methods=["POST"])
def predict_api():

    data = request.get_json()

    # Create empty dataframe
    input_df = pd.DataFrame(columns=feature_names)
    input_df.loc[0] = 0

    # Fill numeric features
    for key, value in data.items():
        if key in input_df.columns:
            input_df.loc[0, key] = value

    prediction = model.predict(input_df)[0]

    if prediction == 1:
        risk = "HIGH RISK"
    else:
        risk = "LOW RISK"

    return jsonify({
        "prediction": int(prediction),
        "risk": risk
    })

if __name__ == "__main__":
    app.run(debug=True)

import os

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        debug=False
    )