import numpy as np
import cv2

imagepath = '4k_Test.jpg'
# imagepath = 'Panda.jpg' #Image to find data into
# imagepath = 'lena.jfif' #Image to find data into
filename = "Bit-plane_Coder.zip" #Data that you want to hide in a image


originalImg = cv2.imread(imagepath)

#Split the image into R G and B layers
#For now we are only coding in the Blue layer
img = originalImg[:,:,0]
g = originalImg[:,:,1]
r = originalImg[:,:,2]

row ,col = img.shape
# Change the image to 1D array
imgIn1D = []
for i in range(row):
    for j in range(col):
            imgIn1D.append (img[i][j])

#Read the file to be hidden
data = []
secretCode = filename + "@" 
with open(filename, 'rb') as file:
    while True:
        byte = file.read(1)
        if not byte:
            break
        data.append(byte[0])

#Adding below bytes to detect EOF
#This works but is a very dirty way of doing it so pls HELP :(
for i in range(0,8,2):
    for j in range(10):
        data.append(i)
    

#Adding file name to code
text = []
for i in secretCode:
	text.append(np.binary_repr( ord(i) ,width=8  ) )

#Change the data to binary form
for i in data:
    text.append(np.binary_repr( i ,width=8  ) )


#Combining file name + data
text2 = ''
for i in text:
	text2 = text2+i

#Check if the last bit is 0 or 1, and according to data change it
for i in range(len(text2)):
    if(int(text2[i])%2 == 0 and imgIn1D[i]%2==1):
        imgIn1D[i] = imgIn1D[i] + 1
    elif(int(text2[i])%2 == 1 and imgIn1D[i]%2==0):
        imgIn1D[i] = imgIn1D[i] - 1

#Convert the 1D array to 2D array
imgs = np.reshape(imgIn1D,(row,col))
imgs = imgs.astype(np.uint8)


#Reconstruct the image adding RGB layers into a final image
finalImg = np.zeros((row,col,3), 'uint8')
finalImg[:,:,0] = imgs
finalImg[:,:,1] = g
finalImg[:,:,2] = r

#Write the coded image
cv2.imwrite("coded.png",finalImg)
