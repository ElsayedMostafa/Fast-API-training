from school.database import Base


from sqlalchemy import Column, String,Integer





class Student(Base):
    __tablename__ = 'students'
    

    id = Column(Integer,primary_key=True,index=True)
    name = Column(String)
    email = Column(String)
    mobile = Column(String)


