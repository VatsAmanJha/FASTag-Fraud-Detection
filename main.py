from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pickle
import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from fastapi.middleware.cors import CORSMiddleware

# Load the trained model
with open('xgb_model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('preprocessor.pkl', 'rb') as f:
    preprocessor = pickle.load(f)

# Define the request body model
class FraudDetectionRequest(BaseModel):
    Vehicle_Type: str
    Lane_Type: str
    Vehicle_Dimensions: str
    Transaction_Amount: float
    Amount_paid: float
    Geographical_Location: str
    Vehicle_Speed: float
    Year: int
    Month: str
    Day: str
    Hour: int

# Initialize FastAPI app
app = FastAPI(title="FASTag Fraud Detection")

origins = [
    "http://127.0.0.1:5500",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/predict")
def predict_fraud(data: FraudDetectionRequest):
    # Convert the input data to a DataFrame
    input_data = pd.DataFrame([data.dict()])
    
    # Predict using the trained model
    prediction = model.predict(preprocessor.transform(input_data))

    # Map the prediction to the corresponding label
    prediction_label = 'Fraud' if prediction[0] == 1 else 'Not Fraud'

    return {"prediction": prediction_label}

# Run the FastAPI application
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
