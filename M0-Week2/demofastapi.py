from fastapi import FastAPI, Path,HTTPException
import json

app = FastAPI()


def load_data():
    with open('patients.json', 'r') as f:
      data = json.load(f)

    return data

@app.get("/")
def home(): 
 return {"message":"A tool for doctor to manage patients"}

@app.get("/about")
def about(): 
 return {"message":"An API to know more about this whole project"}

@app.get("/view")
def view(): 
 data = load_data()
 return data


@app.get("/patient/{patient_id}", responses={
        404: {
            "description": "Patient not found"
        }
    })
def get_patient(patient_id: str = Path(..., description= "ID OF THE PATIENT",lt="P009")): 
    data = load_data()
    print(patient_id)

    if patient_id in data:
      return data[patient_id]
    raise HTTPException(404, "Patient not found")