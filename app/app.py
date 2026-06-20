from flask import Flask, render_template, request
import joblib
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from scripts import process
from xquik_source import search_xquik_posts


app = Flask(__name__)


model = joblib.load("outputs/model.pkl")
vectorizer = joblib.load("outputs/vectorizer.pkl")


positive_words = {"great", "amazing", "best", "happy", "love", "awesome", "fantastic"}
negative_words = {"stfu", "hate", "worst", "terrible", "sucks", "angry", "mad"}

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        raw_text = request.form["tweet"].strip()
        query = request.form.get("xquik_query", "").strip()

        if not raw_text and query:
            try:
                posts = search_xquik_posts(query, limit=1)
                raw_text = posts[0] if posts else ""
            except RuntimeError as exc:
                return render_template("home.html", error_text=str(exc), tweet=raw_text)
            except Exception:
                return render_template("home.html", error_text="Unable to load X posts.", tweet=raw_text)

        if not raw_text:
            return render_template("home.html", error_text="Enter a tweet or Xquik search query first.", tweet=raw_text)

        text = process.clean_tweet(raw_text)


        if text.strip() == "":
            sentiment = "Neutral"
            return render_template("home.html", prediction_text=f"Sentiment: {sentiment}", tweet=raw_text)


        text_vec = vectorizer.transform([text])
        neg_prob, pos_prob = model.predict_proba(text_vec)[0]

        if text_vec.nnz == 0:
            sentiment = "Neutral"


        elif abs(pos_prob - neg_prob) < 0.2:
            sentiment = "Neutral"

       
        elif any(word in text.split() for word in positive_words):
            sentiment = "Positive"
        elif any(word in text.split() for word in negative_words):
            sentiment = "NEGATIVE"

        elif pos_prob > neg_prob:
            sentiment = "Positive"
        else:
            sentiment = "Negative"

        return render_template("home.html", prediction_text=f"Sentiment: {sentiment}", tweet=raw_text)

if __name__ == '__main__':
    app.run(debug=True)
