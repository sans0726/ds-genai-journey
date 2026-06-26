from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/predict', methods=['POST'])
def predict():

    solar_wind = float(request.form['solar_wind'])
    if solar_wind > 500:
      risk = "HIGH RISK"
    else:
       risk = "LOW RISK"

    return render_template(
    "result.html",
    risk=risk
)

    solar_wind = request.form['solar_wind']
    xray_flux = request.form['xray_flux']
    proton_flux = request.form['proton_flux']
    sunspot_number = request.form['sunspot_number']
    magnetic_field = request.form['magnetic_field']

    print("Solar Wind:", solar_wind)
    print("X-Ray Flux:", xray_flux)
    print("Proton Flux:", proton_flux)
    print("Sunspot Number:", sunspot_number)
    print("Magnetic Field:", magnetic_field)

    return "Data Received Successfully"


if __name__ == "__main__":
    app.run(debug=True)