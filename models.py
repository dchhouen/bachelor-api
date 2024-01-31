from uuid import UUID
from fastapi import FastAPI
from pydantic import BaseModel
from enum import Enum

# Define an Enum for contestant occupations
class Occupation(str, Enum):
    singer = "Singer"
    general_contractor = "General Contractor"
    pilot = "Pilot"
    marketing_specialist = "Marketing Specialist"
    interior_designer = "Interior Designer"
    # Add more occupations as needed

class Contestants(BaseModel):
    id: int
    first_name: str
    last_name : str
    age: int
    occupation: Occupation


