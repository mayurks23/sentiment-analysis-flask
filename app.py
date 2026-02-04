from flask import Flask, render_template, request
import joblib
import re
import string

# ----------------------------
# App Initialization
# ----------------------------
app = Flask(__name__)

# ----------------------------
# Load Model & Vectorizer ONCE
# ----------------------------
model = joblib.load("sentiment_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

# ----------------------------
# Text Preprocessing Function
# ----------------------------
def preprocess_text(text):
    """
    Clean and normalize input text
    """
    text = text.lower()
    text = re.sub(r"http\S+|www\S+", "", text)  # remove URLs
    text = re.sub(r"\d+", "", text)             # remove numbers
    text = text.translate(str.maketrans("", "", string.punctuation))
    text = re.sub(r"\s+", " ", text).strip()
    return text

# ----------------------------
# Routes
# ----------------------------
@app.route("/", methods=["GET", "POST"])
def index():
    sentiment = None

    if request.method == "POST":
        review = request.form.get("review")

        if review:
            cleaned_review = preprocess_text(review)

            # Vectorize using trained TF-IDF
            X = vectorizer.transform([cleaned_review])

            # Predict sentiment
            prediction = model.predict(X)[0]

            sentiment = int(prediction)

    return render_template("index.html", sentiment=sentiment)

# ----------------------------
# Run Application
# ----------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
