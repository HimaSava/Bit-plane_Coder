import numpy as np
import cv2

imagepath = 'coded.png'             #Image with coded data
filename = ''    #File in which you want to save the decoded data

originalImg = cv2.imread(imagepath)
#Divide the layers into R,G and B
img = originalImg[:,:,0]

row ,col = img.shape

# Convert the image to 1D array
imgInArr = []
for i in range(row):
    for j in range(col):
            imgInArr.append (img[i][j])


#Extracting the info from the LSB bit plane
file =[]
data = []
flag =  0
#Create a buffer for the read data. If the data matches the EOF then break
buffer = []
a = []
b = [0,0,0,0,0,0,0,0,0,0,2,2,2,2,2,2,2,2,2,2,4,4,4,4,4,4,4,4,4,4,6,6,6,6,6,6,6,6,6,6] #EOF
for i in range(0,len(imgInArr)-8,8):
    blank = ""
    for j in range(8):
        if(imgInArr[i+j]%2==0):
            blank += "0"
        else:
            blank += "1"    

    if flag == 0:
        character = chr(int(blank,2))
        if character == '@':
            flag = 1
            continue
        file.append(character)
    else:
        currentData = int(blank,2).to_bytes(1,"little")
        a.append(currentData[0])
        buffer.append(currentData)
        if(len(a)>=40):
            if(a[0:40] == b):
                break
            else:
                data.append(buffer[0])
                a.pop(0)
                buffer.pop(0)

#Modifying the filename
filename = "Decoded_" 
for i in file:
    filename = filename + i 

#Saving the data into the file
with open(filename, 'wb') as file:
    for i in data:
        file.write(i)

