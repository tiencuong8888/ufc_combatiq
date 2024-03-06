from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {'setup': "I'm on it dudes !"}

@app.get("/predict")
def predict(fighter_red, fighter_blue):
    """
    parameters : red or blue corresponds to the fighter corner
    """

    return {'fight_outcome': "Work in progress"}
