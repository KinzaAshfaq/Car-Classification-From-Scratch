# use the following code to read the images from a specific folder, resize, and saved it. 
for i in range (1,101): 
    image = cv2.imread("..\\stairs\\"+str(i)+".png") 
    image = cv2.resize(image,(64,64)) 
    cv2.imwrite('1\\'+str(i)+'.png',image) 
# use the following code to make the array of images 
image1=[] 
for i in range(0,100): 
    image_path_1 = "0\\"+str(i+1)+".png" 
    image = cv2.imread(image_path_1) 
    image=cv2.cvtColor(image, cv2.COLOR_BGR2RGB) 
    image1.append(image) 
# Create the datasets for the training and testing images 
import h5py 
    with h5py.File("train_stairsvnonstairs.h5", "w") as hf: 
    train_set_x = hf.create_dataset("train_set_x", data=train_images) 
    train_set_y = hf.create_dataset("train_set_y", data=train_labels) 