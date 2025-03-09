from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()
students = {
    1:{
        "name":"jhon",
        "age":17,
        "class":"year 12"
    }
}
class Student(BaseModel):
    name:str
    age:int
    year:str

@app.get("/")
def index():
    return {"name ":"first data "}

@app.get("/student/{student_id}")
def getstudent(student_id: int ):
    return students[student_id]


@app.get("/st")
# none for the not require the qurey parameter as all time 
def getstudent(name:str = None):
    # for the ?name=jhon like that 
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
        return {"data" : "is not Found "}
    


@app.post("/create/{student_id}")
def create_student(student_id:int, student : Student):
        if student_id in students:
             return {"error":"existed "}
        students[student_id]= student
        return students[student_id]

@app.put("/update/{student_id}")
def update(student_id:int,student : Student):
     pass