import uvicorn
from fastapi import FastAPI, Query
import joblib
from pydantic import BaseModel
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer

model = joblib.load(open("model/naive_bayes.pkl","rb"))

vec = joblib.load(open("model/vectorizer.pkl","rb"))

class User_name(BaseModel):
   name: str 

app = FastAPI()

@app.get("/")
async def index():
    return {"text":"Our First route"}

@app.post('/predict/')
async def predict(user_name: User_name):
    data = [user_name.name]
    vect =  vec.transform(data).toarray()
    result = model.predict(vect)
    result_list = result.tolist()
    return {"orig_name": user_name.name, "prediction": result_list}