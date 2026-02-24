from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI(title="Emotion Classifier API")

# Load model once
model = joblib.load("model/emotion_bow_lr_90f1.pkl")
label_encoder = joblib.load("model/label_encoder.pkl")

class TextInput(BaseModel):
    text: str

@app.get("/")
def home():
    return {"message": "Emotion Classifier API is running"}

@app.post("/predict")
def predict_emotion(input: TextInput):

    prediction = model.predict([input.text])[0]
    probability = model.predict_proba([input.text]).max()

    emotion_label = label_encoder.inverse_transform([prediction])[0]

    return {
        "text": input.text,
        "predicted_emotion": emotion_label,
        "confidence": round(float(probability), 4)
    }
    