from fastapi import FastAPI, Path, Query
from typing import Optional
from pydantic import BaseModel
app = FastAPI()
class Student(BaseModel):
    last: str
    first: str
    id: int

class UpdateStudent(BaseModel):
    last: Optional[str] = None
    first: Optional[str] = None
    id: Optional[int] = None

data = {}
@app.get("/get-item/{item_id}")
def get_item(item_id: int = Path(0, studID = "Student ID Number")):
    return data[item_id]

@app.get("/get-by-name")
def get_item(name: str = "None"):
    for item_id in data:
        if data[item_id].last == name:
            return data[item_id]
    return {"Data": "Not found"}

@app.post("/create-student/{student_id}")
def create_student(student_id: int, student: Student):
    if student_id in data:
        return {"Error": "Student already exists"}
    data[student_id] = student
    return data[student_id]

@app.put("/update-student/{student_id}")
def update_student(studID: int, student: UpdateStudent):
    if studID not in data:
        return {"Error": "Student does not exist"}
    data[studID].update(student)
    return data[studID]
@app.delete("/delete-student")
def delete_student(student_id: int = Query(..., description = "ID of Student to be deleted")):
    if student_id not in data:
        return {"Error:" "Student does not exists"}
    del data[student_id]
