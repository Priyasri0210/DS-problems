#File handling mean doing read/write and append opertaions on file
#syntax
# Read - r
# write - w
# append - a
#with open(<filename>,<type of operation>) as <file_variable>:
    #<variablename> = <file_variable>.read()

#Reading a file 

#Use of this method is it closes the file automatically once we get out of with function
with open('E:/Data_Science_Sripriya/Python_basics/files/sample.txt','r') as f:
    data = f.read()
    print(data)

print('Done')


# file = open('E:/Data_Science_Sripriya/Python_basics/files/sample.txt','r')
# file.close()

#Write into file
#write --> deletes all the content in the file, writes new lines
# with open('E:/Data_Science_Sripriya/Python_basics/files/sample.txt','w') as f:
#     f.writelines('Welcome to the Class !')

#append ---> add new line to the existing data
with open('E:/Data_Science_Sripriya/Python_basics/files/sample.txt','a') as f:
    f.writelines('\n Welcome to the Class !')

