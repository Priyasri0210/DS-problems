with open("C:/Users/DELL/OneDrive/Desktop/demo-repo/DS-problems/sample.txt",'w') as f:
    f.writelines("Hello, this is a sample file.\n\n Python file handling is easy")

with open("C:/Users/DELL/OneDrive/Desktop/demo-repo/DS-problems/sample.txt",'a') as f:
    f.writelines("\n\n Appending a new line to the file")
with open("C:/Users/DELL/OneDrive/Desktop/demo-repo/DS-problems/sample.txt",'r') as f:
    data=f.read()
    print(data)
    #f.close()
    print(len(data))
print("done")
