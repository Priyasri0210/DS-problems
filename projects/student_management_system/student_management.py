import json
import uuid

#load the database
# json.load()
# json.dump()
def load_data():
    with open('E:/Git/DS-problems/projects/student_management_system/sample.json','r') as f:
        students_db = json.load(f)
        return students_db

def save_data(data):
    with open('E:/Git/DS-problems/projects/student_management_system/sample.json','w') as f:
        json.dump(data,f)


def add_student(students_db):
    try:
        student_id = input("Enter student Id")
        #it checks the key
        if student_id in students_db:
            print('Student is already registered')
            return None
        
        name = input("Enter student name : ")
        age = int(input('Enter student age : '))
        course = input("Enter student course : ")
        marks = float(input('Enter student mark : '))

        students_db[student_id] = {"Name":name,"Age":age,"Course":course,"Marks":marks}
        save_data(students_db)
        print('Student registered successfully')
    except Exception as e:
        print('error in adding student')
        print(e)

def search_student(students_db):
    student_id = input("Enter the student id to be searched : ")
    if student_id in students_db:
        print("Details : ")
        print(students_db[student_id])
    else:
        print('Student id is not present')

def update_details(students_db):
    student_id = input("Enter the student id to be searched : ")
    if student_id not in students_db:
        print("student id is not present")
    else:
        name = input("Enter student name : ")
        age = int(input('Enter student age : '))
        course = input("Enter student course : ")
        marks = float(input('Enter student mark : '))

        students_db[student_id] = {"Name":name,"Age":age,"Course":course,"Marks":marks}

        save_data(students_db)
        print('Student details updated successfully')

def delete_student(students_db):
    student_id = input("Enter the student id to be searched : ")
    if student_id not in students_db:
        print("student id is not present")
    else:
        del students_db[student_id]
        save_data(students_db)
        print('Student details deleted successfully')
    