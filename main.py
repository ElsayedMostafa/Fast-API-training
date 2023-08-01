from fastapi import FastAPI
from school.database import engine
from school import models


app = FastAPI()


#

models.Base.metadata.create_all(engine)


@app.get("/")
async def root():
    return {"message": "Hello World"}




