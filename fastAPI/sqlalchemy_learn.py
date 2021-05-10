from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

#CREATE DATABASE
engine=create_engine('postgresql://myuser:mypass@localhost:5432/mydb',echo=False)


Session=sessionmaker(bind=engine)
session=Session()

Base = declarative_base()

class Student(Base):
    __tablename__='student'
    id=Column(Integer,primary_key=True)
    name=Column(String(50))
    age=Column(Integer)
    grade=Column(String(50))

#Base.metadata.create_all(engine)

#INSERT INTO DATABASE
student1=Student(name="Kanav Raina",age=27,grade="B")
student2=Student(name="Tarun Raina",age=24,grade="A")
student3=Student(name="Ajay Raina",age=27,grade="C")

session.add(student3)
#session.add_all(student2,student3)

#session.commit() #Add data into database

#READ DATA FROM DATABASE

students = session.query(Student)
for student in students:
    print(student.name)


#UPDATE DATA FROM DATABASE
student=session.query(Student).filter(Student.name=="Karan Sharma").first()
student.name="Kanav Sharma"
session.commit()


"""students = session.query(Student)
for student in students:                        #check your updated data
    print(student.name)"""

#DELETE DATA IN DATABASE
student=session.query(Student).filter(Student.name=="Tarun Raina").first()
session.delete(student)
session.commit()

"""students = session.query(Student)
for student in students:
    print(student.name)"""


"""
References:
CREATE A USER IN POSTGRESQL
https://medium.com/coding-blocks/creating-user-database-and-adding-access-on-postgresql-8bfcd2f4a91e

check if you are able to connect to database from your python script(https://stackoverflow.com/questions/48999379/psycopg2-operationalerror-fatal-password-authentication-failed-for-user-my-u/49008883)
import psycopg2
psycopg2.connect("dbname=postgres user=postgres host=localhost password=oracle port=5432")

"""
