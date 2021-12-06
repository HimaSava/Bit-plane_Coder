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
filename = ''    #File in which you want to save the decoded data

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
file =[]
data = []
flag =  0
count = 0
character = ''
temp = []
for i in range(0,onebiting.size-8,8):
    blank = str(onebiting[i]) + str(onebiting[i+1]) + str(onebiting[i+2]) + str(onebiting[i+3]) + str(onebiting[i+4]) + str(onebiting[i+5]) + str(onebiting[i+6]) + str(onebiting[i+7])
    
    if flag == 0:
        character = chr(int(blank,2))
        if character == '@':
            flag = 1
            continue
        file.append(character)
    else:
        data.append(int(blank,2).to_bytes(1,"little"))

hiddendata = []
count = 0
for i in range(len(data)-39):
    if data[i][0] == data[i+1][0] == data[i+2][0] == data[i+3][0] == data[i+4][0] == data[i+5][0] == data[i+6][0] == data[i+7][0] == data[i+8][0] == data[i+9][0] == 0:
            if data[i+10][0] == data[i+11][0] == data[i+12][0] == data[i+13][0] == data[i+14][0] == data[i+15][0] == data[i+16][0] == data[i+17][0] == data[i+18][0] == data[i+19][0] == 1:
                    if data[i+20][0] == data[i+21][0] == data[i+22][0] == data[i+23][0] == data[i+24][0] == data[i+25][0] == data[i+26][0] == data[i+27][0] == data[i+28][0] == data[i+29][0] == 3:
                            if data[i+30][0] == data[i+31][0] == data[i+32][0] == data[i+33][0] == data[i+34][0] == data[i+35][0] == data[i+36][0] == data[i+37][0] == data[i+38][0] == data[i+39][0] == 5:
                                break
    hiddendata.append(data[i])




filename = "Decoded_" 
for i in file:
    filename = filename + i 

#Saving the data into the file
with open(filename, 'wb') as file:
    for i in hiddendata:
        file.write(i)


