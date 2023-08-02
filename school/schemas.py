from pydantic import BaseModel



class NewStudent(BaseModel):
    name:str
    email:str
    mobile:str