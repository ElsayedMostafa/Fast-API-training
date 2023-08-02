from fastapi import FastAPI,Depends
from school.database import engine,get_db
from school import models
from school import schemas
from sqlalchemy.orm import Session

app = FastAPI()

db_session = get_db

#c-r-u-d

models.Base.metadata.create_all(engine)


@app.get("/")
async def root():
    return {"message": "Hello World"}


#create user
@app.post("/student")
def createUser(request:schemas.NewStudent,db:Session=Depends(db_session)):
    
    #convert from schema to student model
    new_student = models.Student(name=request.name,email=request.email,mobile=request.mobile)
    db.add(new_student) #operation
    db.commit() #commit
    db.refresh(new_student) # refresh

    return 'Student add successfully'

@app.get("/students")
def getAllUsers(db:Session=Depends(db_session)):
    students = db.query(models.Student).all()
    return students


#get user by id
@app.get("/student/{id}")
def getUserById(id,db:Session=Depends(db_session)):
    student = db.query(models.Student).filter(models.Student.id==id).first()
    if not student:
        return "student not found"
    else:
        return student


#function to update user by id

@app.post("/updatestudent/{id}")
def updateUserById(id,request:schemas.NewStudent,db:Session=Depends(db_session)):
    student = db.query(models.Student).filter(models.Student.id==id)
    if not student.first():
        return "student not found"
    else:
        student.update({'name':request.name,'email':request.email,'mobile':request.mobile})
        db.commit()
        return 'done'

#function to delete student by id

@app.delete("/deletestudent/{id}")
def deleteStudentById(id,db:Session=Depends(db_session)):
    student = db.query(models.Student).filter(models.Student.id==id)
    if not student.first():
        return "student not found"
    else:
        student.delete()
        db.commit()
        return 'done'




        
























