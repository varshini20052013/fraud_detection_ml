from flask import Flask, render_template, request
from model import predict_fraud

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None

    if request.method == "POST":
        amount = float(request.form["amount"])
        hour = int(request.form["hour"])
        merchant = int(request.form["merchant"])

        result = predict_fraud(amount, hour, merchant)

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
