# enhanced_classifier.py
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import make_pipeline
from sklearn.svm import SVC

def train_classifier():
    # Sample data
    texts = [
        "This is a document about machine learning.",
        "This document is about Python programming.",
        "Machine learning and data science are related fields.",
        "Python is a popular programming language.",
        "Data science involves machine learning and statistics.",
        "Programming in Python is fun and easy."
    ]
    labels = ["ML", "Python", "ML", "Python", "ML", "Python"]

    # Create a pipeline that combines TF-IDF and a Support Vector Machine classifier
    model = make_pipeline(TfidfVectorizer(), SVC(kernel='linear'))
    model.fit(texts, labels)
    return model

def classify_text(model, text):
    return model.predict([text])[0]

def main():
    model = train_classifier()
    test_texts = [
        "This is a new document about data science.",
        "Programming with Python is great."
    ]
    for text in test_texts:
        print(f"Text: '{text}' Classified as: {classify_text(model, text)}")

if __name__ == "__main__":
    main()
