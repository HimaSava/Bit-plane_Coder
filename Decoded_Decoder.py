import numpy as np
import cv2

imagepath = 'coded.png'             #Image with coded data
filename = ''    #File in which you want to save the decoded data

originalImg = cv2.imread(imagepath)
#Divide the layers into R,G and B
img = originalImg[:,:,0]

row ,col = img.shape


imgInArr = []
for i in range(row):
    for j in range(col):
            imgInArr.append (img[i][j])


#Extracting the info from the LSB bit plane
file =[]
data = []
flag =  0
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
        data.append(currentData)

hiddendata = []
for i in range(len(data)-39):
    flag=0
    for k in range(4):
        for j in range(10):
            if(data[i+j+k*10][0]!=k*2):
                flag = 1
                break
        if flag == 1:
            break
 
    if flag == 0:
        break
    hiddendata.append(data[i])

#Modifying the filename
filename = "Decoded_" 
for i in file:
    filename = filename + i 

#Saving the data into the file
with open(filename, 'wb') as file:
    for i in hiddendata:
        file.write(i)


