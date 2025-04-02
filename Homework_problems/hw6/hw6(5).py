import pickle
with open('student.pkl','rb') as f:
    student = pickle.load(f)
print(student)