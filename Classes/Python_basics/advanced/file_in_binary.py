with open('E:/Data_Science_Sripriya/Python_basics/advanced/image.png','rb') as f:
    image_data = f.read()
    print(image_data)

#1user ---> 2nd user
#binary ---> transfer speed is also higher

with open('E:/Data_Science_Sripriya/Python_basics/advanced/image_2.png','wb') as f:
    f.write(image_data)

