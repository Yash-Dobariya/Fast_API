from pydantic import BaseModel

class Blog(BaseModel):

    name : str
    enrollment_no : int
    course : str
    mobail_no : int
    address : str

