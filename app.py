from flask import Flask, render_template, request, jsonify
import json
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os

app = Flask(__name__)

# Load FAQs
def load_faqs():
    try:
        with open("faqs.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return [
            {"question": "What is your refund policy?", "answer": "You can request a refund within 30 days of purchase."},
            {"question": "How can I contact support?", "answer": "You can email us at support@example.com."},
            {"question": "What are your working hours?", "answer": "We are available Monday to Friday, 9 AM to 6 PM."}
        ]

faqs = load_faqs()
questions = [item["question"] for item in faqs]
answers = [item["answer"] for item in faqs]

# Preprocess
nltk.download("punkt", quiet=True)
nltk.download("punkt_tab", quiet=True)
nltk.download("stopwords", quiet=True)
from nltk.corpus import stopwords

stop_words = set(stopwords.words("english"))

def preprocess(text):
    tokens = nltk.word_tokenize(text.lower())
    tokens = [t for t in tokens if t.isalpha() and t not in stop_words]
    return " ".join(tokens)

clean_questions = [preprocess(q) for q in questions]
vectorizer = TfidfVectorizer()
faq_vectors = vectorizer.fit_transform(clean_questions)

def get_best_answer(user_query, threshold=0.2):
    clean_q = preprocess(user_query)
    user_vec = vectorizer.transform([clean_q])
    sims = cosine_similarity(user_vec, faq_vectors)[0]
    best_idx = int(sims.argmax())
    best_score = float(sims[best_idx])
    if best_score < threshold:
        return "Sorry, I couldn't find a good answer for that. Please rephrase your question."
    return answers[best_idx]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_msg = data.get("message", "")
    if not user_msg:
        return jsonify({"reply": "Please enter a question."})
    bot_reply = get_best_answer(user_msg)
    return jsonify({"reply": bot_reply})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
