import pickle
student = {'name:Alice','Age:20','marks:85'}
#print(student)
with open('student.pkl','wb') as f:
    pickle.dump(student,f)
with open('student.pkl','rb') as f:
    student = pickle.load(f)
print(student)

