import joblib
import sys

svm_classifier = joblib.load("svm_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

def predict_category(user_input):
    input_vectorized = vectorizer.transform([user_input])
    prediction = svm_classifier.predict(input_vectorized)
    return prediction[0]

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py '<text>'")
    else:
        user_input = sys.argv[1]
        category = predict_category(user_input)
        print(f"Predicted Category: {category}")
