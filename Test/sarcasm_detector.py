import pickle
import re


def predict(text):
    """This function predicts if a sentence is sarcastic or not."""

    data = text

    data = re.sub('[^a-zA-Z]', ' ', data)

    s = []

    s.append(data)

    with open('tfidf.pkl', 'rb') as f:
        vectorizer = pickle.load(f)

    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)

    data = vectorizer.transform(s).toarray()

    prediction = model.predict(data)

    return int(prediction[0])
