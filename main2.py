from enum import Enum

from fastapi import FastAPI


class ModelName(str, Enum):
    cp = "CP.Comapny"
    si = "Stone.Island"
    nike = "Nike"


app = FastAPI()


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.cp:
        return {"model_name": model_name, "message": "Cool boy!"}

    if model_name.value == "Stone.Island":
        return {"model_name": model_name, "message": "50/50 boy"}

    return {"model_name": model_name, "message": "Mimo"}