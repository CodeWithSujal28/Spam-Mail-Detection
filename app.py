from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# Load model & vectorizer
model = joblib.load("LR_Spam.pkl")
vectorizer = joblib.load("feature_extraction.pkl")

@app.route("/", methods=["GET", "POST"])
def home():
    prediction = ""
    if request.method == "POST":
        email_text = request.form.get("email")

        if email_text:
            data = vectorizer.transform([email_text])
            result = model.predict(data)[0]

            if result == 1:
                prediction = "🚨 Spam Mail"
            else:
                prediction = "✅ Ham (Not Spam)"

    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
