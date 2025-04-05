with open("C:/Users/DELL/OneDrive/Desktop/demo-repo/DS-problems/sample.txt",'w') as f:
    f.writelines("Hello, this is a sample file.\n\n Python file handling is easy")

with open("C:/Users/DELL/OneDrive/Desktop/demo-repo/DS-problems/sample.txt",'a') as f:
    f.writelines("\n\n Appending a new line to the file")
with open("C:/Users/DELL/OneDrive/Desktop/demo-repo/DS-problems/sample.txt",'r') as f:
    data=f.read()
    print(data)
    #f.close()
<<<<<<< HEAD
    print(len(data))
=======
print(len(data))


>>>>>>> 2444ddbc0e4f7337b1004f2a9cf34a027c333122
print("done")

