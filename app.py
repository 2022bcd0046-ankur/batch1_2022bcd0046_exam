from fastapi import FastAPI
import uvicorn

from scripts.predict import predict

app = FastAPI()


@app.post("/predict")
def prediction(payload):
    return {
        "result": predict(payload),
        "batch1_2022bcd0046": "Ankur"
    }


if __name__ == "__main__":
    uvicorn.run(
        "app:app",
        host="127.0.0.1",
        port=8083,   
        reload=True
    )
