#serialize --> converting binary format for security and storage concern
import pickle

with open('E:/Data_Science_Sripriya/Python_basics/advanced/image.png','rb') as f:
    image_data = f.read()

with open('E:/Data_Science_Sripriya/Python_basics/advanced/image.pkl','wb') as f:
    #dump is for saving into file
    pickle.dump(image_data,f)

#1user ---> 2nd user
#binary ---> transfer speed is also higher
#It is also secure

with open('E:/Data_Science_Sripriya/Python_basics/advanced/image.pkl','rb') as f:
    #load is for reading from file
    image_data_pickle = pickle.load(f)

with open('E:/Data_Science_Sripriya/Python_basics/advanced/image_3.png','wb') as f:
    f.write(image_data_pickle)


#backup
#1. Image ---> converting to binary()
#2. Restore ---> 
