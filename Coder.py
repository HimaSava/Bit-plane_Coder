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



# imagepath = '4k_Test.jpg' #Image to find data into
imagepath = 'lena.jfif' #Image to find data into

filename = 'message.txt' #Data that you want to hide in a image

originalImg = cv2.imread(imagepath)

#Split the image into R G and B layers
#For now we are only coding in the Blue layer
img = originalImg[:,:,0]
g = originalImg[:,:,1]
r = originalImg[:,:,2]

row ,col = img.shape

imgIn1D = intToBitArray(img)
imgIn2D = np.reshape(imgIn1D , (row,col) )

#Split the img into the 8 bit planes
eightbitimg = np.array( bitplane(0, imgIn1D ) ) * 128
sevenbitimg = np.array( bitplane(1,imgIn1D) ) * 64
sixbiting = np.array( bitplane(2,imgIn1D) ) * 32
fivebiting = np.array( bitplane(3,imgIn1D) ) * 16
fourbiting = np.array( bitplane(4,imgIn1D) ) * 8
threebiting = np.array( bitplane(5,imgIn1D) ) * 4
twobiting = np.array( bitplane(6,imgIn1D) ) * 2
onebiting = np.array( bitplane(7,imgIn1D) ) * 1


# print(onebiting.shape)
print("Number of letters allowed are: " + str(int(onebiting.size/8)))
text = []
with open(filename, 'r') as csvfile:   
  content = csvfile.read()  
print("Coding " + str(len(content)) + " characters into the image")

for i in content:
	text.append (np.binary_repr( ord(i) ,width=8  ) )
text2 = ''
for i in text:
	text2 = text2+i
for i in range(0,len(text2)):
	onebiting[i] = text2[i]

print("Coding done. Reconstrcting the image")

#Reconstruct the image by adding all the planes back together
full_img = eightbitimg + sevenbitimg + sixbiting + fivebiting + fourbiting + threebiting + twobiting + onebiting
imgs = np.reshape(full_img,(row,col))
imgs = imgs.astype(np.uint8)


#Reconstruct the image adding RGB layers into a final image
finalImg = np.zeros((row,col,3), 'uint8')
finalImg[:,:,0] = imgs
finalImg[:,:,1] = g
finalImg[:,:,2] = r

cv2.imwrite("coded.png",finalImg)
cv2.imshow("Coded Image",finalImg)

cv2.waitKey()