from fastapi import FastAPI
from models import Info

app = FastAPI()

@app.put('/details')
def take_detail(student_info:Info):
    return {"Successful submited",student_info}