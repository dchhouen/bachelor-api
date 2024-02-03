from fastapi import FastAPI, HTTPException
from models import Contestants, Occupation

app = FastAPI()

# Sample data for contestants
contestants_data = [
    {"id": 1, "first_name": "Hannah","last_name": "Brown", "age": 24, "occupation": Occupation.interior_designer},
    {"id": 2, "first_name": "Jed","last_name": "Wyatt", "age": 25, "occupation": Occupation.singer},
    {"id": 3, "first_name": "Tyler","last_name": "Cameron", "age": 26, "occupation": Occupation.general_contractor},
]

# Route to get all contestants
@app.get("/api/v1/contestants")
async def get_all_contestants():
    return contestants_data

# Route to add a contestants
@app.post("/api/v1/contestant")
async def add_contestant(contestant_input: Contestants):
    contestants_data.append(contestant_input.model_dump())
    return {"message": "Contestants has been added"}

# Route to get a specific contestants by ID
@app.get("/api/v1/contestants/{contestant_id}")
async def get_contestant_by_id(contestant_id: int):
    for contestant in contestants_data:
        if contestant.get('id') == contestant_id:
            return contestant
    raise HTTPException(status_code=404, detail="Contestant not found")

# Route to search contestants by name
@app.get("/api/v1/contestants/search/")
async def search_contestants_by_name(contestant_input: Contestants):
    for constestant in contestants_data:
        if constestant.get('first_name') == Contestants['first_name']:
            return constestant
