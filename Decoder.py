import numpy as np
import cv2

def intToBitArray(img) :
    list = []
    for i in range(row):
        for j in range(col):
             list.append (np.binary_repr( img[i][j] ,width=8  ) )
    return list

def bitplane(bitImgVal , img1D ):
    bitList = [  int(   i[bitImgVal]  )    for i in img1D]
    return bitList



imagepath = 'coded.png'             #Image with coded data
filename = 'decoded_message.txt'    #File in which you want to save the decoded data

originalImg = cv2.imread(imagepath)
#Divide the layers into R,G and B
img = originalImg[:,:,0]

row ,col = img.shape


imgIn1D = intToBitArray(img)
imgIn2D = np.reshape(imgIn1D , (row,col) )

#Splitting the image into the 8 bit-planes
eightbitimg = np.array( bitplane(0, imgIn1D ) ) * 128
sevenbitimg = np.array( bitplane(1,imgIn1D) ) * 64
sixbiting = np.array( bitplane(2,imgIn1D) ) * 32
fivebiting = np.array( bitplane(3,imgIn1D) ) * 16
fourbiting = np.array( bitplane(4,imgIn1D) ) * 8
threebiting = np.array( bitplane(5,imgIn1D) ) * 4
twobiting = np.array( bitplane(6,imgIn1D) ) * 2
onebiting = np.array( bitplane(7,imgIn1D) ) 

#Extracting the info from the LSB bit plane
blank = ""
data =[]
for i in range(0,onebiting.size-8,8):
    blank = str(onebiting[i]) + str(onebiting[i+1]) + str(onebiting[i+2]) + str(onebiting[i+3]) + str(onebiting[i+4]) + str(onebiting[i+5]) + str(onebiting[i+6]) + str(onebiting[i+7])
    data.append(chr(int(blank,2)))

#Decoding the data
text = ''
for i in data:
    if i == '@':
        break
    text = text + i
print("Your coded data is: ")
print(text)

#Saving the data into the file
with open(filename, 'w') as file:
    file.write(text)

