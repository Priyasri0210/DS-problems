import pickle
numbers = [10,20,30,40,50]
with open('numbers.pkl','wb') as f:
    pickle.dump(numbers,f)
with open('numbers.pkl','rb') as f:
    numbers=pickle.load(f)
print("loaded list",numbers)

