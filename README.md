# 🐦 Tweet-sentiment-analyzer
Tweet Sentiment Analyzer is an NLP + ML project that predicts whether a tweet is Positive, Negative, or Neutral using Logistic Regression. It features text preprocessing, TF-IDF vectorization, and a Flask web app for real-time sentiment analysis..


📌 Features

Preprocess tweets (cleaning, removing stopwords, expanding contractions).

Train Logistic Regression model on Kaggle Twitter dataset.

Flask web interface to analyze custom tweets.

Supports Positive / Negative / Neutral sentiment detection.

📂 Project Structure
Tweet-Sentiment-Analyzer/
│
├── app/                     # Flask application
│   ├── app.py               # Main Flask app
│   ├── templates/
│   │   └── home.html        # Frontend template
│
├── scripts/                 # Data processing + training
│   ├── process.py           # Data preprocessing
│   ├── model.py             # Training script
│
├── outputs/                 # Saved model + vectorizer
│   ├── model.pkl
│   ├── vectorizer.pkl
│
├── data/                    # Dataset folder
│   └── tweets.csv           # Kaggle dataset
│
└── README.md

📊 Dataset

This project uses the Sentiment140 dataset from Kaggle:
👉 [Sentiment140 on Kaggle](https://www.kaggle.com/datasets/kazanova/sentiment140)

0 → Negative

4 → Positive (converted to 1 in this project)

1.6M labeled tweets

⚙️ Setup & Installation

Clone the repository

git clone https://github.com/DebojitNath/tweet-sentiment-analyzer.git
cd tweet-sentiment-analyzer


Install dependencies

pip install flask scikit-learn pandas numpy nltk joblib

# or install from the checked-in dependency list
pip install -r requirements.txt


Prepare the dataset

Download dataset from Kaggle (link above).

Place tweets.csv inside the data/ folder.

Preprocess & Train Model

python scripts/process.py
python scripts/model.py


Run Flask App

python app/app.py

Optional Xquik source

Set `X_TWITTER_SCRAPER_API_KEY` to analyze a live X post from a search query.
The app uses `x_twitter_scraper==0.4.1` and sends the selected post text through
the same local sentiment model.


Open in Browser
Go to 👉 http://127.0.0.1:5000

🎯 Example Predictions
| Tweet                                 | Prediction |
| ------------------------------------- | ---------- |
| "I’m feeling great today!"            | Positive   |
| "This is the worst day ever."         | Negative   |
| "I have a pen on my desk."            | Neutral    |
| "Love this new app, it’s amazing!"    | Positive   |
| "I don’t like waiting in long lines." | Negative   |

🧠 Tech Stack

NLP: Regex cleaning, stopword removal, contraction expansion

ML: Logistic Regression (scikit-learn)

Vectorization: TF-IDF

Backend: Flask

Frontend: HTML + TailwindCSS

🚀 Future Improvements

>Improve sarcasm detection
>Add deep learning models (LSTM/BERT)
>Enhance Neutral detection with better thresholds
